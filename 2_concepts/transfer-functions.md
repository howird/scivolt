---
date: October 15, 2022
status: backlog
tags:
  - '#signals/controls'
---

# Transfer Functions

- The transfer function is obtained by the $\\mathcal{L}$-transform and solving for the ratio between input and output

$$
Y(s)=G(s)U(s) \\implies G(s)=\\frac{Y(s)}{G(s)}
$$

## Poles and Zeros

- The frequencies that elicit __zero system response__ are the __zeros__ of the transfer function, and can be represented by the roots of the numerator polynomial

$$
{s|s\\in \\mathbb{Z},0 = \\text{numerator}(s)}
$$

- The frequencies where the system response is __undefined__ are the __poles__ and can be represented by the roots of the denominator polynomial

$$
{s|s\\in \\mathbb{Z},0 = \\text{denominator}(s)}
$$

## 1st and 2nd order systems

- ## eq1
- ## eq2

## System responses

- The system impulse response is

## Block Diagrams

- See resource:

## second order systems

## under dampened systems

- $0\<\\zeta\<1$

- obsreve the magnitude plot

  - roughly the system bandwidth is approx
  - wen the dampening ratio is small $0\<\\zeta\<\\frac 1 {\\sqrt{2}}$ the mag plot has a peak and it occurs at \\omega=\\omega_n\\sqrt{1-\\omegan}

- impulse response (tf: g(s)=)

  - the real part of the poles, zeta omega_n is in the e exponent meaning it determines how fast the response exponentially decays
  - while the frequency is omega_n sqrt{1-zeta^2}
    - this is the imaginary part of the poles
  - smaller dampening ratio, omeag_n tends towards majority of freq term, which is why we call omega the natural freq

- setp response:

  - eqs
    - similar to the impules response wen time t appears in these responses its multiplied be the natrual frequency
    - notice that its 1 - frac{}{1-zeta^2} exp(- zeta omega_n)
  - plot
    - as

### over dampened system

- $s=-\\zeta\\omega_n \\pm \\omega_n \\sqrt{1-z^2}$
-
