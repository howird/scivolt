---
status: backlog
tags:
  - '#hwe/embedded-computer-systems'
---

# Transaction Level Parallelism

- Transaction Level Parallelism, also known as data flow parallelism, is a concept in high-level synthesis (HLS) where a top-level function is decomposed into several submodules that can execute in parallel

```c
void toplevel(args) {
	module1; // L1  <- function call on loop
	module2; // L2
	module3; // L3
}
```

![](Pasted%20image%2020240223160355.png)

- Pipelined Transactions doesn't reduce the total latency from the start of the first module to the end of the last, but it improves throughput

  - top level latency will always = $L_1 + L_2 + L_3$

- throughput improvement comes from the pipeline's ability to process new inputs at the interval of the longest module latency

  - interval = $\text{max}(L_1, L_2, L_3)$

- effectively allowing for continuous data flow and processing, enhancing the system's overall efficiency

```ad-question
- This is essentially just pipelining to improve throughput
- The difference between data-level parallelism pipelining and transaction level is that:
	- data-level parallelism is pipelining at the loop level for smaller operations
	- transaction-level parallelism is pipelining at the top-level module level
```
