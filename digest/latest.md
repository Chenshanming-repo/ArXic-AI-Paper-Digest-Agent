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
