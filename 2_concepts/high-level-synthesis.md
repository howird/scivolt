---
status: backlog
tags:
  - '#hwe/embedded-computer-systems'
---

# High Level Synthesis

## Introduction

- HLS converts C/C++/SystemC into [RTL (register transfer level) designs](../ece327-digital-hardware-systems/01-intro.md)
- It maps data structures, operations on those structures, and communication onto hardware blocks (Verilog, VHDL)
- A standard synthesis tool (i.e. Vivado for Xilinx) then converts the RTL design to an FPGA bitstream (configures the FPGA) or ASIC programming masks

```ad-info
__Status Quo__

- The jury is still out on whether HLS is better than RTL design in the long run 
- While most major industries have tools for HLS, they seem to be pretty niche
- The greatest positive of HLS is its potential for labour saving
	- ex. can do pipelining with one line of code (via a `pragma` or a compiler directive)
```

## Quick Recap: Field Programmable Gate Arrays (FPGAs)

- An aside: before we discuss Higher Level Synthesis, it is important to know where the synthesized RTL designs will be exported to

### An FPGA's Building Block: CLBs

- FPGAs are basically a big grid of __configurable logic blocks (CLBs)__

![diagram of configurable logi blocks](Pasted%20image%2020240205195844.png)

```ad-note
- **bold** represents components
- `code` represents signals
```

The CLB diagram consists of 2 main components:

- **Look-Up Table (LUT):**
  - the primary component implementing programmed logic
  - essentially a small block of memory that can be programmed to replicate the truth table of a particular logic function
  - I/O
    - `comb_in`, `comb_out`: inputs and outputs for the combinational logic of the **LUT**
      - `comb_out` can be saved into the flip-flop or read directly from output
    - `c_in`, `c_out`: carry-in and carry-out signals for the **LUT**
      - required when the **LUT** is programmed to perform arithmetic functions like addition
      - Enables **CLB**s to be connected in series to handle multi-bit wide arithmetic functions
- **Flip-Flop (FF):**
  - stores data
  - `ff_in` or `comb_out` can be written to it (on the posedge clock) depending on a **mux** (and probably a write enable signal)
    - `comb_out` is the output of the **LUT** stored to the flip-flop
    - `ff_in` is an arbitrary input to the **CLB**

```ad-info
- This is a high-level explanation, and actual CLB architectures can vary significantly between different FPGAs
- They may contain additional features like more LUTs, more flip-flops, multiplexers, arithmetic units, and so on
```

### An FPGA's Structure and Other Components

![grid of configurable logic blocks](Pasted%20image%2020240205195914.png)

- Each column in an FPGA's grid structure will likely contain these components:

  - **CLBs (Configurable Logic Blocks):** previously mentioned
  - **DSP Blocks:** specialized logic blocks designed to perform digital signal processing tasks such as multiplication, accumulation, filtering
    - less common than CLBs but more powerful as they are highly optimized for specific applications
  - **Block RAM (BRAM):** dedicated memory within the FPGA
    - larger memory used for efficient storage and retrieval of large data arrays
    - are dual-port memories that can be accessed simultaneously by different parts of the FPGA.
  - **Dual-Ported SRAM:** While not explicitly shown or labeled in the provided diagram, dual-ported SRAM is a type of BRAM that allows simultaneous read and write operations from two different ports. This enables high-speed data access and throughput within the FPGA.

