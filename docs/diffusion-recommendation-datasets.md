# 扩散推荐数据集：官方入口、字段与复现说明

核查日期：2026-10-16。对应[扩散推荐中文导读](2026-10-16-diffusion-generative-recommendation.md)。

本页保存可获取的数据入口、字段与实验建议。遵循本仓库资料范围，不再分发第三方原始数据；例如 MovieLens 官方条款限制未经许可再分发。下载后按各数据源条款使用。未对所有下载地址执行实际下载测试。

## 1. 数据选择表

| 数据 | 官方获取入口 | 主要内容 | 适合的实验 | 需要注意 |
|---|---|---|---|---|
| MovieLens-1M | [GroupLens 页面](https://grouplens.org/datasets/movielens/1m/)、[ZIP](https://files.grouplens.org/datasets/movielens/ml-1m.zip)、[README](https://files.grouplens.org/datasets/movielens/ml-1m-README.txt) | 用户评分、电影标题与类型、评分时间 | 快速检查训练、排序与采样流程 | 评分不是点击，评分时间未必等于观看时间；需定义正反馈阈值 |
| Amazon Reviews 2023 | [官方文档](https://amazon-reviews-2023.github.io/main.html)、[官方数据仓库](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023) | 评论、评分、用户与商品 ID、时间戳、商品元数据 | 序列推荐、文本条件、新商品分析 | 先选单个领域；不是旧版 Amazon Beauty 等基准的可直接替代品 |
| Amazon 较早版本 | [2018 数据入口](https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/)、[更早数据入口](https://mcauleylab.ucsd.edu/public_datasets/data/amazon/index_snap.html) | 评论与商品元数据 | 对齐较早论文的数据版本 | 必须以目标论文代码及说明为准；类别名称相同不代表样本、ID 或切分相同 |
| KuaiRec | [作者仓库及下载说明](https://github.com/chongminggao/KuaiRec) | 短视频观看行为、观看比例、类别等 | 行为反馈推荐、多样性和覆盖分析 | small 与 big 矩阵用途不同；不能把观看比例直接称为点赞 |
| DiffRec 作者处理版 | [datasets 目录](https://github.com/YiyanXu/DiffRec/tree/main/datasets) | Amazon-Book、Yelp、MovieLens-1M 的论文实验输入 | 尽快复现 DiffRec | 区分 clean/noisy；L-DiffRec 的部分预训练嵌入需要额外获取 |
| DreamRec 作者处理版 | [data 目录](https://github.com/YangZhengyi98/DreamRec/tree/main/data)、[运行说明](https://github.com/YangZhengyi98/DreamRec) | YooChoose、KuaiRec、Zhihu 等实验数据入口 | 对齐 DreamRec 的实验设置 | 处理版与原始完整数据不等价，文件格式和划分以仓库为准 |

上述数据事实以各行官方链接为准。建议先使用作者处理版复现，再用独立、明确记录的切分做扩展实验。

## 2. 常见字段

### MovieLens-1M

`ratings.dat` 的原始格式：

```text
UserID::MovieID::Rating::Timestamp
```

`movies.dat`：

```text
MovieID::Title::Genres
```

来源：[官方 README](https://files.grouplens.org/datasets/movielens/ml-1m-README.txt)。若把 Rating 转成二值反馈，公开阈值和过滤规则；不要把不满足阈值的评分悄悄改成未观测值而不记录。

### Amazon Reviews 2023

常用评论字段包括 `user_id`、`parent_asin`、`asin`、`rating`、`timestamp`、`title`、`text`；元数据包括商品标题、类别等。以官方配置为准，通常用 `parent_asin` 关联商品元数据，避免混淆商品变体 ID。评论的 `title` 是评论标题，不是商品标题。[官方字段说明](https://amazon-reviews-2023.github.io/main.html)

官方页面的不同示例可能出现 `sort_timestamp`/`timestamp`、`helpful_votes`/`helpful_vote` 等命名差异。写读取程序前应检查实际下载文件，保存 schema 和版本，不能只照搬旧代码。

### KuaiRec

常用行为字段包括 `user_id`、`video_id`、`play_duration`、`video_duration`、`timestamp`、`watch_ratio`，字段随文件类型不同。`watch_ratio` 表示观看时长与视频时长的比例，可能超过 1。主反馈不是 like；阈值、截断与重复观看处理都需说明。[官方仓库](https://github.com/chongminggao/KuaiRec)

近完全观测指 small matrix（约 99.6% 密度），不是整个库。官方曾更新视频 ID 索引，下载交互与侧信息时应固定相同版本。

## 3. 统一成序列样本

可以在本地转换为以下自定义格式；这不是每个数据集原生表头：

```text
user_id,item_id,timestamp,feedback
```

概念示例：

```text
历史：[item_12, item_35, item_08]
目标：item_27
```

历史作为扩散模型的条件，目标商品作为训练时的去噪对象。多次交互去重、序列截断、短序列过滤、冷启动处理以及时间相同的排序规则，都应固定并保存。

## 4. 防止“数据相同，实验却不可比”

- 数据年份：Amazon 2014/2018/2023 不混用；论文中的 Beauty 不能默认映射到 2023 All_Beauty。
- 时间可见性：预测时只能使用此前发生的行为、评论与已知商品信息。元数据可能不是历史快照。
- 切分：记录随机切分、逐用户留一法或全局时间切分。逐用户留一并不自动消除跨用户的未来信息泄漏。
- ID 与商品库：保存映射，不能从另一个版本拿嵌入直接套用。
- 评估候选：记录全物品排序还是采样负例，是否过滤已交互商品，是否允许重复消费。
- 反馈定义：评分、点击、观看比例的含义不同；没有交互不等于明确负反馈。
- 训练标签：不能使用测试目标构造条件、选择采样结果或调节超参数。
- 资源统计：连续生成仍需商品匹配，延迟包含整个推荐过程。

以上是建议采用的实验规范。模型原始配置可用于复现，但改变协议后应重新运行全部对照，不沿用论文表格数字。

## 5. 建议的最小实验组合

**学习流程**：MovieLens-1M + 一个简单基线 + 一个扩散模型。目标是确认数据与评估正确，不以单一数据集结果声称方法泛化。

**复现序列推荐**：从 DreamRec 或 DiffuRec 选择一个作者数据配置，在同一划分上训练 SASRec 与扩散模型，核查排名指标与训练成本。

**扩展研究**：再添加第二个领域；需要文本条件时选择相应 Amazon 子集，需要观看行为分析时考虑 KuaiRec。

建议保存：数据版本及校验和、来源 URL、下载日期、处理脚本版本、用户/物品/交互数、划分统计、随机种子、候选策略、训练配置和评估结果。

本文的数据易用性排序是研究安排建议，不是运行结果。当前仅完成资料与入口核对，尚未训练模型或生成可复现指标。
