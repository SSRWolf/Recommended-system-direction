# 从行为子集搜索走向隐性表征学习：解耦、对比学习与推荐公平性

整理与检索日期：2026-11-04。本文承接[行为子集与推荐刻板印象放大的讨论](2026-11-03-behavior-subset-stereotype-discussion.md)，归纳研究反馈并整理相关论文。以下方案是待验证的研究设计，不代表已经证明的创新点。只保留讨论摘要，不转载私人聊天记录。

## 1. 研究问题如何调整

原始想法是：定义刻板印象指标，删除不同的行为子集，观察指标变化，寻找最能解释推荐偏差的子集。它直观、可用于验证，但穷举长度为 n 的历史存在 2^n 个子集；若每次还重训推荐器，成本更高。固定模型下修改输入与删除训练数据后重训，是不同干预，不能混用结论。

讨论反馈建议探索深度模块学习隐性表征，并用对比学习引导发现与不公平有关的因素。这不等于完全放弃行为子集，而是把子集搜索放到表征学习之后：

```text
行为序列或用户—物品图
        ↓
深度编码器：学习行为之间的关联
        ↓
潜在意图／多因素表征：分离不同兴趣或背景信号
        ↓
对比、互信息或对抗目标：引导需要保留与区分的信息
        ↓
检验哪些因素与预先定义的不公平输出有关
        ↓
回溯相关行为，形成少量候选子集
        ↓
通过删除、替换或表征干预验证，评估准确率与公平性
```

更具体的研究问题可以是：**能否学习用户行为中的多因素隐性表征，并识别其中在特定推荐模型中放大刻板关联、压制其他有证据支持的兴趣的因素，再将其关联到可验证的行为片段？**

这里有三层证据：表征包含某类信息；该信息与不公平输出相关；干预该因素能够改变输出。前两层不能直接推出第三层。模型训练也有成本，应与候选子集搜索的总计算量实际比较。

## 2. 论文清单：发表在哪里、什么时候、解决哪一部分

时间口径：AAAI 的具体日期取官方页面 Published 字段；会议日期明确标为会议举行时间，不冒充论文上线日；没有核实具体上线日的条目只列正式论文集年份。预印本首次提交时间单列，不能当作正式发表时间。本清单是围绕当前问题的定向调研，不是系统性综述。

