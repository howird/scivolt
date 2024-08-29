---
tags:
- '#hwe/digital-hardware-eng'
---

## Memories

```ad-summary
Data storage structures
- kinds of memories
- how are they organized
- what do they do
- how to use them
```

## Introduction

- In cpu's we have registers, data ram, instruction ram and caches (L1, L2, etc.)

  - support the execution in the cpu

- in our own hardware designs, we will have flip flops, register, denser srams or off chip for dram (which are actually on-chip with HBM tech)

- Cost: When implementing storage in hardware, you have a choice of implementations. Must know when to use which kind of memory.

  - __Flip Flips (FFs)__ are fast parallel access but expensive. Single-cycle access to all FFs or registers is possible
    - We can group the FFs together and give them multiple read/write ports to create __Register Files__
  - SRAMs (Static RAMs): are compact but only access one element at a time. Single-cycle access is possible
  - DRAMs (Dynamic RAMs) are cheapest, but require several cycles per access
    - they require multiple accesses because they are built with capacitors so they are leaky and unpredictable
    - HBMs are DRAMs that are brought onto the same chip (SOC)

- Scheduling: Timing behaviour of different memories is different. Must think of memory properties when scheduling a datapath

```ad-info
### Recap: Memory in a CPU

- memory is used to store instructions + data
- in hardware, instructions are operations distributed in space + resource shared if required
- Variables on stack, dynamic allocation on heap → data memory
- Modern CPUs mix these two memory spaces, so we can write self-modifying code (downside: data can be made executable)

### Memory in Hardware Design

- We dont store instuctions in memory, since the our computations are spread out in space - i.e. we have multiple ALUs be performing operations on different data in parallel
- Focus on using `dmem` to store intermediate variables
- Implement imem for pre-compiled sequence of signals -> microcode for datapath (state machine)

```

## Abstract view of memory operations

- Memory is a collection of storage locations (registers)
- Registers can be individually accessed (one at a time) using a `mux` and `demux`
- Signals
  - write address (`wraddr`): select for the \`demux
    - write enable (`we`): input to the `demux` to enable single registers
  - read address (`rdaddr`): select for the `mux`:
    - no enable needed, since reads are not destructive

![](Pasted%20image%2020240308151834.png)

```ad-note

- we include `oreg` to add a one cycle latency
- reads and writes can happen at the same time
	- in this case, the read will take the value from 2 cycles ago if an `oreg` is used or the last cycle without `oreg`
	- if we dont want the 1-2 cycle read latency, we can `mux` `wrdata` and `oreg` to output `rddata`, picking `wrdata` when `we && (wraddr == rdaddr)` 

```

## RTL Code for Memory Inference

```systemverilog
module mem #(
	parameter [31:0] ADDRWIDTH=8,
	parameter [31:0] DATAWIDTH=32
) (
	input wire clk,
	input wire rst,
	input wire [DATAWIDTH - 1:0] wrdata,
	output reg [DATAWIDTH - 1:0] rddata,
	input wire [ADDRWIDTH - 1:0] wraddr,
	input wire [ADDRWIDTH - 1:0] rdaddr,
	input wire we
);
	reg [DATAWIDTH - 1:0] mem[2 ** ADDRWIDTH - 1:0] /* num locations*/;
	
	integer i;
	always @(posedge clk) begin
		if(rst) begin
			`ifndef SYNTHESIS
				for (i=0; i <= 2**ADDRWIDTH - 1; i = i+1) begin
					mem[i] <= i;
				end 
			`endif
			rddata <= 0;
		end else begin
			if(we) begin
				mem[wraddr] <= wrdata;
			end
			rddata <= mem[rdaddr];
		end
	end
endmodule
```

```ad-note

- We wrap the resetting the `mem` ram block with `ifndef SYNTHESIS` so that it only runs in simulation
- This is because resetting each element implies to the compiler that you want to be able to modify each register in a single cycle; thus this design will synthesize a bank of flip flops, NOT an SRAM
	- obviously this is not what we want, and it is undesirable since the design will use more hardware resources

