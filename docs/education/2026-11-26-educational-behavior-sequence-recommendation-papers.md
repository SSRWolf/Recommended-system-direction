# 教育行为序列推荐论文广泛检索：出处、链接与中文摘要（25 篇）

> 整理日期：2026-11-26。来自上一轮广泛检索清单，并重新检索出版方、会议及学术索引的原始摘要。**中文摘要是依据可访问的摘要/方法概述所作的概括，不是官方摘要全文翻译**；对无法直接核实的数据集和实验细节不作臆测。  
> 研究主线：**用户行为事件流 → 局部行为子序列 → 行为因子与时间依赖 → 学习状态/学习需求 → 习题、资源、学习路径推荐**。

## 口径与阅读说明

- 本清单共 **25 篇**，按实际任务分类，包含**直接教育推荐、过程/序列挖掘、知识追踪支撑、多行为通用推荐、2026 近期研究**。
- “使用学习者历史序列”并不等于“使用 EdNet 原始 `action_type` 操作事件”；课程选课序列、题目正误序列、学习资源点击日志是不同粒度。
- 发表年份主要采用期刊卷期/会议年份；对提前在线发表的文章另外注明，避免年份冲突。
- 下列条目中的链接优先为 DOI 或出版方页面。**严禁从摘要推断论文明确证明了学生真实知识增益或学习需求因果机制。**
- 相关前期笔记：[2026-11-24 LBKT、EdNet 与行为序列建模](2026-11-24-lbkt-ednet-weekly-notes.md)、[2026-11-16 教育研究方向与数据](2026-11-16/README.md)。

## 快速导航

| 类别 | 篇数 | 主要关注 |
|---|---:|---|
| A. 直接教育推荐 | 6 | 多行为状态、习题推荐、路径规划 |
| B. 过程和序列挖掘 | 6 | 频繁模式、教育过程模型、路径 |
| C. 知识状态与课程序列 | 5 | 知识追踪、课程偏好、解释规则 |
| D. 对比学习与多行为动态依赖 | 3 | 跨视图表示学习、序列依赖 |
| E. 2026 年及近期 | 5 | EdNet-KT4、知识决策、在线增益 |


## A. 直接教育推荐：多行为、知识追踪、资源与路径

### 1. Learning path recommendation with multi-behavior user modeling and cascading deep Q networks