- Other components in an FPGA include:

  - **Memory Interfaces:**  e.g., DDR (Double Data Rate
    - required for applications that need more memory than what is available internally in the FPGA
    - required to access memory from co-processors
  - **I/O Interfaces:**: e.g. PCIe (Peripheral Component Interconnect Express)
    - connect FPGAs to other components in a larger computer system with other like CPUs, GPUs, and other peripherals
  - **Processors:** can have co-procesors
    - soft processor: processor implemented using the reconfigurable logic of the FPGA itself
    - hard processor: dedicated processor core(s)
      - for the board we are using, theres is a dual-core ARM processor physically present on the FPGA
    - good tasks that are better suited for sequential processing (FPGA handles parallel processing tasks)

## Comparing HLS and RTL Design

![](Pasted%20image%2020240222151717.png)

- pros:

  - C/C++ spec more compact than the RTL
  - quicker exploration of design alternatives
    - e.g. pipelining - requires a rewrite in RTL but only takes 1 annotation in HLS
  - good at optimizing datapath
  - generates interfaces automatically

- cons:

  - not so good at optimizing conrol flow (e.g. complex functions)
  - limitations on what kinds of sftware that can be turned into hardware
    - limitations on C/C++
      - ie complex pointers stuff like trees
    - need to understand the tool to generate a n efficient design

- Summary: increases productivity

  - but doesn't turn software designers into hardware designers
  - its a hardware designers' tool but not a software designers' tool

- HLS transforms a function into a hw IP block and generates the interface to the software for you

  - each nested function call generates a hardware module/block (unless the function is inlined)
  - multiple nested calls may result in multiple instances (parallelism)
    - if you have multiple nested calls to the subroutine then it may reuse the same block for that subroutine or it may create duplicates
  - invoking the function is turned into triggering the hw block (know as a "transaction")

## Restrictions on C/C++ for HLS

- no recursion - no call stack
  - instead, translate recursive algorithms into iterative algorithms
- avoid (complex) pointers
  - some simple pointer arithmetic can be handled
    - traversing through a fixed size arrays is okay
  - manipulating dynamic (heap-allocated) data structures (lists, trees) not okay

#### 1. Use constant array sizes

- the HLS tool needs to determine memory size
- if the size must depend on the input, then we should declare and upper bound
  - e.g. `assert(size < CONST);`
    - actually we use compiler directives in Vitis HSL

#### 2. Use constant loop bounds

- needed to determine latency
- if the number of iterations depends on input, declare an upper bound
- `assert(k<CONST); for (i=0, i<k ...`
- can handle simple cases such as:
  - eg. for (i=0, i \<CONST;i++)
    - for(j=i, j\< CONST; j++)
      - foo(i,j);
    - the number of ierations of foo() = $\sum_{j=1}^{CONST}j = \frac{(const)(const + 1)}2$

#### 3. avoid branches that cannot be "flattened"

```ad-info
- `if` or `switch` statements are considered "branches"
- branches will end up synthesizing into multiplexers
```

- We "flatten" a branch during synthesis by computing all paths and using a mux to choose the output
- Branches can be difficult to flatten if alternate path have different latencies

```c
void ex1(int* a) {
	for(int i=0; i<N; i++) {
		if(a[i] < 0)
			a[i] *= 2;
		else
			a[i] *= a[i]
	}
}
void ex2(int a) {
	if(a < 0)
		for(int i=0; i<N1; i++) foo();
	else
		for(int i=0; i<N2; i++) bar();
}
```

- in the above code block:
  - `ex1` is okay to synthesize:  the operations that happen in each branch both take a similar amount of time
  - `ex2` is not: since the branches can vary greatly in time
    - it would compile but would lead to very bad performance; very long high clock cycles

## Interfacing with Synthesized Hardware

- In FPGA design, we often abstract sections into functional blocks and use IP (intellectual property) blocks from third parties

![block diagram of an IP block](Pasted%20image%2020240222153246.png)

```cpp
Type3 /* output */ toplevel(
	Type1 /*input only, pass by val*/ in,
	Type2 /*in/out pass by ref*/ &inout
) {
	Type3 out;
	// do work
	return out;
}
```

- the above code and diagram represent the same block, it can have:

  - unidirectional signals: inputs and outputs (`in` and `out`)
  - bidirectional signals: `&inout`, represented using a pass by reference in `cpp`

- The HLS tool will also provide various options to control the block including:

  - **Implicit Control**: block automatically starts processing when all the necessary inputs are ready, without any explicit start signal
  - **Signalling Control**: block is controlled by specific control signals that might be wired to other parts of the system
    - This can allow for more complex control schemes, such as handshaking or enable signals
  - **Bus Slaves**: block has memory-mapped control registers that the processor can access
    - more sophisticated method allowing the processor to control the IP block by reading from and writing to these registers as if they were part of the memory space
    - how do we know when it is complete? 2 options:
      - polling: software periodically checks status bit
      - interrupt: block sends an interrupt signal to the processor to notify that the operation is complete

## Data Interfacing with an IP Block

- The IP block needs to interface with different types of data, and the interface type chosen depends on the characteristics of the data

### 1. Fixed Sized Data

- Used for scalars (like `int`, `double`), structs, and classes

- **Interface Options:**

  - **a) Direct Connections to local memory:**
    - small, fixed size data can be stored in the FPGA's local memory (BRAM)
    - can be directly wired to the IP block, for fast, access
  - **b) Memory-mapped registers:**
    - If the data originates from the processor (CPU), it's accessed via memory-mapped registers
    - cpu can write/read from these registers to communicate data with the IP block

### 2. Arrays

- **a) Stored in local memory (BRAM):**
  - the HLS tool can generate load/store blocks to move data from global memory to BRAM as needed
  - 'global memory' is the off-chip DDR memory, also accessible to the CPU

![](Pasted%20image%2020240222174525.png)

- **b) Bus Master:**

  - instead of storing data locally, the IP block can be synthesized to be a bus master - directly initiating transactions on the bus to access global memory
  - The global memory (DRAM) has high throughput but also high latency

- **c) Streaming interface** using Direct Memory Access (DMA):

  - data is transferred to/from the IP block's streaming interface, which is designed to interface with the DMA engine on the processor side
  - For algorithms that typically need random access to data, you might need to either:
    - Transform the algorithm to work sequentially, or
    - Cache global data into local memory to maintain random access capabilities at the cost of local memory creation and access overhead
      ![](Pasted%20image%2020240222174612.png)

## HLS: Methods to Use Parallelism

- Software is fundamentally __sequential__, hardware is inherently **parallel**

  - we want to take advantage of this parallelism when moving from software to hardware

- We will discuss 3 types of parallelism:

  - [Instruction Level Parallel](2.2-instruction-level-parallelism.md) (datapath parallelism):
    - taking individual blocks and optimizing them
    - HLS tools are good at this
  - [Data Level Parallelism](2.3-data-level-parallelism.md) (loop parallelism)
    - doing the same thing across an array
      - kinda like [SIMD](20-gpu-programming.md) (same instruction multiple data)
    - HLS tools will need guidance on this
  - [Transaction Level Parallelism](2.4-transaction-level-parallelism.md) (dataflow parallelism)
    - HLS tools are good at taking loops and nested function calls and optimizing that
