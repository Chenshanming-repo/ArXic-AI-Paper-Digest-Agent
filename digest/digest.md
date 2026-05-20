# ArXiv Daily Digest

Automatically generated daily summaries of recent ArXiv papers.

---
## 2026-05-11

### 1. LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
**Authors:** Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
**Link:** https://arxiv.org/abs/2605.08083v1
**Summary:** The paper addresses the problem of inefficient manually designed test-time scaling (TTS) strategies for improving the performance of large language models during inference. The authors propose AutoTTS, an environment-driven framework that automatically discovers optimal TTS strategies by controlling the allocation of computation based on reasoning trajectories. Key results show that the automatically discovered strategies outperform traditional baselines in both accuracy and cost-efficiency across various benchmarks, while the entire discovery process is inexpensive and quick.

### 2. Normalizing Trajectory Models
**Authors:** Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
**Link:** https://arxiv.org/abs/2605.08078v1
**Summary:** The paper addresses the limitations of existing diffusion-based models for generating images in a few steps, which often compromise likelihood accuracy. The authors introduce Normalizing Trajectory Models (NTM), a method that employs conditional normalizing flows for each reverse sampling step while maintaining exact likelihood training. NTM achieves high-quality image generation in just four steps, outperforming strong baselines and preserving precise likelihood throughout the generation process.

### 3. Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
**Authors:** Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
**Link:** https://arxiv.org/abs/2605.08077v1
**Summary:** The paper addresses the issue of unreliable answer coverage in Knowledge Graph Question Answering (KGQA) systems, which often produce overly large prediction sets without sufficient reliability. The authors propose Conformal Path Reasoning (CPR), which incorporates query-level conformal calibration and a new Residual Conformal Value Network to improve the selection of path-level scores. Their approach significantly enhances the validity of predictions, achieving a 34% increase in empirical coverage while reducing the average size of prediction sets by 40% compared to previous methods.

### 4. Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
**Authors:** Maryam Maghsoudi, Shihab Shamma
**Link:** https://arxiv.org/abs/2605.08075v1
**Summary:** This paper addresses the challenge of decoding imagined speech from brain recordings, which is hindered by a lack of well-aligned data across individuals. The authors introduce a novel three-stage method that maps neural responses from imagined speech to actual listened speech using data from trained musicians, leading to the successful decoding of imagined words with notable accuracy. Key findings suggest that their approach can scale with more training data, making it viable for real-world brain-computer interface applications.

### 5. GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
**Authors:** Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
**Link:** https://arxiv.org/abs/2605.08074v1
**Summary:** The paper addresses the challenge of applying conformal prediction (CP) to graph neural networks (GNNs), which often leads to uncertain predictions due to the complex structure of graphs. The authors introduce GRAPHLCP, a new localized CP framework that integrates graph topology and node relationships to enhance prediction accuracy, employing a method that includes a feature-aware densification step and Personalized PageRank for improved modeling of local and long-range dependencies. Their extensive experiments show that GRAPHLCP achieves reliable prediction sets while ensuring accurate uncertainty estimation in various scenarios.

### 6. EmambaIR: Efficient Visual State Space Model for Event-guided Image Reconstruction
**Authors:** Wei Yu, Yunhang Qian
**Link:** https://arxiv.org/abs/2605.08073v1
**Summary:** The paper presents EmambaIR, a new model for event-guided image reconstruction that overcomes limitations of existing methods, which struggle with global feature correlations and high computational costs. EmambaIR employs a unique combination of a top-k sparse attention mechanism and a gated state-space module to efficiently process event data, achieving better performance in tasks like motion deblurring and HDR enhancement. Experimental results show that it significantly outperforms current state-of-the-art techniques while reducing memory usage and processing time.

### 7. A Note on Non-Negative $L_1$-Approximating Polynomials
**Authors:** Jane H. Lee, Anay Mehrotra, Manolis Zampetakis
**Link:** https://arxiv.org/abs/2605.08072v1
**Summary:** The paper addresses the problem of finding non-negative polynomials that can approximate indicator functions in the $L_1$-norm under Gaussian distributions. The authors demonstrate that for sets with a bounded Gaussian surface area, it is possible to construct degree-$k$ non-negative polynomials that approximate these indicator functions to within a specified accuracy. Notably, their result shows that the degree required for such approximations is comparable to existing bounds for general $L_1$ approximations, but with the added constraint of non-negativity.

### 8. VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection
**Authors:** James Petullo, Sonny George, Dylan Cashman, Nianwen Xue
**Link:** https://arxiv.org/abs/2605.08070v1
**Summary:** The paper addresses the inefficiency and high cost of confidence-informed self-consistency in reasoning, which requires multiple evaluations of candidate answers by a critic language model. The authors propose VecCISC, a method that uses semantic similarity to filter out redundant or low-quality reasoning traces, thereby reducing the number of evaluations needed. The key finding is that VecCISC can decrease overall token usage by 47% while maintaining or improving the accuracy of the original approach.

### 9. Flow-OPD: On-Policy Distillation for Flow Matching Models
**Authors:** Zhen Fang, Wenxuan Huang, Yu Zeng, Yiming Zhao, Shuang Chen, Kaituo Feng, Yunlong Lin, Lin Chen, Zehui Chen, Shaosheng Cao, Feng Zhao
**Link:** https://arxiv.org/abs/2605.08063v1
**Summary:** The paper addresses critical issues in Flow Matching text-to-image models, specifically reward sparsity and gradient interference that lead to ineffective multi-task alignment. It introduces Flow-OPD, a novel approach that incorporates on-policy distillation to align models effectively, first training specialized teacher models and then consolidating their expertise into a single student model. As a result, Flow-OPD significantly improves performance metrics, achieving a GenEval score increase from 63 to 92 and enhancing OCR accuracy from 59 to 94, while maintaining image quality and human preference alignment.

### 10. Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning
**Authors:** Manish Bhattarai, Ismael Boureima, Nishath Rajiv Ranasinghe, Scott Pakin, Dan O'Malley
**Link:** https://arxiv.org/abs/2605.08061v1
**Summary:** The paper introduces a novel approach called rubric-grounded reinforcement learning (RL), which enhances model training by breaking down rewards into multiple verifiable criteria assessed by a large language model (LLM) judge. By using this structured reward system, the authors demonstrate that their model, trained on a large corpus of scientific documents, achieves higher performance in evaluating and reasoning tasks compared to the base model. Notably, the trained policy not only excels in rubric evaluations but also shows improved reasoning capabilities on unrelated benchmarks.

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

---
## 2026-05-12

### 1. ELF: Embedded Language Flows
**Authors:** Keya Hu, Linlu Qiu, Yiyang Lu, Hanhong Zhao, Tianhong Li, Yoon Kim, Jacob Andreas, Kaiming He
**Link:** https://arxiv.org/abs/2605.10938v1
**Summary:** The paper introduces Embedded Language Flows (ELF), a new class of language models that enhance diffusion processes by operating primarily in a continuous embedding space before converting to discrete tokens at the final step. By adapting techniques from image diffusion models, ELF significantly improves generation quality and efficiency, outperforming leading language models with fewer sampling steps. This approach demonstrates a promising direction for developing more effective continuous diffusion language models.

### 2. Variational Inference for Lévy Process-Driven SDEs via Neural Tilting
**Authors:** Yaman Kindap, Manfred Opper, Benjamin Dupuis, Umut Simsekli, Tolga Birdal
**Link:** https://arxiv.org/abs/2605.10934v1
**Summary:** The paper addresses the challenge of performing Bayesian inference in Lévy-driven stochastic differential equations, which are important for modeling extreme events and heavy-tailed phenomena. The authors propose a novel neural exponential tilting framework that uses neural networks to adjust the Lévy measure, allowing for more accurate and scalable inference while preserving the jump characteristics typical of these processes. Their approach shows significant improvements in capturing jump dynamics and providing reliable posteriors compared to traditional Gaussian-based methods, validated through experiments on both synthetic and real-world data.

### 3. DECO: Sparse Mixture-of-Experts with Dense-Comparable Performance on End-Side Devices
**Authors:** Chenyang Song, Weilin Zhao, Xu Han, Chaojun Xiao, Yingfa Chen, Zhiyuan Liu
**Link:** https://arxiv.org/abs/2605.10933v1
**Summary:** The paper introduces DECO, a sparse Mixture-of-Experts architecture that aims to achieve the performance of dense Transformers while using significantly fewer computational resources, making it suitable for deployment on end-side devices. By utilizing a novel routing mechanism and a new activation function, DECO activates only 20% of its experts yet matches or exceeds the performance of traditional dense models. Additionally, a specialized acceleration kernel developed for DECO offers a threefold increase in processing speed on real hardware compared to dense inference.

### 4. Quantifying Concentration Phenomena of Mean-Field Transformers in the Low-Temperature Regime
**Authors:** Albert Alcalde, Leon Bungert, Konstantin Riedl, Tim Roith
**Link:** https://arxiv.org/abs/2605.10931v1
**Summary:** This paper investigates how tokens in deep encoder-only transformers evolve during inference, particularly as the number of tokens increases, by using a mean-field continuity equation to describe their behavior. The authors prove that the token distribution quickly becomes concentrated around a specific limiting distribution influenced by the model parameters and remains stable over a moderate time scale. Their findings are supported by numerical experiments, which also reveal that for longer time periods, the dynamics shift to a new phase affected by the value matrix's spectral properties.

