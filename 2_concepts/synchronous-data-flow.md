---
date: null
tags:
- '#hwe/embedded-computer-systems'
---

# Synchronous Data Flow (SDF)

- Introduced in [Lee & Messerschmitt](https://ieeexplore.ieee.org/document/1458143) in 1987
- The KPN is very flexible but a schedule can't be produced deterministically
- SDF adds restrictions to KPNs to enable deterministci and ompile time scheduling
- each node (process) has fixed production/consumption of tokens ecery time it 'fires'
- assumption: node firing is atomic; it reads all input buffers at the same time
  - it doesnt fire until the required number of tokens is available on each input
- this model ignore node execution time
- the system is described solely by the number of tokens read and written when each node fires
- ex. DAT-TO-CD converter
  - dat = digital audio tape: samples at 44.1 kHz
  - CD = compact disc: samples at 48 kHz

INS DIAGRAM

- can determine the relative firing rates of each node which leads to a periodic schedule (dont remember if done)

- unlike kpn, sdf doesnt permit initialization phases in nodes since input and output rates are fixed

- instead the sdf can start with initial tokens in buffers

  - these may be needed to avoid deadlock

- trivial example prepopulatiing a buffer: two stang finite impulse response (FIR) filter (SDF graph)

- represent the initialization step with the diamod

- deamond will be initialized to zero (doesnt have to be)

- \[\*C_0\]

sdf scheduling algo

- (1) establish node firing rates (per iteration of the periodic schedule) using __balancing equations__

- (2)  determine periodic schedule by simulationg for 1 iteration (done when number of tokens in each channel/buffer reaturns to is initial count)

- the resulting schedule will have bounded beffer size (ie tokens will not accumulate)