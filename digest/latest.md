---
## 2026-05-21

### 1. Variance Reduction for Expectations with Diffusion Teachers
**Authors:** Jesse Bettencourt, Xindi Wu, Matan Atzmon, James Lucas, Jonathan Lorraine
**Link:** https://arxiv.org/abs/2605.21489v1
**Summary:** The paper addresses the problem of high computational costs associated with using pretrained diffusion models in downstream tasks, due to the variability of Monte Carlo estimates from noise samples. To tackle this, the authors introduce CARV, a framework that reduces variance in these estimates by employing a hierarchical Monte Carlo approach that allows for more efficient reuse of expensive computations combined with importance sampling techniques. The key contribution is that CARV significantly improves computational efficiency, achieving 2-3x effective compute savings in various experiments, although it does not enhance performance in all scenarios.

### 2. Equilibrium Reasoners: Learning Attractors Enables Scalable Reasoning
**Authors:** Benhao Huang, Zhengyang Geng, Zico Kolter
**Link:** https://arxiv.org/abs/2605.21488v1
**Summary:** The paper addresses the challenge of enabling iterative reasoning models to generalize effectively beyond memorized patterns. The authors introduce Equilibrium Reasoners (EqR), which leverage learned dynamical systems that stabilize at solution points, allowing for scaling of reasoning processes during inference. Their approach significantly enhances performance in challenging tasks, such as solving complex Sudoku puzzles, where accuracy improved from 2.6% to over 99% by effectively utilizing test-time computation.

### 3. Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate
**Authors:** Dayal Singh Kalra, Maissam Barkeshli
**Link:** https://arxiv.org/abs/2605.21486v1
**Summary:** The paper addresses the challenge of transferring optimal hyperparameters when training large language models (LLMs) across different scales. The authors propose a framework to quantify hyperparameter transfer and demonstrate that the "Maximal Update" (μP) approach significantly enhances learning rate transfer compared to standard parameterization. A key finding is that optimizing the embedding layer's learning rate reduces training instability and improves hyperparameter transfer effectiveness.

### 4. EvoStruct: Bridging Evolutionary and Structural Priors for Antibody CDR Design via Protein Language Model Adaptation
**Authors:** Mansoor Ahmed, Sujin Lee, Umar Khayaz, Murray Patterson
**Link:** https://arxiv.org/abs/2605.21485v1
**Summary:** The paper introduces EvoStruct, a novel method for antibody CDR design that tackles the problem of vocabulary collapse in existing graph neural networks, which tend to over-predict certain amino acids while missing important ones. By integrating a frozen protein language model with 3D structural information through a cross-attention mechanism, EvoStruct significantly improves sequence recovery and amino acid diversity. The results show a 16% increase in sequence recovery and a 43% reduction in perplexity compared to leading GNN methods, aligning more closely with known binding correlations.

### 5. Velocityformer: Broken-Symmetry-Matched Equivariant Graph Transformers for Cosmological Velocity Reconstruction
**Authors:** Tilman Tröster, David Mirkovic, Veronika Oehl, Arne Thomsen
**Link:** https://arxiv.org/abs/2605.21483v1
**Summary:** The paper presents Velocityformer, a novel graph transformer model designed to accurately reconstruct galaxy velocities from spectroscopic surveys to enhance measurements of the kinematic Sunyaev-Zel'dovich (kSZ) effect, which informs cosmological theories. By aligning the model with the broken symmetry in observational data, Velocityformer achieves a 35% improvement in accuracy over traditional methods and demonstrates enhanced performance even with limited training data, ultimately improving the signal-to-noise ratio in kSZ measurements by 30%.

### 6. DeepWeb-Bench: A Deep Research Benchmark Demanding Massive Cross-Source Evidence and Long-Horizon Derivation
**Authors:** Sixiong Xie, Zhuofan Shi, Haiyang Shen, Jiuzheng Wang, Siqi Zhong, Mugeng Liu, Chongyang Pan, Peilun Jia, Baoqing Sun, Xiang Jing, Yun Ma
**Link:** https://arxiv.org/abs/2605.21482v1
**Summary:** The paper introduces DeepWeb-Bench, a challenging benchmark for evaluating language models on deep research tasks that require extensive evidence gathering, cross-source verification, and complex multi-step reasoning. The benchmark reveals that most errors arise from issues in deriving and calibrating answers rather than retrieving information, highlighting distinct failure modes between strong and weak models, and showing that models perform differently across domains. The publicly available benchmark includes data and evaluation tools for further research.

### 7. AiraXiv: An AI-Driven Open-Access Platform for Human and AI Scientists
**Authors:** Junshu Pan, Panzhong Lu, Yixuan Weng, Qiyao Sun, Fang Guo, Zijie Yang, Qiji Zhou, Yue Zhang
**Link:** https://arxiv.org/abs/2605.21481v1
**Summary:** The paper presents AiraXiv, an AI-driven open-access platform designed to tackle the challenges faced by traditional academic publishing, such as increasing submission volumes and reviewer workload. AiraXiv enables both human and AI authors to contribute and refine research through iterative feedback and AI-assisted analysis, promoting a more inclusive and scalable approach to publishing. The platform was validated through real-world applications, showing its effectiveness as a modern research infrastructure.

### 8. WikiVQABench: A Knowledge-Grounded Visual Question Answering Benchmark from Wikipedia and Wikidata
**Authors:** Basel Shbita, Pengyuan Li, Anna Lisa Gentile
**Link:** https://arxiv.org/abs/2605.21479v1
**Summary:** The paper introduces WikiVQABench, a new benchmark for Visual Question Answering (VQA) that requires external knowledge from sources like Wikipedia and Wikidata, addressing the limitation of existing benchmarks that focus only on visual content. To create this dataset, images from Wikipedia were combined with relevant captions and knowledge, and multiple-choice questions were generated using large language models and then curated by human annotators for quality and factual accuracy. The evaluation of various vision-language models on this benchmark showed a significant range in performance, highlighting its effectiveness in assessing knowledge-driven reasoning capabilities in AI systems.

### 9. Is Fixing Schema Graphs Necessary? Full-Resolution Graph Structure Learning for Relational Deep Learning
**Authors:** Yi Huang, Qingyun Sun, Jia Li, Xingcheng Fu, Jianxin Li
**Link:** https://arxiv.org/abs/2605.21475v1
**Summary:** The paper addresses the challenge of enhancing relational prediction tasks using relational deep learning by moving beyond fixed graph structures in relational databases. The authors introduce FROG, a framework that learns graph structures dynamically during the learning process by treating tables as flexible nodes and edges, while incorporating mechanisms to capture relational semantics effectively. Their experiments show that this approach outperforms existing methods and provides insightful contributions to how graph structures can be optimized for better performance in relational deep learning tasks.

### 10. Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling
**Authors:** Caleb Winston, Ron Yifeng Wang, Azalia Mirhoseini, Christos Kozyrakis
**Link:** https://arxiv.org/abs/2605.21470v1
**Summary:** The paper addresses the high latency and error rates in computer-use agents (CUA) that automate web tasks using natural language instructions by proposing an agent just-in-time (JIT) compilation method. This approach generates executable code from task descriptions, allowing for optimized tool usage and parallel execution. The results show significant improvements, with JIT-Planner achieving over 10 times faster execution and increased accuracy compared to existing methods.