### 5. Dynamic Skill Lifecycle Management for Agentic Reinforcement Learning
**Authors:** Junhao Shen, Teng Zhang, Xiaoyan Zhao, Hong Cheng
**Link:** https://arxiv.org/abs/2605.10923v1
**Summary:** The paper addresses the challenge of efficiently managing external skills in reinforcement learning agents to optimize their performance on complex tasks. It introduces a framework called SLIM that dynamically adjusts the active skill set based on their effectiveness, allowing agents to retain valuable skills, retire those that are no longer useful, and expand their capabilities when needed. The key finding is that SLIM significantly improves performance over existing methods, demonstrating that not all skills need to be internalized into the agent's policy, thus enhancing the overall flexibility and effectiveness of skill utilization in reinforcement learning.

### 6. Optimal and Scalable MAPF via Multi-Marginal Optimal Transport and Schrödinger Bridges
**Authors:** Usman A. Khan, Joseph W. Durham
**Link:** https://arxiv.org/abs/2605.10917v1
**Summary:** The paper addresses the problem of multi-agent path finding (MAPF) for robots navigating to targets on a graph, proposing a new approach that treats MAPF as a type of multi-marginal optimal transport (MMOT) problem. They show that this problem can be simplified into a manageable linear program and further enhance scalability by using a probabilistic method called Schrödinger bridges, which streamlines the solution process. The key contribution is the demonstration that their approach yields optimal and efficient paths for numerous robots without overlap in both space and time, even in large-scale scenarios.

### 7. Confidence-Guided Diffusion Augmentation for Enhanced Bangla Compound Character Recognition
**Authors:** Md. Sultan Al Rayhan, Maheen Islam
**Link:** https://arxiv.org/abs/2605.10916v1
**Summary:** This paper addresses the difficulty of recognizing handwritten Bangla compound characters, which are complex and varied due to their intricate structures and limited training data. The authors introduce a confidence-guided diffusion augmentation technique that synthesizes high-quality character samples using a combination of diffusion modeling and classifier guidance, along with a filtering mechanism for quality control. Their approach significantly improves recognition performance, achieving 89.2% accuracy on the AIBangla dataset, which is a notable advancement over previous benchmarks.

### 8. Shepherd: A Runtime Substrate Empowering Meta-Agents with a Formalized Execution Trace
**Authors:** Simon Yu, Derek Chong, Ananjan Nandi, Dilara Soylu, Jiuding Sun, Christopher D Manning, Weiyan Shi
**Link:** https://arxiv.org/abs/2605.10913v1
**Summary:** The paper presents Shepherd, a functional programming model designed to enhance the efficiency and effectiveness of meta-agents through a structured framework for recording and replaying interactions with their environment. By utilizing a Git-like execution trace, Shepherd enables rapid forking and replay of agent processes, resulting in significant performance improvements across various applications, such as increasing coding pass rates and optimizing exploration strategies in reinforcement learning. The system is open-sourced to facilitate ongoing research in this area.

### 9. WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation
**Authors:** Shuangrui Ding, Xuanlang Dai, Long Xing, Shengyuan Ding, Ziyu Liu, Yang JingYi, Penghui Yang, Zhixiong Zhang, Xilin Wei, Xinyu Fang, Yubo Ma, Haodong Duan, Jing Shao, Jiaqi Wang, Dahua Lin, Kai Chen, Yuhang Zang
**Link:** https://arxiv.org/abs/2605.10912v1
**Summary:** The paper introduces WildClawBench, a benchmark designed to assess the performance of AI agents in realistic, long-horizon tasks within their actual runtime environments, moving away from traditional synthetic benchmarks. It features 60 bilingual tasks that run in a Docker container with real command-line interfaces, incorporating both deterministic and semantic evaluation methods. The key finding reveals that even leading models like Claude Opus 4.7 only achieve a 62.2% success rate, indicating significant challenges in effectively evaluating agent performance over extended tasks.

### 10. Equivariant Reinforcement Learning for Clifford Quantum Circuit Synthesis
**Authors:** Richie Yeung, Aleks Kissinger, Rob Cornish
**Link:** https://arxiv.org/abs/2605.10910v1
**Summary:** The paper addresses the challenge of synthesizing Clifford quantum circuits, which are crucial for quantum computing, particularly in fully connected qubit systems. The authors developed a reinforcement learning approach using a specially designed neural network that can adapt to different qubit configurations. Their key contribution is an agent that can efficiently find near-optimal or optimal circuit solutions for qubits, demonstrating significantly better performance than existing synthesis methods even for larger circuits.

---
## 2026-05-12

### 1. Revisiting Policy Gradients for Restricted Policy Classes: Escaping Myopic Local Optima with $k$-step Policy Gradients
**Authors:** Alex DeWeese, Guannan Qu
**Link:** https://arxiv.org/abs/2605.10909v1
**Summary:** This paper addresses the issue of standard policy gradient methods getting stuck in suboptimal solutions when using restricted policy classes due to their one-step, myopic nature. The authors propose a generalized $k$-step policy gradient method that integrates multi-step decision-making to effectively escape these local optima. Their key contribution is a theoretical guarantee that this approach can converge to near-optimal solutions in a significantly shorter number of iterations while avoiding common pitfalls linked to distribution mismatches.

### 2. Engineering Robustness into Personal Agents with the AI Workflow Store
**Authors:** Roxana Geambasu, Mariana Raykova, Pierre Tholoniat, Trishita Tiwari, Lillian Tsai, Wen Zhang
**Link:** https://arxiv.org/abs/2605.10907v1
**Summary:** This paper addresses the problem of the reliability and security of AI agents that currently operate in an "on-the-fly" manner, which can lead to untested and vulnerable responses. The authors propose the integration of rigorous software engineering processes into the development of AI agents, advocating for the creation of a reusable repository of reliable "AI workflows" instead. Their key contribution is the outline of a vision for an AI Workflow Store, which would allow for more robust and secure agent operations, thereby overcoming the challenges posed by the current rapid synthesis paradigm.

### 3. DataMaster: Towards Autonomous Data Engineering for Machine Learning
**Authors:** Yaxin Du, Xiyuan Yang, Zhifan Zhou, Wanxu Liu, Zixing Lei, Zimeng Chen, Fenyi Liu, Haotian Wu, Yuzhu Cai, Zexi Liu, Xinyu Zhu, WenHao Wang, Linfeng Zhang, Chen Qian, Siheng Chen
**Link:** https://arxiv.org/abs/2605.10906v1
**Summary:** The paper presents DataMaster, an autonomous data engineering framework designed to enhance machine learning by optimizing data selection and transformation without changing the underlying learning algorithm. By employing a structured search process and utilizing a shared data repository, DataMaster improves the quality of training data and consequently boosts the performance of ML models. In evaluations, DataMaster achieved a 32.27% improvement in performance on MLE-Bench Lite and outperformed existing models on the PostTrainBench dataset.

### 4. Beyond Red-Teaming: Formal Guarantees of LLM Guardrail Classifiers
**Authors:** Nikita Kezins, Urbas Ekka, Pascal Berrang, Luca Arnaboldi
**Link:** https://arxiv.org/abs/2605.10901v1
**Summary:** The paper addresses the lack of formal guarantees for Guardrail Classifiers that aim to prevent harmful behavior in language models. The authors propose a novel verification method that shifts the analysis to the pre-activation space of classifiers, defining harmful regions and using geometric structures for certification. Their findings reveal that while some classifiers perform well in practice, significant safety gaps exist, particularly in the BERT model, highlighting the need for more reliable safety measures beyond conventional testing methods.

### 5. RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards
**Authors:** Gaotang Li, Bhavana Dalvi Mishra, Zifeng Wang, Jun Yan, Yanfei Chen, Chun-Liang Li, Long T. Le, Rujun Han, George Lee, Hanghang Tong, Chen-Yu Lee, Tomas Pfister
**Link:** https://arxiv.org/abs/2605.10899v1
**Summary:** The paper addresses the challenge of enhancing deep research agents, which struggle with tasks that lack clear rewards and ground-truth answers, by introducing the RubricEM framework. This approach utilizes rubrics not just for evaluation but as a structured guide for policy execution and feedback, combining stagewise policy decomposition with a reflection-based meta-policy evolution process. The key contribution is the development of RubricEM-8B, which achieves superior performance on long-form research tasks compared to existing models, demonstrating the effectiveness of rubric-guided learning for complex decision-making.

### 6. V4FinBench: Benchmarking Tabular Foundation Models, LLMs, and Standard Methods on Corporate Bankruptcy Prediction
**Authors:** Marcin Kostrzewa, Sebastian Tomczak, Roman Furman, Anna Poberezhna, Michał Furgała, Oleksii Furman, Maciej Zięba
**Link:** https://arxiv.org/abs/2605.10896v1
**Summary:** The paper introduces V4FinBench, a large benchmark dataset for predicting corporate bankruptcy, addressing the lack of extensive public datasets in this domain. It includes over one million records and aims to evaluate various prediction models, including tabular methods and foundation models, under realistic conditions of class imbalance. The key finding shows that with appropriate finetuning, a tabular model outperforms traditional methods, while a foundation model struggles, highlighting the effectiveness of tailored approaches in financial distress prediction.

