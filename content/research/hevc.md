---
title: High Efficiency Video Coding (HEVC)
summary: In April 2010, the ITU-T Video Coding Expert Group (VCEG) and ISO/IEC Moving Picture Experts Group (MPEG) formed the Joint Collaborative Team on Video Coding (JCT-VC) to develop the new coding standard, which is known as High Efficiency Video Coding (HEVC) or H.265, formally published in 2013. HEVC can achieve about 50% bit-rate saving compared to H.264/AVC. We have investigated many techniques based on HEVC.
date: "2018-07-28T00:00:00Z"

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

In April 2010, the ITU-T Video Coding Expert Group (VCEG) and ISO/IEC Moving Picture Experts Group (MPEG) formed the Joint Collaborative Team on Video Coding (JCT-VC) to develop the new coding standard, which is known as High Efficiency Video Coding (HEVC) or H.265, formally published in 2013. HEVC can achieve about 50% bit-rate saving compared to H.264/AVC. We have investigated many techniques based on HEVC.

#### Adaptive Progressive Motion Vector Resolution Selection
It is widely acknowledged that the resolution of motion vector has a significant impact on coding performance. Generally speaking, on one hand, higher MV resolution implies that more potential sub-pel positions will be searched during the motion estimation (ME), leading to lower prediction distortion. On the other hand, the rate used for coding the motion vector constraints the MV resolution as MVs with higher resolution desire more coding bits for lossless representation. We proposed an adaptive MV resolution selection scheme which select the optimal MV resolution in a scientifically sound way with rate-distortion optimization. Specifically, the prediction distortion and rate models in terms of the MV resolution are established by taking the local properties of the input sequence into account. Based on our method, more flexibilities could be provided to achieve the MV resolution adjustment on frame and block and improve coding efficiency significantly. 

![Illustration of the PMVR](pmvr.png "Illustration of the PMVR")

#### Three-Zone Segmentation Based Motion Compensation
Motion compensation (MC) has been widely employed for removing temporal redundancies in typical hybrid video coding framework. To improve the performance of MC, a frame is usually divided into non-overlapped sub-regions as the basis to capture motion characteristics. However, block based MC may not align with the actual object motion boundaries, potentially limiting the compression efficiency. In view of this, we propose a three-zone segmentation based motion compensation scheme to improve the description accuracy of motion field as well as the coding efficiency. In particular, image segmentation is applied on the reference block to locate the object edges, and then the reference block is divided into three zones, including one foreground zone, one background zone and one edge zone. The background zone will obtain refined MV based on the local motion field, the prediction of the foreground zone is improved by the multi-hypothesis prediction and the edge zone is processed as an overlapped zone and the weighted compensated strategy is adopted in edge zone.

![Illustration of three-zone segmentation based motion compensation scheme](tzsmc.png "Illustration of three-zone segmentation based motion compensation scheme")

#### Hybrid All Zero Soft Quantized Block Detection
There are a large number of discrete cosine transform coefficients which are finally quantized into zeros. In essence, blocks with all zero quantized coefficients do not transmit any information, but still occupy substantial unnecessary computational resources. As such, detecting all-zero block (AZB) before transform and quantization has been recognized to be an efficient approach to speed up the encoding process. We incorporate the properties of soft-decision quantization into the AZB detection, instead of considering the hard-decision quantization (HDQ) only. In particular, we categorize the AZB blocks into genuine AZBs (G-AZB) and pseudo AZBs (P-AZBs) to distinguish their origins. For G-AZBs directly generated from HDQ, the sum of absolute transformed difference-based approach is adopted for early termination. Regarding the classification of P-AZBs which are generated in the sense of rate-distortion optimization, the rate-distortion models established based on transform coefficients together with the adaptive searching of the maximum transform coefficient are jointly employed for the discrimination.

![The workflow of G-AZB and P-AZB detection](azb.png "The workflow of G-AZB and P-AZB detection")
 
#### Hybrid Laplace Distribution-Based Low Complexity Rate-Distortion Optimized Quantization
Rate distortion optimized quantization (RDOQ) is an efficient encoder optimization method that plays an important role in improving the rate-distortion (RD) performance of the high-efficiency video coding (HEVC) codecs. However, the superior performance of RDOQ is achieved at the expense of high computational complexity cost in two stages RD minimization. To reduce the computational cost of the RDOQ algorithm in HEVC, we propose a low-complexity RDOQ scheme by modeling the statistics of the transform coefficients with hybrid Laplace distribution. In this manner, specifically designed block level rate and distortion models are established based on the coefficient distribution. Therefore, the optimal quantization levels can be directly determined by optimizing the RD performance of the whole block, while the complicated RD cost calculations can be eventually avoided.

![The proposed exact cost RDOQ scheme for model parameters training](rdoq.png "The proposed exact cost RDOQ scheme for model parameters training")

#### Non-local Structure-based in-loop filter (NLSF)
The existing in-loop filters in video coding standard, i.e. Deblocking Filter, Sample Adaptive Offset and Adaptive Loop Filter, are only based on local correlation without fully exploiting nonlocal similarity structure in video. In view of this, we propose non-local structure-based in-loop filter (NLSF) by simultaneously enforcing the intrinsic local sparsity and the non-local self-similarity of each frame. NLSF not only deals with the boundary pixels, but also the inside area, which is able to effectively reduce block artifacts while enhancing the quality of the deblocked frames. 

![Illustrations for NLSF](nlsf.png "Illustrations for NLSF")

![Fast block matching algorithm for NLSF](nlsf_bm.png "Fast block matching algorithm for NLSF")
