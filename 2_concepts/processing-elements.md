---
status: backlog
tags:
  - '#hwe/embedded-computer-systems'
---

# Processing Elements

```ad-summary
Course Roadmap:
- intro
- models of computations (system specification)
	- KPN, simply a leadup to:
	- SDF
	- State Charts
- perfomance estimation (system design and validation)
	- SystemC (gives us an estimate of timing)
- system architecture (still part of system design)
	- PE, memory, on-chip interconnect
```

## Processing Elements Taxonomy

- 1. Instruction Processors (IP)
  - executes a program according to the instruction set architecture (ISA)
- 2. Hardware Accelerators
  - execute one (or more) fixed functions
- 3. Hardware Co-processors
  - extends ISP

# Instruction Processors

## Instruction Processors Types

- 1. general purpose
  - designed for a variety of uses
  - measured against benchmarks
    - e.g. SPEC CPU2017 (sequential) spec.org
    - e.g. PARSEC (parallel) cs.princeton.edu
    - e.g. EEMBC (embedded)
- 2. application specific
  - DSP: digital signal processors
  - GPU: image processing/numerical computing

## Instruction Processor Performance

- improve performance by increasing:
  - clock rate
  - instruction parallelism

### (1) Increasing Clock Rate:

- Increasing the clock rate speeds up the rate at which instructions are processed, effectively boosting the performance of the processor
- There are two primary methods to achieve this:

#### (a) increasing voltage

- The clock frequency can increase roughly linearly with voltage.
- However, this also increases the dynamic [(switching) power consumption](../ece327/power.md), which can be expressed by the formula $P=CV^2f$ where:
  - $C$ is the capacitance, depending on the number of transistors and interconnecting wires.
  - $V$ is the voltage.
  - $f$ is the frequency.
- Increasing the voltage to raise the clock rate comes with the downside of significantly increased power consumption and heat generation, potentially leading to thermal issues

#### (b) increasing pipeline depth

- **Pipeline Depth**: A deeper pipeline allows each stage of the pipeline to be shorter, potentially enabling a faster clock rate without an increase in voltage

- However, as the pipeline becomes deeper, particularly beyond 8 stages, complexities increase:

  - **Branch Prediction**: Needed to guess the outcomes of branches to keep the pipeline filled.
  - **Out-of-Order Execution**: Helps in executing instructions out of the order they appear to avoid stalls and improve efficiency

- **Hardware and Power Overhead**: Both branch prediction and out-of-order execution mechanisms increase the hardware complexity and power usage

- For example, comparing ARM and Intel architectures, the increase in pipeline stages over generations (from ARM7 to Cortex and Pentium to Core) typically corresponds with increased capabilities but also greater complexity and power consumption.

- e.g.:

  - ARM
    - 7 (1993): 3
    - 11 (2002): 8
    - Cortex A9 (2007): 8
    - Cortex A15 (2010): 15
    - Cortex A77 (2019): 13
  - Intel
    - Pentium (1993) 5 stage pipeline
    - Pentium 3 (1999): 10
    - Pentium 4 (): 20-31: this hit the power wall which "hit the power wall", very hot
    - Core (2006): 14-19
    - Atom (embeddied line) (2008): 12-14

### (2) Increasing instruction parallelism

- Expanding instruction parallelism allows the processor to handle multiple instructions simultaneously, which can significantly enhance throughput

#### (a) super-scalar datapath

- **Multiple Instructions per Cycle**: In a super-scalar architecture, essentially, each stage will be performing more than one instruction
- the processor can fetch, decode, execute, and commit multiple instructions per cycle, exploiting instruction-level parallelism (ILP) transparently
- stages: fetch, decode, dispatch, execute, commit 2/4/6/8 instructions/cycle
- extracts instruction-level parallelism (ILP) from a thread of execution (transparent to the software)
- decode widths:
- e.g.:
  - ARM
    - 11 (2002): 1 (scalar)
    - Cortex A9 (2007): 2
    - Cortex A15 (2010): 3
    - Cortex A77 (2019): 4
  - Intel
    - Pentium: 2
    - Core (2006): 4
    - Apple M1 (2020): 8
    - IBM Power: 8

#### (b) #### Very Long Instruction Word (VLIW)

- **Compiler-Specified ILP**: VLIW architectures allow the compiler to bundle instructions that can be executed simultaneously
- this simplifies the processor’s control logic by offloading complexity to the compiler

![](Pasted%20image%2020240415134316.png)

#### (c) Parallel Programming

- **Simultaneous Multi-threading (SMT)**: Techniques like Intel's Hyperthreading enable a single core to manage multiple threads by sharing its functional units among them, improving resource utilization

  - Single core has a state for 2+ threads (includes registers, program counter, status register)
  - However, in the context of this course, embedded systems, due to dependency on other threads’ performance

- **Multiprocessing**: Involves using multiple processing elements to handle different parts of a program simultaneously

  - although this can be limited by bottlenecks in memory and interconnects
