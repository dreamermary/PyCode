>关键词：框架/综述实时/流/多语/预训练微调/数据增强/S2S/ML/iwlst/NA/CS/NER/transformer改进/seg/
>   CS: code-switch
>   NA: Non-autogress
>   iwslt比赛: 低资源，多语，离线


### 综合
|---|---|---|---|
|---|---|---|---|
|Cascade versus Direct Speech Translation: Do the Differences Still Make a Difference?|acl21|综述：级联&端到端 |https://aclanthology.org/2021.acl-long.224/|
|An Empirical Study on Task-Oriented Dialogue Translation	|icassp21| |https://ieeexplore.ieee.org/document/9413521|
|NeurST: Neural Speech Translation Toolkit|acl21| 框架|https://aclanthology.org/2021.acl-demo.7/|
|The Multilingual TEDx Corpus for Speech Recognition and Translation|interspeech21|语料|https://www.isca-speech.org/archive/interspeech_2021/salesky21_interspeech.html|
|kosp2e: Korean Speech to English Translation Corpus|interspeech21|语料|https://www.isca-speech.org/archive/interspeech_2021/cho21b_interspeech.html|
|BSTC: A Large-Scale Chinese-English Speech Translation Dataset|naacl21| 语料|https://aclanthology.org/2021.autosimtrans-1.5/|
|GigaST: A 10,000-hour Pseudo Speech Translation Corpus|interspeech22|语料 |https://arxiv.org/abs/2204.03939|
|Highland Puebla Nahuatl Speech Translation Corpus for Endangered Language Documentation|naacl21| 语料|https://aclanthology.org/2021.americasnlp-1.7/|
|A Large-Scale Chinese Multimodal NER Dataset with Speech Clues|acl21|NER语料 |https://aclanthology.org/2021.acl-long.218/|

### 自/半监督，自训练
|---|---|---|---|
|---|---|---|---|
|Investigating Self-Supervised Pre-Training for End-to-End Speech Translation|interspeech20|自监督预训练/综述/Multimodal Learning|https://www.isca-speech.org/archive/interspeech_2020/nguyen20_interspeech.html|
|Self-Training for End-to-End Speech Translation|interspeech20|自训练|https://www.isca-speech.org/archive/interspeech_2020/pino20_interspeech.html|
|Self-Supervised Representations Improve End-to-End Speech Translation|interspeech20|自监督表征|https://www.isca-speech.org/archive/interspeech_2020/wu20g_interspeech.html|
|Large-Scale Self- and Semi-Supervised Learning for Speech Translation|interspeech21|自监督/半监督|https://www.isca-speech.org/archive/interspeech_2021/wang21r_interspeech.html|
|Combining Spectral and Self-Supervised Features for Low Resource Speech Recognition and Translation|interspeech22| 自监督、特征融合|https://arxiv.org/abs/2204.02470|

### 数据的利用：MTL/KD/PT
|---|---|---|---|
|---|---|---|---|
|Stacked Acoustic-and-Textual Encoding: Integrating the Pre-trained Models into Speech Translation Encoders|acl21| |https://aclanthology.org/2021.acl-long.204/|
|Improving Speech Translation by Understanding and Learning from the Auxiliary Text Translation Task|acl21| |https://aclanthology.org/2021.acl-long.328/|
|Listen, Understand And Translate: Triple Supervision Decouples End-To-End Speech-To-Text Translation	|aaai21| |https://www.aaai.org/AAAI21Papers/AAAI-10343.DongQ.pdf|
|Consecutive Decoding For Speech-To-Text Translation	|aaai21| |https://www.aaai.org/AAAI21Papers/AAAI-9845.DongQ.pdf|
|STEMM: Self-learning with Speech-text Manifold Mixup for Speech Translation|acl22| |https://arxiv.org/abs/2203.10426|
|End-to-End Speech Translation via Cross-Modal Progressive Training|interspeech21| |https://www.isca-speech.org/archive/interspeech_2021/ye21_interspeech.html|
|Regularizing End-to-End Speech Translation with Triangular Decomposition Agreement|aaai22| 周|https://arxiv.org/abs/2112.10991|
||||
|Beyond Sentence-Level End-to-End Speech Translation: Context Helps|acl21|文档水平上下文 |https://aclanthology.org/2021.acl-long.200/|
|Cascaded Models with Cyclic Feedback for Direct Speech Translation|icassp21| |	https://ieeexplore.ieee.org/document/9413719|
|Robust Latent Representations Via Cross-Modal Translation and Alignment|icassp21| 复杂|	https://ieeexplore.ieee.org/document/9413456|
|Jointly Trained Transformers Models for Spoken Language Translation|icassp21|HOW2 |	https://ieeexplore.ieee.org/document/9414159|
|Source and Target Bidirectional Knowledge Distillation for End-to-end Speech Translation|naacl21|KD |https://aclanthology.org/2021.naacl-main.150/|
|ASR Posterior-Based Loss for Multi-Task End-to-End Speech Translation|interspeech21|MTL|https://www.isca-speech.org/archive/interspeech_2021/ko21_interspeech.html|
|Lexical Modeling of ASR Errors for Robust Speech Translation|interspeech21|ASR错误-健壮性|https://www.isca-speech.org/archive/interspeech_2021/martucci21_interspeech.html|



