---
## 2026-05-23

### 1. DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback
**Authors:** Yunpeng Dong, Jingkai He, Yuze Hou, Dong Du, Zhonghu Xu, Si Yu, Yubin Xia, Haibo Chen
**Link:** https://arxiv.org/abs/2605.22781v1
**Summary:** The paper addresses the latency issue in stateful AI agents that rely on frequent checkpointing and rollback of their entire state, which can take hundreds of milliseconds. To solve this, the authors introduce a new OS-level abstraction called DeltaState, which only captures changes between consecutive checkpoints instead of duplicating the entire state. The key contribution is DeltaBox, a sandbox system that achieves millisecond-level checkpoint and rollback times (14ms and 5ms, respectively), thus enabling AI agents to explore significantly more options within fixed time limits.

### 2. FAME: Failure-Aware Mixture-of-Experts for Message-Level Log Anomaly Detection
**Authors:** Huanchi Wang, Zihang Huang, Yifang Tian, Kristina Dzeparoska, Hans-Arno Jacobsen, Alberto Leon-Garcia
**Link:** https://arxiv.org/abs/2605.22779v1
**Summary:** The paper addresses the challenge of detecting log anomalies at the message level, which is crucial for identifying specific issues within production systems, as existing methods focus on broader session-level alerts. The authors propose FAME, a label-efficient framework that leverages a large language model offline to classify log lines into failure domains, significantly reducing the need for extensive labeled data. Key results show that FAME achieves high accuracy (F1 scores of 98.16 and 99.95 on different datasets) while minimizing annotation effort by 76 times and effectively detecting a majority of anomalies from previously unseen event types.

### 3. SDPM: Survival Diffusion Probabilistic Model for Continuous-Time Survival Analysis
**Authors:** Stanislav R. Kirpichenko, Andrei V. Konstantinov, Lev V. Utkin
**Link:** https://arxiv.org/abs/2605.22776v1
**Summary:** The paper introduces the Survival Diffusion Probabilistic Model (SDPM) to enhance continuous-time survival analysis, addressing limitations of existing methods related to hazard function assumptions and time discretization. By utilizing a denoising diffusion model to estimate survival distributions without these restrictions, SDPM demonstrates competitive performance against established models on various datasets. Its innovative approach to transforming target space significantly improves the model's predictive accuracy and calibration of event rates.

### 4. MambaGaze: Bidirectional Mamba with Explicit Missing Data Modeling for Cognitive Load Assessment from Eye-Gaze Tracking Data
**Authors:** Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh, Mimi Xie, Rocky Slavin, Leslie Neely, John Davis, John Quarles
**Link:** https://arxiv.org/abs/2605.22775v1
**Summary:** The paper presents MambaGaze, a novel framework for assessing cognitive load in real-time using eye-tracking data, addressing issues of data loss from blinks and the need for effective modeling of long-term dependencies. The approach includes a unique encoding method to capture data uncertainty and a bidirectional modeling technique with efficient computation. It achieves significant accuracy improvements over existing methods and demonstrates the capability for real-time performance on portable devices, making it suitable for applications like driver monitoring.

### 5. CogAdapt: Transferring Clinical ECG Foundation Models to Wearable Cognitive Load Assessment via Lead Adaptation
**Authors:** Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh, Mimi Xie, Rocky Slavin, Leslie Neely, John Davis, John Quarles
**Link:** https://arxiv.org/abs/2605.22774v1
**Summary:** The paper addresses the challenge of accurately assessing cognitive load using wearable ECG devices, which traditionally struggle with limited data and individual differences. The authors introduce CogAdapt, a framework that uses a learnable adapter to convert signals from wearable sensors into formats compatible with clinical ECG models, along with a fine-tuning approach to improve performance. The results indicate that CogAdapt significantly enhances cognitive load assessment accuracy compared to models trained from scratch, demonstrating its effectiveness in transferring knowledge from clinical to wearable settings.

