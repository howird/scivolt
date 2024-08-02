---
lectures: 
---

- period of 10
- uncertainty of 1.25

- main goal
	- replace the software idct calls with a hardware idct module
- download `import_files.zip`
	- contains `2D_idct.c`
		- rewritten version of that the `idct` function from a1 that just uses arrays, not pointers
		- this enables it to be compatible with the HLS
		- this is our top level function
- vitis hls steps:
- (1) create project:
	- name, location
	- add source files (from `import_files.zip`)
	- pick the toplevel function
	- add testbench (not provided)
	- configuration: period = 10, uncertainty = 1.25, part 
- (2) implement a test bench
	- main() invoke top-level function with test inputs and check the output against expected results
	- return 0 for success or number of errors
	- see `icdt_2d_tb{1,2}.txt`
- (3) run c simulation
	- output will be in `solution 1 > csim > report > *.log`