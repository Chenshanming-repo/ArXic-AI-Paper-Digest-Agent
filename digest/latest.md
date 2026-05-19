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
