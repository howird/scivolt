---
date: null
tags:
- '#hwe/embedded-computer-systems'
---

# Kahn Process Networks

- a form of dataflow language/representation

- a kpn is a set of processes that communicate over unidirectional communication channels that are not shared

- channels: 1 reader, 1 writer, infinite FIFO of tokens

- tokens can be any data structure e.g. image

- processes execute concurrently

  - we will have to scheduele them

- each process can be descibed by imperative code (e.g. C)

- the processes need to be deterministic

  - no shared data
  - must use message passing type of distributed system setup

- the language is augmented with a blocking wait and a non-blocking send

- example:

- INS: img

```c
process f(in int u, in int v, out int w) {
  bool b = true;
  for(;;) {
	  int i = b ? wait(u) : wait(v);
	  printf("%d\n", i);
	  send(i, 1);
	  b = !b;
  }
}
```

```c
process g(in int u, in int v, out int w) {
  bool b = true;
  for(;;) {
	  int i = wait(u);
	  if(b) send(i, v);
	  else send(i, u);
	  b = !b;
  }
}
```

```c
process h(in int u, out int v, int init) {
  int i = init;
  send(i, v);
  for(;;) {
	  i = wait(u);
	  if(b) send(i, v);
	  else send(i, v);
  }
}
```

- KPN are deterministic (good thing)

  - the history of a channel is the sequence of tokens both written and read
  - KPN are deterministic in the sense that the histories of all the channels depend only on the history of the imput channels

- this imples that the behaviour of a KPN is independent of timing (e.g. execution order, communication time,)

  - no race conditions

- the process code/execution must be determiistic - its behaviour only depends on the sequence of input tokens (no shared data)

- quesiton of termination and boundedness are undecidable

  - termination: all procs are blocked on wiat
  - boundedness: finite length queues

- if kpn has a bounded implementation, then it can be transformed into a strictly bounded network without losing its determinism

- tom parks's algo

  - simulation based
  - schedules a KPN in bounded memory if possible
  - starts with all buffers with size = 1 and blocking sends
    - will discuss how to implement blocking sends with kpns later
  - use any working-conserivng scheduling technique (run something if at least 1 process can run)
  - if the system deadlocks due to blocking sends, increase the size of the smallest buffer and continue
    - keep on incrementing, keep track of the size
  - there is no stopping condition:
    - run it for a "long time", keep track of the buffer size, and if they continue to grow, a bounded implementation isnt possible

- how to simulate finite buffers with a KPN simulation

  - for every channel, $a$, add a virtual channel $a_v$, in the opposite direction
  - each virtual channel is initialized with $n$ tokens, where $n$ is the buffer size that we want to emulate
  - `send(a) -> wait(a_v); send(a);`
  - `wait(a) -> wait(a); send(a_v);`

- example of simulating a bounded buffer in a KPN simulation (which doesn't have blocking sends)

```c
process_f(out int a, out int b) {
  for(;;) {
    send(1, a);
    send(1, a);
    send(1, b);
  }
}
```

```c
process_g(out int a, out int b) {
  for(;;) {
    wait(b);
    wait(a);
    wait(b);
  }
}
```

- this will deadlock on a blocking send
- set `size(a) = 2`

```c
process_f(out int a, out int b) {
  for(;;) {
    wait(a_prime); send(1, a);
    wait(a_prime); send(1, a);
    wait(b_prime); send(1, b);
  }
}
```

```c
process_g(out int a, out int b) {
  send(1, a_prime); send(1, a_prime); send(1, b_prime);
  for(;;) {
    wait(b); send(1, b_prime);
    wait(a); send(1, a_prime);
    wait(a); send(1, a_prime);
  }
}
```

- wont deadlock with `size(a) = 2`