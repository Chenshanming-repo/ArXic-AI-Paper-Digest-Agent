---
## 2026-05-25

### 1. SkillOpt: Executive Strategy for Self-Evolving Agent Skills
**Authors:** Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, Chong Luo
**Link:** https://arxiv.org/abs/2605.23904v1
**Summary:** The paper introduces SkillOpt, a novel approach for optimizing agent skills in a systematic and controlled manner, addressing the limitations of existing methods that lack reliable improvement under feedback. By treating skills as external states of a fixed agent and employing a text-space optimization model, SkillOpt effectively edits skill documents to enhance performance. The results demonstrate significant improvements in accuracy across various benchmarks and models, outperforming existing techniques and showing that optimized skills maintain their effectiveness across different environments.

### 2. LLMs as Noisy Channels: A Shannon Perspective on Model Capacity and Scaling Laws
**Authors:** Xu Ouyang, Deyi Liu, Yuhang Cai, Jing Liu, Yuan Yang, Chen Zheng, Thomas Hartvigsen, Yiyuan Ma
**Link:** https://arxiv.org/abs/2605.23901v1
**Summary:** This paper addresses the limitations of existing scaling laws for Large Language Models (LLMs) that do not account for issues like performance degradation despite increased resources. The authors propose the Shannon Scaling Law, which frames LLM training as information transmission over a noisy channel, allowing for a better understanding of model capacity and performance. Their experiments demonstrate that this new framework not only explains observed non-monotonic phenomena but also outperforms traditional scaling laws in predicting model performance accurately.

### 3. From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills
**Authors:** Zisu Huang, Jingwen Xu, Yifan Yang, Ziyang Gong, Qihao Yang, Muzhao Tian, Xiaohua Wang, Changze Lv, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Xue Yang, Dongdong Chen, Xiaoqing Zheng, Chong Luo
**Link:** https://arxiv.org/abs/2605.23899v1
**Summary:** The paper addresses the challenge of effectively utilizing model-generated skills in language agents by systematically studying their lifecycle—how they are generated, extracted, and consumed. The authors developed a comprehensive evaluation framework to analyze the effectiveness of these skills across various tasks and found that while model-generated skills provide average benefits, they can also lead to negative transfer depending on the model's role in extraction and consumption. As a key contribution, they propose a "meta-skill" that enhances skill extraction by focusing on features that improve utility, thereby reducing negative transfer across different domains.

### 4. SPACENUM: Revisiting Spatial Numerical Understanding in VLMs
**Authors:** Jianshu Zhang, Yijiang Li, Huifeixin Chen, Haoran Lu, Letian Xue, Bingyang Wang, Han Liu
**Link:** https://arxiv.org/abs/2605.23898v1
**Summary:** The paper "SPACENUM" addresses the challenge of whether Vision-Language Models (VLMs) effectively understand numerical outputs related to spatial perceptions in dynamic and static environments. The authors introduce SpaceNum, a framework to evaluate VLMs through two tasks that assess their mapping of visual spatial structures to numerical representations. The key finding reveals that current VLMs struggle to genuinely ground numerical values in spatial contexts, often performing poorly and relying on superficial cues rather than robust spatial reasoning.

### 5. ETCHR: Editing To Clarify and Harness Reasoning
**Authors:** Beichen Zhang, Yuhong Liu, Jinsong Li, Yuhang Zang, Jiaqi Wang, Dahua Lin
**Link:** https://arxiv.org/abs/2605.23897v1
**Summary:** The paper addresses the challenge of improving visual reasoning in multimodal large language models, which often struggle with complex questions requiring precise image transformations. The authors propose ETCHR, a specialized image editing model that separates the editing process from the reasoning model, enhancing its ability to correctly modify images based on abstract questions. This approach significantly improves reasoning accuracy across various tasks, boosting performance metrics by up to 5.47 points in different model implementations.

### 6. Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models
**Authors:** Hongwu Peng, Ohiremen Dibua, Yuanjun Xiong, Yifan Gong, Jianming Zhang, Yan Kang
**Link:** https://arxiv.org/abs/2605.23893v1
**Summary:** The paper presents Complete-muE, a framework designed to improve the transfer of hyperparameters between dense feedforward networks and mixture-of-experts (MoE) models in transformer architectures. It utilizes a two-bridge system that effectively facilitates this transfer despite changes in model complexity and token distribution, allowing for consistent hyperparameter optimization across various model configurations. The key contribution is that hyperparameters tuned on a single dense model can be successfully adapted to multiple MoE setups, enabling faster convergence and a more efficient scaling process without extensive hyperparameter tuning.

### 7. Good Token Hunting: A Hitchhiker's Guide to Token Selection for Visual Geometry Transformers
**Authors:** Shuhong Zheng, Michael Oechsle, Erik Sandström, Marie-Julie Rakotosaona, Federico Tombari, Igor Gilitschenski
**Link:** https://arxiv.org/abs/2605.23892v1
**Summary:** This paper addresses the computational inefficiency of visual geometry transformers, which struggle to scale due to quadratic growth in costs linked to the number of input tokens. The authors propose a two-stage token selection framework that reduces the number of key/value tokens by first selecting crucial frames and then filtering redundant tokens within them. Their method significantly accelerates these models by over 85% while maintaining or improving performance, highlighting its potential for enhancing future applications.

### 8. CHRONOS: Temporally-Aware Multi-Agent Coordination for Evolving Data Marketplaces
**Authors:** Joydeep Chandra
**Link:** https://arxiv.org/abs/2605.23887v1
**Summary:** The paper presents CHRONOS, a three-layer architecture designed to improve the coordination in temporal knowledge-graph data marketplaces, addressing issues such as outdated information retrieval, inaccurate value attribution, and inefficient privacy budget management. By utilizing neural-ODE for updating data shortcuts, adjusting Shapley pricing based on data changes, and applying a specific algorithm for regret minimization while maintaining differential privacy, CHRONOS achieves competitive performance metrics, such as high recall rates and low latency. The results indicate that while privacy metrics may lead to noise-dominated valuations, the system effectively enhances data retrieval and agent coordination in evolving environments.

### 9. Multilingual Knowledge Transfer under Data Constraints via Lexical Interventions
**Authors:** Anastasiia Sedova, Natalie Schluter, Skyler Seto, Maartje ter Hoeve
**Link:** https://arxiv.org/abs/2605.23885v1
**Summary:** The paper addresses the challenge of transferring knowledge from high-resource languages to low-resource languages in multilingual models, particularly when target language data is limited. The authors introduce a method called LINK, which uses lexical substitutions in the high-resource training data based on bilingual vocabularies, requiring no additional training or resources. Their evaluation demonstrates significant improvements in performance for target languages across multiple model sizes, achieving up to twice the training efficiency to reach similar performance levels.

### 10. PGT: Procedurally Generated Tasks for improving visual grounding in MLLMs
**Authors:** Rim Assouel, Amir Bar, Michal Drozdzal, Adriana Romero-Soriano
**Link:** https://arxiv.org/abs/2605.23883v1
**Summary:** The paper addresses the challenge of fine-grained visual understanding in Multimodal Large Language Models (MLLMs), which often struggle with complex perception tasks. The authors introduce Procedurally Generated Tasks (PGT), a framework that creates additional training data by overlaying geometric shapes on images, helping to improve visual grounding and identify weaknesses in model perception. Their experiments show significant performance gains, with improvements of up to 20% on specific benchmarks, suggesting that enhanced supervision can effectively address existing limitations in these models.
