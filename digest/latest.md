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
