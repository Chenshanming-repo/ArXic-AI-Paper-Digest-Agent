---
## 2026-05-11

### 1. The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents
**Authors:** Jiayuan Liu, Tianqin Li, Shiyi Du, Xin Luo, Haoxuan Zeng, Emanuel Tewolde, Tai Sing Lee, Tonghan Wang, Carl Kingsford, Vincent Conitzer
**Link:** https://arxiv.org/abs/2605.08060v1
**Summary:** The paper investigates how increasing the memory capacity of large language model (LLM) agents affects their ability to cooperate in multi-agent social dilemmas, revealing a phenomenon called the "memory curse". Through various analyses, the authors demonstrate that while expanding memory tends to deteriorate cooperative intent, targeted fine-tuning and memory sanitization techniques can counteract this decline, highlighting that the content of memory, rather than its length, plays a crucial role in influencing cooperative behavior. Ultimately, the study suggests that memory's impact on multi-agent interactions is complex, as it can either hinder or promote collaboration based on the reasoning strategies employed.

### 2. CA-SQL: Complexity-Aware Inference Time Reasoning for Text-to-SQL via Exploration and Compute Budget Allocation
**Authors:** James Petullo, Nianwen Xue
**Link:** https://arxiv.org/abs/2605.08057v1
**Summary:** The paper introduces CA-SQL, a novel pipeline designed to improve reasoning in Text-to-SQL tasks, particularly for challenging queries in the Bird-Bench benchmark. It utilizes a dynamic exploration strategy based on task difficulty and incorporates an innovative prompt seeding technique to enhance query generation. CA-SQL achieves a state-of-the-art score of 51.72% on difficult BIRD problems, outperforming other approaches while maintaining competitive execution accuracy and F1 scores.

### 3. Reinforcement Learning for Exponential Utility: Algorithms and Convergence in Discounted MDPs
**Authors:** Gugan Thoppe, L. A. Prashanth, Ankur Naskar, Sanjay Bhat
**Link:** https://arxiv.org/abs/2605.08053v1
**Summary:** This paper addresses the lack of value-based reinforcement learning algorithms for optimizing exponential utility in discounted Markov decision processes. The authors derive two Q-value-style extensions with contraction properties, leading to the development of two model-free algorithms that demonstrate almost-sure convergence and finite-time convergence rates, despite challenges in the one-timescale algorithm. Their work establishes a foundational framework for applying value-based RL methods to exponential-utility objectives.

### 4. Accurate and Efficient Statistical Testing for Word Semantic Breadth
**Authors:** Yo Ehara
**Link:** https://arxiv.org/abs/2605.08048v1
**Summary:** The paper addresses the challenge of accurately comparing the semantic breadth of words using contextualized embeddings, which can yield misleading results due to the influence of directional differences. The authors propose a novel permutation test based on Householder reflections that effectively isolates true differences in word breadth from these directional effects, while also enhancing computational efficiency through a GPU-optimized implementation. Their method significantly reduces false positives in statistical tests and allows for faster processing times.

### 5. Uncertainty-Aware Structured Data Extraction from Full CMR Reports via Distilled LLMs
**Authors:** Yi Yu, Parker Martin, Zhenyu Bu, Yixuan Liu, Yi-Yu Zheng, Orlando Simonetti, Yuchi Han, Yuan Xue
**Link:** https://arxiv.org/abs/2605.08045v1
**Summary:** The paper addresses the challenge of converting free-text cardiac magnetic resonance (CMR) reports into structured data for better clinical use. It introduces CMR-EXTR, a framework that uses a teacher-student distillation method to perform this task offline while also providing confidence levels for each extracted data field. The key result is a high variable-level accuracy of 99.65%, marking the first CMR-specific extraction system to incorporate confidence estimation.

