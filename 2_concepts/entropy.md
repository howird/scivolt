---
tags:
  - note
  - math/info-theory
---
# Entropy

- The general concept of "entropy" is very important in science (statistics, physics, computer vision, ML, AI, information threory, data analysis, etc)
- The general formula for the entropy is:
$$
H({\mathbf S}) = -\sum_k S^k \ln S^k
$$
- where:
    - ${\mathbf S}:= (S^1,...,S^K)\;\;\in \;\;\Delta^K$ is any distribution over $K$ values (e.g. classes, categories, decisions, etc)
    - $\Delta^K:= \{p\in{\cal R}^K\;|p^k\geq 0,\;\sum_{k=1}^K p^k=1\}\subset {\cal R}^K$ is a so-called _probability simplex_
- Probably the most basic property of entropy one should know is that it measures "randomness" of a distribution

- In this exercise you should visualize the entropy function
    - $H: \Delta^K \rightarrow {\cal R}^1$ for $K=2$
- In this simple case, the distribution ${\mathbf S} = (S^1,S^2)$ may correspond to some binary random variable $X$, s.t.:
    - $S^1=Pr(X=1)$
    - $S^2=Pr(X=0)$
    
- For example, $X$ could represent a binary decision about the category of an object observed in an image (person or not-a-person)
- Since $S^1+S^2=1$, probability simplex $\Delta^2$ has only one degree of freedom - one scalar is enough to represent an arbitrary binary distribution

- It is easy to visualize the entropy function over all possible binary distributions:
    - ${\mathbf S}=(S^1,S^2)\in\Delta^2 \impliedby \Delta^2 = \{(x,1-x)\,|\, 0\leq x\leq 1\}$ 
        - is a line interval inside ${\cal R}^2$
        
- Visualize the entropy function $H({\mathbf S})$ for $K=2$ as follows
    - Derive the expression for function $H(x):=H({\mathbf S})$ for ${\mathbf S}=(x,1-x)$ and use `matplotlib` to plot  $H(x)$ for $x\in[0,1]$ in the code cell below
    - State which binary distribution(s) ${\mathbf S}=(S^1,S^2)$  have the lowest and the largest entropy values
    - Informally relate your observations to "randomness" of these distributions. 