```

## Memory Usage

- Memories are are generally used to store intermediate data, inputs, and outputs
- The best practice for accessing a memory is to use a state machine to supply read/write address and write enables
- From a high level:
  - We have our user circuit that read/writes data from/to our memory module
  - This circuit can will likely have a fully pipelined datapath and will be sharing this memory module resource with other circuits
  - We must design this circuit in a way that ensures the address pattern and write enables matches the expected data consumption rate of the data path
  - Thus, a state machine should be used:
    - supply addresses and synchronize/integrate with fully-pipelined circuit with the memory to consume/produce a set of inputs/outputs each cycle
    - A resource-shared datapath consumes inputs once every $t$ cycles (where $t$ is the datapath throughput)

## Examples

### Simple Pipelined Polynomial Function

![](Pasted%20image%2020240308184500.png)

```ad-note
- Here, we are computing $ax^2+bx+c$ in a pipelined manner
- As per usual in a pipelined design, when we begin our computation, we have `x_v`, a signal representing the validity of our input, `x`
- With memory, we sync and pipeline the `x_v` signal with the reading of `x` from memory and once all stages of the pipeline are completed, the validity signal, now called `y_v`, can be used as the `we` (write enable) to save our computation to memory
- **NOTE** this is the same memory on both sides, the diagram duplicates it for simplicity
```

### Polynomial Function with Variable Factors

![](Pasted%20image%2020240308191934.png)

```ad-note
- Unlike the previous example, we now have variable $a$, $b$, and $c$, when calculating our polynomial function
- To accomplish this without memory modules, we can simply increase the width of the memory (not the size)
	- previously the memory stored $N$, $b$-bit numbers and now it stores $N$, $4b$-bit numbers
```

### Memory Sharing

- In the last example, we "shared" memory by widening the bit size
- This solution was fully pipelined with full throughput - however, it is not very practical
- Being fully-pipelined and fully-spatial (using up a lot of memory and registers), means that it uses a lot of resources
  - This may be desirable if this circuit was always __constantly__ being used
  - But, the resources would likely stay idle; waiting for memory operations (which can take multiple cycle)
- In practice, we would more likely see a design with a lower bandwidth memory, sharing a single ALU, this may have lower throughput but a __resource-shared datapath__ will significantly reduce resource cost

### Resource Shared Polynomial

![](Pasted%20image%2020240308201303.png)

![](Pasted%20image%2020240308201333.png)

```ad-note
- Pack all input arrays x, a, b, and c into `ipmem`
	- Output `y` array stored in `opmem`
- Modify schedule table to load a input in first cycle
- Modify datapath to provide a third “load” input to mux
- Note: no multiplexers are required since input to operators -> all inputs in same memory
	- If multiple input memories used, muxes need to be put back
