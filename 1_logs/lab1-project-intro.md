---
lectures: w1d2, w2d1
tags:
- '#hwe/embedded-computer-systems'
---

# Lab 1 Introduction

- Main Goal of the lab: implement a Video Decoder on an SoC
- File format is: `mpeg423`
  - simpler version of `mpeg4` file format
  - lossy encoding
  - a sequence of frames (simplified `jpeg` images)

### Color Spaces

- bitmaps (`.bmp` files) and screen output are normally in the RGB (red green blue) space
  - where each pixel is represented using 8 bits per color $\in \[0, 255\]$
- Instead of the RGB color space, we use YCbCr (luminance, blue chrominance, red chrominance)
  - also using 8 bits per color $\in \[0, 255\]$

```ad-info
Human eyes are more sensitive to changes in brightness (luminance) than changes in colour (chrominance)
- YCbCr seperates brightness (Y) from color information (Cb, Cr) in unlike RGB which stores color information in all of its' components
- This separation allows more bits to be dedicated to the critical brightness information
- Therefore, when we perform a lossy compression (like `mp4`) the color components are compressed more aggressively without significant __percieved__ visual quality loss
```

- Equations for converting RGB Y'CbCr:
  - $Y' = 0 + 2.999R + 0.587G + 0.114B$
  - $Cb = 128 - 0.169R - 0.331G + 0.500B$
  - $Cr = 128 + 0.500R - 0.419G - 0.081R$

### Encoding Process

- (1) sub-divide channel into 8x8 blocks
- (2) processor blocks from left to right, top to bottom (lossless)
- (3) apply a 2D-discrete cosine transform (DCT) to each block (lossy)
- (4) quntize resutling 8x8 coefficients (loseless)
- (5) entropy encode the quantized coefficicents

#### 1. + 2. Divide and Process

#### 3. Apply DCT to Each Block

#### 4. Quantization (Compressiong)

the program processes them in this order

- mjpeg423 takes advantage of the similarity between successive frames

  - there are two frame types:
    - index (i-) frames:
      - majority will be i-frames
      - stored as a normal jpeg image
      - DC coefficient is differential between successive blocks (as you process them sequentially)
        - $\Delta DC_i = DC_i - DC_{i-1}$
    - progressive (p-)
      - differential encoding of DC and AC coefficients between frames
        - $\Delta DC_i^j=DC_i^i - DC_i^{j-1}$
        - $\Delta AC_i^i(x,y)=AC_i^i(x,y) - AC_i^{j-1}(x,y)$
          - $j$ is frame number
          - what is the difference between the $j$ frame number and $i$ frame number

- File Format = \[header | payload | trailer\]

  - Header: always 20 bytes
    - 5 equal 4 byte sections
      - (1) total number of frames (i- and p-) in the payload
      - (2) frame width
      - (3) frame height
      - (4) number of i-frames
        - lets us know how long the trailer is going to be
      - (5) number of payload bytes
  - Payload: sequence of frames (4B aligned)
    - each frame:
      - (1) number of frame bytes (4B)
      - (2) 0 for i-frame, 1 for p-frame
      - (3) number of Y' bytes
      - (4) number of Cb bytes
        - number of Cr bytes can be inferred from (1) (3) and (4)
      - (5) Y' bitstream
      - (6) Cb bitstream
      - (7) Cr bitstream
  - Trailer: size = 8 x number of i frames
    - (1): frame index 4B
    - (2) frame offset: frame offset from start of file 4B

- Decode Steps

  - (1) lossless entropy decode
  - (2) dequantize block (multiply by quantization table values)
  - (3) apply inverse DCT (IDCT)
    - for x=0..7, y=0..7:
      - $f(x,y) = 1/4 \sum_u \sum_v C(u)C(v)F(u, v)\times cos(\frac{(2x+1)u\pi}{16})cos(\frac{(2x+1)v\pi}{16})$

- Given a reference implementation

  - does encode and decode
  - decoder outputs a sequence (one per frame) of bmp files using 32 bits/pixel
  - Video DMA: transfers 24 bits/pixel: RBG (8 bit ea, 24 bit total)

- overall term goal: achieve 24 fps playback