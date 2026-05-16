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
