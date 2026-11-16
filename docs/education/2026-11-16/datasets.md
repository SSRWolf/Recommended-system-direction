# 数据字段、行为事件与适配性

证据来自 [完整字段清单](../../../data/education/2026-11-16/field-catalog.md) 和 [机器摘要](../../../data/education/2026-11-16/workbook-summary.json)。本页是基于已读取字段和样例的人工判断；全量规模、缺失率、序列长度分布、跨表覆盖率未测量。

## 1. 工作簿覆盖与原始粒度

| 数据/版本 | 工作表与字段数 | 当前记录 | 粒度与直接可用信息 | 主要限制 |
| --- | --- | --- | --- | --- |
| Algebra05/06 | 各19列 | 各5行；06为文档展示行 | 学生-题目出现次数-步骤；开始/结束时间、首答、Incorrects/Hints/Corrects、KC、Opportunity | 计数不是操作流；多KC以 `~~` 分隔；06样例出现文本 NaN |
| ASSIST2009 | 30列 | 5行 | user_id、problem_id、correct、attempt_count、hint_count、ms_first_response、skill_id | order_id只有顺序；correct含义需按版本确认；同一交互多KC展开可能造成重复 |
| ASSIST2012 | 35列 | 5行 | 起止时间、actions、用时/重试/提示、skill；另有情感预测列 | actions含嵌套序列文本，应安全解析而非 eval；情感预测不是人工真值 |
| ASSIST2015 | 4列 | 5行 | user_id、log_id、sequence_id、correct | 缺实际时间、独立题目ID、提示和尝试；sequence_id是题集，不应改名为题目或KC |
| ASSIST2017 | 82列 | 5行 | studentId、problemId、skill、startTime/endTime、timeTaken、hintCount、attemptCount | 大量预计算特征、情感预测与后续结果；高泄漏风险 |
| Junyi | 操作21列；题目11列 | 各5行 | ATTEMPT/Outcome、毫秒时间、会话、练习/主题/领域；题目表 prerequisites | 题目名称与练习级标识粒度不同；不能仅凭5行验证联结覆盖 |
| OLI | 操作47列、步骤28列、题目27列 | 各5行 | transaction可记录页面访问/作答/反馈；步骤、题目表是聚合视图 | 不把三个视图当独立行为追加；重复表头须保留列序；时区US/Eastern |
| OULAD | 7表，列数依次6/3/12/5/6/6/5 | 各5行 | 学生-课程开课期-网站-相对日点击计数，评估分数、注册信息 | 没有日内点击顺序、答题KC或提示事件；成绩与退课字段是未来结果 |
| EdNet | KT1/2/3/4为5/6/6/7列；题库7、讲解5、付费4、优惠券3 | 前6表各5行，后2表各4行；均为文档样例 | KT1作答汇总；KT2动作；KT3增解析/讲解；KT4更细媒体/非学习动作 | 用户标识在文件名；当前样例无文件名，无法重建真实学生；偏移时间不作跨用户真实日历 |
| MoocRadar | 交互7列、题目7列 | 0行 | 文件说明中的尝试、得分、时间、concepts、cognitive_dimension、detail | 未取得原始记录；字段有描述不等于文本/标注已可用 |
| FoundationalASSIST | 交互7列、题库10列 | 0行 | 发布方描述的提示、是否看答案、得分与题干字段 | 申请制；技能表仅在覆盖清单出现；表头顺序未核验 |
| DBE-KT22 | 作者生成的序列表10列 | 0行 | 题目、正确性、难度自评、置信度、提示、耗时、改答案次数数组 | 不是 transaction.csv 表头；原始三表未取得，不能混用版本 |

工作簿整体有33张表，其中2张是元数据，31张是数据/字段表。128条是混合粒度样例行数。原文的“前五条”也包括文档示例和未取到记录的表，不代表每个数据集都有5条原始训练数据。

