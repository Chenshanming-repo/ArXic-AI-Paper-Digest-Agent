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