### 7. Grounded or Guessing? LVLM Confidence Estimation via Blind-Image Contrastive Ranking
**Authors:** Reza Khanmohammadi, Erfan Miahi, Simerjot Kaur, Charese H. Smiley, Ivan Brugere, Kundan Thind, Mohammad M. Ghassemi
**Link:** https://arxiv.org/abs/2605.10893v1
**Summary:** The paper addresses the issue of visual ungroundedness in large vision-language models (LVLMs), where models may provide confident, yet misleading answers based solely on language rather than visual input. The authors propose a method called BICR (Blind-Image Contrastive Ranking), which trains a lightweight probe to assess the reliability of predictions by comparing model responses to real images against blacked-out views of those images. BICR outperforms existing confidence estimation methods in both accuracy and efficiency, achieving better calibration and discrimination with significantly fewer parameters than competing approaches.

### 8. Unmasking On-Policy Distillation: Where It Helps, Where It Hurts, and Why
**Authors:** Mohammadreza Armandpour, Fatih Ilhan, David Harrison, Ajay Jaiswal, Duc N. M Hoang, Fartash Faghri, Yizhe Zhang, Minsik Cho, Mehrdad Farajtabar
**Link:** https://arxiv.org/abs/2605.10889v1
**Summary:** The paper addresses the challenges of determining when on-policy distillation is beneficial or harmful for training reasoning models. The authors introduce a diagnostic framework that analyzes the effectiveness of distillation on a per-token basis, allowing them to assess the quality of the supervisory signal provided by teacher models. They discover that distillation is more aligned with ideal guidance for incorrect outputs than correct ones, highlighting the need for tailored analyses based on model capacity and task specificity.

### 9. Shields to Guarantee Probabilistic Safety in MDPs
**Authors:** Linus Heck, Filip Macák, Roman Andriushchenko, Milan Češka, Sebastian Junges
**Link:** https://arxiv.org/abs/2605.10888v1
**Summary:** This paper addresses the challenge of ensuring safety for autonomous agents operating under uncertainty by extending classical shielding techniques to probabilistic safety scenarios, where some risks are acceptable. The authors develop a formal framework that elucidates the limitations of maintaining strong safety guarantees while also proposing offline and online methods for creating effective shields with weaker assurances. The results demonstrate that these new shields are both practical and computationally feasible, offering significant advantages for real-world applications.

### 10. LoKA: Low-precision Kernel Applications for Recommendation Models At Scale
**Authors:** Liang Luo, Yinbin Ma, Quanyu Zhu, Vasiliy Kuznetsov, Yuxin Chen, Jian Jiao, Jiecao Yu, Buyun Zhang, Tongyi Tang, Xiaohan Wei, Yanli Zhao, Zeliang Chen, Yuchen Hao, Venkatesh Ranganathan, Sandeep Parab, Yantao Yao, Maxim Naumov, Chunzhi Yang, Shen Li, Ellie Wen, Wenlin Chen, Santanu Kolay, Chunqiang Tang
**Link:** https://arxiv.org/abs/2605.10886v1
**Summary:** The paper addresses the challenges of using low-precision FP8 arithmetic in large recommendation models, which are sensitive to numerical precision and require careful handling to maintain quality and efficiency. The authors introduce LoKA, a framework that utilizes profiling to identify where FP8 can be safely applied, adapts model components for better performance, and optimizes kernel selection at runtime. Key contributions include a benchmarking method to evaluate precision trade-offs and a set of model adaptations that enhance stability and efficiency when using FP8 in recommendation systems.

---
## 2026-05-14

### 1. AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward
**Authors:** Runhui Huang, Jie Wu, Rui Yang, Zhe Liu, Hengshuang Zhao
**Link:** https://arxiv.org/abs/2605.12495v1
**Summary:** The paper presents AlphaGRPO, a new framework that enhances the capabilities of Unified Multimodal Models (UMMs) for complex tasks like text-to-image generation and output refinement, without requiring an initial training phase. By introducing a Decompositional Verifiable Reward system that breaks down user requests into manageable components for evaluation, the framework achieves significant performance improvements in multimodal generation benchmarks and editing tasks. This self-reflective approach effectively leverages the model's inherent understanding to produce higher-quality outputs.

### 2. LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues
**Authors:** Di Wu, Zixiang Ji, Asmi Kawatkar, Bryan Kwan, Jia-Chen Gu, Nanyun Peng, Kai-Wei Chang
**Link:** https://arxiv.org/abs/2605.12493v1
**Summary:** The paper introduces LongMemEval-V2, a benchmark designed to assess how well memory systems in agents can retain and utilize experience in specialized web environments. It evaluates five key memory abilities through 451 curated questions and compares two memory methods: AgentRunbook-R and AgentRunbook-C, where the latter significantly outperformed existing baselines with an average accuracy of 72.5%, despite facing high latency issues. This work establishes LME-V2 as a valuable tool for advancing long-term memory systems in agents.

### 3. Pion: A Spectrum-Preserving Optimizer via Orthogonal Equivalence Transformation
**Authors:** Kexuan Shi, Hanxuan Li, Zeju Qiu, Yandong Wen, Simon Buchholz, Weiyang Liu
**Link:** https://arxiv.org/abs/2605.12492v1
**Summary:** The paper presents Pion, a new optimizer designed for training large language models that maintains the singular values of weight matrices by using orthogonal transformations, as opposed to traditional additive methods. This approach helps preserve the spectral properties of the model while still allowing for effective updates during training. The authors demonstrate that Pion provides stable and competitive performance compared to standard optimizers in both the pretraining and finetuning phases.

### 4. Elastic Attention Cores for Scalable Vision Transformers
**Authors:** Alan Z. Song, Yinjie Chen, Mu Nan, Rui Zhang, Jiahang Cao, Weijian Mai, Muquan Yu, Hossein Adeli, Deva Ramanan, Michael J. Tarr, Andrew F. Luo
**Link:** https://arxiv.org/abs/2605.12491v1
**Summary:** The paper addresses the computational inefficiency of Vision Transformers (ViTs), which struggle with high-resolution images due to their quadratic scaling with the number of image patches. The authors introduce VECA (Visual Elastic Core Attention), an architecture that uses a small set of learned core tokens to facilitate communication among patches, reducing attention complexity to linear time while maintaining high accuracy. The key contribution is that VECA can achieve competitive performance with existing models while substantially lowering computational costs, making it a scalable option for ViTs.

### 5. Task-Adaptive Embedding Refinement via Test-time LLM Guidance
**Authors:** Ariel Gera, Shir Ashury-Tahan, Gal Bloch, Ohad Eytan, Assaf Toledo
**Link:** https://arxiv.org/abs/2605.12487v1
**Summary:** The paper addresses the challenge of improving the performance of embedding models in zero-shot search and classification tasks by refining user queries with guidance from a generative language model (LLM). The authors propose an LLM-guided query refinement method that adapts embedding representations in real-time, leading to significant performance improvements in various benchmarks. Key findings show that this approach enhances ranking quality and better aligns embeddings with the specific requirements of user queries, making it a valuable alternative for practical applications where large LLMs are impractical.

### 6. Learning, Fast and Slow: Towards LLMs That Adapt Continually
**Authors:** Rishabh Tiwari, Kusha Sareen, Lakshya A Agrawal, Joseph E. Gonzalez, Matei Zaharia, Kurt Keutzer, Inderjit S Dhillon, Rishabh Agarwal, Devvrit Khatri
**Link:** https://arxiv.org/abs/2605.12484v1
**Summary:** The paper addresses the issue of catastrophic forgetting in large language models (LLMs) when updating parameters for specific tasks, which limits their flexibility and adaptability. To overcome this, the authors propose a fast-slow learning framework that uses "fast" weights for task-specific adjustments while keeping the "slow" weights close to the base model. The key finding is that this Fast-Slow Training method is significantly more sample-efficient and minimizes forgetting, allowing for better adaptability in continual learning scenarios compared to traditional parameter-only updates.

### 7. Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Principle for Language-Model Post-Training
**Authors:** Yuanda Xu, Hejian Sang, Zhengze Zhou, Ran He, Zhipeng Wang, Alborz Geramifard
**Link:** https://arxiv.org/abs/2605.12483v1
**Summary:** The paper addresses the inefficiency in allocating scarce labeled training data when fine-tuning language models by proposing a reward-density principle. It suggests using sparse rewards for exploration with a strong model (teacher) and then transferring that learned behavior as dense supervision to a smaller model (student). The key findings demonstrate that this strategy improves performance on verifiable tasks, significantly outperforming traditional methods like direct GRPO in specific benchmarks.

### 8. ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
**Authors:** Xuhao Hu, Xi Zhang, Haiyang Xu, Kyle Qiao, Jingyi Yang, Xuanjing Huang, Jing Shao, Ming Yan, Jieping Ye
**Link:** https://arxiv.org/abs/2605.12481v1
**Summary:** The paper presents ToolCUA, an innovative approach for optimizing the decision-making process of Computer Use Agents (CUAs) when choosing between GUI actions and tool calls, a challenge stemming from the lack of quality training data. To address this, the authors developed a method that synthesizes diverse GUI-Tool interactions from existing data and employs a tailored reinforcement learning strategy to enhance decision-making at critical junctures. The results indicate that ToolCUA achieves a 46.85% accuracy, outperforming previous models by a significant margin and demonstrating the effectiveness of training in a hybrid action framework.

