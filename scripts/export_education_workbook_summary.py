"""Export a reproducible, record-free inventory of the supplied sample workbook."""
import argparse
import collections
import hashlib
import json
from pathlib import Path
import openpyxl


def export(source, output):
    source, output = Path(source), Path(output)
    workbook = openpyxl.load_workbook(source, data_only=False, read_only=True)
    sheets = []
    for sheet in workbook:
        rows = list(sheet.values)
        metadata = sheet.title in ("来源与覆盖", "共同字段")
        headers = list(rows[0])
        samples = rows[2:] if not metadata else []
        counts = collections.Counter(headers)
        item = {
            "name": sheet.title,
            "worksheet_rows": len(rows),
            "columns": len(headers),
            "kind": "metadata" if metadata else "dataset_schema_and_samples",
            "sample_rows": len(samples),
            "duplicate_headers": {str(k): v for k, v in counts.items() if v > 1},
            "fields": [
                {"column_1based": i + 1, "name": name,
                 "description_from_workbook": None if metadata else rows[1][i],
                 "sample_null_cells": sum(row[i] is None for row in samples),
                 "sample_missing_marker_cells": sum(
                     isinstance(row[i], str) and row[i].strip().lower() in {"nan", "na", "null", ""}
                     for row in samples)}
                for i, name in enumerate(headers)
            ],
        }
        if metadata:
            item["metadata_rows"] = [list(row) for row in rows[1:]]
        sheets.append(item)
    result = {
        "format_version": 1,
        "source_filename": source.name,
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "scope": "Workbook sample/schema inventory, not full dataset statistics. No individual sample records exported.",
        "sheet_count": len(sheets),
        "sample_row_count": sum(s["sample_rows"] for s in sheets),
        "sheets": sheets,
    }
    output.mkdir(parents=True, exist_ok=True)
    (output / "workbook-summary.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    lines = ["# Excel 字段清单（自动导出）", "", "字段解释逐字保留自工作簿；不是本项目对原数据定义的独立认证。",
             "空单元格和文本缺失标记分开计数，统计仅覆盖工作簿样例。重复表头按原始列序保留。", "",
             f"源文件 SHA-256：`{result['source_sha256']}`", "",
             f"工作表：{len(sheets)}；数据/字段表：{len(sheets)-2}；样例总行数：{result['sample_row_count']}。", ""]
    def escape(value):
        return str(value if value is not None else "").replace("|", "\\|").replace("\n", "<br>").replace("\r", "")
    for sheet in sheets:
        lines += ["## " + sheet["name"], "", f"列数：{sheet['columns']}；样例行数：{sheet['sample_rows']}。", ""]
        if sheet["kind"] == "metadata":
            lines += ["| " + " | ".join(escape(f["name"]) for f in sheet["fields"]) + " |",
                      "| " + " | ".join("---" for _ in sheet["fields"]) + " |"]
            lines += ["| " + " | ".join(escape(v) for v in row) + " |" for row in sheet["metadata_rows"]]
        else:
            lines += ["| 列序 | 原字段 | 工作簿字段说明 | 样例空值数 | 样例文本缺失标记数 |", "| --- | --- | --- | --- | --- |"]
            for field in sheet["fields"]:
                lines.append("| " + " | ".join(escape(field[k]) for k in
                    ("column_1based", "name", "description_from_workbook", "sample_null_cells", "sample_missing_marker_cells")) + " |")
        lines.append("")
    (output / "field-catalog.md").write_text("\n".join(lines), encoding="utf-8")
    workbook.close()
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("--output", default="data/education/2026-11-16")
    args = parser.parse_args()
    result = export(args.source, args.output)
    print(f"{result['sheet_count']} sheets; {result['sample_row_count']} sample rows; {result['source_sha256']}")
