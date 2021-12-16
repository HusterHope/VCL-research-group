---
title: Versatile Video Coding (VVC)
summary: To further improve coding efficiency, the Joint Video Exploration Team (JVET) begins to develop the next generation video coding standard, Versatile Video Coding (VVC), in October 2017. VVC, which is a block-based hybrid video coding standard, is still in development and we have many proposals adopted by it.
date: "2018-06-28T00:00:00Z"

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

To further improve coding efficiency, the Joint Video Exploration Team (JVET) begins to develop the next generation video coding standard, Versatile Video Coding (VVC), in October 2017. VVC, which is a block-based hybrid video coding standard, is still in development and we have many proposals adopted by it.

#### Hardware-friendly Inter/Intra Coding Scheme in VVC

Compared to HEVC, there are many new inter/intra prediction technologies adopted in VVC, such as History-based MVP (HMVP), shared merge list, triangle prediction, Sub-block TMVP (SbTMVP), Cross-Component Linear Model prediction (CCLM) and so on. Those newly adopted tools may cause higher storage burden or longer pipeline latency and we propose optimization scheme to improve the hardware friendliness of them. 

#### Storage reduction and simplification

In shared merge list, there are two HMVP tables maintained for coding small blocks in VVC. We propose to use a single HMVP table, which can reduce the storage burden of HMVP in shared merge list by half.
In triangle prediction, a CU is split evenly into two triangle-shaped partitions, using either the diagonal split or the anti-diagonal split. After predicting each triangle partition using its own motion, blending is applied to the two prediction signals to derive samples around the diagonal or anti-diagonal edge. As the derivation of bi-prediction MV to be stored in the blending area is complicated. We propose to remove the reference picture mapping process and store uni-prediction MV in the area when MV1 and MV2 are from the same reference list.

![Triangle partition based inter prediction](triangle_pred.png "Triangle partition based inter prediction")

![An example of motion vector storage for triangle prediction](triangle_pred_mv.png "An example of motion vector storage for triangle prediction")

#### Latency reduction
SbTMVP derives multiple motion for sub-blocks of one coding unit (CU) based on the motion information of the collocated blocks from temporal reference picture. Although it has improved the coding efficiency of inter prediction, complexity issues still exist. We proposed:
a)  Restricts the number of scanning process for deriving the collocated block to one time and therefore both the average and worst-case complexity is reduced.
b)  Fix the sub-CU size of SbTMVP to 8x8

![Illustration of SbMVP](SbMVP.png "Illustration of SbMVP")

Because of the adoption of SbTMVP, there are some unnecessary Temporal Motion Vector Prediction (TMVP) in inter prediction. In order to reduce the timing of small blocks, we propose to remove TMVP from merge list and AMVP list at specified small block sizes.
CCLM is to reduce the cross-component redundancy, for which the chroma samples are predicted based on the reconstructed luma samples by using a linear model. The dependency of the parsing process of chroma prediction mode causes latency for hardware design. We propose a hardware-friendly scheme to remove the context selection dependency.

![Context selection for bins related to intra chroma mode coding(CCLM on)](context_selection.png "Context selection for bins related to intra chroma mode coding(CCLM on)")

#### High Level Syntax Design for Adaptive Loop Filter in VVC

Adaptive Loop Filter (ALF) is adopted to VVC to minimize the mean square error between original and reconstructed samples by using Wiener-based filter. ALF can improve coding efficiency significantly. However, the coefficients and parameters of ALF may cause huge overhead. Hence, high level syntax design is important to reduce the overhead caused by ALF. We propose to redesign the ALF clipping parameter coding method by using fixed length coding and remove the dependency between ALF coefficients to reduce overhead while simplify encoder and decoder complexity.

![Filter shape of adaptive loop filter](alf.png "Filter shape of adaptive loop filter")

#### Probabilistic Decision Based Block Partitioning

During the development of VVC, the quadtree plus binary tree (QTBT) block partitioning structure was proposed. Compared to the traditional quadtree structure of High Efficiency Video Coding (HEVC) standard, QTBT provides more flexible patterns for splitting the blocks, which could improve the coding performance dramatically but result in high computational complexity. We propose a confidence interval based early termination scheme for the QTBT block partitioning structure to identify the unnecessary partition modes in the sense of rate-distortion (RD) optimization. In particular, a RD model based on motion divergence field is established to predict the RD cost of each partition mode without the full encoding process. To further improve the partition accuracy and achieve a good trade-off between the coding performance and the computational complexity, we cast the mode decision problem into a probabilistic framework which could be regarded as a binary-classification problem to eliminate unnecessary partition iterations.

![Illustration of the motion divergence field](motion_field.png "Illustration of the motion divergence field. (a) Block-based MV. (b) Pixel-based MVF.")

![Illustration of the prediction error](pred_error.png "Illustration of the prediction error")