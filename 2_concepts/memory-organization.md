---
status: backlog
tags:
  - '#hwe/embedded-computer-systems'
---

# Memory Organization

## Homogeneous Multi-cores

![](Pasted%20image%2020240415151007.png)

- The average memory access time ($t_avg$​) is a fundamental metric used to understand the efficiency of memory hierarchies in processors

- It is calculated based on the hit time ($t_{hit}$​), the miss rate ($% \times t_{miss}$​), and the time it takes to retrieve data from the next level of cache or memory when there is a miss
  $$
  \displaylines{
  t_{avg} = t_{hit} + % \times t_{miss} \\
  L1: t_{miss} = t_{arg}(L2) \\
  L2: t_{miss} = t_{arg}(L3) \\
  L3: t_{miss} = t_{DRAM} \\
  }
  $$

- Where:

  - $t_{hit}$​ is the time to access data in the cache if it is present
  - $%$ represents the miss rate percentage
  - $t_{miss}$ is the time taken to handle a cache miss, including fetching data from a lower level of the memory hierarchy

- The rule of thumb that doubling the cache size typically reduces the miss rate by $\sqrt 2$

## Inclusivity Options

- Cache inclusivity refers to the relationship between data held in different levels of the cache hierarchy:

- **(1) Inclusive**: All data in a lower-level cache (e.g., L1) is also present in the higher-level cache (e.g., L3)

  - $L_i \subset L_{i+1}$
  - This simplifies cache coherency protocols because only the highest-level cache needs to be checked for coherency issues, and ensures a single point of update or invalidation.

- \*\* (2) Exclusive\*\*: Data stored in a lower-level cache (L1) is not stored in any higher-level cache (L3)

  - $L_i \cap L_{i+1} = 0$
  - This maximizes the total unique data stored across all caches but can complicate cache coherency and require more frequent access to slower memory.

- **(3) Non-inclusive**: There is no strict relationship between lower and higher-level caches

  - $L_i \cap L_{i+1} \ne 0$
  - Some data may be duplicated, and some may not
  - This offers a balance, potentially optimizing different aspects of cache utilization and coherency handling

### Implementation Examples

- **Intel**: Often uses a non-inclusive L2 and an inclusive L3 cache
  - focusing on keeping a broad set of recently used data available at the L3 level while allowing the L2 cache to store data that is actively being used by each core without redundancy
- **AMD**: Typically employs an inclusive L2 cache and a non-inclusive L3 cache
  - optimizing for fast access to recent data at the L2 level and a more diverse set of data in the L3 cache

## Lockup-Free Caches

A lockup-free cache design is crucial for maintaining high performance in modern processors, especially those that support out-of-order execution:

- **Miss Status Holding Registers (MSHRs)**: These registers track cache misses that have outstanding memory fetch requests.

  - When a cache miss occurs, the request details are stored in an MSHR
  - The system then continues to process other instructions rather than stalling until the data returns, thus allowing multiple outstanding cache miss requests

- **Max Outstanding Requests**: The number of MSHRs limits the number of cache misses that can be simultaneously handled

  - Increasing the number of MSHRs can reduce stalls in high-throughput environments but at a cost of higher complexity and silicon area

### Increasing Cache Bandwidth

To meet the demands of faster core processors and prevent bottlenecks, several strategies are employed to increase cache bandwidth:

1. **Pipelined Cache Access**: Splitting the cache access process into several stages (e.g., TLB check, tag read, tag compare, data read) allows for multiple accesses to be in process at the same time, improving throughput even though each access takes multiple cycles to complete.

1. **Clocking Cache Faster Than Core**: Useful in scenarios where core frequency is relatively low, allowing the cache to respond more quickly to requests.

1. **Fetching Multiple Bytes per Instruction**: For instance, x86 architectures fetch 16-32 bytes (instructions are 1-15 bytes) per access to handle variable instruction lengths efficiently.

