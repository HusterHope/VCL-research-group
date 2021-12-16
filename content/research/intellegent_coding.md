---
title: Intelligence Video Coding

summary: In recent years, the image and video coding technologies have advanced by leaps and bounds. However, due to the popularization of image and video acquisition devices, the growth rate of image and video data is far beyond the improvement of the compression ratio. With the development of deep learning, we also try to use deep learning to boost video coding. Deep convolution neural network (CNN) which makes the neural network resurge in recent years and has achieved great success in both artificial intelligent and signal processing fields, also provides a novel and promising solution for image and video compression. More specifically, the cutting-edge video coding techniques by leveraging deep learning and HEVC framework are investigated and discussed, which promote the state-of-the-art video coding performance substantially.

date: "2018-05-28T00:00:00Z"

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

In recent years, the image and video coding technologies have advanced by leaps and bounds. However, due to the popularization of image and video acquisition devices, the growth rate of image and video data is far beyond the improvement of the compression ratio. With the development of deep learning, we also try to use deep learning to boost video coding. Deep convolution neural network (CNN) which makes the neural network resurge in recent years and has achieved great success in both artificial intelligent and signal processing fields, also provides a novel and promising solution for image and video compression. More specifically, the cutting-edge video coding techniques by leveraging deep learning and HEVC framework are investigated and discussed, which promote the state-of-the-art video coding performance substantially.

#### CNN-Based Bi-Directional Motion Compensation for HEVC

The state-of-the-art High Efficiency Video Coding (HEVC) standard adopts bi-prediction to improve the coding efficiency for B frame. However, the underlying assumption of this technique is that the motion field is characterized by the block-wise translational motion model, which may not be efficient in the challenging scenarios such as rotation and deformation. Inspired by the excellent signal level prediction capability of deep learning, we propose a bi-directional motion compensation algorithm with convolutional neural network, which is further incorporated into the video coding pipeline to improve the performance of video compression.

![CNN-Based Bi-Directional Motion Compensation](cnn_bi_pred.png "Top: The network architecture; bottom: the flowchart of CNN based bi-directional inter prediction in video coding")

#### Content-Aware Convolutional Neural Network for In-loop Filtering in High Efficiency Video Coding

Recently, convolutional neural network (CNN) has attracted tremendous attention and achieved great success in many image processing tasks. We focus on CNN technology joining with image restoration to facilitate coding performance, and propose the content-aware CNN based in-loop filtering for High Efficiency Video Coding (HEVC). More specifically, each Coding Tree Unit (CTU) is treated as an independent region for processing, such that the proposed content-aware multi-model filtering mechanism is realized by the restoration of different regions with different CNN models under the guidance of the discriminative network. To adapt the image content, the discriminative neural network is learned to analyze the content characteristics of each region for the adaptive selection of the deep learning model.
 
 
![Content-aware CNN in-loop filter for HEVC](cnn_filter.png "Content-aware CNN in-loop filter for HEVC")

![R-D curves](cnn_filter_rd.png "R-D curves")
 
#### Enhance CTU-Level Inter Prediction with Deep Frame-Rate Up-Conversion for HEVC

The state-of-the-art video coding standard employs the reconstructed frames as the references in the process of inter prediction. Motion vector conveys the relative position shift between the current block and the prediction block, and it is explicitly signaled into the bitstream. We propose a high efficient inter prediction scheme by introducing a new virtual reference framework. In particular, the high quality virtual reference frame is generated with the deep learning based frame rate up-conversion (FRUC) algorithm from two reconstructed bi-prediction frames

![FRUC](fruc.png)

![The Frame-rate-up-conversion based inter prediction using Deep Virtual Reference Frame (DVRF) generation](dvrf.png "The Frame-rate-up-conversion based inter prediction using Deep Virtual Reference Frame (DVRF) generation")
 
#### CNN-based fast QTBT partitioning decision

Recently, the convolution neural network (CNN) has been found to be an effective method in determining the behavior of codec. We design a single network to predict the depth range of QTBT partitioning for 64x64 Coding Unit (CU). Firstly, we apply motion compensation to the original block and convert it into residual block. Then, the residual block is subtracted by the mean intensity values. After pre-processing, 4x4 kernels at the first convolutional layer is used to extract the low level features. For the second and third layers, feature maps are further convoluted twice with 2x2 kernels. The final feature map is concatenated together and flatten into a vector. In the proposed method, the QTBT partitioning decision is modelled as a multi-classification problem and the false prediction risk is controlled based on temporal correlation to improve the robustness of the scheme.

![Architecture of the CNN for QTBT fast partitioning](cnn_partition.png "Architecture of the CNN for QTBT fast partitioning")