### 多语
|---|---|---|---|
|---|---|---|---|
|Multilingual Speech Translation from Efficient Finetuning of Pretrained Models|acl21|多语/预训练微调|https://aclanthology.org/2021.acl-long.68/|
|Lightweight Adapter Tuning for Multilingual Speech Translation|acl21|多语|https://aclanthology.org/2021.acl-short.103/|
|CoVoST 2 and Massively Multilingual Speech Translation|interspeech21|多语|https://www.isca-speech.org/archive/interspeech_2021/wang21s_interspeech.html|
|Improving Cross-Lingual Transfer Learning for End-to-End Speech Recognition with Speech Translation|interspeech20|多语/ASR-ST|https://www.isca-speech.org/archive/interspeech_2020/wang20ia_interspeech.html|
### 杂
|---|---|---|---|
|---|---|---|---|
|Speechformer - Reducing Information Loss in Direct Speech Translation.|emnlp21|transformer改进 |	https://arxiv.org/abs/2109.04574|
|Mutual-Learning Improves End-to-End Speech Translation.	|emnlp21|ML|https://dblp.org/rec/conf/emnlp/ZhaoLCG21|
|End-to-End Speech Translation for Code Switched Speech|acl22|CS|https://arxiv.org/abs/2204.05076|
|Sample, Translate, Recombine: Leveraging Audio Alignments for Data Augmentation in End-to-end Speech Translation|acl22|数据增强|https://arxiv.org/abs/2203.08757|
|Is "moby dick" a Whale or a Bird? Named Entities and Terminology in Speech Translation.|emnlp21|NER |	https://arxiv.org/abs/2109.07439|
|ORTHROS: non-autoregressive end-to-end speech translation With dual-decoder|icassp21|NA|	https://ieeexplore.ieee.org/document/9415093|
|Under the Morphosyntactic Lens: A Multifaceted Evaluation of Gender Bias in Speech Translation|acl22| |https://arxiv.org/abs/2203.09866|
||||
|SpecRec: An Alternative Solution for Improving End-to-End Speech-to-Text Translation via Spectrogram Reconstruction|interspeech21|频谱增强|https://www.isca-speech.org/archive/interspeech_2021/chen21i_interspeech.html|
|Effects of Feature Scaling and Fusion on Sign Language Translation|interspeech21|特征放缩融合|https://www.isca-speech.org/archive/interspeech_2021/ananthanarayana21_interspeech.html|
|Relative Positional Encoding for Speech Recognition and Direct Translation|interspeech20|相对位置编码/ASR-ST|https://www.isca-speech.org/archive/interspeech_2020/pham20_interspeech.html|
|Low-Latency Sequence-to-Sequence Speech Recognition and Translation by Partial Hypothesis Selection|interspeech20|ASR-ST|https://www.isca-speech.org/archive/interspeech_2020/liu20s_interspeech.html|
|Subtitle Translation as Markup Translation|interspeech21|Spoken Machine Translation|https://www.isca-speech.org/archive/interspeech_2021/cherry21_interspeech.html|
|AlloST: Low-Resource Speech Translation Without Source Transcription|interspeech21|Spoken Machine Translation|https://www.isca-speech.org/archive/interspeech_2021/cheng21_interspeech.html|
|Weakly-Supervised Speech-to-Text Mapping with Visually Connected Non-Parallel Speech-Text Data Using Cyclic Partially-Aligned Transformer|interspeech21|Spoken Machine Translation|https://www.isca-speech.org/archive/interspeech_2021/effendi21_interspeech.html|
|Transcribing Paralinguistic Acoustic Cues to Target Language Text in Transformer-Based Speech-to-Text Translation|interspeech21|Spoken Machine Translation|https://www.isca-speech.org/archive/interspeech_2021/tokuyama21_interspeech.html|
|Optimally Encoding Inductive Biases into the Transformer Improves End-to-End Speech Translation|interspeech21|Spoken Machine Translation|https://www.isca-speech.org/archive/interspeech_2021/vyas21_interspeech.html|
|Integrating Frequency Translational Invariance in TDNNs and Frequency Positional Information in 2D ResNets to Enhance Speaker Verification|interspeech21|SdSV Challenge 2021: Analysis and Exploration of New Ideas on Short-Duration Speaker Verification|https://www.isca-speech.org/archive/interspeech_2021/thienpondt21_interspeech.html|
|Lost in Interpreting: Speech Translation from Source or Interpreter?|interspeech21|Spoken Language Processing II|https://www.isca-speech.org/archive/interspeech_2021/machacek21_interspeech.html|