- **出处**：Knowledge-Based Systems，2024
- **原文链接**：[出版方 / DOI](https://doi.org/10.1016/j.knosys.2024.111743)
- **摘要依据**：期刊摘要与方法概述
- **中文摘要（概述）**：cDQN-PathRec 将学习者的多类型平台交互、知识背景和学习偏好纳入基于知识图谱的多行为 Transformer 用户建模，并采用级联深度 Q 网络为短期变化需求与长期学习目标选择学习路径。其强化学习部分考虑局部与整体奖励。
- **与本研究的联系**：操作行为→学生状态→路径推荐；优先检查原文中多类行为的定义与时序编码。

### 2. Recommendation of Learning Resources for MOOCs Based on Historical Sequential Behaviours

- **出处**：Expert Systems，2025
- **原文链接**：[出版方 / DOI](https://doi.org/10.1111/exsy.70034)
- **摘要依据**：出版方摘要
- **中文摘要（概述）**：从 MOOC 学习者的历史课程学习顺序挖掘频繁高效用序列模式（FHUSP），结合学习时长、成绩和参与等信息区分有用的历史学习路径，再根据目标学习者历史与模式匹配推荐资源。
- **与本研究的联系**：序列模式怎样参与推荐决策；注意主要是课程序列，不是音视频级事件流。

### 3. Multi-knowledge enhanced graph convolution for learning resource recommendation

- **出处**：Knowledge-Based Systems，2024
- **原文链接**：[出版方 / DOI](https://doi.org/10.1016/j.knosys.2024.111521)
- **摘要依据**：期刊摘要
- **中文摘要（概述）**：提出多知识增强图卷积框架 MkEGC，构造学习资源—知识和学习者—知识两类关联图，通过双图卷积传播获取高阶语义与多类型知识连接信息，以缓解学习资源推荐的稀疏性并增强个性化表征。
- **与本研究的联系**：图结构辅助资源推荐的直接参照；不应简单当成事件级顺序挖掘论文。

### 4. MLKT4Rec: Enhancing Exercise Recommendation Through Multitask Learning With Knowledge Tracing

- **出处**：IEEE Transactions on Computational Social Systems，2025
- **原文链接**：[出版方 / DOI](https://ieeexplore.ieee.org/document/10806780)
- **摘要依据**：IEEE 摘要
- **中文摘要（概述）**：构建知识追踪增强的多任务习题推荐框架 MLKT4Rec，使用图神经网络获取习题推荐场景的节点表示，并联合学习知识追踪和推荐相关目标，以改善学生状态利用与习题排序。
- **与本研究的联系**：比较知识追踪损失与推荐损失如何联合设计；其任务是习题推荐。

### 5. Personalized Exercise Recommendation with Semantically-Grounded Knowledge Tracing

- **出处**：NeurIPS，2025
- **原文链接**：[出版方 / DOI](https://proceedings.nips.cc/paper_files/paper/2025/hash/13707aad517ddd6c09ea02e0f55e1e7a-Abstract-Conference.html)
- **摘要依据**：会议官方摘要及作者开源说明
- **中文摘要（概述）**：ExRec 指出以知识追踪驱动的习题推荐常忽视题目语义和知识发展的结构化顺序；框架利用习题知识概念与解题步骤语义学习学生状态，再将其用于个性化习题推荐与学习轨迹建模。
- **与本研究的联系**：推荐效果和知识状态之间的连接；非 EdNet 原始微操作方法。

### 6. Learning path recommendation based on forgetting factors and knowledge graph awareness

- **出处**：Information Processing & Management，2026（2025 在线）
- **原文链接**：[出版方 / DOI](https://www.sciencedirect.com/science/article/pii/S0306457325003346)
- **摘要依据**：出版方摘要及卷期信息
- **中文摘要（概述）**：FKGRec 将知识遗忘与知识图谱意识引入学习路径推荐，使推荐不仅考虑新知识探索，也覆盖已学知识复习。作者将遗忘与动作空间设计相联系，并以路径决策平衡巩固与扩展。
- **与本研究的联系**：可将已发现的行为模式用在复习/新学资源选择上；注意在线发表与卷期年份不同。


## B. 行为/课程过程挖掘与路径推荐

### 7. Personalized process–type learning path recommendation based on process mining and deep knowledge tracing

- **出处**：Knowledge-Based Systems，2024
- **原文链接**：[出版方 / DOI](https://doi.org/10.1016/j.knosys.2024.112431)
- **摘要依据**：出版方摘要
- **中文摘要（概述）**：利用深度知识追踪给历史学习日志标注知识状态，再采用过程挖掘生成个性化过程型学习路径；路径不只是线性顺序，还显式刻画学习对象间的顺序、并行与选择关系。
- **与本研究的联系**：最接近‘行为过程结构→知识状态→推荐路径’的研究链条。

### 8. Course Recommendation based on Sequences: An Evolutionary Search of Emerging Sequential Patterns

- **出处**：Cognitive Computation，2022
- **原文链接**：[出版方 / DOI](https://doi.org/10.1007/s12559-022-10015-5)
- **摘要依据**：出版方摘要
- **中文摘要（概述）**：以学生已经修读的课程序列为基础，利用进化式搜索识别具有区分性的、新兴的序列模式，为后续课程生成推荐索引与建议。重点在课程选择顺序及不同学习群体的模式差异。
- **与本研究的联系**：可借鉴区分性序列挖掘；不是题内操作日志。

### 9. Personalized Learning Path Recommendations: Fusing Knowledge Graph Embedding, Sequence Mining, and Collaborative Filtering

- **出处**：2024 IEEE International Conference on Big Data (BigData)，2024
- **原文链接**：[出版方 / DOI](https://doi.org/10.1109/BIGDATA62323.2024.10825001)
- **摘要依据**：IEEE 摘要
- **中文摘要（概述）**：融合知识图谱嵌入、协同过滤与序列模式挖掘（SPM），为在线学习者生成视频学习资源序列；将资源语义联系与用户学习轨迹一起用于个性化路径排序。
- **与本研究的联系**：学习行为序列、知识图与协同过滤的组合路线。

### 10. Using Process Mining for Learning Resource Recommendation: A Moodle Case Study

- **出处**：Procedia Computer Science（KES 相关论文），2021
- **原文链接**：[出版方 / DOI](https://www.sciencedirect.com/science/article/pii/S1877050921015763)
- **摘要依据**：出版方摘要
- **中文摘要（概述）**：研究 Moodle 学习管理系统的事件日志，通过教育过程挖掘提取学生访问学习资源的过程模型，面向学习资源推荐分析可重复的学习路径和活动结构。
- **与本研究的联系**：平台原始事件如何变成过程模型；与 EdNet 用户事件序列最接近的数据形式之一。

### 11. Mining sequential patterns with flexible constraints from MOOC data

- **出处**：Applied Intelligence，2022
- **原文链接**：[出版方 / DOI](https://doi.org/10.1007/s10489-021-03122-7)
- **摘要依据**：开放获取摘要
- **中文摘要（概述）**：针对 MOOC 注册/选课序列，研究如何在序列模式挖掘时加入灵活约束，减少海量候选模式并得到更有用的序列规律。其核心是序列模式挖掘而非直接输出推荐列表。
- **与本研究的联系**：用于行为片段筛选与约束设计；明确标记为推荐前置方法。

### 12. Towards prescriptive analytics of self-regulated learning strategies: A reinforcement learning approach

- **出处**：British Journal of Educational Technology，2024
- **原文链接**：[出版方 / DOI](https://doi.org/10.1111/bjet.13429)
- **摘要依据**：出版方摘要
- **中文摘要（概述）**：针对在线环境中的自我调节学习（SRL），使用强化学习学习不同调节过程的策略组合，以学习目标奖励评估何种学习策略顺序可能更有效，关注从描述学习过程走向学习支持决策。
- **与本研究的联系**：把过程模式转化为支持策略的启发；不是标准 Top-K 资源推荐。


## C. 知识状态、课程序列与教育推荐（含支撑研究）

### 13. Knowledge-aware sequence modelling with deep learning for online course recommendation

- **出处**：Information Processing & Management，2023
- **原文链接**：[出版方 / DOI](https://www.sciencedirect.com/science/article/pii/S0306457323001140)
- **摘要依据**：出版方摘要
- **中文摘要（概述）**：提出知识感知课程序列推荐方法 KSCR，通过课程知识图组织异构课程信息，再用深度序列建模学习课程依赖及用户学习顺序，提升对在线课程偏好的表示。
- **与本研究的联系**：课程知识关联和长短期序列结合；学习粒度以课程为主。

### 14. Exercise recommendation based on knowledge concept prediction

- **出处**：Knowledge-Based Systems，2021
- **原文链接**：[出版方 / DOI](https://www.sciencedirect.com/science/article/pii/S0950705120306109)
- **摘要依据**：出版方摘要
- **中文摘要（概述）**：KCP-ER 利用循环神经网络预测习题所覆盖的知识概念，并通过深度知识追踪估计学生对知识概念的掌握情况，将题目内容覆盖与学习者状态结合生成习题推荐。
- **与本研究的联系**：知识概念预测与学生掌握状态的组合方法。

### 15. EKT: Exercise-Aware Knowledge Tracing for Student Performance Prediction

- **出处**：IEEE Transactions on Knowledge and Data Engineering，2021（2019 在线）
- **原文链接**：[出版方 / DOI](https://doi.org/10.1109/TKDE.2019.2924374)
- **摘要依据**：IEEE 摘要
- **中文摘要（概述）**：EKT 以学生历史答题序列预测未来习题表现，利用题目内容的双向 LSTM 表示和知识概念关联，构建更具知识维度解释性的学生状态追踪方式。虽然服务于个性化习题推荐的基础能力，但**论文本身的直接预测目标是学生表现，不是推荐列表**。
- **与本研究的联系**：知识追踪经典参考基线，须单独标为非直接推荐研究。

### 16. Personalized recommendations for learning activities in online environments: a modular rule-based approach

- **出处**：User Modeling and User-Adapted Interaction，2024
- **原文链接**：[出版方 / DOI](https://doi.org/10.1007/s11257-024-09396-z)
- **摘要依据**：出版方摘要
- **中文摘要（概述）**：提出在线学习活动推荐的模块化规则框架，利用不同类型的种子活动、规则及推荐上下文支持知识巩固、探索等目标；每个推荐项可以追溯到具体规则、规则类型和触发活动。
- **与本研究的联系**：可解释性与可控推荐的参考；不是深度事件序列表示学习。

### 17. Learning multi-behavior user intent for session-based recommendation

- **出处**：Expert Systems with Applications，2025
- **原文链接**：[出版方 / DOI](https://www.sciencedirect.com/science/article/pii/S0957417424021365)
- **摘要依据**：出版方摘要
- **中文摘要（概述）**：提出多行为用户意图会话推荐模型 MUIR，区别对待会话中的不同类型行为，联合学习交互之间的关系与短期意图，改善多行为条件下的物品推荐。**属于通用推荐而非教育专用。**
- **与本研究的联系**：多行为与会话序列融合的可迁移技术。


## D. 对比学习与多行为动态图（含通用方法）

### 18. Contrastive Personalized Exercise Recommendation With Reinforcement Learning

- **出处**：IEEE Transactions on Learning Technologies，2024（2023 在线）
- **原文链接**：[出版方 / DOI](https://ieeexplore.ieee.org/document/10290979)
- **摘要依据**：IEEE 摘要及卷期核对
- **中文摘要（概述）**：提出 RCL4ER，将对比学习用于个性化习题推荐的表示优化，同时利用强化学习建模习题选择决策；研究核心是结合表征判别能力与序列式推荐决策。
- **与本研究的联系**：教育场景中对比学习与推荐的直接参照，优先核对正负样本构造。

### 19. Integrating learners’ knowledge background to improve course recommendation fairness: A multi-graph recommendation method based on contrastive learning

- **出处**：Information Processing & Management，2024
- **原文链接**：[出版方 / DOI](https://www.sciencedirect.com/science/article/pii/S0306457324001109)
- **摘要依据**：出版方摘要
- **中文摘要（概述）**：提出 CLGADN，综合学习者已有课程知识背景，使用多图结构及对比学习缓解课程推荐的数据稀疏与流行度偏置，兼顾推荐准确性和知识背景相关的公平性。
- **与本研究的联系**：知识背景、图对比学习、推荐公平性结合的参考。

### 20. MBDL: Exploring dynamic dependency among various types of behaviors for recommendation

- **出处**：Information Systems，2024
- **原文链接**：[出版方 / DOI](https://www.sciencedirect.com/science/article/pii/S0306437924000656)
- **摘要依据**：出版方摘要
- **中文摘要（概述）**：提出多行为动态依赖学习方法 MBDL，用对比学习保持跨行为类型的长期模式一致性，并通过多头注意力捕获短期行为之间的动态依赖。**非教育数据场景**。
- **与本研究的联系**：最适合迁移到 EdNet 的多行为动态依赖/对比学习设计。


## E. 2026 年及近期候选工作

### 21. Context-aware sequential course recommendation via conditional variational autoencoders and transformer architectures in IoT-enabled E-learning systems

- **出处**：Scientific Reports，2026
- **原文链接**：[出版方 / DOI](https://doi.org/10.1038/s41598-026-45764-y)
- **摘要依据**：出版方摘要及正文概述
- **中文摘要（概述）**：在在线教育场景下结合条件变分自编码器与 Transformer，建模用户/课程表示的不确定性、时间学习模式和 IoT 情境特征，形成情境感知的课程序列推荐框架。
- **与本研究的联系**：拓展场景特征与序列推荐；非细粒度学习操作行为。

### 22. Personalised learning path optimisation in digital English learning environments via multi-factor knowledge tracing and reinforcement learning

- **出处**：International Journal of Information and Communication Technology，2026
- **原文链接**：[出版方 / DOI](https://www.inderscience.com/info/e_inarticle.php?artid=153797)
- **摘要依据**：出版方摘要
- **中文摘要（概述）**：研究多因子融合知识追踪（MFFKT）与强化学习联合的英语学习路径优化，综合行为序列、题目属性、知识结构和时间特征，用估计的学习状态驱动长期奖励决策；摘要报告使用 ASSISTments 2017 与 EdNet-KT4。
- **与本研究的联系**：**与 EdNet 数据源直接重合**；需要精读具体使用了哪些 KT4 操作字段。

### 23. Analysing student learning pathways in educational systems using CRNN-based multichannel temporal modelling

- **出处**：Connection Science，2026
- **原文链接**：[出版方 / DOI](https://doi.org/10.1080/09540091.2026.2682059)
- **摘要依据**：出版方摘要及方法概述
- **中文摘要（概述）**：提出结合多通道 CRNN 与图卷积的 PathNet-GC 框架，分析异构学习行为时间序列及其结构关联，并通过行为分类、学习阶段预测和异常检测等任务检验模型。**主要是学习路径分析，不是直接的教育推荐算法**。
- **与本研究的联系**：排查与 EdNet 多通道事件序列建模的已有工作重合度。

### 24. A concept-aware intelligent decision support system for effective personalized learning path recommendation

- **出处**：Expert Systems with Applications，2026
- **原文链接**：[出版方 / DOI](https://www.sciencedirect.com/science/article/pii/S0957417426015824)
- **摘要依据**：出版方摘要及方法概述
- **中文摘要（概述）**：构建概念感知的个性化路径决策系统，结合知识概念编码、序列解码、知识追踪辅助目标及策略梯度，处理概念依赖、延迟反馈与教学质量约束。
- **与本研究的联系**：知识结构、序列决策与 RL 联合方案。

### 25. A Bandit-Based Approach to Educational Recommender Systems: Contextual Thompson Sampling for Learner Skill Gain Optimization

- **出处**：INFORMS Transactions on Education，2026
- **原文链接**：[出版方 / DOI](https://doi.org/10.1287/ited.2025.0174)
- **摘要依据**：期刊摘要及作者预印本信息
- **中文摘要（概述）**：将情境 Thompson Sampling 用于教育推荐，根据学习者背景/技能状态选择后续练习，优化技能增益目标，体现推荐问题中的在线探索与个性化决策。
- **与本研究的联系**：推荐目标从下一点击扩展到技能提升；严格区别观察增益与离线模拟收益。

## 最优先精读的五篇

| 顺序 | 论文 | 先确认的核心问题 |
|---|---|---|
| 1 | cDQN-PathRec | 多类学生事件的编码、序列状态和 RL 路径输出 |
| 2 | Personalized process–type learning path recommendation | 历史日志如何挖出顺序、并行、选择关系并进入路径推荐 |
| 3 | MOOCs Based on Historical Sequential Behaviours | 高频/高效用序列如何筛选与连接推荐 |
| 4 | MBDL（通用推荐） | 不同行为类型的长期/短期依赖与对比学习设计 |
| 5 | MFFKT + RL（EdNet-KT4） | 是否真正使用改选、排除、音视频等细粒度动作 |

## 面向 EdNet 的复现实验建议

1. **先核验真实字段**：用户文件、时间戳、动作类型、item_id、Contents 中可连接的题目/知识标签/正确答案；确认标签与实际推荐候选资源覆盖。
2. **以用户操作序列为原始样本**，用时间窗口、事件数量或可靠业务边界提取局部子序列；不能直接假设原始数据已经按题目切分。
3. 用统计基线（频次、2/3/4-gram、PrefixSpan）检验重复模式；再用 GRU/Transformer 编码子序列；外积用于行为因子之间的交互，**本身不保留顺序**。
4. 显式隔离**知识追踪预测**（AUC、RMSE、ACC）和**教育推荐**（Recall@K、NDCG@K、覆盖、多样性、学习目标代理指标）。如果没有真实推荐曝光和结果日志，离线下一资源预测不能解释为已证实的推荐干预学习增益。
5. 对比学习只在正样本构造能保持行为语义时引入；GNN 仅在确有题目—知识点/资源—知识点关系时使用。最终应针对知识难度和历史表现控制后验证**跨时间行为模式的额外预测价值**。

## 核验状态与范围说明

本清单对**标题及出版出处**做了出版方/索引层面的复核，对**摘要**提供忠实的中文概述；没有声称逐篇通读全文、核验所有实验指标或复现结果。原检索中部分论文属于相关方法而非直接教育推荐，已显式分组和标注。遇到官网摘要不可完整读取的条目，中文描述仅限能核实的公开信息；正式论文引用前请再检查作者、卷期与 DOI。
