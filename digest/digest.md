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
