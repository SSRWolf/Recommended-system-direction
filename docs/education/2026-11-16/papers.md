# 相关论文：准确出处、时间与中文摘要

核验日期：2026-11-16。P00—P09覆盖历史讨论中的综述与近期论文；P10—P13补充实验基线和方法来源。中文摘要均为重新撰写的简述，方法适配与阅读问题是本项目分析，不属于原作者结论。以出版方页面、正式论文或作者预印本为依据；部分ScienceDirect全文页面访问受限，已使用其公开索引摘要和出版方登记的DOI元数据核对书目，未声称完成全文复现。

## P00｜教育数据挖掘综述

**A Comprehensive Survey on Deep Learning Techniques in Educational Data Mining**。Yuanguo Lin, Hong Chen, Wei Xia, Fan Lin, Zongyue Wang, Yong Liu。*Data Science and Engineering* 10: 564–590，2025；在线发表2025-07-12，期次日期2025年12月。DOI：[10.1007/s41019-025-00303-z](https://doi.org/10.1007/s41019-025-00303-z)。另有[2023年起的预印本](https://arxiv.org/abs/2309.04761)，不要混用版本年份。

**中文摘要：** 综述深度学习在知识追踪、学生行为检测、成绩预测和个性化推荐中的应用，整理公开数据和处理工具，并讨论教育数据的复杂性与后续研究方向。适合先建立任务之间的对应关系。[出版方摘要](https://link.springer.com/article/10.1007/s41019-025-00303-z)

**适配与阅读：** 覆盖六方向的研究背景。用来明确输入、标签和评价对象，不能据综述认定某个新组合已具备创新性。

## P01｜DFIKT：多行为与知识状态

**Dual-domain knowledge fusion for interpretable knowledge tracing**。Tao Zhou, Guilin Li, Yanting Li, Renyue Zhang, Shenggen Ju。*Knowledge-Based Systems* 340: 115715，2026；卷期日期2026-05-12。DOI：[10.1016/j.knosys.2026.115715](https://doi.org/10.1016/j.knosys.2026.115715)。

**中文摘要：** 分别从题目与作答结果、用时与尝试和提示行为提取知识状态，通过高阶交互与门控注意力融合；进一步校准知识获取效率，提取概念级状态，并以单调约束进行响应预测。论文在四个公开数据集上报告预测与解释性实验。[出版方摘要与方法概述](https://www.sciencedirect.com/science/article/pii/S0950705126004557)

**适配与阅读：** 方向①的直接参考；ASSIST2012、Algebra、OLI具有相关行为字段。重点核查行为特征何时产生，以及所谓认知解释使用了什么独立证据。它没有直接提供“潜在学习需求”的人工真值。

## P02｜MTKT：多粒度时间

**Learning multi-granularity temporal characteristics for attention based knowledge tracing**。Youheng Bai, Xueyi Li, Zitao Liu, Yaying Huang, Teng Guo, Mingliang Hou, Weiqi Luo。*Neurocomputing* 655: 131338，2025；卷期日期2025-11-28。DOI：[10.1016/j.neucom.2025.131338](https://doi.org/10.1016/j.neucom.2025.131338)。

**中文摘要：** 面对不规则时间间隔、不同序列长度与多尺度学习过程，MTKT结合题目/时间表征、双注意力中的线性衰减偏置和因果交互卷积，捕获短长期依赖。论文比较预测准确性和长度外推性能。[出版方摘要](https://www.sciencedirect.com/science/article/pii/S0925231225020107)

**适配与阅读：** 方向②；需真实时间信息。ASSIST2015不足以重现时间间隔模块。阅读时区分elapsed time、相邻间隔、同KC重访间隔，以及训练长度外推与普通长序列测试。

## P03｜MHG-KT：图、时间和语义

**Towards explainable knowledge tracing through meta-path-free heterogeneous graph learning with large language models**。Olaniyan Deborah, Wario Ruth（姓名写法依出版方）。*Discover Artificial Intelligence* 6: 914，2026-08-25。DOI：[10.1007/s44163-026-02049-7](https://doi.org/10.1007/s44163-026-02049-7)。正式题名不以“MHG-KT:”开头。

**中文摘要：** 将无需手工元路径的异构图编码、Transformer时间建模和Llama 3 8B语义表示联合起来，通过跨模态注意力让结构与语义在学习过程中交互。论文在ASSISTments、EdNet和Junyi上评价知识追踪和迁移表现。[出版方正文与摘要](https://link.springer.com/article/10.1007/s44163-026-02049-7)

**适配与阅读：** 方向③、⑥。必须核对题干/提示文本究竟来自哪个版本，以及跨数据集迁移如何处理ID、图节点和测试可见性。当前Excel只有字段和极少样例，不能视为具备论文全部语义输入。作者报告的性能不等于本仓库已复现结果。

## P04｜IPDGKT：动态记忆交互图

**Information Processing Dynamic Graph For Knowledge Tracing**。Xiong Xiao, Shengyingjie Liu, Yue Li, Xiuling He, Jing Fang, Yangyang Li。*Information Processing & Management* 63(1): 104331，2026年1月。DOI：[10.1016/j.ipm.2025.104331](https://doi.org/10.1016/j.ipm.2025.104331)。

**中文摘要：** 以信息加工理论组织短期记忆激活、长期记忆感知和记忆应用三个模块。通过记忆交互图及处理网络建模练习中的知识吸收，再预测未来表现；论文以三个公开数据集和可视化实验检验模型。[出版方摘要](https://www.sciencedirect.com/science/article/pii/S0306457325002729)

**适配与阅读：** 方向②、③；动态记忆图不等于专家先修图。核查构图是否只用过去交互，并将机制启发与心理机制已验证区分。其DOI包含2025，但正式卷期是2026年；部分二级目录记为63(2)，此处按出版方页面与Crossref登记的63(1)记录。[作者代码入口](https://github.com/xxiongGG/IPDGKT-main)

## P05｜L-HAKT：LLM与双曲层级对齐

**Towards LLM-Empowered Knowledge Tracing via LLM-Student Hierarchical Behavior Alignment in Hyperbolic Space**。Xingcheng Fu, Shengpeng Wang, Yisen Gao, Xianxian Li, Chunpei Li, Qingyun Sun, Dongran Yu。*Proceedings of the AAAI Conference on Artificial Intelligence* 40(17): 14747–14755，AAAI-26；论文集页面发表于2026-03-14。DOI：[10.1609/aaai.v40i17.38494](https://doi.org/10.1609/aaai.v40i17.38494)。

**中文摘要：** 教师智能体解析题目与知识层级，学生智能体生成模拟学习行为，再在双曲空间对齐合成与真实行为，以表达难度感知、遗忘模式及层级差异。论文通过四个真实教育数据集检验L-HAKT。[会议官方摘要](https://ojs.aaai.org/index.php/AAAI/article/view/38494)

**适配与阅读：** 方向③、⑤的方法补充；需要题目语义和知识结构。合成行为不能作为真实学生需求的独立证据；应检查合成数据、教师模型和测试题是否发生信息交叉。本文主要任务仍是知识追踪，不是直接验证学习路径效果。

## P06｜行为模式能否泛化

**Does sequence mining uncover generalizable behavioral patterns? A methodological case study**。Esther Ulitzsch, Leonard Tetzlaff, Frank Goldhammer, Carolin Hahnel, Ulf Kroehne, Oliver Lüdtke。*Large-scale Assessments in Education* 14: 20，2026-03-26。DOI：[10.1186/s40536-026-00289-8](https://doi.org/10.1186/s40536-026-00289-8)。

**中文摘要：** 在PISA 2025数字世界学习单元的四项任务中，对比基于简单行为特征的聚类和基于序列相似度的聚类。两者得到相近且具有跨任务一致性的分组，并与表现和外部变量相关。作者强调结合理论与额外效度证据解释模式。[出版方摘要与讨论](https://link.springer.com/article/10.1186/s40536-026-00289-8)

**适配与阅读：** 方向④、⑥的评价参考。不能只保留历史对话的“可能不泛化”提醒而遗漏论文确实观察到跨任务一致性；同样不能把同一单元四任务的一致性扩展为跨学科成立。研究应加入简单计数聚类作为强对照。

## P07｜序列推荐与LLM学习路径

**Personalized learning path generation using large language models and sequential recommendations**。Prasad Deshmukh, Harshit Samrat, Nargis Pervin。*Data & Knowledge Engineering* 164: 102595，2026年7月。DOI：[10.1016/j.datak.2026.102595](https://doi.org/10.1016/j.datak.2026.102595)。

**中文摘要：** 先由序列推荐模型学习学习者交互与偏好表示、预测下一资源，再把表示接入LLM生成多步个性化路径。论文在三个数据集上评价排序指标和文本生成指标，讨论序列信息与语义生成联合建模的作用。[出版方摘要](https://www.sciencedirect.com/science/article/pii/S0169023X2600042X)

**适配与阅读：** 方向⑤直接相关。重点核查路径参考答案怎么形成、候选资源是否真实可用，以及排名/ROUGE改进是否对应先修合法性或学习收益。当前工作簿不提供完整LLM资源语料，不可只凭题目ID复现语义阶段。

## P08｜面向技能增益的bandit推荐

**A Bandit-Based Approach to Educational Recommender Systems: Contextual Thompson Sampling for Learner Skill Gain Optimization**。Lukas De Kerpel, Arthur Thuy, Dries F. Benoit。*INFORMS Transactions on Education*，2026-03-10在线发表（Articles in Advance，1–13页）。DOI：[10.1287/ited.2025.0174](https://doi.org/10.1287/ited.2025.0174)。预印本首版2026-02-04：[arXiv:2602.04347](https://arxiv.org/abs/2602.04347)。此处保留已核验的在线版书目，未另推断最终期号。

**中文摘要：** 利用学习者上下文和历史表现，以线性Thompson采样动态选择练习，奖励围绕目标技能估计值的变化构造。使用在线数学辅导数据，与非上下文采样和协同过滤等比较，关注个体差异与练习的教育价值。[出版方论文](https://pubsonline.informs.org/doi/10.1287/ited.2025.0174)

**适配与阅读：** 方向⑤。需仔细检查技能增益估计和离线评价假设；模型估计的增益不自动具有因果含义。阅读[作者机构存档](https://backoffice.biblio.ugent.be/download/01KKH1V22KSEHYYWQ9F71XRH5E/01KKH7PJ8WW08854QECKA7085G)可核对在线发表日期。

## P09｜课程过程挖掘综述

**A Systematic Review on Process Mining for Curricular Analysis**。Daniel Calegari, Andrea Delgado。*WIREs Data Mining and Knowledge Discovery* 15(2): e70005，2025-04-23。DOI：[10.1002/widm.70005](https://doi.org/10.1002/widm.70005)。另有[2024年预印本](https://arxiv.org/abs/2409.09204)。

**中文摘要：** 汇总27项课程分析过程挖掘研究，将目标归为学习轨迹、行为偏离、瓶颈、辍学/停学和推荐，并讨论跨学校标准化、过程与数据挖掘结合及工具支持等问题。[出版方摘要](https://doi.org/10.1002/widm.70005)

**适配与阅读：** 方向④的过程视角，OULAD可做课程级轨迹。课程进度与题内动作的粒度不同，引用时不将课程层结论直接移植成提示行为机制。

## P10｜simpleKT：知识追踪基线

**simpleKT: A Simple But Tough-to-Beat Baseline for Knowledge Tracing**。Zitao Liu, Qiongqiong Liu, Jiahao Chen, Shuyan Huang, Weiqi Luo。ICLR 2023；预印本2023-02-14，修订2023-02-23。[作者预印本与录用信息](https://arxiv.org/abs/2302.06881)。

**中文摘要：** 为解决复杂模型之间评价协议不一致的问题，显式刻画同知识点题目之间的差异，并用普通点积注意力建模交互历史，形成结构简单但具有竞争力的基线。论文在七个公开数据集与多种深度KT方法比较。

**适配与阅读：** 方向①—③的主要预测基线；要沿用相同拆分、KC处理和调参预算。普通注意力学到序列关系不等于已显式利用真实时间间隔。

## P11｜SASRec：序列推荐基线

**Self-Attentive Sequential Recommendation**。Wang-Cheng Kang, Julian McAuley。IEEE ICDM 2018，197–206页。DOI：[10.1109/ICDM.2018.00035](https://doi.org/10.1109/ICDM.2018.00035)。[作者预印本](https://arxiv.org/abs/1808.09781)首发2018-08-20，注明ICDM录用。

**中文摘要：** 通过自注意力从历史中挑选与下一项预测相关的行为，在较短局部依赖与较长历史之间取得适应性平衡。论文在稀疏和稠密推荐数据上比较预测效果与计算效率。

**适配与阅读：** 方向⑤候选排序基线；它优化下一物品预测，没有天然的教学目标、知识掌握或先修约束。[作者实现](https://github.com/kang205/SASRec)

## P12｜PrefixSpan：频繁序列模式

**PrefixSpan: Mining Sequential Patterns Efficiently by Prefix-Projected Pattern Growth**。Jian Pei, Jiawei Han, Behzad Mortazavi-Asl, Helen Pinto, Qiming Chen, Umeshwar Dayal, Mei-Chun Hsu。ICDE 2001，215–224页。DOI：[10.1109/ICDE.2001.914830](https://doi.org/10.1109/ICDE.2001.914830)。[作者所在机构书目及摘要](https://scholars.duke.edu/publication/1530847)

**中文摘要：** 通过前缀投影分解序列模式搜索，在投影数据库中逐步增长频繁模式，减少候选枚举成本。适合从离散行为序列中提取可读的重复子序列。

**适配与阅读：** 方向④的方法基础，不是教育有效性证据。先定义按学生还是按会话计支持度，是否允许跨步骤间隔，限制模式长度；频繁不等于具有独立预测或教学价值。

## P13｜DANN：通用领域适配基线

**Domain-Adversarial Training of Neural Networks**。Yaroslav Ganin, Evgeniya Ustinova, Hana Ajakan, Pascal Germain, Hugo Larochelle, François Laviolette, Mario Marchand, Victor Lempitsky。*Journal of Machine Learning Research* 17(59): 1–35，2016年4月。[正式论文](https://www.jmlr.org/papers/volume17/15-239/15-239.pdf)

**中文摘要：** 在有标签源域和无标签目标域下，通过梯度反转联合优化任务预测与域判别，鼓励特征对主任务有用而对领域差异不敏感。论文在情感、图像等任务验证领域适配。

**适配与阅读：** 方向⑥的方法参考，原论文不是学生行为研究。教育迁移需额外验证动作语义、知识点结构和标签含义；强行抹平领域差异可能造成负迁移。出版方网页作者名字曾显示缩写异常，此处按正式PDF的Mario Marchand记录。

## 本次核验结论与适用边界

1. 六个方向可与上述真实论文相连，但方向⑥的完整“共享需求表示+领域知识可控推荐”仍是拟研究方案，不是某一论文已完成的结论。
2. 区分预印本年份、在线发表日期、正式卷期；DOI中的年份不能替代出版日期。IPDGKT卷期按出版方与DOI注册记录纠正，Bandit保留两种版本时间。
3. MHG-KT是模型简称，不是正式题名前缀。simpleKT是ICLR 2023论文。
4. 书目和公开摘要已核验；数据处理、效果数值、开源代码可运行性与实验公平性留给后续全文阅读和复现。本文未把论文宣称的改进百分比当作本项目结果。
