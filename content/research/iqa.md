---
title: Image Quality Assessment
summary: Contrast distortion has a significant influence on the perceptual quality of an image, which may be generated in various image processing procedures. We propose a no-reference image quality assessment (IQA) algorithm for contrast-distorted images based on hybrid features from information and appearance attributes.

date: "2018-02-28T00:00:00Z"

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

Contrast distortion has a significant influence on the perceptual quality of an image, which may be generated in various image processing procedures. We propose a no-reference image quality assessment (IQA) algorithm for contrast-distorted images based on hybrid features from information and appearance attributes. From information attribute aspect, we utilize the basic information feature to quantify the information of the visible part and the extended information feature further containing the invisible part of an image. From the appearance aspect, we propose an efficient perceptual contrast and colorfulness index to capture the direct visual changes. With the hybrid information attribute and appearance attribute features, support vector regression (SVR) is utilized to learn an IQA model to predict the quality of contrast distorted images. Extensive experimental results on CCID2014 and TID2013 databases further demonstrate the superior performance and robustness of the proposed method.

![iqa](iqa.png)