- Note: throughput is 5
```

### Benefits of Resource Shared Datapath + Shared Memories

- Carefully balance resources against memory access bottleneck
- Isolated from rest of chip through ipmem and opmem structures
- Input and datapath muxes vanish → folded into the memory address decoders (internal to RAM structures)
- Now, we must create scheduling tables for memory read/write ports just like we did for operators and registers

## Advanced Memories

### Multi-ported Memories

- Modern CPU register files allow multiple reads/writes, obviously the more you can do in parallel, the better
- Even simple instruction like $y = a + b$ require two reads + one write
- How do we provide multiple ports?
- How do we handle hazards (multiple writes to same location)?

#### Multiple Read Ports: Naive Solution - Adding Read MUX

![](Pasted%20image%2020240308203558.png)

- In this implementation we add another `mux` to the read port of the register file
  - However this doubles the load on each register
- This impractical for larger memories → multiple wires per Q port (data out) of the register, slower wires tend to be more expensive

#### Multiple Read Ports: Practical Solution - Duplicating Memory

![](Pasted%20image%2020240309150333.png)

- We can also provide 2 read ports by duplicating the physical RAM modules
- One write port to both memory modules and so all data is replicated perfectly on both
  - Since their data is identical, we can read from both of them at the same time
- This is obviously wasteful for the hardware

##### Polynomial Example

![](Pasted%20image%2020240308204000.png)

![](Pasted%20image%2020240308204035.png)

- compared to the previous solution, we saved 1 cycle, which probably was not worth trading the hardware cost of duplicating the ram
- we can also alias cycle 4 (copy it to cycle 0) in order to increase throughput

#### Multiple Write Ports: Naive Solution - Adding Write MUX

![](Pasted%20image%2020240309144718.png)

- Here, the write enable and data signals must be decoded independently
- This requires a `mux` and `or` block for each register's `we`, as well as a `mux` for each register's `D` (data input) port
- This implementation become extremely hardware resource-intensive and impractical to implement
- NOTE: this solution does not even consider `wraddr` conflicts

#### Multiple Read Ports: Practical Solution - Memory Banks

![](Pasted%20image%2020240309145829.png)

- This solution once again duplicates the memory module, each module is now called a "Bank", and uses `mux`es at the read and write ports to that each read and write can go to any of the banks
- This solution is not functionally the same as having a memory with multiple reads since it cannot do multiple reads from the same bank
- This means that you must implement logic in your circuit:
  - to keep track of which bank the data you wrote was stored in
  - to avoid any write conflicts (data being stored in the same register)

### Shift Registers

- A shift register is a fixed-sized memory that adds storage + latency to a signal
- Constant (minimum) latency for data passing through a Shift Register
- Popular in signal processing and network systems to perform arithmetic over a window of inputs
- Useful in datapaths to implement register/pipeline chains compactly

![](Pasted%20image%2020240309151108.png)

- Here is an implementation snippet

```verilog
module sreg #(
	parameter DEPTH=8,
	parameter DATAWIDTH=32
) (
	input wire clk,
	input wire rst,
	input wire [DATAWIDTH - 1:0] data_in,
	output wire [DATAWIDTH - 1:0] data_out,
	input wire shift_en
);
	// instantiate shift register
	// solution 1: multibit
	reg [DATAWIDTH - 1:0] mem[DEPTH - 1:0];
	// solution 2: 1 bit
	reg [DATAWIDTH - 1:0] mem[DEPTH - 1:0];

	always @(posedge clk) begin
		if(rst) begin
			// reset all memory
			for (i = 0; i<=DEPTH-1; i = i + 1) begin
				mem[i] <= 0 ;
			end
		end else begin
			if(shift_en) begin
				// solution 1
				mem[0] <= data_in;
				for(i = 0; i<DEPTH - 1; i=i+1) begin
					mem[i + 1] <= mem[i];
				end
				// solution 2: concatenation works for 1 bit signals
				mem[DEPTH-1:0] <= {mem[DEPTH - 2:0],data_in};
			end
		end
	end
	
	assign data_out = mem[DEPTH - 1];

```

#### FIFO Memories

-

### FIFO

# 8C

- modern cpu reg files allow multiple r/w
  - unlike our prev design which only had 1 of each r/w port
- even simple instructions like y=a+b requires two reads + one wirte
- for superscalar multiple issue processors you could need several ports
- how do we provide muliple ports?
- how do we handle hazards: ie handle multiple writes to same spot

multiple read ports to reg file

- logically what we want is two muxes
- same diagram as last time, but t there are stacked muxes
- unfortunately this is impractical for larger memories, mult wires per q port of the register, slower wires tend to be more expensive
  - what s the q port

practical multiple read port ram

- provideing two read ports is by duplicating the ram
- only one write prot available
- they should be exactly the same data-wise

multiple write ports to reg file

- write data must be muxed at each register location
  - we's must be dcoded independently to allow two writes to happen at same time -> demux +or