### 6. Deep Reinforcement Learning for Flexible Job Shop Scheduling with Random Job Arrivals
**Authors:** Yu Tang, Muhammad Zakwan, Efe Balta, John Lygeros, Alisa Rupenyan
**Link:** https://arxiv.org/abs/2605.22773v1
**Summary:** The paper addresses the Flexible Job Shop Scheduling Problem (FJSP), which involves efficiently allocating jobs with unpredictable arrivals to machines, a task complicated by its combinatorial complexity. The authors propose using a Deep Reinforcement Learning (DRL) approach, specifically the Proximal Policy Optimization algorithm, to minimize job completion times, while leveraging simple neural networks and established dispatching rules. The key finding is that their DRL method significantly outperforms traditional dispatching rules and performs well compared to a mixed-integer linear programming solution, particularly in heterogeneous environments.

### 7. Reducing Political Manipulation with Consistency Training
**Authors:** Long Phan, Devin Kim, Alexander Pan, Alice Blair, Adam Khoja, Dan Hendrycks
**Link:** https://arxiv.org/abs/2605.22771v1
**Summary:** The paper addresses the issue of systematic political bias in large language models (LLMs), which show uneven responses to topics from different political perspectives, a phenomenon termed covert political bias. To combat this, the authors propose Political Consistency Training (PCT), a reinforcement learning method that focuses on improving symmetry in sentiment and helpfulness across political prompts. The results demonstrate that PCT effectively reduces covert bias while maintaining the overall helpfulness of the model, showing promise for application to other benchmarks.

### 8. Understanding Data Temporality Impact on Large Language Models Pre-training
**Authors:** Pilchen Hippolyte, Fabre Romain, Signe Talla Franck, Perez Patrick, Grave Edouard
**Link:** https://arxiv.org/abs/2605.22769v1
**Summary:** This paper addresses the issue of how the temporal ordering of training data affects the knowledge retention of large language models (LLMs). The authors created a benchmark for evaluating time-sensitive factual knowledge and pretrained models on temporally ordered datasets rather than the typical shuffled corpora. Their key finding is that sequentially trained models are better at retaining up-to-date knowledge and associating facts with their correct time periods compared to those trained on shuffled data.

### 9. Uniform Diffusion Models Revisited: Leave-One-Out Denoiser and Absorbing State Reformulation
**Authors:** Samson Gourevitch, Yazid Janati, Dario Shariatian, Umut Simsekli, Eric Moulines, Eric P. Xing, Alain Durmus
**Link:** https://arxiv.org/abs/2605.22765v1
**Summary:** This paper addresses the discrepancy in training objectives for Uniform Diffusion Models (UDM) by introducing the concept of a leave-one-out denoiser, which predicts each token without relying on its own noisy observation. The authors present a new framework that optimizes this denoising process and reformulates UDM to utilize simpler sampling operations, leading to improved performance in language modeling. Key findings indicate that enhancements in UDM generation are primarily due to changes in parameterization and sampling strategy rather than the choice of model marginals.

### 10. Advancing Mathematics Research with AI-Driven Formal Proof Search
**Authors:** George Tsoukalas, Anton Kovsharov, Sergey Shirobokov, Anja Surina, Moritz Firsching, Gergely Bérczi, Francisco J. R. Ruiz, Arun Suggala, Adam Zsolt Wagner, Eric Wieser, Lei Yu, Aja Huang, Miklós Z. Horváth, Andrew Ferrauiolo, Henryk Michalewski, Codrut Grosu, Thomas Hubert, Matej Balog, Pushmeet Kohli, Swarat Chaudhuri
**Link:** https://arxiv.org/abs/2605.22763v1
**Summary:** The paper addresses the challenge of unreliable mathematical reasoning from large language models (LLMs) by using them to generate formal proofs in languages like Lean. The authors conducted a large-scale evaluation and found that their most capable AI agent successfully solved 9 out of 353 open Erdős problems and proved 44 OEIS conjectures at competitive costs. This work highlights the potential of AI to enhance formal proof search in various mathematical domains, showcasing effective agent designs for this purpose.
