---
status: backlog
tags:
  - '#hwe/embedded-computer-systems'
---

## Digital Signal Processors (DSP)

- Digital Signal Processors (DSPs) are specialized types of microprocessors designed specifically for performing high-speed arithmetic operations on digital signals

### Characteristics and Features

- DSPs are optimized to handle operations on streaming data efficiently. Key features of DSPs include:

- **Multiply-Accumulate (MAC) Instructions**: This is a fundamental operation in many signal processing algorithms.

  - `MACa Ri, Rj;` $\implies R_a := R_a + R_i \times R_j$
  - The `MACa Ri, Rj;` instruction multiplies two registers, `Ri`​ and `Rj`, ​ and accumulates the result into a third register, `Ra`
  - This single instruction, doing both multiplication and addition, enhances performance for tasks such as filtering and convolution operations

- **Circular Address Registers**: These are used for implementing circular buffers efficiently, which are commonly used in digital signal processing for handling data in a cyclic fashion

  - This feature automates the process of wrapping around the buffer index, eliminating the need for additional logic to handle buffer boundaries.

- **Single Loop Instruction**: DSPs often include instructions that facilitate loop control, such as `RPT i;` which repeats the next instruction `i` times

  - This reduces the overhead of loop management in software, speeding up the execution of repeated operations typical in DSP applications

### Example DSP Code Comparison

The C code example provided demonstrates a common DSP operation — a convolution of inputs with coefficients. The equivalent assembly code snippet for a DSP showcases how these operations are efficiently managed:

- **C Code**: The loop performs the convolution by accessing the `input` buffer and `coefficients` array, applying the modulo operation to simulate a circular buffer.

```c
float *inputs = SOME_BUFFER; 
float coeff[LARGE_VALUE] = CONSTANTS;
float res = 0;

int ii = START_VALUE; // initial index to circular input buffer
for(int c=0; c<LARGE_VALUE; c++) {
	res += input[(ii+c)%LARGE_VALUE] * coeff[c];
}
```

- **DSP Assembly Code**:
- Registers are set up for the input index, coefficient index, and result accumulation.
- The `RPT` instruction repeats the multiply-accumulate operation across the buffer length, significantly speeding up the operation by reducing the instruction overhead compared to typical processor architectures.

```
MOV Rca0, START_VALUE;
MOV Rcs0, LARGE_VALUE;
MOV Rca1, 0;
MOV Rcs1, LARGE_VALUE;
MOV Ra, 0;

RPT LARGE_VALUE;
	MACa inputs[Rca0++], coeff[Rca1++];
STR res, Ra;
```

# General Purpose GPU Programming

## Introduction

- GPUs can do thousands of floating point operations (FLOPs) in parallel

- 2 main gpgpu frameworks:

  - 1. CUDA: proprietary (NVIDIA gpus)
  - 2. OpenCL: open (AMD, IBM, Intel, NVIDIA, Qualcomm, ...)

- Generic Hardware Model:

  - multprocessor

- exectution model

  - blocks get assigned to muliptocessors
  - threads are executed in warps of (32, 62)executing the instructions in lockstep
  - they can use predication for conditional execution

```
var = 0;
if condition
    var = 1;
else
```