### 9. OmniNFT: Modality-wise Omni Diffusion Reinforcement for Joint Audio-Video Generation
**Authors:** Guohui Zhang, XiaoXiao Ma, Jie Huang, Hang Xu, Hu Yu, Siming Fu, Yuming Li, Zeyue Xue, Lin Song, Haoyang Huang, Nan Duan, Feng Zhao
**Link:** https://arxiv.org/abs/2605.12480v1
**Summary:** The paper addresses the challenges of generating high-quality audio and video simultaneously, particularly focusing on maintaining fidelity, alignment, and synchronization across modalities. The authors present OmniNFT, a novel reinforcement learning framework that incorporates three main strategies to improve the generation process, including routing rewards per modality, managing gradient flow, and adjusting optimization efforts based on critical alignment areas. Extensive experiments show that OmniNFT significantly enhances the quality and synchronization of generated audio and video compared to existing methods.

### 10. MEME: Multi-entity & Evolving Memory Evaluation
**Authors:** Seokwon Jung, Alexander Rubinstein, Arnas Uselis, Sangdoo Yun, Seong Joon Oh
**Link:** https://arxiv.org/abs/2605.12477v1
**Summary:** The paper addresses the challenge of evaluating memory systems in language model-based agents that operate in environments requiring management of multiple entities and evolving information over time. The authors introduce the MEME benchmark, which includes six diverse tasks that assess memory performance, revealing that existing systems struggle with dependency reasoning despite performing well in static retrieval scenarios. A notable finding is that only a specific configuration of a file-based agent with a powerful LLM shows improved performance, although this method is significantly more costly, highlighting a gap in practical scalability.

---
## 2026-05-14

### 1. WARDEN: Endangered Indigenous Language Transcription and Translation with 6 Hours of Training Data
**Authors:** Ziheng Zhang, Yunzhong Hou, Naijing Liu, Liang Zheng
**Link:** https://arxiv.org/abs/2605.13846v1
**Summary:** The paper presents WARDEN, a language model specifically designed to transcribe and translate the endangered Wardaman language into English using only six hours of training data. To address the scarcity of large datasets, WARDEN employs separate models for transcription and translation, incorporating techniques like utilizing related phonemes from Sundanese and leveraging a Wardaman-English dictionary. The approach successfully outperforms conventional models that require more data, establishing a strong baseline for low-resource language processing.

### 2. EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents
**Authors:** Tara Bogavelli, Gabrielle Gauthier Melançon, Katrina Stankiewicz, Oluwanifemi Bamgbose, Fanny Riols, Hoang H. Nguyen, Raghav Mehndiratta, Lindsay Devon Brin, Joseph Marinier, Hari Subramani, Anil Madamala, Sridhar Krishna Nemala, Srinivas Sunkara
**Link:** https://arxiv.org/abs/2605.13841v1
**Summary:** The paper presents EVA-Bench, a new framework for evaluating voice agents that improves upon existing benchmarks by simulating realistic conversations and assessing various quality metrics. It introduces two composite metrics, EVA-A and EVA-X, to evaluate task completion and conversational quality, respectively, across different voice agent architectures. The key findings reveal that no evaluated system excels in both accuracy and user experience, highlighting significant robustness gaps in handling variations like accent and background noise.

### 3. What is Learnable in Valiant's Theory of the Learnable?
**Authors:** Steve Hanneke, Anay Mehrotra, Grigoris Velegkas, Manolis Zampetakis
**Link:** https://arxiv.org/abs/2605.13840v1
**Summary:** The paper revisits Valiant's original learning model from 1984, which differs from the PAC learning framework by allowing only positive samples and membership queries without false positives. The authors characterize learnability in this model, revealing that a class is learnable if positive samples can be efficiently certified via an adaptation of query-compression schemes. They demonstrate that learnability in this model is distinct from both PAC learning and a variant without queries, and provide a new algorithm for learning $d$-dimensional halfspaces with queries, marking a significant advancement in understanding Valiant's model of learnability.

### 4. Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights
**Authors:** Wenrui Bao, Huan Wang, Jian Wang, Zhangyang Wang, Kai Wang, Yuzhang Shang
**Link:** https://arxiv.org/abs/2605.13839v1
**Summary:** The paper addresses the inefficiencies of multi-agent large language model (LLM) systems that rely on natural language communication, which can slow down processing and increase memory usage. The authors propose TFlow (Thought Flow), a novel framework that allows agents to directly modify the receiver's weights during inference using low-rank perturbations instead of sending textual messages. This approach results in significant improvements in accuracy and a reduction in processed tokens and inference time, suggesting a more efficient method for agent collaboration.

### 5. R-DMesh: Video-Guided 3D Animation via Rectified Dynamic Mesh Flow
**Authors:** Zijie Wu, Lixin Xu, Puhua Jiang, Sicong Liu, Chunchao Guo, Xiang Bai
**Link:** https://arxiv.org/abs/2605.13838v1
**Summary:** The paper presents R-DMesh, a framework designed to tackle the challenge of aligning user-provided static meshes with reference videos for video-guided 3D animation, where initial pose mismatches can cause significant distortion. By utilizing a novel VAE to disentangle the mesh into a base shape, motion trajectories, and a rectification offset, and applying a Triflow Attention mechanism for processing, R-DMesh effectively rectifies the mesh pose before animation starts. The approach demonstrates strong performance in resolving pose misalignment and enables advanced applications like pose retargeting and comprehensive 4D mesh generation.

### 6. Topology-Preserving Neural Operator Learning via Hodge Decomposition
**Authors:** Dongzhe Zheng, Tao Zhong, Christine Allen-Blanchette
**Link:** https://arxiv.org/abs/2605.13834v1
**Summary:** This paper addresses the challenge of accurately learning solution operators for physical field equations on geometric meshes by using Hodge decomposition to separate learnable geometric dynamics from unlearnable topological features. The authors introduce a new architecture called Hodge Spectral Duality, which utilizes discrete differential forms to effectively capture topological elements and an auxiliary space for local dynamics. Their approach demonstrates improved accuracy and efficiency in modeling, while preserving important physical properties.

### 7. QLAM: A Quantum Long-Attention Memory Approach to Long-Sequence Token Modeling
**Authors:** Hoang-Quan Nguyen, Sankalp Pandey, Khoa Luu
**Link:** https://arxiv.org/abs/2605.13833v1
**Summary:** The paper addresses the challenge of modeling long-range dependencies in sequential data, where traditional transformers struggle due to their quadratic complexity. It introduces Quantum Long-Attention Memory (QLAM), a hybrid quantum-classical memory mechanism that leverages quantum superposition to enhance the representation of historical information while maintaining linear time complexity. QLAM demonstrates superior performance on sequential image classification tasks compared to both recurrent models and transformers.

### 8. Quantifying Sensitivity for Tree Ensembles: A symbolic and compositional approach
**Authors:** S. Akshay, Chaitanya Garg, Ashutosh Gupta, Kuldeep S. Meel, Ajinkya Naik
**Link:** https://arxiv.org/abs/2605.13830v1
**Summary:** The paper addresses the problem of quantifying sensitivity in decision tree ensembles, focusing on how small changes in input features might lead to misclassification. The authors present a new algorithm that uses algebraic decision diagrams to break down the problem and compute sensitivity efficiently, while ensuring a certified error and confidence bound. Their experimental results demonstrate that their tool, XCount, significantly outperforms existing methods in both speed and scalability for various ensemble sizes.

### 9. Negation Neglect: When models fail to learn negations in training
**Authors:** Harry Mayne, Lev McKinney, Jan Dubiński, Adam Karvonen, James Chua, Owain Evans
**Link:** https://arxiv.org/abs/2605.13829v1
**Summary:** The paper addresses the issue of "Negation Neglect," where fine-tuning large language models (LLMs) on documents that assert a claim is false leads the models to incorrectly believe the claim is true. The researchers conducted experiments showing that models significantly increased their belief in false claims when exposed to negated documents, demonstrating that the presence of negations in separate sentences does not effectively teach the models to learn these negations. A key finding is that this neglect not only affects factual claims but also influences model behaviors, raising concerns for AI safety.

### 10. Reducing cross-sample prediction churn in scientific machine learning
**Authors:** Gordan Prastalo, Kevin Maik Jablonka
**Link:** https://arxiv.org/abs/2605.13826v1
**Summary:** The paper addresses the issue of "cross-sample prediction churn" in scientific machine learning, where different models trained on the same dataset produce conflicting predictions for a significant number of test samples. The authors introduce two data-driven approaches to reduce this churn: $K$-bootstrap bagging, which significantly lowers churn rates without sacrificing accuracy, and a novel method called twin-bootstrap, which further decreases churn by applying a consistency loss between predictions of two jointly trained networks. The key contribution is demonstrating that these methods can effectively mitigate prediction inconsistencies, highlighting the importance of reporting churn alongside predictive performance in benchmarks.

---
## 2026-05-15

