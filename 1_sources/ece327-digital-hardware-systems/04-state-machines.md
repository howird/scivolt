# State Machines in Hardware

## Need for state machines

- CS theory tells us about Turing Machines! abstract models of computing
	- Infinite tape (memory): storage device controlled by :
	- FSM (finite-state machine) 
		- this can move accross the tape
- Major implications:
- (1) State (infinite tape) is a pre-requisite to compute any function that is computable!
	- Yes, state is necessary for computation 
	- Not just that, it must be infinite!
- (2) FSMs here have finite state and manage/control the computation

- software examples:
	- trivial case:
		- for loops
			- loop counter is state
			- in each state execute body of loop
			- update loop and repreat
			- jumping / branching is the state transition

- Combinational logic is stateless (memoryless), composed of logic gates, arithmetic operations, and wires
- Registers add state. But, we have only covered feed-forward design → data flows in one direction only!
- Fundamental new idea in state machine design is that of feed-back
	- data can flow backwards in a particular manner


![](Pasted%20image%2020240204200015.png)
- presence of feedback is fundamental to the iddea of state machines
- state machines are a powerful abstraction for reasoning about compution in presence of feed back

## Kinds of state machines in hardware



## Drawing Waveforms + RTL Coding Styles