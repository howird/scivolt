---
tags:
- '#hwe/digital-hardware-eng'
---

[02 simulation](simulation.md)
[03 synthesis](synthesis.md)
[03b synthesis-examples](synthesis-examples.md)
[04 state-machines](state-machines.md)
[05 pipelining](pipelining.md)
[06 scheduling](scheduling.md)
[07 memory](memory.md)

- State of hardware engineering/chip design
  - Moores law is fundamentally changing due to physical limits of matter
  - Commoditization of computing resources (Cloud computing services)
  - cheap hardware abundantly available (Arduino, Raspberry Pi)
  - Do we need to learn how to design chips?
- What is moores law
  - doubling in transistor capacity every technology generation
- end of moores law
  - transistors cannot shrink beyond a few atoms thicl
  - Oppurtunity:New chips that use 3D stacking + cooling tech
  - clock frequency has plateaued well before transistors/per chip
- need for hardware enginerring/chip design
  - cost to fab chips is low (at old technologies)
    - google has an open source toolkit where you can develop your own kit
  - reconfigurable computing now mainstream (onw your own cheap fab)
    - amazon is using fpgas instead because their asics quickly deprecated and had to be thrown out too often
  - hardware-aware programming practices creeping into software design (parallel programming)
    - verilog has built in parllelism
  - if new materials replace silicon, we still need to preserve abstractions?
- the power of abstractions
  - most computing devices built with silicon today
  - we do not describe computation in terms of a network of slilcon atom interatcitn
  - engineers good at building layers of abstractions
  - for chip design we can operate at various levels:
    - silicon atoms - transistors - switches- gates - RTL - system
      - we work in RTL
        - we can design modular systems by assuming a global signal setting a clock edge
- Hardware description languages
  - goal: describe functionality of logic + connectivity between components:
    - functional programming -> describe what you wnat to comput not how you want to compute it
  - VHDL, Verilog, SystenC: descive hardware + extra features for verification, accurate modeling, synthesizabity, layout data capture
    - language must permit modeling of hardware and ease of constructing testing frameworks
    - language must of course support generation of fixed-size hardware sturctures
- c vs verilog
  - c diff
    - function call supplies inputs abcx
    - pointer to y is provided for return
  - differences:
    - explicit bit
    - bulk synchronous barrier: on the pos clock edge the RHS
  - Verilog
    - understand wire reg logic
      - types in verilog model wires in circuits
        - mu
      - must opproximate electrical behavior
      - X- unintitialized -> not driven by any logic or unknown -> driven by multiple logic elements (short circuit)
        - ideally we do not want to see an X in a simulation
      - Z- tristate -> not driven by any logic at that point in time
        - perfectly legal safe byt rarely used. Typically useful shared busses
      - verilong uses wire for connecting components, and reg for signals drivin
    - diff
      - module declares the ports into a hardware block external world interacts only through these ports
      - analogous to function call signature in C
      - arguments (signals) to the entity have a strict direction
      - unlike pointers, there is no confusion of signal flow
      - llimitations: no strict type checking on number of bits
    - always shit: TODO
      - this block implies a timing budget
        - everything you put in this block must be computed within that clock cycle
        - by splitting the long expression into multiple lines we are excecuting them in prallel
    - concurency
      - imagine RHS and LHS eveluations are done in seprate phases
- goals of verilog
  - sim: model hardware behavior, write testbenches, may not reflect real hardware that is generated
  - su
- synthesis: generates physical hardware from software description
  - structural vs behavioral composition
  - only a subset of the language is synthesizable
  - write rtl with attention to optimization
- test benches in verilog
  - important to test hardware components prior to manufacture
  - software can often be updated in the field through pateches, bugfixes, new release
  - chips are fixed once they are manufactured
  - we often add BIST (build-in self-test) circuits for runtime debugging
- test bench setup
  - dut: device under test
  - tb: test bench
    - generates DUT inputs
    - validates DUT outputs