### 流/实时
|---|---|---|---|
|---|---|---|---|
|Learning When to Translate for Streaming Speech|acl22|流|https://arxiv.org/abs/2109.07368|
|Streaming Simultaneous Speech Translation with Augmented Memory Transformer|icassp21|实时/流|	https://ieeexplore.ieee.org/document/9414897|
|An Empirical Study of End-To-End Simultaneous Speech Translation Decoding Strategies|icassp21|实时/解码策略综述|	https://ieeexplore.ieee.org/document/9414276|
|Multilingual Simultaneous Speech Translation|interspeech22| 实时|https://arxiv.org/abs/2203.14835|
|Efficient Wait-k Models for Simultaneous Machine Translation|interspeech20|实时|https://www.isca-speech.org/archive/interspeech_2020/elbayad20_interspeech.html|
|Large-Scale Streaming End-to-End Speech Translation with Neural Transducers|interspeech22|流 |https://arxiv.org/abs/2204.05352|
|Towards Simultaneous Machine Interpretation|interspeech21|实时/MT|https://www.isca-speech.org/archive/interspeech_2021/perezgonzalezdemartos21_interspeech.html|

#### SEG
|---|---|---|---|
|---|---|---|---|
|Impact of Encoding and Segmentation Strategies on End-to-End Simultaneous Speech Translation|interspeech21|实时|https://www.isca-speech.org/archive/interspeech_2021/nguyen21d_interspeech.html|
|Contextualized Translation of Automatically Segmented Speech|interspeech20|seg|https://www.isca-speech.org/archive/interspeech_2020/gaido20_interspeech.html|
|Speech Segmentation Optimization using Segmented Bilingual Speech Corpus for End-to-end Speech Translation|interspeech22|seg |https://arxiv.org/abs/2203.15479|
|SHAS: Approaching optimal Segmentation for End-to-End Speech Translation|interspeech22|seg|https://arxiv.org/abs/2202.04774|




### MT
|---|---|---|---|
|---|---|---|---|
|Machine Translation Verbosity Control for Automatic Dubbing|icassp21| |	https://ieeexplore.ieee.org/document/9414411|
|Sentence Boundary Augmentation for Neural Machine Translation Robustness|icassp21| |	https://ieeexplore.ieee.org/document/9413492|
|Tackling data scarcity in speech translation using zero-shot multilingual machine translation techniques|icassp22|多语MT|https://arxiv.org/abs/2201.11172|
|Isometric MT: Neural Machine Translation for Automatic Dubbing|icassp22| |https://arxiv.org/abs/2112.08682|
|Prosody-Aware Neural Machine Translation for Dubbing|icassp22| |https://arxiv.org/abs/2112.08548|
|Domain-Aware Self-Attention for Multi-Domain Neural Machine Translation|interspeech21|Novel Neural Network Architectures for ASR|https://www.isca-speech.org/archive/interspeech_2021/zhang21n_interspeech.html|