### 1. EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation
**Authors:** Ruozhen He, Meng Wei, Ziyan Yang, Vicente Ordonez
**Link:** https://arxiv.org/abs/2605.15199v1
**Summary:** The paper addresses the challenge of maintaining consistency of characters, objects, and locations in long multi-shot video generation. It introduces EntityBench, a benchmark with detailed entity tracking across a variety of narrative scenarios, and proposes EntityMem, a memory-augmented system that improves consistency by storing visual references for entities. The results demonstrate that using explicit per-entity memory significantly enhances character fidelity and presence in generated videos.

### 2. ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both
**Authors:** Ziyu Guo, Rain Liu, Xinyan Chen, Pheng-Ann Heng
**Link:** https://arxiv.org/abs/2605.15198v1
**Summary:** The paper presents ATLAS, a novel framework that combines agentic and latent visual reasoning using a single discrete 'functional token', which simplifies the process and avoids the complexities and inefficiencies of generating intermediate visual content. By allowing these tokens to operate without visual supervision and ensuring compatibility with existing training methods, ATLAS enhances performance on visual reasoning tasks while maintaining interpretability. The introduction of Latent-Anchored GRPO further improves training stability by providing stronger gradient updates, ultimately leading to superior results on challenging benchmarks.

### 3. RefDecoder: Enhancing Visual Generation with Conditional Video Decoding
**Authors:** Xiang Fan, Yuheng Wang, Bohan Fang, Zhongzheng Ren, Ranjay Krishna
**Link:** https://arxiv.org/abs/2605.15196v1
**Summary:** The paper addresses the issue of detail loss and inconsistency in video generation caused by decoders that lack sufficient conditioning on input images. It introduces RefDecoder, a video decoder that enhances quality by integrating high-fidelity reference images into the decoding process using reference attention. This approach significantly improves performance, achieving up to +2.1dB PSNR on various benchmarks and demonstrating better subject and background consistency in generated videos.

### 4. FutureSim: Replaying World Events to Evaluate Adaptive Agents
**Authors:** Shashwat Goel, Nikhil Chandak, Arvindh Arun, Ameya Prabhu, Steffen Staab, Moritz Hardt, Maksym Andriushchenko, Jonas Geiping
**Link:** https://arxiv.org/abs/2605.15188v1
**Summary:** The paper addresses the challenge of evaluating AI agents' ability to adapt to new information in dynamic environments by introducing FutureSim, a simulation that replays real-world events chronologically. This approach allows agents to forecast future events while interacting with a timeline of actual news and resolutions. The key finding reveals significant variability in agents' predictive capabilities, with the best performing agent achieving only 25% accuracy, highlighting the need for improved methods in long-term adaptation and reasoning under uncertainty.

### 5. VGGT-Edit: Feed-forward Native 3D Scene Editing with Residual Field Prediction
**Authors:** Kaixin Zhu, Yiwen Tang, Yifan Yang, Renrui Zhang, Bohan Zeng, Ziyu Guo, Ruichuan An, Zhou Liu, Qizhi Chen, Delin Qu, Jaehong Yoon, Wentao Zhang
**Link:** https://arxiv.org/abs/2605.15186v1
**Summary:** The paper presents VGGT-Edit, a novel framework for editing 3D scenes in response to text instructions without the need for traditional 2D editing methods, which often lead to poor visual quality. By using depth-synchronized text injection and a residual transformation head, it predicts direct 3D changes while maintaining consistent geometry and detail. Experiments demonstrate that VGGT-Edit significantly outperforms existing methods, providing sharper details and greater consistency across multiple views.

### 6. Quantitative Video World Model Evaluation for Geometric-Consistency
**Authors:** Jiaxin Wu, Yihao Pi, Yinling Zhang, Yuheng Li, Xueyan Zou
**Link:** https://arxiv.org/abs/2605.15185v1
**Summary:** The paper addresses the challenge of evaluating the geometric consistency of generative video models, as existing methods often rely on subjective judgments. The authors propose a quantitative framework called PDI-Bench, which assesses geometric coherence by analyzing 3D structural and motion characteristics using projective-geometry residuals. The key contribution is the introduction of systematic and objective metrics that reveal geometric failure modes in generated videos, which are not captured by traditional perceptual assessments, thereby advancing the evaluation of realistic video generation.

### 7. Is Grep All You Need? How Agent Harnesses Reshape Agentic Search
**Authors:** Sahil Sen, Akhil Kasturi, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah
**Link:** https://arxiv.org/abs/2605.15184v1
**Summary:** This paper investigates the effectiveness of different information retrieval strategies in enhancing the performance of Large Language Model (LLM) agents during complex search tasks. It empirically compares traditional grep-based searching against vector retrieval methods across various agent harnesses. The key finding is that grep generally outperforms vector retrieval in accuracy, but results vary significantly based on the specific agent architecture and tool-calling approach used.

### 8. When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability
**Authors:** ML Nissen Gonzalez, Melwina Albuquerque, Laurence Wroe, Jacob Meyer Cohen, Logan Riggs Smith, Thomas Dooms
**Link:** https://arxiv.org/abs/2605.15183v1
**Summary:** The paper addresses the challenge of determining when two neural network components perform the same computation, which is crucial for understanding their functionality. It introduces a new metric called tensor similarity that is invariant to weight-space symmetries and effectively measures the global equivalence of tensor-based models. The authors demonstrate that this metric better tracks functional training dynamics compared to existing similarity measures, simplifying the assessment of network similarity and interpretability.

### 9. Eradicating Negative Transfer in Multi-Physics Foundation Models via Sparse Mixture-of-Experts Routing
**Authors:** Ellwil Sharma, Arastu Sharma
**Link:** https://arxiv.org/abs/2605.15179v1
**Summary:** The paper addresses the challenge of negative transfer in multi-physics foundation models, where training on diverse physical regimes can lead to optimization issues. The authors propose Shodh-MoE, a sparse mixture-of-experts architecture that dynamically routes data to specialized subnetworks based on physical mechanisms, while ensuring mass conservation in fluid dynamics. They demonstrate that this approach allows the model to train effectively across different physical domains, achieving low mean squared errors in validation metrics.

### 10. OpenDeepThink: Parallel Reasoning via Bradley--Terry Aggregation
**Authors:** Shang Zhou, Wenhao Chai, Kaiyuan Liu, Huanzhi Mao, Qiuyang Mang, Jingbo Shang
**Link:** https://arxiv.org/abs/2605.15177v1
**Summary:** The paper presents OpenDeepThink, a framework designed to enhance the reasoning capabilities of large language models (LLMs) during test-time by using parallel candidate evaluation and selection. It employs a pairwise comparison method based on the Bradley-Terry model to rank multiple reasoning outputs and improve selection efficiency without ground-truth supervision. The key result shows a significant boost in performance—specifically, an increase of 405 Elo points for the Gemini 3.1 Pro model in competitive programming tasks, with the approach demonstrating effective transferability across various model strengths.

---
## 2026-05-16

### 1. MetaBackdoor: Exploiting Positional Encoding as a Backdoor Attack Surface in LLMs
**Authors:** Rui Wen, Mark Russinovich, Andrew Paverd, Jun Sakuma, Ahmed Salem
**Link:** https://arxiv.org/abs/2605.15172v1
**Summary:** The paper addresses the security vulnerability of large language models (LLMs) to backdoor attacks, which traditionally rely on modifying the input text. The authors introduce a novel backdoor attack, called MetaBackdoor, that exploits the positional encoding used in these models, allowing attackers to trigger malicious behavior without altering the text itself. Key findings demonstrate that even simple positional cues can effectively activate hidden backdoors, revealing sensitive information and enabling attacks that can occur without direct manipulation of the input.

### 2. Evidential Reasoning Advances Interpretable Real-World Disease Screening
**Authors:** Chenyu Lian, Hong-Yu Zhou, Jing Qin
**Link:** https://arxiv.org/abs/2605.15171v1
**Summary:** The paper addresses the problem of limited interpretability and performance in current disease screening models for medical images. It presents EviScreen, an evidential reasoning framework that incorporates historical case evidence to improve both the accuracy of predictions and the transparency of the reasoning process. The key contribution is that EviScreen achieves better disease screening outcomes, particularly in terms of clinical specificity and recall, while also enhancing interpretability through a novel approach to abnormality localization.

### 3. Text Knows What, Tables Know When: Clinical Timeline Reconstruction via Retrieval-Augmented Multimodal Alignment
**Authors:** Sayantan Kumar, Shahriar Noroozizadeh, Juyong Kim, Jeremy C. Weiss
**Link:** https://arxiv.org/abs/2605.15168v1
**Summary:** The paper addresses the challenge of accurately reconstructing clinical timelines, which are crucial for understanding patient conditions like sepsis. The authors propose a novel framework that combines unstructured clinical narratives with structured electronic health record (EHR) data, using a graph-based method to align and enhance temporal precision. Their results show that this multimodal approach significantly improves the accuracy of timestamps and provides a more comprehensive view of patient events compared to using text alone, revealing that many important events are missing from EHR data.

