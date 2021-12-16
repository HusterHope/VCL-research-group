---
title: Cross-Media Application
summary: We also aim to study the problem of better retaining the semantic information when transforming across different media formats, such as videos, images, texts, and audios. Concretely, we have conducted research in various cross-media analysis and generation tasks, including image/video captioning, audio/text based image generation, pose-guided human action video generation, etc.

date: "2018-01-28T00:00:00Z"

reading_time: false  # Show estimated reading time?
share: false  # Show social sharing links?
profile: false  # Show author profile?
comments: false  # Show comments?
show_date: false

# Optional header image (relative to `assets/media/` folder).
header:
  caption: ""
  image: ""
---

We also aim to study the problem of better retaining the semantic information when transforming across different media formats, such as videos, images, texts, and audios. Concretely, we have conducted research in various cross-media analysis and generation tasks, including image/video captioning, audio/text based image generation, pose-guided human action video generation, etc.

#### Pose-guided Human Action Video Generation

Human action video generation has attracted increasing attention due to its great potential in many application scenarios, such as creative movie making, interactive fashion design, and dataset augmentation for video analysis tasks. We propose a two-stage decoupled learning framework for generating human action videos with both visual and motion conditions, where the attribute encoder and pose-aware generator are separately trained over color-augmented video frames to achieve better feature disentanglement. Compare to existing end-to-end learning schemes, our framework can produce more diverse human action videos where the color of clothes can be flexibly manipulated through latent codes.

![Framework](human_gen.png "Framework")

![Generated human action videos](human_gen_video.png "Generated human action videos")

#### Self-critical n-step Training for Image Captioning

Image captioning aims at generating natural captions automatically for images. Recently it has been shown advantages of incorporating techniques from reinforcement learning into training, where one of the popular techniques is the advantage actor-critic algorithm that calculates per-token advantage by estimating state value with a parametrized estimator at the cost of introducing estimation bias. Here, we estimate per-token advantage without using a parametrized value estimator. With the properties of image captioning, we reformulate advantage function by simply replacing the state value with its preceding state-action value. Moreover, the reformulated advantage is extended to n-step, which can generally increase the absolute value of reformulated advantage. Then two kinds of rollout are adopted to estimate state-action value, which we call self-critical n-step training. Empirically we find that our method can obtain better performance compared to the state-of-the-art methods that use the sequence level advantage and parametrized estimator respectively.

![n-step training for image caption](image_caption.png "n-step training for image caption")
 