| 论文／方法 | 正式发表地点 | 时间及口径 | 可借鉴模块 | 与当前任务的距离 |
|---|---|---|---|---|
| [Intent Oriented Contrastive Learning for Sequential Recommendation（IOCLRec）](https://ojs.aaai.org/index.php/AAAI/article/view/33390) | AAAI 2025，39(12):12748–12756 | 官方发表日 **2025-04-11** | 行为子序列、细粒度意图及单／多意图对比学习 | 很贴近“行为片段→隐性意图”；本身不是公平性方法 |
| [Intent Contrastive Learning for Sequential Recommendation（ICLRec）](https://doi.org/10.1145/3485447.3512090) | The Web Conference（WWW）2022，2172–2182 | 正式论文集 **2022**；[预印本](https://arxiv.org/abs/2202.02519)首次提交 **2022-02-05** | 序列编码、聚类意图原型、意图对比学习 | 隐性意图学习的基础阅读 |
| [Fair Representation Learning for Recommendation: A Mutual Information Perspective（FairMI）](https://ojs.aaai.org/index.php/AAAI/article/view/25617) | AAAI 2023，37(4):4911–4919 | 官方发表日 **2023-06-26** | 敏感属性编码器、兴趣编码器、对比互信息估计 | 最贴近“用学习目标引导表征与公平性”的部分 |
| [Disentangling User Interest and Conformity for Recommendation with Causal Embedding（DICE）](https://doi.org/10.1145/3442381.3449788) | WWW 2021 | 正式发表 **2021**；会议 **2021-04-19—23**；[预印本](https://arxiv.org/abs/2006.11011)首次提交 **2020-06-19** | 兴趣／从众双因素嵌入、按因果假设构造训练信号 | 学习如何把“多因素”变成有明确含义的解耦目标 |
| [Learning Disentangled Representations for Recommendation（MacridVAE）](https://proceedings.neurips.cc/paper/2019/hash/a2186aa7c086b46ad4e8bf81e2a3a19b-Abstract.html) | NeurIPS 2019，论文集第32卷 | 正式论文集 **2019** | 宏观概念与微观因素解耦的变分自编码器 | 理解“高层潜变量”；其中宏观概念不等于社会身份 |
| [Learning Fair Representations for Recommendation: A Graph-based Perspective（FairGo）](https://doi.org/10.1145/3442381.3450015) | WWW 2021 | 正式发表 **2021**；会议 **2021-04-19—23**；[预印本](https://arxiv.org/abs/2102.09140)首次提交 **2021-02-18** | 图邻域表征、敏感信息过滤与对抗学习 | 学习图结构如何携带并传播敏感信号 |
| [Learning Fair Representations for Recommendation via Information Bottleneck Principle（FairIB）](https://www.ijcai.org/proceedings/2024/273) | IJCAI 2024，2469–2477 | 正式论文集 **2024** | 信息瓶颈：保留交互信息、降低敏感信息 | 公平表征的另一种约束方式 |
| [Self-supervised Graph Learning for Recommendation（SGL）](https://doi.org/10.1145/3404835.3462862) | SIGIR 2021 | 正式发表 **2021**；会议 **2021-07-11—15** | 图增强、节点跨视图对比、图协同过滤 | 图对比学习基础与实验基线；不直接识别公平性 |
| [Disentangling confounders via counterfactual interventions for fair recommendations（FairDC）](https://www.sciencedirect.com/science/article/pii/S0957417426002010) | Expert Systems with Applications，第311卷，131288 | 卷期日期 **2026-05-15**，不是首次在线日期 | 混杂因素解耦、反事实干预、公平性学习 | 近期直接相关工作，需重点比较任务和假设 |

### 2.1 补充更新：五篇2025—2026年工作

补查日期：2026-11-04。下表在原九篇基础上新增五篇，共十四篇；原表的 IOCLRec（2025）与 FairDC（2026）不重复计数。新旧不是唯一排序标准，以下按与研究问题的关系选择。正式出版信息以出版社／会议官方页面为依据；只查到预印本的单独注明，不推定其已录用。

| 论文／方法 | 发表地点与状态 | 时间及口径 | 模块与用途 | 需要保留的边界 |
|---|---|---|---|---|
| [FairFU: A study of fair recommendation mechanisms for graph comparison by fusing structural interaction and information bottlenecks](https://www.sciencedirect.com/science/article/pii/S0925231226009616) | **Neurocomputing**，正式期刊论文，文章号133564 | **2026-07-01，卷期日期**；不等于首次上线日 | 深度交互融合、图扰动对比学习、双路径信息瓶颈；直接关联公平表征 | 约束敏感信息，不等于自动发现未知社会身份或解释具体行为子集 |
| [Intent-enhanced sequential recommendation via multi-view contrastive learning over stabilized essential intents（IeSRec）](https://link.springer.com/article/10.1007/s44443-026-01197-1) | **Journal of King Saud University Computer and Information Sciences**，38，文章号789 | **2026-08-26，官方 Published／Version of record 日期** | 意图增强、子序列编码与聚类、多视图意图对比 | 研究推荐意图；不是刻板印象或敏感群体公平方法 |
| [Intent-aware Diffusion with Contrastive Learning for Sequential Recommendation（InDiRec）](https://doi.org/10.1145/3726302.3730010) | **SIGIR 2025**，正式会议论文 | 正式论文集 **2025**；会议 **2025-07-13—18**；[预印本](https://arxiv.org/abs/2504.16077)首次提交 **2025-04-22** | 意图聚类指导条件扩散，生成对比学习视图 | 生成增强序列是训练手段，不是生成敏感身份；仍需公平目标 |
| [Intent-Driven Multi-level Augmentation with Contrastive Learning for Sequential Recommendation（IDMARec）](https://www.sciencedirect.com/science/article/abs/pii/S0950705125006525) | **Knowledge-Based Systems**，正式期刊论文，文章号113606 | **2025-08-03，卷期日期**；不等于首次上线日 | 隐性意图对比、多层增强、结合对比结构的GAN | 侧重稀疏与噪声处理，不能把所有少数兴趣当噪声删除 |
| [Intent-Guided Reasoning for Sequential Recommendation（IGR-SR）](https://arxiv.org/abs/2512.14034) | **arXiv预印本**，arXiv:2512.14034；本次未核实正式会议／期刊录用 | **2025-12-16，首次提交日期** | 冻结编码器与可学习token蒸馏多面意图、意图引导推理、一致性正则 | 高层意图不自动具备人口统计语义；预印本状态应与正式出版区分 |

### 2.2 新论文具体值得学什么

**FairFU：最贴近“深度表征＋对比学习＋公平约束”。** 论文结合图扰动对比、结构交互融合与双路径信息瓶颈，在图传播前后约束敏感信息。可重点看它如何区分协同推荐信号和敏感信号，以及对比目标与公平目标如何配合。它主要学习减少敏感信息依赖的表征；若自己的目标是“发现并解释放大偏差的行为”，仍需补充行为回溯与干预验证。该定位基于出版社摘要和方法概述，尚未完成全文复现级审读。[出版社原文](https://www.sciencedirect.com/science/article/pii/S0925231226009616)

**IeSRec：最贴近“从行为片段发现隐性意图”。** 方法通过子序列构造、意图增强、编码和聚类组织多视图对比信号。它适合作为 IOCLRec 的后续比较：怎样让增强保留意图，而不是破坏原始行为语义？针对本研究，尤其要检验那些被视为噪声或非典型偏好的交互，是否其实代表需要保护的次要兴趣；这是我们的评审问题，并非论文已证明的缺陷。[出版社全文](https://link.springer.com/article/10.1007/s44443-026-01197-1)

**InDiRec：用意图约束增强样本的生成。** 它先对序列表征做 K-means 聚类，再以意图表示引导条件扩散生成正视图，通过对比学习对齐原序列和增强序列。可用于研究“正样本究竟应该保留什么”，也衔接此前的扩散推荐调研。需要额外评估生成成本和次要兴趣是否被覆盖，不能把语义保持直接等同于公平保持。[SIGIR官方论文页面](https://sigir2025.dei.unipd.it/detailed-program/paper?paper=6bc24fc1ab650b25b4114e93a98f1eba)；[作者代码](https://github.com/qyp9909/InDiRec)

**IDMARec：多层增强与噪声控制的补充对照。** 出版社介绍其通过意图对比及包含对比结构的GAN进行增强与噪声平衡。适合与 InDiRec 比较不同增强策略，暂不作为公平性的直接基线。当前依据为出版社摘要与 Highlights，具体生成器、损失和样本构造需要精读全文后确认。[出版社页面](https://www.sciencedirect.com/science/article/abs/pii/S0950705125006525)

**IGR-SR：从隐性意图连接到高层推理。** 预印本提出潜在意图蒸馏、意图引导推理和一致性正则，可用于拓展“多面背景表征如何服务决策”的思路。但其高层意图、人类可读背景概念及敏感属性是不同概念，应分别验证。它不是已确认的公平性方法，发表状态也尚未核实到正式录用。[作者预印本](https://arxiv.org/abs/2512.14034)

### 2.3 更新后的阅读安排

1. **先读 IOCLRec＋IeSRec**：理解行为子序列、潜在意图和对比样本。
2. **再读 FairMI＋FairFU**：理解公平监督怎样进入表征学习，避免普通对比学习保留原有偏差。
3. **补读 InDiRec**：研究意图保持的增强视图，判断扩散模块是否确有必要。
4. **对照 DICE＋FairDC**：检查因素定义、解耦依据和干预假设。
5. **IDMARec、IGR-SR 作为扩展**：分别关注增强策略与高层意图推理。

最新文献进一步提示：**“学习隐性意图”与“过滤敏感信息”已经各有成熟研究路线，候选贡献应落在两者之间的可验证联系——哪些隐性因素在什么条件下放大指定偏差，以及如何回溯和干预。** 这是根据上述工作的研究判断，并非已经完成查重或证明新颖性。

## 3. 最值得精读的论文及阅读问题

### IOCLRec：先从行为片段学习意图

论文将行为历史分为多个子序列，以表达不同阶段的粗粒度意图，并设计细粒度意图、单意图和多意图三个对比学习模块。它非常贴近“一个用户的不同片段由不同隐性动机驱动”的设想。

可借鉴的是子序列构造与多意图训练方式。需要注意：子序列分段不等于自动找到任意不连续的最优行为子集；学出的意图也不等于消费阶层、职业或性别，更不自动具有公平性含义。精读时记录：如何分段、正负样本如何形成、如何避免多个意图被合并。[官方论文与摘要](https://ojs.aaai.org/index.php/AAAI/article/view/33390)

### ICLRec：隐性意图可以通过聚类与对比目标学出来

它对无意图标签的行为序列学习潜在意图分布，以聚类构造意图表示，让序列视图与对应意图保持一致，并在广义 EM 框架下交替更新意图与推荐模型。

适合回答“没有现成的背景标签，潜变量从哪里来”。但聚类编号没有天然的人类语义，解释需要额外证据。其目标主要是推荐效果及稀疏、噪声条件下的鲁棒性。精读时记录：聚类输入、原型更新频率、意图对比损失和推荐损失的关系。[作者预印本](https://arxiv.org/abs/2202.02519)

### FairMI：让表征学习具有明确的公平性方向

它使用敏感属性编码器捕获敏感信息，再由兴趣编码器学习保留非敏感信息的表征；通过互信息最小化与最大化，以及对比信息估计构造的界进行优化。

这与老师提到的“通过对比学习引导表征发现不公平”很接近，但论文更偏向过滤敏感信息，而非发现并解释导致不公平的行为子集。它需要敏感信息作为训练依据，不能直接宣称可无监督识别未知社会角色。精读时区分：对比互信息估计与普通实例对比学习分别在优化什么。[官方论文](https://ojs.aaai.org/index.php/AAAI/article/view/25617)

### DICE：给不同表征分支明确的建模含义

论文将用户兴趣与从众因素分开建模，并依据因果假设组织训练样本，而不是简单增加两个 embedding 分支后就宣称“已经解耦”。

可借鉴其因子定义、监督信号和验证设计。兴趣／从众与兴趣／敏感背景不是同一组因素，不能直接改名套用。精读时重点看：为什么某类训练样本能区分两种因素，以及这些假设在自己的数据里是否成立。[作者论文 PDF](https://fi.ee.tsinghua.edu.cn/~gaochen/papers/WWW2021-DICE.pdf)

### MacridVAE：高层概念与低层偏好如何分开

它用变分自编码器实现宏观概念和微观因素解耦，分别刻画意图概念及概念内偏好。可借鉴多因素组织方式和可控推荐实验。

但原文宏观概念的例子仍包括买衬衫、买手机等意图，不能据此声称已经发现“高收入白领女性”这类社会画像。概念层级提升需要独立定义、标注和验证。[官方论文](https://proceedings.neurips.cc/paper/2019/hash/a2186aa7c086b46ad4e8bf81e2a3a19b-Abstract.html)

### FairGo、FairIB、SGL 与 FairDC：各自补哪一块

- **FairGo**：从图邻域考虑敏感信息，用过滤器与对抗训练学习公平表征。适合当前已有 GCN 基础的学习路径；敏感属性可预测性与推荐结果群体差距应分别评估。[作者论文 PDF](https://www.microsoft.com/en-us/research/uploads/prod/2021/06/WWW2021_Learning-Fair-Representations-for-Recommendation-A-Graph-based-Perspective.pdf)
- **FairIB**：最大化用户表征与观测交互的互信息，同时最小化其与敏感属性的互信息。可借鉴保留推荐信号与抑制敏感信号的权衡；不等于自动命名未知背景因素。[官方论文](https://www.ijcai.org/proceedings/2024/273)
- **SGL**：通过节点丢弃、边丢弃、随机游走等构造图视图，以节点对比学习辅助推荐。适合做图对比基线；随机增强可能删掉本就稀少的兴趣证据，自己的任务需检查这一点。[作者论文 PDF](https://staff.ustc.edu.cn/~hexn/papers/sigir21-SGL.pdf)
- **FairDC**：将混杂因素解耦与反事实干预引入公平推荐，适合检查已有工作是否覆盖自己的问题。这里只依据出版社摘要与方法概述定位，尚未完成全文复现级审读，不能据此断言自己的方案有新颖性。[出版社页面](https://www.sciencedirect.com/science/article/pii/S0957417426002010)

建议阅读顺序：**IOCLRec → ICLRec → FairMI → DICE**，再补 FairGo／FairIB；MacridVAE 与 SGL 用于基础模块学习，FairDC 用于近期相关工作对照。

## 4. 一个可以逐步验证的方案

以下是综合文献提出的候选方案，不是任何一篇论文的原模型。

### 第一步：先把“不公平”定义清楚

选择一个有明确评估条件的数据集，说明是否有可信的敏感属性标签、历史偏好证据、推荐曝光和反馈。不要由口红、裙子等行为直接认定用户的性别、收入或职业；这些行为可以对应自用、送礼或其他情境。

把三个问题分别测量：

1. **信息泄漏**：表征是否能预测已知敏感属性？用独立探针和留出数据测量。
2. **结果不公平**：不同群体是否存在定义清楚的推荐质量、曝光或机会差距？
3. **刻板关联放大**：在合理控制真实偏好与候选供给后，推荐是否比基准更依赖某种群体—内容关联？该指标需要单独定义，不能直接用前两项代替。

没有敏感标签时，可以探索潜在行为群体和偏好覆盖，但不能把这些簇直接称为真实人口群体，也不能宣称完成了相应群体公平验证。

### 第二步：从一个简单的表征模块开始

采用一个序列编码器，先参考 ICLRec 或 IOCLRec 学习多个意图；如果问题主要关心用户—商品关系传播，则选择图编码器。编码器选择由数据和研究问题决定，不需要同时堆叠 GCN、LSTM、Transformer。

得到多个潜在因素后，检查它们是否稳定、是否塌缩为同一种偏好、是否只是热门度或行为长度的编码。此阶段先验证表征质量，不提前赋予社会身份名称。

### 第三步：构造具有任务含义的对比信号

普通“同一用户两个随机视图”为正样本，主要鼓励一致性，可能把已有偏差一并保留。对比学习本身不知道什么是不公平。

候选做法是在有证据支持的条件下，构造兴趣尽量相近而背景不同的匹配样本，或经过约束的行为视图；同时检查两者是否真正保留了目标兴趣。不能把“敏感属性不同”直接当作语义负样本，否则可能强化群体分离。

也可以先借鉴 FairMI／FairIB 的信息约束作为公平基线，再研究它是否会误删有用的次要兴趣。多个损失应逐个加入并做消融，不应一开始就同时启用全部模块。

### 第四步：回溯行为并做小规模干预验证

利用归因、门控或稀疏选择器得到候选行为，再进行受控删除或替换。注意力权重只能提供候选线索，不是因果证据。

至少比较同等大小的随机子集、近期子集、热门商品子集和学习得到的子集，并尽量匹配时间分布与商品流行度。固定模型修改输入，可解释该模型的局部响应；删除训练交互后重训，研究的是训练数据影响，应单独报告。

候选子集若能改变指定指标，还要检查准确率与其他兴趣覆盖是否恶化。删减带来的分布外输入和历史长度变化，是需要控制的替代解释。

### 第五步：报告可解释性与干预效果，而不只报告推荐准确率

| 检验目标 | 建议证据 |
|---|---|
| 推荐有效性 | Recall／NDCG 等，统一候选集合与切分协议 |
| 结果公平性 | 预先定义的群体指标及置信区间，不只敏感探针准确率 |
| 表征有意义 | 跨随机种子的稳定性、因素差异、外部标签或人工审查 |
| 子集具有解释力 | 同等预算对照、删除与保留实验、替换实验 |
| 次要兴趣被保留 | 有历史或后续反馈支持的兴趣覆盖，而不只是商品类别数 |
| 方法值得使用 | 训练成本、候选生成成本、干预次数与推理开销 |

## 5. 后续检索关键词

```text
"sequential recommendation" "latent intent" "contrastive learning"
"subsequence" "intent" "recommendation"
"disentangled representation learning" "recommendation" "fairness"
"fair representation learning" "recommendation" "mutual information"
"recommendation" "sensitive attribute leakage"
"recommendation" "counterfactual explanation" "user history"
"recommendation" "rationale extraction"
"recommendation" "stereotype amplification"
```

当前最需要补齐的不是再选一种编码器，而是：定义要解释的输出偏差，确定监督信息来源，并说明什么样的对比关系能够让隐性因素与该偏差建立可检验的联系。