### 4. Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands
**Authors:** Pratinav Seth, Vinay Kumar Sankarapu
**Link:** https://arxiv.org/abs/2605.15164v1
**Summary:** This paper addresses the problem that current behavioral assurance methods cannot effectively verify the safety claims required by new AI governance frameworks, which demand proof of aspects like hidden objectives and long-term safety. The authors introduce the concept of the "audit gap," highlighting the limitations of existing methodologies and propose a shift to include more mechanistic types of evidence alongside behavioral assessments. Their key contribution is a formal analysis of the mismatch between safety claims and the capabilities of current assurance practices, advocating for a more balanced approach to evidence in AI safety governance.

### 5. Hand-in-the-Loop: Improving Dexterous VLA via Seamless Interventional Correction
**Authors:** Zhuohang Li, Liqun Huang, Wei Xu, Zhengming Zhu, Nie Lin, Xiao Ma, Xinjun Sheng, Ruoshi Wen
**Link:** https://arxiv.org/abs/2605.15157v1
**Summary:** The paper addresses the issue of errors in dexterous manipulation by robotic hands, which can be exacerbated during human intervention due to mismatches in control commands. The authors introduce a method called Hand-in-the-Loop (HandITL) that seamlessly combines human corrections with automated actions, significantly reducing abrupt movements and improving manipulation performance. The key findings demonstrate that HandITL not only minimizes errors during human takeovers but also leads to better-trained policies, improving success rates and efficiency in complex tasks.

### 6. MeMo: Memory as a Model
**Authors:** Ryan Wei Heng Quek, Sanghyuk Lee, Alfred Wei Lun Leong, Arun Verma, Alok Prakash, Nancy F. Chen, Bryan Kian Hsiang Low, Daniela Rus, Armando Solar-Lezama
**Link:** https://arxiv.org/abs/2605.15156v1
**Summary:** The paper addresses the challenge of updating large language models (LLMs) with new, domain-specific knowledge without modifying their existing parameters. It presents MeMo (Memory as a Model), a modular framework that encodes new information into a separate memory system, allowing for efficient integration and robust performance across complex tasks. Experimental results demonstrate that MeMo outperforms existing methods while preventing issues like catastrophic forgetting and maintaining retrieval efficiency regardless of the corpus size.

### 7. Self-Distilled Agentic Reinforcement Learning
**Authors:** Zhengxi Lu, Zhiyuan Yao, Zhuowen Han, Zi-Han Wang, Jinyang Wu, Qi Gu, Xunliang Cai, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
**Link:** https://arxiv.org/abs/2605.15155v1
**Summary:** The paper addresses the challenge of providing fine-grained supervision for long-horizon tasks in reinforcement learning (RL) for multi-turn dialogue agents, which often suffer from instability. The authors propose a new approach called Self-Distilled Agentic Reinforcement Learning (SDAR), which integrates On-Policy Self-Distillation (OPSD) as a gated auxiliary objective alongside traditional RL to improve learning stability and performance. Key results demonstrate that SDAR significantly outperforms existing methods on various benchmarks, achieving notable gains in task performance while mitigating instability issues.

### 8. RoSHAP: A Distributional Framework and Robust Metric for Stable Feature Attribution
**Authors:** Lanxin Xiang, Liang Shi, Youhui Ye, Boyu Jiang, Dawei Zhou, Feng Guo
**Link:** https://arxiv.org/abs/2605.15154v1
**Summary:** This paper addresses the issue of inconsistent feature attribution in machine learning, where different runs can yield varying importance scores for the same features. The authors introduce RoSHAP, a robust metric that utilizes bootstrap resampling and kernel density estimation to model the distribution of feature attribution scores, providing a stable ranking of features. Their key finding is that RoSHAP outperforms traditional methods in identifying important features while allowing for effective model building with fewer predictors, enhancing both stability and interpretability in model analysis.

### 9. Pelican-Unified 1.0: A Unified Embodied Intelligence Model for Understanding, Reasoning, Imagination and Action
**Authors:** Yi Zhang, Yinda Chen, Che Liu, Zeyuan Ding, Jin Xu, Shilong Zou, Junwei Liao, Jiayu Hu, Xiancong Ren, Xiaopeng Zhang, Yechi Liu, Haoyuan Shi, Zecong Tang, Haosong Sun, Renwen Cui, Kuishu Wu, Wenhai Liu, Yang Xu, Yingji Zhang, Yidong Wang, Senkang Hu, Jinpeng Lu, Nga Teng Chan, Yechen Wu, Yong Dai, Jian Tang, Xiaozhu Ju
**Link:** https://arxiv.org/abs/2605.15153v1
**Summary:** The paper introduces Pelican-Unified 1.0, a novel embodied foundation model designed to integrate understanding, reasoning, imagination, and action into a single framework. By employing a unified vision-language model that processes and optimizes these capabilities together, it outperforms existing systems on multiple benchmarks. The key contribution is demonstrating that this unified approach can achieve strong performance across various tasks without sacrificing the specialized strengths of individual capabilities.

### 10. Widening the Gap: Exploiting LLM Quantization via Outlier Injection
**Authors:** Xiaohua Zhan, Kazuki Egashira, Robin Staab, Mark Vero, Martin Vechev
**Link:** https://arxiv.org/abs/2605.15152v1
**Summary:** This paper addresses the security vulnerabilities in large language models (LLMs) that arise from quantization, which is often used for efficient deployment. The authors present a novel attack method that exploits the injection of outliers into model weights, causing significant and predictable behavior changes during quantization. Their findings reveal that advanced quantization techniques are susceptible to these attacks, highlighting a broader scope of security risks than previously recognized.

---
## 2026-05-17

### 1. Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution
**Authors:** Saisab Sadhu, Pratinav Seth, Vinay Kumar Sankarapu
**Link:** https://arxiv.org/abs/2605.15138v1
**Summary:** The paper addresses the problem of effective unlearning in quantized language models, where traditional methods struggle to achieve meaningful forgetting due to the compression effects of quantization. The authors propose a novel approach called MANSU (Mechanistic-Aligned Null-Space Unlearning) that uses causal circuit attribution and a specialized projection technique to isolate and forget specific information while maintaining the model's performance and compliance with quantization. Key findings show that MANSU successfully achieves significant forgetting without sacrificing model accuracy or structural integrity, outperforming existing gradient-based methods in various tests.

### 2. Training ML Models with Predictable Failures
**Authors:** Will Schwarzer, Scott Niekum
**Link:** https://arxiv.org/abs/2605.15134v1
**Summary:** The paper addresses the challenge of predicting failure rates for machine learning models at deployment scale, particularly when evaluation sets are too small to capture rare failures. The authors introduce a new fine-tuning objective called forecastability loss, which corrects biases in existing failure prediction methods. Their experiments demonstrate that this approach significantly reduces prediction errors while maintaining the model's main performance and ensuring safety comparable to traditional supervised methods.

### 3. Causal Foundation Models with Continuous Treatments
**Authors:** Christopher Stith, Medha Barath, Vahid Balazadeh, Jesse C. Cresswell, Rahul G. Krishnan
**Link:** https://arxiv.org/abs/2605.15133v1
**Summary:** The paper addresses the challenge of estimating causal effects in situations where treatments vary continuously, which is less commonly studied than binary treatments. The authors introduce a novel causal foundation model that utilizes a transformer to predict treatment-response curves from observational data without requiring additional training on new tasks. Their approach outperforms existing causal models in reconstructing treatment-response curves, representing a significant advancement in causal inference methods for continuous treatment scenarios.

### 4. APWA: A Distributed Architecture for Parallelizable Agentic Workflows
**Authors:** Evan Rose, Tushin Mallick, Matthew D. Laws, Cristina Nita-Rotaru, Alina Oprea
**Link:** https://arxiv.org/abs/2605.15132v1
**Summary:** The paper addresses the challenges faced by autonomous multi-agent systems using large language models (LLMs) when processing complex tasks, specifically issues with reasoning, coordination, and computational scaling. The authors propose the Agent-Parallel Workload Architecture (APWA), which decomposes workflows into non-interfering subproblems that can be executed in parallel, allowing for efficient processing across various domains. The results show that APWA effectively scales with larger tasks and can dynamically handle complex queries, outperforming previous systems.

### 5. Natural Synthesis: Outperforming Reactive Synthesis Tools with Large Reasoning Models
**Authors:** Frederik Schmitt, Matthias Cosler, Niklas Metzger, Julian Siber, Vladimir Krsmanovic, Mohamed Ghanem, Bernd Finkbeiner
**Link:** https://arxiv.org/abs/2605.15131v1
**Summary:** This paper addresses the challenging problem of reactive synthesis, which involves automatically creating hardware circuits from complex logical specifications. The authors introduce a neuro-symbolic approach that combines advanced reasoning models with model checking to improve Verilog implementations and offer a novel method to convert natural language specifications into formal requirements. Their results show that this new "natural synthesis" method outperforms existing tools and can tackle more benchmarks, including harder cases in parameterized systems synthesis.

### 6. MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory
**Authors:** Minghao Guo, Qingyue Jiao, Zeru Shi, Yihao Quan, Boxuan Zhang, Danrui Li, Liwei Che, Wujiang Xu, Shilong Liu, Zirui Liu, Mubbasir Kapadia, Vladimir Pavlovic, Jiang Liu, Mengdi Wang, Yiyu Shi, Dimitris N. Metaxas, Ruixiang Tang
**Link:** https://arxiv.org/abs/2605.15128v1
**Summary:** The paper addresses the challenge of evaluating long-term multimodal memory in agents, particularly regarding their ability to retain and utilize detailed visual evidence necessary for reasoning over time. The authors introduce MemEye, a framework that assesses memory capabilities based on the granularity of visual evidence and its application in reasoning. Their evaluation of various memory methods reveals that existing architectures often fail to adequately preserve fine-grained visual details and struggle with reasoning about changing visual states.