### 6. Fast Byte Latent Transformer
**Authors:** Julie Kallini, Artidoro Pagnoni, Tomasz Limisiewicz, Gargi Ghosh, Luke Zettlemoyer, Christopher Potts, Xiaochuang Han, Srinivasan Iyer
**Link:** https://arxiv.org/abs/2605.08044v1
**Summary:** The paper presents the Byte Latent Transformer (BLT), a new model that improves the slow generation speed of byte-level language models, which previously generated text one byte at a time. The authors introduce innovative training and generation techniques, including a diffusion-based approach that allows for parallel byte generation, as well as methods that enhance quality without significantly sacrificing speed. Key contributions include notable reductions in memory bandwidth costs during generation and practical solutions that enhance the usability of byte-level models.

### 7. SCOPE: Structured Decomposition and Conditional Skill Orchestration for Complex Image Generation
**Authors:** Tianfei Ren, Zhipeng Yan, Yiming Zhao, Zhen Fang, Yu Zeng, Guohui Zhang, Hang Xu, Xiaoxiao Ma, Shiting Huang, Ke Xu, Wenxuan Huang, Lionel Z. Wang, Lin Chen, Zehui Chen, Jie Huang, Feng Zhao
**Link:** https://arxiv.org/abs/2605.08043v1
**Summary:** The paper addresses the challenge of maintaining consistency in complex image generation tasks, where various visual requirements can easily become misaligned. The authors introduce SCOPE, a framework that systematically tracks these requirements (referred to as semantic commitments) throughout the generation process by orchestrating retrieval, reasoning, and repair skills as needed. Their results show that SCOPE significantly outperforms existing methods in a new benchmark, highlighting its effectiveness in ensuring that intended imagery accurately reflects specified requirements.

### 8. Beyond Pairs: Your Language Model is Secretly Optimizing a Preference Graph
**Authors:** Ning Liu, Chuanneng Sun, Kristina Klinkner, Shervin Malmasi
**Link:** https://arxiv.org/abs/2605.08037v1
**Summary:** The paper addresses the limitations of pairwise preference comparisons in aligning language models, which often overlook the richer preference structures present in training data. The authors propose Graph Direct Preference Optimization (GraphDPO), a method that utilizes directed acyclic preference graphs to optimize language model alignment more effectively. Their experiments show that this approach enhances performance in various tasks, demonstrating that leveraging graph structures for preference modeling is a powerful alternative to traditional methods.

### 9. Don't Get Your Kroneckers in a Twist: Gaussian Processes on High-Dimensional Incomplete Grids
**Authors:** Mads Greisen Højlund, August Smart Lykke-Møller, Henry Moss, Ove Christiansen
**Link:** https://arxiv.org/abs/2605.08036v1
**Summary:** The paper presents CUTS-GPR, a novel approach for efficient Gaussian process regression in high-dimensional spaces where traditional methods struggle due to computational demands. By utilizing an additive kernel and an incomplete grid, CUTS-GPR achieves rapid kernel matrix-vector products, enabling effective modeling of complex data sets with billions of points and thousands of dimensions. The method successfully allows for fast and accurate Bayesian modeling of potential energy surfaces in computational chemistry, addressing a significant challenge in the field.

### 10. PropSplat: Map-Free RF Field Reconstruction via 3D Gaussian Propagation Splatting
**Authors:** William Bjorndahl, Maninder Pal Singh, Farhad Nouri, Joseph Camp
**Link:** https://arxiv.org/abs/2605.08035v1
**Summary:** The paper addresses the challenge of creating accurate radio frequency (RF) propagation models without relying on detailed geographic maps or extensive measurement campaigns, which are often prohibitively expensive. The authors introduce PropSplat, a method that utilizes 3D Gaussian primitives to reconstruct RF fields by optimizing path loss over observed transmitter-receiver paths. This approach significantly outperforms existing methods in both outdoor and indoor scenarios, demonstrating that effective RF modeling can be achieved from sparse data without the need for comprehensive geographic information.
