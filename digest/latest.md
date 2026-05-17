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