### 7. Understanding How International Students in the U.S. Are Using Conversational AI to Support Cross-Cultural Adaptation
**Authors:** Laleh Nourian, Anisa Callis, Stephanie Patterson, Jadeline Miao, Jamison Heard, Garreth W. Tigwell
**Link:** https://arxiv.org/abs/2605.15127v1
**Summary:** The paper explores how international students in the U.S. use conversational AI tools to navigate their cultural adaptation challenges, noting the lack of cohesive support resources. Through a survey and interviews, the authors find that while students view AI as a quick fix for immediate issues, there is a strong desire for these tools to evolve into ongoing support systems. The study offers insights and recommendations for developing AI solutions that better address the long-term needs of international students.

### 8. CoCo-InEKF: State Estimation with Learned Contact Covariances in Dynamic, Contact-Rich Scenarios
**Authors:** Michael Baumgartner, David Müller, Agon Serifi, Ruben Grandia, Espen Knoop, Markus Gross, Moritz Bächer
**Link:** https://arxiv.org/abs/2605.15122v1
**Summary:** The paper addresses the challenge of state estimation in legged robots during dynamic, contact-rich activities, where traditional methods struggle with nuanced contact scenarios. The authors introduce CoCo-InEKF, a novel extended Kalman filter that employs learned continuous contact velocity covariances rather than binary contact states, allowing for more accurate estimation of contact conditions. Experimental results show that this approach significantly improves the accuracy and consistency of velocity estimation, enabling the robots to perform complex movements like dancing and interacting with varied surfaces more effectively.

### 9. CLOVER: Closed-Loop Value Estimation \& Ranking for End-to-End Autonomous Driving Planning
**Authors:** Sining Ang, Yuguang Yang, Canyu Chen, Yan Wang
**Link:** https://arxiv.org/abs/2605.15120v1
**Summary:** The paper addresses the mismatch between training and evaluation methods in end-to-end autonomous driving planners, which often leads to safety and performance issues. The authors propose CLOVER, a framework that generates diverse trajectory candidates and ranks them using a scorer that predicts planning metrics, enhancing the training process with pseudo-expert trajectories. Key results demonstrate CLOVER's superior performance, achieving state-of-the-art scores in both standard and challenging evaluation settings.

### 10. Talk is (Not) Cheap: A Taxonomy and Benchmark Coverage Audit for LLM Attacks
**Authors:** Karthik Raghu Iyer, Yazdan Jamshidi, Nicholas Bray, Alexey A. Shvets
**Link:** https://arxiv.org/abs/2605.15118v1
**Summary:** The paper addresses the inadequacy of existing benchmarks in evaluating attacks on large language models (LLMs) by creating a comprehensive framework that maps various attack types and techniques. This framework, consisting of a detailed taxonomy and a coverage matrix, was applied to existing benchmarks, revealing that they collectively cover only a small portion of possible attacks, particularly neglecting critical threat categories. The authors provide their taxonomy and findings as reusable resources to help the research community identify and address gaps in benchmark coverage.

---
## 2026-05-19

### 1. DashAttention: Differentiable and Adaptive Sparse Hierarchical Attention
**Authors:** Yuxiang Huang, Nuno M. T. Gonçalves, Federico Alvetreti, Lei Li, Xu Han, Edoardo M. Ponti, André F. T. Martins, Marcos V. Treviso
**Link:** https://arxiv.org/abs/2605.18753v1
**Summary:** The paper presents DashAttention, a novel hierarchical attention mechanism that addresses the limitations of existing methods by allowing for a variable number of key-value blocks to be selected adaptively based on the query. This approach maintains a fully differentiable architecture, resulting in improved long-context modeling capabilities and better performance than current methods like NSA and InfLLMv2, particularly in high-sparsity scenarios. Additionally, DashAttention's implementation shows significant speed improvements during inference compared to previous attention techniques.

### 2. A Readiness-Driven Runtime for Pipeline-Parallel Training under Runtime Variability
**Authors:** Ruitao Liu, Xinyang Tian, Shuo Chen, Tingrui Zhang, Guang Yang, Alan Zhao, Wei Xu
**Link:** https://arxiv.org/abs/2605.18750v1
**Summary:** The paper addresses the inefficiencies in pipeline-parallel training caused by runtime variability, where models may wait for unready tasks, leading to idle time and suboptimal resource usage. It introduces the Runtime-Readiness-First Pipeline (RRFP), which allows for more flexible scheduling based on task readiness rather than rigid predefined orders. The key contribution is that RRFP significantly enhances training speed, achieving up to 1.77 times faster performance on language tasks and up to 2.77 times on multimodal tasks compared to traditional methods, while maintaining training correctness.

### 3. Code as Agent Harness
**Authors:** Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, Yuanchen Bei, Jiaru Zou, Mengting Ai, Zhining Liu, Ting-Wei Li, Lingjie Chen, Yanjun Zhao, Ke Yang, Bingxuan Li, Cheng Qian, Gaotang Li, Xiao Lin, Zhichen Zeng, Ruizhong Qiu, Sirui Chen, Yifan Sun, Xiyuan Yang, Ruida Wang, Rui Pan, Chenyuan Yang, Dylan Zhang, Liri Fang, Zikun Cui, Yang Cao, Pan Chen, Dorothy Sun, Ren Chen, Mahesh Srinivasan, Nipun Mathur, Yinglong Xia, Hong Li, Hong Yan, Pan Lu, Lingming Zhang, Tong Zhang, Hanghang Tong, Jingrui He
**Link:** https://arxiv.org/abs/2605.18747v1
**Summary:** The paper addresses the evolving role of code in agentic systems, where it functions not only as output but also as a foundational element for agent reasoning and actions. The authors introduce the concept of "code as agent harness," organizing their survey into three layers: the interaction between code and agents, the mechanisms that improve performance, and the scaling of these systems to multi-agent environments. Their key contribution is a comprehensive framework for understanding and developing AI agents that can reliably execute complex tasks using code, while also identifying important challenges for future research in this area.

### 4. ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop
**Authors:** Yining Hong, Jiageng Liu, Han Yin, Manling Li, Leonidas Guibas, Li Fei-Fei, Jiajun Wu, Yejin Choi
**Link:** https://arxiv.org/abs/2605.18746v1
**Summary:** The paper introduces ESI-Bench, a new benchmark designed to evaluate embodied spatial intelligence by mimicking how agents actively explore their environments instead of simply processing observations passively. Through extensive experimentation with state-of-the-art models, the authors found that agents using active exploration techniques significantly outperform those that rely on passive sensing, discovering effective spatial strategies on their own. A notable challenge identified is that many errors arise not from perception issues but from poor action choices, highlighting a gap in metacognitive reasoning compared to human strategies.

### 5. SURGE: Approximation-free Training Free Particle Filter for Diffusion Surrogate
**Authors:** Lifu Wei, Yinuo Ren, Naichen Shi, Yiping Lu
**Link:** https://arxiv.org/abs/2605.18745v1
**Summary:** The paper addresses the challenge of improving sample quality in diffusion-based generative models during inference without incurring high computational costs or introducing bias from gradient evaluations. It introduces a new algorithm called \texttt{URGE}, which utilizes a resampling technique based on Girsanov estimation, allowing for effective weight adjustments of simulated trajectories without the need for score calculations. The key contribution is that \texttt{URGE} demonstrates improved generation quality compared to existing methods while being easier to implement and completely free of gradient-based computations.

### 6. Actionable World Representation
**Authors:** Kunqi Xu, Jitao Li, Jianglong Ye, Tianshu Tang, Isabella Liu, Sifei Liu, Xueyan Zou
**Link:** https://arxiv.org/abs/2605.18743v1
**Summary:** The paper addresses the challenge of creating a unified representation of actionable objects in the physical world, which are typically dynamic and change states based on their properties. The authors introduce WorldString, a neural architecture that learns from point clouds or RGB-D video streams to model the state of real-world objects effectively. This framework serves as a versatile digital twin, laying the groundwork for more advanced physical world models and facilitating future integration with policy learning and neural dynamics.

### 7. Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation
**Authors:** Qianhao Yuan, Jie Lou, Xing Yu, Hongyu Lin, Le Sun, Xianpei Han, Yaojie Lu
**Link:** https://arxiv.org/abs/2605.18740v1
**Summary:** The paper addresses the challenge that multimodal large language models (MLLMs) face in understanding fine details in images, particularly when answers depend on small pieces of visual evidence. The authors introduce a self-distillation framework called Vision-OPD, which allows the model to leverage its own focused perceptions of cropped images to improve its performance on full images. Their experiments demonstrate that models trained with Vision-OPD achieve competitive or superior results in fine-grained visual understanding tasks compared to larger existing models.