## 2. 统一事件结构与预测时点

建议保留以下字段而不强行补齐缺失项：

```text
dataset_id, dataset_version, source_file, source_row,
student_id, course_instance, session_id,
item_id, item_type, knowledge_ids[],
event_type_raw, event_type_normalized, outcome_raw, outcome_normalized,
timestamp_raw, timestamp_unit, timezone, order_index,
duration_ms, attempt_count, hint_count, available_at, provenance
```

`student_id` 使用数据集命名空间；匿名 ID 也不跨库拼接。保留 raw 和 normalized 两套值。时间顺序由学生和课程上下文确定；同一时间戳按源顺序稳定排序并记录不确定性。耗时、事件间隔与媒体播放位置是三种不同量；`cursor_time` 不作为墙钟时间。

区分两个任务：①作答前预测本题，输入仅含之前完成的历史和当时已知题目属性；②本题结束后更新状态，允许使用本题提示/耗时，但目标必须是后续表现。`available_at` 用于检查特征在预测时点是否已经产生。

## 3. 可以还原什么行为

| 数据证据 | 可生成事件或特征 | 不能据此断定 |
| --- | --- | --- |
| EdNet-KT2样例：enter题组→respond同题c→respond同题d→submit题组 | 进入题组、两次选项选择、提交；提交前答案修改 | 两次独立评分尝试；c或d正确（需题库匹配） |
| EdNet-KT3样例：提交题组后enter解析 | 提交后访问解析的候选模式 | 解析完整阅读、知识已掌握 |
| EdNet-KT4样例：pay、enter、text_enter、play_audio、pause_audio | 付费单列为非学习上下文；媒体控制与游标 | 播放位置10秒等于专注听了10秒 |
| Algebra样例：首答错误、Incorrects=2、Hints=3 | 一个步骤内多次错误、使用提示的汇总特征 | “错→提示→错→正确”的确切顺序 |
| OLI操作首行VIEW_PAGE | 页面访问事件，Outcome为空属结构性不适用候选 | 空Outcome为答错 |
| Junyi：ATTEMPT与INCORRECT | 有结果的作答事件，按日志字段保留KC层级 | 每种知识层级都是独立题目 |
| OULAD：date与sum_click | 每日资源访问强度；按周聚合 | 将sum_click展开成若干有顺序点击 |