### S2S
|---|---|---|---|
|---|---|---|---|
|Sig2Sig: Signal Translation Networks to Take the Remains of the Past	|icassp21| |https://ieeexplore.ieee.org/document/9415084|
|Uwspeech: Speech To Speech Translation For Unwritten Languages|aaai21|S2S|	https://arxiv.org/abs/2006.07926|
|Direct speech-to-speech translation with discrete units|acl22|S2S|https://arxiv.org/abs/2107.05604|
|Leveraging unsupervised and weakly-supervised data to improve direct speech-to-speech translation|interspeech22| S2S|https://arxiv.org/abs/2203.13339|
|From Start to Finish: Latency Reduction Strategies for Incremental Speech Synthesis in Simultaneous Speech-to-Speech Translation|interspeech22| S2S|https://arxiv.org/abs/2110.08214|
|Enhanced Direct Speech-to-Speech Translation Using Self-supervised Pre-training and Data Augmentation|interspeech22|S2S |https://arxiv.org/abs/2204.02967|



### iwslt
|---|---|---|---|
|---|---|---|---|
|Towards the evaluation of automatic simultaneous speech translation from a communicative perspective|acl21|实时|https://aclanthology.org/2021.iwslt-1.29/|
|Without Further Ado: Direct and Simultaneous Speech Translation by AppTek in 2021|acl21| 实时|https://aclanthology.org/2021.iwslt-1.5/|
|The USTC-NELSLIP Systems for Simultaneous Speech Translation Task at IWSLT 2021|acl21|实时|https://aclanthology.org/2021.iwslt-1.2/|
|The NiuTrans End-to-End Speech Translation System for IWSLT 2021 Offline Task|acl21|离线|https://aclanthology.org/2021.iwslt-1.9/|
|ESPnet-ST IWSLT 2021 Offline Speech Translation System|acl21|离线|https://aclanthology.org/2021.iwslt-1.10/|
|VUS at IWSLT 2021: A Finetuned Pipeline for Offline Speech Translation|acl21|离线|https://aclanthology.org/2021.iwslt-1.12/|
|KIT’s IWSLT 2021 Offline Speech Translation System|acl21|离线|https://aclanthology.org/2021.iwslt-1.13/|
|FST: the FAIR Speech Translation System for the IWSLT21 Multilingual Shared Task|acl21|多语|https://aclanthology.org/2021.iwslt-1.14/|
|Maastricht University’s Multilingual Speech Translation System for IWSLT 2021|acl21|多语|https://aclanthology.org/2021.iwslt-1.15/|
|Edinburgh’s End-to-End Multilingual Speech Translation System for IWSLT 2021|acl21|多语|https://aclanthology.org/2021.iwslt-1.19/|
|Multilingual Speech Translation with Unified Transformer: Huawei Noah’s Ark Lab at IWSLT 2021|acl21|多语|https://aclanthology.org/2021.iwslt-1.17/|
|Multilingual Speech Translation KIT @ IWSLT2021|acl21|多语|https://aclanthology.org/2021.iwslt-1.18/|
|ON-TRAC’ systems for the IWSLT 2021 low-resource speech translation and multilingual speech translation shared tasks|acl21|低资源/多语|https://aclanthology.org/2021.iwslt-1.20/|
|IMS’ Systems for the IWSLT 2021 Low-Resource Speech Translation Task|acl21|低资源|https://aclanthology.org/2021.iwslt-1.21/|
|The USYD-JD Speech Translation System for IWSLT2021|acl21|iwslt|https://aclanthology.org/2021.iwslt-1.22/|
|Inverted Projection for Robust Speech Translation|acl21| |https://aclanthology.org/2021.iwslt-1.28/|
|The Volctrans Neural Speech Translation System for IWSLT 2021|acl21|iwslt|https://aclanthology.org/2021.iwslt-1.6/|
|ZJU’s IWSLT 2021 Speech Translation System|acl21|iwslt|https://aclanthology.org/2021.iwslt-1.16/|
|End-to-End Speech Translation with Pre-trained Models and Adapters: UPC at IWSLT 2021|acl21|iwslt|https://aclanthology.org/2021.iwslt-1.11/|




