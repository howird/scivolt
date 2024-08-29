---
tags:
- '#hwe/digital-hardware-eng'
---

- need for resource sharing

  - example a cu already does scheduling and deciding how to use that datapath
  - in hardware we do it completely statically, before compilation

- dataflo analysis

- Efficiency: Hardware design on small budgets often have to use limited chip resources

- Performance: Even when hardware costs are not a constraint, packing multiple operations into small chip area → saves on wire delay costs

- Portability: If the list of resource shared operators are known, computation becomes portable. CPU ALUs are the simplest example of resource sharing

- s13

  - if we have 6 inputs should we do
    - 4+2 mux
    - 3+3 mux
  - count how many 2 bit muxes are required to make up the logic
  - calculate a histogram of path lengths

- s14: called aliasing

# 6b

- s11: add pic of our changes
  - latency = 7
    - latency: Time required for the first output(s) to emerge from the circuit for a given input
  - throughput $= \\frac26 = \\frac13$
  - efficiency = $\\frac{6\\times4-3}{6\\times4}$