EdNet 的 `respond` 是选项选择，`submit` 常是题组级；需按题组会话关联每题提交前最后一次有效选择，并联结题库 `correct_answer` 才能计算正确性。不能把 enter/exit/付费等非评分事件标成0分。KT层级是不同粒度视图，不能直接拼成同一用户的重复轨迹。[官方说明](https://github.com/riiid/EdNet)

## 4. 表关联与清洗规则

- **Algebra/OLI步骤：** `(student, Problem Name, Problem View, Step Name)` 加时间/会话识别步骤实例，不能只用题目名去重。OLI交易用 Transaction Id 追踪来源。OLI操作有两个 Input、多个同名KC列；导出以列位置保留，加载分析表后可加 `__2/__3` 后缀，禁止字典覆盖。
- **ASSIST：** 核对相同日志/学生/题目记录是重复行还是多KC展开。多KC在集合中保留，避免相同交互分入训练和测试两侧。正确性可能有部分分，保留原值并单独定义二值标签；不直接转布尔值。
- **Junyi：** 优先尝试 `KC (Exercise)` 对 `Junyi_题目.name`，核验唯一性和覆盖率后使用；`Problem Name` 可能含题型后缀。prerequisites解析成边时保留源字符串。`h_position/v_position` 是布局坐标，不能把几何距离解释为知识距离。样例展示名有问号字符，不能自动“纠正”未知原字。
- **OULAD：** studentVle与vle用 `(code_module, code_presentation, id_site)`，学生上下文用 `(code_module, code_presentation, id_student)`；studentAssessment先用id_assessment联assessments补课程开课期，再关联学生上下文。date是相对开课日，可为负，不能作为Unix时间或直接删除负值。
- **EdNet：** user_id取原始每学生文件名；题库以question_id、讲解以lecture_id等分类型关联。标签与实体ID分开，题组和题目不可混淆。工作簿已记录KT1文档示例中solving_id/question_id列顺序修正，摘要保持当前工作簿版本，不声称逐字复制官方原表。
- **MoocRadar/Foundational/DBE：** 先取得文件，再核对字段、时间单位、数组长度及授权范围；对DBE序列表要求所有逐题数组与seq_len一致，不能仅从表头断言有效。

## 5. 特征泄漏重点

ASSIST2017 的 `timeGreater10SecAndNextActionRight` 明示下一动作结果，不能用于预测下一动作；`Ave*`、`sum*` 等先查其计算窗口，无法证明只用过去就剔除或从原日志重算。`MCAS/Enrolled/Selective/isSTEM` 等按预测目标与采集时点单独处理。`confidence(*)/RES_*` 和ASSIST2012的Average_confidence是模型生成或汇总信号，不能直接当潜在需求的独立金标准。

OULAD的final_result、date_unregistration只能在其可见时点之后作输入，早期预测应作为结局标签。DBE中自报难度与置信度是否作答后取得需核实。任何数据集的整段正确率、全量题目难度、全量共现图都可能泄漏测试信息。

## 6. 六方向适配矩阵

“优先”表示字段结构合适但仍需全量数据；“条件”表示缺事件/图/文本等关键条件；“弱”表示当前粒度不匹配；“待取”表示只有描述。不是模型效果评分。

| 数据 | ①多行为 | ②时间 | ③知识图 | ④模式 | ⑤LLM路径 | ⑥迁移 |
| --- | --- | --- | --- | --- | --- | --- |
| ASSIST2009 | 优先 | 条件：仅顺序/耗时 | 条件：KC关联图 | 条件：计数 | 条件：资源文本 | 条件：行为对齐 |
| ASSIST2012 | 优先 | 优先 | 条件：KC关联图 | 条件：解析actions | 条件：资源文本 | 条件 |
| ASSIST2015 | 弱 | 弱 | 弱 | 条件：仅正确性/题集 | 弱 | 条件：最小特征对照 |
| ASSIST2017 | 优先：先剔泄漏列 | 优先 | 条件：skill映射 | 条件：粒度核验 | 条件 | 条件 |
| Algebra05/06 | 优先 | 优先 | 条件：KC映射 | 条件：步骤汇总 | 条件 | 条件 |
| Junyi及题目表 | 优先 | 优先 | 优先：有先修字段 | 优先 | 条件：先修可用，文本有限 | 条件 |
| OLI操作/步骤 | 优先 | 优先 | 条件：KC映射 | 优先：transaction | 条件：资源目录 | 条件 |
| OULAD | 条件：活动量 | 优先：天/周 | 弱：无KC | 条件：仅日/周模式 | 条件：课程级 | 条件：需粗化 |
| EdNet-KT1 | 条件：作答/用时 | 优先 | 条件：tags关联图 | 条件：汇总 | 条件：缺正文 | 条件 |
| EdNet-KT2/3/4 | 优先：3/4更丰富 | 优先 | 条件：tags | 优先 | 条件：缺正文/先修 | 条件 |
| MoocRadar | 待取 | 待取 | 待取 | 待取 | 待取：detail/concepts | 待取 |
| FoundationalASSIST | 待取 | 待取 | 待取：Skills表 | 待取 | 待取：Problem Body | 待取 |
| DBE-KT22 | 待取 | 待取：time_taken不是间隔 | 待取：关系表 | 待取 | 待取 | 待取 |

跨领域迁移没有单库“直接满足”的选项。优先准备数学和英语两个完整、粒度可比的日志版本，再决定公共动作空间。
