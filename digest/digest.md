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
