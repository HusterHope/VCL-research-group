---
title: Enhanced Image Decoding
summary: With the explosion of digital media services, there is an increasing demand to compress the images/videos to facilitate storage and transmission, which may degenerate their quality especially at low bit rate. The popular lossy compression standards (e.g., JPEG and HEVC) adopt the block-based compression architecture and quantize every block independently to reduce the amount of transform coefficients. Lossy image compression usually introduces undesired compression artifacts, such as blocking, ringing and blurry effects, especially in low bit rate coding scenarios. Although many algorithms have been proposed to reduce these compression artifacts, most of them are based on image local smoothness prior, which usually leads to over-smoothing around the areas with distinct structures, e.g., edges and textures, leading to poor user experience.

date: "2018-03-28T00:00:00Z"

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

With the explosion of digital media services, there is an increasing demand to compress the images/videos to facilitate storage and transmission, which may degenerate their quality especially at low bit rate. The popular lossy compression standards (e.g., JPEG and HEVC) adopt the block-based compression architecture and quantize every block independently to reduce the amount of transform coefficients. Lossy image compression usually introduces undesired compression artifacts, such as blocking, ringing and blurry effects, especially in low bit rate coding scenarios. Although many algorithms have been proposed to reduce these compression artifacts, most of them are based on image local smoothness prior, which usually leads to over-smoothing around the areas with distinct structures, e.g., edges and textures, leading to poor user experience.
 
#### Perceptual-oriented Enhanced Image Decoding
To reconstruct a high quality decoded image, we incorporate the latest generative adversarial networks (GANs) to predict visually pleasing texture. Besides, the edge prior of original images has also been exploit for preserving edge fidelity. We proposed edge-preserving generative adversarial network (EP-GAN) to achieve edge restoration and texture generation simultaneously, resulting in high-quality perceptual results.  
 

![Edge-preserving Generative adversarial network (EP-GAN)](ep-gan.png "Edge-preserving Generative adversarial network (EP-GAN)")
 
![Comparisons with state-of-the-art method ARCNN](ep-gan_cmp.jpg "Comparisons with state-of-the-art method ARCNN")
 
#### Balance Fidelity and Quality via Hybrid Framework

However, GANs always lead to poor objective results such as PSNR, which means low fidelity. Therefore, we further introduce a region-aware visual signal restoration scheme to achieve a good balance between visual quality and fidelity with hybrid neural networks, such that the base fidelity layer and texture quality enhancement layer are combined adaptively to restore the compressed images.

![The framework of region-aware enhanced image decoding](regin-aware-gan.png "The framework of region-aware enhanced image decoding")
