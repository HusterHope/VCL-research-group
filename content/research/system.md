---
title: System Development
summary: We also transfer algorithms into actual engineering projects, including 863 project, number of projects cooperated with many enterprises.

date: "2018-01-27T00:00:00Z"

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

We also transfer algorithms into actual engineering projects, including 863 project, number of projects cooperated with many enterprises.

#### Codec system optimization

Interpolation is a very important module in inter prediction for any video decoder, e.g. AVS2 and HEVC, which occupies most of the time in the whole decoding process. Thus, the real-time decoder is largely limited by the speed of inter prediction. To solve this problem, we propose an efficient GPU-based interpolation framework for inter prediction. Through optimizing shared memory allocation and thread scheduling on the GPU side, GPU are utilized efficiently and inter prediction is accelerated effectively. The experimental results on AVS2 show that for all Ultra HD 4K, WQXGA and full HD video sequences tested, the inter prediction acceleration ratio is over 6 times, and the average processing time is up to 1.25ms, 0.75ms and 0.45ms, respectively, with the NVIDIA GeForce GTX 1080TI GPU.
 
#### Point cloud compression system
We propose a novel point cloud compression method for attributes, based on geometric clustering and Normal Weighted Graph Fourier Transform (NWGFT). Firstly, we divide the entire point cloud into different sub-clouds via K-means based on the geometry to acquire sub-clouds with more uniform structures, which enables efficient representation with less cost. Secondly, for the purpose of reducing the redundancy further, we apply NWGFT to each sub-cloud, in which graph edge weights are derived from the similarity in normal combining the local and global features of point clouds.

![point cloud compression system](pcc.png)

We propose an adaptive scanning scheme to improve color attribute compression performance of static point cloud. To better exploit the intrinsic correlations of point cloud color data, multiple scanning modes are dedicated to projecting the color attributes into a series of texture blocks before compression. The best mode is subsequently selected in the sense of rate distortion optimization, such that the compression flexibility and performance can be greatly improved. To achieve rate-distortion optimized scan, the Lagrange multiplier that balances the rate and distortion is off-line derived based on the statistics of color attribute coding.

![scanning scheme](scanning_scheme.png)

#### VAMR (Virtual, Argument, Mixed Reality) System

VAMR system focuses on the research about XR and related systems. The VR systems we developed have been invited to participate China International Industry Fair. 

![Wandering in Yanyuan System](wandering.jpg)
![Wandering in Yanyuan System](wandering2.png "Wandering in Yanyuan System")

![Cave System](cave.jpg)
![Cave System](cave2.jpg "Cave System")
