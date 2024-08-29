---
date: January 16, 2024
tags:
- '#area/hwe/digital-hardware-eng'
---

# Simulation in Digital Hardware

- in parallelized software programs (i.e. C), threads do not truly run concurrently (in a single core machine) and thus can lead to different results depending on the operating system's scheduling
- if two threads are access and modify the same data, this can lead to data races depending on which runs first ex:

```c
void thread1(int* a, int* b) {
	*a = *b + 1;
}

void thread2(int* a, int* c) {
	*c = *a + 1;
}

void main() {
	int a = 0;
	int b = 1;
	int c;

	// CREATE AND JOIN THREADS

	if (c == 1) printf("thread 2 ran first.");
	if (c == 2) printf("thread 1 ran first.")
}
```

- On the other hand, hardware circuits are __truly parallel__
- Thus, Verilog simulation results should not depend on order of firing of blocks (at least in non-blocking assignments `<=`)
- This brings into question "how do we simulate __hardware parallelism__ with software that is inherently __sequential__?"
- We do so using __artificial time steps__
- in a single __artificial__ time step:
  - within each `always` block:
    - We run each statement sequentially, computing and stashing the right hand sides (RHS) operations, without assigning them to the left hand side (LHS) variable
  - after this is done for each `always` block, we increment the simulation time
  - on the next artificial time step we perform the assignments of the stashed RHS's to the LHS's

### Example 1

```verilog
module example32 (
		output reg [31:0] c
	);

	reg [31:0] a=32'bX; // redundant; all vars init as X 
	wire [31:0] b=32'h0001;

	always @(b) begin : thread_1
		a <= b + 1;
	end

	always @(a) begin : thread_2
		c <= a + 1;
	end

endmodule
```

- 0 ps:

  - +0 (artificial time step): everything is `X`
  - +1 (ats):
    - `b` is assigned to `1`
    - `a` is assigned to `X` but is redundant
  - +2:
    - `always @(b)` block triggered `a<=2` assignment occurs
  - +3
    - `always @(a)` block triggered `c<=3` assignment occurs

- verilog events

  - hardware runs in parallel
  - model instantaneous propagation of signal through a circuit -> event driven simulation model
    - (1) blocking assignments + RHS of non-blocking assignments + `$display` statements
    - (2) LHS of non-blocking assignments
    - (3) Re-evaluate (1) based on results of (2)
    - (4) Advance simulation time (NOT the same as artificial time) when there is nothing left to evaluate (values stabilize)

- To create illusion of parallel behavior, Verilog uses events

  - RHS of non-blocking assignments only visible