1. **Multiported Cache**: Involves adding additional access paths to the cache cells, allowing simultaneous multiple accesses, which is particularly useful in FPGA implementations where latency can be tolerated due to generally lower clock rates compared to ASICs

   - dual connections to each bit cell
   - cells increase from 6T/cell to 8T/cell
   - latency also increases
   - latency is okay for an FPGA implementation since the clock rate is lower than in ASICs

![](Pasted%20image%2020240415183750.png)

5. **Duplicated Cache Storage**: Implements multiple copies of cache data to allow concurrent reads or exclusive writes, enhancing access speeds without increasing latency
   - multiple readers or single writers
   - increase size but not latency
   - only good for small caches

![](Pasted%20image%2020240415153759.png)

6. **Multibanked Cache**: Divides the cache into multiple independently accessible sections (banks), which can help reduce access conflicts and enhance parallel data access capabilities

## Multi-banked/ported Cache/Memory

In systems with multiple cores or processing elements, how memory is accessed can significantly impact performance:

- **Ports vs Banks**: The distinction here is between accessing the same memory area simultaneously (multi-ported) and having separate memory sections (multi-banked) to reduce access conflicts.

- **Performance Impact**:

  - Multi-ported designs provide lower latency at high concurrency levels but at a cost of increased complexity and potential for added latency due to port management
  - Multi-banked designs distribute access and reduce conflicts but depend heavily on the uniformity and independence of memory requests

### Multi-banked Cache/Memory

![](Pasted%20image%2020240415153853.png)

- Ports vs Banks

  - consider $C$ cores and $N$ banks or ports
  - assume round-robin access to memories and heavy traffic

- multi-ported (multiple accesses to same memory)

  - $N \ge C$, latency=1
  - $N\<C$ latency=$C/N$

![](Pasted%20image%2020240415154054.png)

- multi-banked
  - also assumes requests are uniformly and independently distributed
  - probability of a conflict for a pair of requests = $1/N$
  - average latency = $1+(C-1)/N$
    - $1$: the request of a single core
    - $C-1$: number of other cores
    - $/N$: divided by the probability of conflict
- we get better performance from multiporting however, it adds latency to every request

## DRAM

### DRAM

Dynamic RAM (DRAM) is the main type of memory used for main storage due to its density and cost-effectiveness, despite its slower access times compared to SRAM:

- **Bank Operations**: DRAM operations within a bank include activate (open a row), read/write (access columns in the open row), and precharge (prepare for the next access).

- **Interleaved vs Partitioned**: Interleaved memory spreads a single process's data across all banks to maximize parallel access, while partitioned memory allocates specific banks to specific processes, reducing contention but also potentially limiting parallelism.

- main memory - dynamic RAM - large and slow

- has been multibanked since 1st gen DDR

- operation: within a bank

  - activate opens a row
  - r/w: columns in the open row
  - precharge: closes the open row and pre-charges the bit lines to Vdd/2 to prepare for the next activate

- DDR3: precharge + activate takes 30-40 cycles, column read/writes take ~4 cycles

- performance/throughput is affected by the number of open/close operations

### DRAM operations

#### Interleaved

- each PE spreads all of its data across all banks
- PEs accessing different rows in the same bank will cause excessive open/close operations

#### Partitioned

- each PE gets its own banks
- each PE has fewer open rows
- limits parallelism available but reduces conflicts between PEs

## ScratchPad Memory ScratchPad Memory

ScratchPad memory provides an alternative to traditional caches by offering programmer-managed local storage:

- **Explicit Management**: Requires the programmer to explicitly control data movement, which can optimize timing and energy use but increases programming complexity.

- **Use Case**: Typically used in embedded systems where predictable timing is crucial and the overhead of cache management (like coherence and replacement policies) is undesirable.

- an alternative to cache memory

- explicitly managed local (on-chip) SRAM memory

  - mapped to a region of the address space
  - PEs DMA data to/from scratchpad memories
  - run a task using 1 scratchpad memory while DMAing data to prepare other scratchpad for next task

- pros:

  - predictable access times
  - energy efficiency, no tag memory

- cons:

  - harder to use - exposed to the programmer
  - moving linked data structures to and from scratchpad is more work