### 8. What Does the AI Doctor Value? Auditing Pluralism in the Clinical Ethics of Language Models
**Authors:** Payal Chandak, Victoria Alkin, David Wu, Maya Dagan, Taposh Dutta Roy, Maria Clara Saad Menezes, Ayush Noori, Nirali Somia, John S. Brownstein, Ran Balicer, Rebecca W. Brendel, Noa Dagan, Isaac S. Kohane, Gabriel A. Brat
**Link:** https://arxiv.org/abs/2605.18738v1
**Summary:** This paper addresses the issue of how large language models (LLMs) in medicine may not adequately consider the diverse ethical values that physicians prioritize, particularly in cases of conflicting principles like patient autonomy. The authors propose a framework to audit the ethical values embedded in medical AI by analyzing clinician-verified dilemmas and determining how LLMs prioritize different ethical considerations in their decisions. They found that while LLMs exhibit some understanding of value pluralism, they often lean towards specific value preferences, which could lead to rigid ethical stances in clinical practice if not managed appropriately.

### 9. PIXLRelight: Controllable Relighting via Intrinsic Conditioning
**Authors:** Miguel Farinha, Ronald Clark
**Link:** https://arxiv.org/abs/2605.18735v1
**Summary:** The paper introduces PIXLRelight, a fast and effective method for relighting single images with physical accuracy by using a novel intrinsic conditioning technique. This approach combines principles from physically based rendering with learned image synthesis, allowing users to control lighting in a highly detailed manner without the computational overhead typically associated with traditional methods. The key contribution is its ability to achieve high-quality relighting in under a tenth of a second per image, setting a new standard for this application.

### 10. Predictable Confabulations: Factual Recall by LLMs Scales with Model Size and Topic Frequency
**Authors:** Matthew L. Smith, Jonathan P. Shock, Samuel T. Segun, Iyiola E. Olatunji, Tegawendé F. Bissyandé
**Link:** https://arxiv.org/abs/2605.18732v1
**Summary:** This paper investigates how well large language models (LLMs) can recall factual information based on their size and the frequency of topics in their training data. By evaluating 38 models on a substantial dataset of scholarly references, the authors found that a combination of model size and topic representation explains a significant portion of the variance in recall quality. The key insight is that recall performance follows a predictable pattern influenced by the strength of relevant information relative to background noise, suggesting a scalable approach to improve factual recall in LLMs.

---
## 2026-05-20

### 1. Atoms of Thought: Universal EEG Representation Learning with Microstates
**Authors:** Xinyang Tian, Ruitao Liu, Ziyi Ye, Siyang Xue, Xin Wang, Xuesong Chen
**Link:** https://arxiv.org/abs/2605.20182v1
**Summary:** This paper addresses the challenge of effectively representing electroencephalogram (EEG) signals for various applications like sleep staging and emotion recognition. The authors introduce a novel method that uses microstates—short patterns of brain activity—by clustering EEG data into discrete sequences. Their findings demonstrate that this microstate approach significantly improves performance over traditional methods and provides better interpretability and scalability for both research and clinical applications.

### 2. TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload
**Authors:** Zhiben Chen, Youpeng Zhao, Yang Sui, Jun Wang, Yuzhang Shang
**Link:** https://arxiv.org/abs/2605.20179v1
**Summary:** The paper presents TIDE, a new system designed to optimize the inference of large diffusion language models (dLLMs) on resource-limited devices by reducing input/output (I/O) overhead and computational bottlenecks. TIDE utilizes the consistency of expert activations during the diffusion process to develop an interval-based strategy that efficiently manages expert placements, formulated as a mathematical problem to minimize resource use. As a result, it achieves up to 1.5 times the throughput of existing methods without requiring any additional model training.

### 3. From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models
**Authors:** Juncheng Wu, Hardy Chen, Haoqin Tu, Xianfeng Tang, Freda Shi, Hui Liu, Hanqing Lu, Cihang Xie, Yuyin Zhou
**Link:** https://arxiv.org/abs/2605.20177v1
**Summary:** The paper addresses the performance limitations of vision-language models (VLMs) in visual tasks, emphasizing that poor visual perception, rather than reasoning, is the main issue. The authors propose a staged training approach, separating visual perception, visual reasoning, and textual reasoning, and demonstrate that targeted optimization of visual perception enhances overall performance. Their results indicate that models trained with this method achieve significantly improved accuracy in reasoning tasks with shorter reasoning processes, highlighting the importance of strong visual perception as a foundation for effective reasoning.

### 4. ClinSeekAgent: Automating Multimodal Evidence Seeking for Agentic Clinical Reasoning
**Authors:** Juncheng Wu, Letian Zhang, Yuhan Wang, Haoqin Tu, Hardy Chen, Zijun Wang, Cihang Xie, Yuyin Zhou
**Link:** https://arxiv.org/abs/2605.20176v1
**Summary:** The paper introduces ClinSeekAgent, an automated system designed to actively gather and synthesize multimodal clinical evidence, moving away from the typical reliance on pre-curated data. By querying various medical data sources and refining its hypotheses in real-time, ClinSeekAgent significantly improves the performance of language models in clinical reasoning tasks, achieving notable F1 score enhancements on both text-only and multimodal challenges. Additionally, it serves as a training pipeline for creating more efficient models capable of effective evidence seeking.

### 5. Multi-axis Analysis of Image Manipulation Localization
**Authors:** Keanu Nichols, Divya Appapogu, Giscard Biamby, Dina Bashkirova, Anna Rohrbach, Bryan A. Plummer
**Link:** https://arxiv.org/abs/2605.20174v1
**Summary:** The paper addresses the challenge of detecting advanced image manipulations, which have become increasingly prevalent due to generative AI but can contribute to misinformation. The authors introduce a new benchmark called AUDITS, which includes over 530,000 images across various domains, manipulation types, and sizes, facilitating a multi-axis analysis of detection methods. Their research aims to enhance the understanding of existing techniques' robustness and drive the development of more effective image manipulation detection tools.

### 6. A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents
**Authors:** Vasundra Srinivasan
**Link:** https://arxiv.org/abs/2605.20173v1
**Summary:** The paper addresses the challenges of integrating stochastic outputs from large language models (LLMs) with deterministic software systems in the context of production agents, introducing the concept of the stochastic-deterministic boundary (SDB) as a key architectural component. It presents a methodology and a catalog of six runtime patterns for effectively composing the SDB across different types of agents, along with strategies for diagnosing failures. A notable contribution is the five-step method for selecting suitable runtime patterns based on workload characteristics, which is demonstrated through a practical implementation for managing contract renewals.

### 7. Long-term Power Grid Planning via Answer Set Programming
**Authors:** Antonio Ielo, Francesco Doria, Sandra Castellanos-Paez, Marco Maratea, Francesco Percassi, Mauro Vallati
**Link:** https://arxiv.org/abs/2605.20172v1
**Summary:** This paper addresses the challenge of long-term power grid planning, which must adapt to sustainability, demand changes, and urbanization while maintaining service quality. The authors introduce a novel approach using Answer Set Programming (ASP) to automate and optimize this planning process, demonstrating its capability to effectively handle complex grid requirements through both synthetic and real-world data evaluations. The key contribution is the successful application of ASP to express and manage intricate topological and combinatorial constraints in grid planning.

### 8. KoRe: Compact Knowledge Representations for Large Language Models
**Authors:** Davide Cavicchini, Fausto Giunchiglia, Jacopo Staiano
**Link:** https://arxiv.org/abs/2605.20170v1
**Summary:** The paper introduces KoRe, a new method for improving Large Language Models (LLMs) by integrating human-readable Knowledge Graphs (KGs) in a more efficient way. Instead of retraining the entire model, KoRe encodes sub-graphs into compact knowledge tokens that can be easily injected into the LLM, achieving competitive performance on benchmarks while significantly reducing token usage by up to 10 times. This approach enhances the interpretability and reliability of LLMs, addressing issues with knowledge representation and hallucinations.

### 9. HaorFloodAlert: Deseasonalized ML Ensemble for 72-Hour Flood Prediction in Bangladesh Haor Wetlands
**Authors:** Salma Hoque Talukdar Koli, Fahima Haque Talukder Jely, Md. Samiul Alim, Md. Zakir Hossen
**Link:** https://arxiv.org/abs/2605.20167v1
**Summary:** The paper addresses the problem of rapid flash floods in Bangladesh's haor wetlands, which threaten the annual boro rice harvest and are poorly predicted by current flood forecasting systems. The authors developed HaorFloodAlert, a deseasonalized machine learning ensemble that accurately forecasts flood probabilities by incorporating data on temperature and upstream river conditions. Their ensemble model achieves high predictive accuracy, with significant validation results that aim to improve flood warning capabilities and mitigate agricultural damage.

### 10. Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR
**Authors:** Utkarsh Tyagi, Xingang Guo, MohammadHossein Rezaei, Daniel George, Anas Mahmoud, Jackson Lee, Bing Liu, Yunzhong He
**Link:** https://arxiv.org/abs/2605.20164v1
**Summary:** The paper addresses the challenge of optimizing reinforcement learning with rubric-based rewards, where certain criteria may not be effective signals for improving model performance. The authors propose POW3R, a policy-aware reward framework that adjusts the importance of rubric criteria based on their current relevance during training, enhancing the learning process. The key result shows that POW3R significantly improves both overall reward and completion rates while requiring fewer training steps compared to traditional methods.
