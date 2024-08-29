---
status: backlog
tags:
  - '#hwe/digital-hardware-eng'
---

### Simulation vs Synthesis

- Synthesizable Verilog is a subset of the language
  - ex: monitor statements don't actually exist in real hardware and thus are not part of the synthesizable subset of Verilog
- Remember Verilog can produce hardware circuits with a __fixed, finite__ structure/size
  - fixed size memory
- be aware of synthesis ptifalls -> careless style will generate more hw than necessary

### Comparing Hardware Synthesis to Software

- In software, there is no real distinction between synthesizable/non-synthesizable subsets of the language

  - one comparison could be low-performance (debug) mode vs. deployment/release mode (fully optimized)

- Software compilers translates C code into machine code

  - this machine code will be of a specific instruction set (ie x86, ARM)
  - Code is synthesized differently on platforms depending on the ISA (instuction set architecture)

- Hardware compilation translates HDL code into physical hardware which also depends on a library

  - For FPGAs, Xilinx or Intel will use different libraries
  - For ASICs, fabs like TSMC or UMC will also have their own libraries

### Hardware Compilation is Spatial

- Hardware is assembled in __space__ by inferring computations and connecting them through signals

  - Unlike software, which is:
    - assembled in time (sequential list of instructions)
    - mapped to instructions (^)
    - each of these instructions are connected (pass information) through reading/writing to shared registers/memory

- In hardware, each concurrent statement or `always` block infers a piece of hardware

- And these pieces of hardware are stitched together by processing the RTL files

- Here we write a block to calculate: $ax^2 + bx + c$

![](Pasted%20image%2020240204151539.png)

### Sequential Logic in Hardware

- when `@(posedge clk)` is in the `always` block's sensitivity list, sequential logic is being generated
- the hardware produced by sequential logic contains registers
  ![](Pasted%20image%2020240204151802.png)
- in comparison to the last block, we have registers instead of wires between operations
- Here, we can see that each variable created to store the intermediate calculations of $ax^2 + bx + c$ , `y0`, `y1`,  and `y2` are synthesized into registers, because they are only update at the `posedge clk`

### Managing time in Software vs Hardware

#### Software

- in software the compiler + CPU splits and executes a task as a series of instructions
- each instruction takes one cycle (this isn't actually true just an oversimplification/abstraction for simplicity/clarity's sake)
- the programmer is (luckily) working many levels of abstraction above the hardware and does not care about the processors' clock frequency or how to pack computation into instructions

#### Hardware

- In the RTL (Register Transfer Level) abstraction the hardware designer has to explicitly manage time - both the frequency of clock and pack logic into register stages
- Recall, in the last block, variables were used to store intermediate calculations of the desired function -- generating a sequence of registers
- This decision to use intermediate registers causes the block to take 4 clock cycles, for a signal to propagate through the 4 stages of registers
- If we were to compute the desired function using 0 intermediate variables, this block would only take a single cycle to compute, however the maximum clock frequency would be decreased
- The having $n$ stages in a block, __does not__ mean that you must wait $n$ cycles to provide new inputs to a function
  - due to the parallel nature of digital circuits, you can pass in new inputs __every__ cycle, it simply will take $n$ cycles to get the corresponding output signal from the block
  - this parallelism is integral to the concept of __pipelines__ in computer hardware,
- Hardware designers must manually determine how many stages to use in order to achieve their desired functions, considering the trade-off between clock latency and computation cycles
- The methodology to do so will be discussed in the [pipelining lecture](./05-pipelining.md)

### Verilog Hardware Synthesis

#### Parameters

- Parameters allow the same Verilog code to be reused in your design with different settings (i.e. n-bit representations of numbers)
- Thus, we must parameterize our designs so the exact desired hardware will be constructed by specifying values
- Accordingly, parameters must be known at compile time
- They are analogous to `template`s in `C++`
- There are runtime parameters which are read from registers at runtime, but they still must generate the exact same hardware
  - ex. having external parameters determine the `a` input to our polynomial function

#### Bit Level Access

```verilog
a_c <= a[8*i-1:8*(i-1)];
y[24*i-1:24*(i-1)] <= y_c;
```

- signals can be handled at a bit level in verilog
- here `i` is a parameter (__compile time__)
- to do dynamic (runtime) bit indexing, a multiplexer must be used

#### Conditionals

- s25: would be the same as a combinatorial block (outside of an always) except with no register

  - registers can only exist within always blocks

- Bits and Precision

  - ability to perform bit level opertations is scrucial for hardware design
  - cometimes want configurable accuracy, support for binary operations
    - logic operations for crypto interface controls

- s32: `reg` value outside of `always` block xists before any signals propagate, including `clk`
