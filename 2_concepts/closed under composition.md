---
status: todo
---

In mathematics, a set of functions is **closed under composition** if the composition of any two functions in the set results in a function that is also a member of that same set.

- Let $S$ be a set of functions
- The set $S$ is closed under composition if for any two functions $f\in S$ and $g\in S$, the composite function $g\circ f$ is also in $S$
- The composite function is defined as $(g\circ f)(x)=g(f(x))$

### Formal Definition

Let S be a set of functions where for each f\in S, we have f:A→A for some set A. The set S is **closed under composition** if the following condition holds:

$$
\forall f,g \in S,g\circ f\in S
$$

- This property is fundamental in abstract algebra, particularly in the study of semigroups, monoids, and groups, where the elements of the set are functions and the binary operation is function composition.

---

### Examples

#### Sets Closed Under Composition:

- **Linear Functions:** The set of all linear functions of the form $f(x)=ax$, where a is a real number. If f(x)=ax and g(x)=bx, then (g\circ f)(x)=g(f(x))=g(ax)=b(ax)=(ab)x. Since ab is a real number, the resulting function is also in the set.
- **Polynomials:** The set of all polynomials is closed under composition. The composition of two polynomials is another polynomial.
- **Invertible Functions:** The set of all invertible functions from a set to itself (a permutation group) is closed under composition. The composition of two invertible functions is also invertible.

#### Sets Not Closed Under Composition:

- **Non-decreasing Functions:** Consider the set of all non-decreasing functions. Let f(x)=x2 and g(x)=−x. Both are not strictly non-decreasing, but let's consider a better example. Let the set be functions from R to R. Let f(x)=x+1 (non-decreasing) and g(x)=−x (not non-decreasing). This isn't a good example. A better counterexample: Consider the set containing only the functions f(x)=x+1 and g(x)=x2.
    - (g\circ f)(x)=g(f(x))=g(x+1)=(x+1)2=x2+2x+1. This new function is not in the original set {f,g}.
- **Odd and Even Functions:** The set of odd functions is closed under composition. However, the set of even functions is also closed under composition. But a set containing both odd and even functions may not be. For example, let f(x)=x2 (even) and g(x)=x+1 (neither odd nor even). Their composition isn't guaranteed to be in a simple set of only odd or only even functions.