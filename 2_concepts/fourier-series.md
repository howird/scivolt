---
status: backlog
tags:
  - '#signals/controls'
---

# Fourier Series Part 1

- We want to approximate the following function, $f(x)$, as a summation of periodic functions within a specific domain, here we choose $\[-\pi, \pi\]$
  ![](https://lh7-us.googleusercontent.com/HAlo-HlcIzOP3gw1Hqo2RK7XOuGlaLG5ZX9oyDeQwy9X1vXWmuWjOxKdCBgk3NqqoHynzVE1uSXmqiiW9YwoRPUJSMJ-GnNLLMXPigOFw_LjWEvZkzsLN8CSt2NjP2scT2ioL0eZ33Gs7fg65ZHCyw)

$$f(x) = \frac{A_0}{2} + \sum _{k=1}^{\infty} A_k \cos (kx)+B_k \sin (kx)$$

- Any function $f$ that is periodic from $-\pi$ to $\pi$ can be approximated by a sum of cosines and sines of increasing frequencies with coefficients determined by the inner product of $f$ with the $k^\text{th}$ cosine or sine wave

$$
\displaylines{
A_k = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(kx) dx \\
B_k = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin(kx)dx
}
$$

- Comparing this to vectors, how would we represent a vector, $\bf{f}$, in terms of a different set of orthogonal basis vectors?

![](https://lh7-us.googleusercontent.com/MqO01krR34PQ0VQwB03GXnq4Z1fSt1jp6-Zd-nzPSSOh9Ng5oogWRqjlQKmmOAkDPdDi8Hof_GVk9fJxfHlpP4ZwvtDpk6cRVcm3Cs6QblNMMZuBmgB9DNlRFP4NG3esmWP3Am3x0VcyY5ndUFg8Ig)

- We would get the value of $\bf{f}$ in the direction of $\bf{u}$, by taking the inner product of $\bf{f}$ and $\bf{u}$
- Then, we multiply the (scalar) value by the basis vector $\bf{u}$ and divide it the norm of $\bf{u}$ to make it a unit vector

$$
\begin{align}
\displaylines{
\bf{f} & = \<\bf{f}, \bf{x}>\frac{\bf{x}}{||\bf{x}||^2} + \<\bf{f}, \bf{y}>\frac{\bf{y}}{||\bf{y}||^2} \\
&=\<\bf{f}, \bf{u}>\frac{\bf{u}}{||\bf{u}||^2} + \<\bf{f}, \bf{v}>\frac{\bf{v}}{||\bf{v}||^2}
}
\end{align}
$$

- This is repeated with $\bf{v}$
- Similarly, if we wanted to represent a function $f$ by a sum of cosines and sines, which are akin to the new basis vectors, we multiply each ‘basis function’ by a coefficient, which is the inner product of $f$ and the new ‘basis,’ and then normalize it:
  $$
  f(x) = \frac{A_0}{2} + \sum _{k=1}^{\infty} A_k \cos (kx)+B_k \sin (kx)
  $$
  $$A_k = \frac{1}{\pi} \int_{-\pi}^{\pi}f(x)cos(kx)dx = \frac{1}{||\cos (kx)||^2} \<f(x), \cos (kx)>$$

$$B_k = \frac{1}{\pi} \int_{-\pi}^{\pi}f(x)sin(kx)dx = \frac{1}{||\sin (kx)||^2} \<f(x), \sin (kx)>$$

- Where this is the inner product of two functions:
  $$
  \<f(x), g(x)> = \int _a^b f(x)\bar g(x) dx
  $$

# Fourier Series Part 2

![](https://lh7-us.googleusercontent.com/J7qFSUj0m2P5oD4B_CThrIRQhco3FA6dx14kMvAPxWUDIUNUDIARd687yiYqokuq0LhzlgAQCEyO8I5cEHhb6MbPDmU--tjXG-hQkQQZCZjWXS2l57bDiwtvT3zUdkcSKTuM2cKz1d_3dG01gfZqWg)

Next, we generalize from a function periodic over $-\pi$ to $\pi$ to one periodic over $0$ to $L$:
$$
f(x) = \frac{A_0}{2} + \sum _{k=1}^{\infty} A_k \cos (\frac{2 \pi k}{L}x)+B_k \sin (\frac{2 \pi k}{L}x)
$$
$$A_k = \frac{2}{L} \int_{0}^{L}f(x)\cos (\frac{2 \pi k}{L}kx)dx$$
$$B_k = \frac{2}{L} \int_{0}^{L}f(x)\sin (\frac{2 \pi k}{L}kx)dx$$

- Here we use $\frac{2\pi}{L}$ constant in the sinusoids to give them a period of $L$
  $$
  \<f(x), g(x)> = \int _a^b f(x)\bar g(x) dx
  $$

# Fourier Series Part 3 Complex Number

Generalizing the Fourier Series to Complex Numbers
$$
f(x) = \sum _{k=-\infty}^{\infty} C_k e^{jkx}
$$

- Where $C_k$ and $e^{jkx}$ are complex numbers
  $$f(x) = \sum _{-\infty}^{\infty} (\alpha_k+ j \beta_k) (\cos(kx)+j \sin(kx))$$

Where: $C_k = -\bar{C}_{-k}$ if $f(x)$ is real

- To prove that each term of the infinite summation is orthogonal, we must show that the inner product of each unique term must be $0$
  $$
  \Psi_k = e^{jkx} = \cos(kx)+j \sin(kx)
  $$

$$
\<\Psi_n, \Psi_m> = \int_{-\pi}^{\pi} e^{jnx}e^{-jmx}dx = \int_{-\pi}^{\pi} e^{j(n-m)x}dx
$$%5Cpsi_k%20%3D%20e%5E%7Bikx%7D%20%3D%20%5Ccos(kx)%2Bi%20%5Csin(kx)

[$$\implies \frac{1}{i(j-k)} \[ e^{j(n-m)x}\]_{-\pi}^{\pi}$$](<https://www.codecogs.com/eqnedit.php?latex=%5Cpsi_k%20%3D%20e%5E%7Bikx%7D%20%3D%20%5Ccos(kx)%2Bi%20%5Csin(kx)#0>)

- Here, since the function is periodic from $-\pi$ to $\pi$, $e^{j(n-m)}$ will always be equal at $-\pi$ and $\pi$, thus when $n \ne m$ it must evaluate to 0, in the equal case use l'hopital's:
  $$
  \displaylines{
  \therefore \<\Psi_n, \Psi_m> = \begin{cases} 0 &\text{if } n \ne m \\
  2\pi &\text{if } n=m \end{cases}
  }
  $$

- Therefore, for all values of k in the summation of the fourier series, all values of $e^{jkx}$ will form an orthogonal basis with which all functions can be represented

- In vector-like notation:\
  $$
  = \frac{1}{2\pi} \sum _{k=1}^{\infty} \underbrace{\<f(x), \Psi_k>}_{C_k} \underbrace{\Psi_k}_{e^{jkx}}
  $$

# Fourier Transform: Generalizing to non-periodic functions

![](https://lh7-us.googleusercontent.com/c42CoT1PyFG6hAUuN_3xcpIn3NbZrJuT55WGMXxiiG_sRzKgFG6IEGF3gWxpawXX0tgpBL45E8MLNvXzmrjebICvQa_fxDgU19TftMuIJ1FD7zykpEujsioh_N_DCMkQYfYng0-uute17G7US8fXPw)

$$f(x)= \sum_{k=-\infty}^{\infty} C_k e^{jk\pi x/L}$$

$$C_k = \frac{1}{2\pi} \<f(x), \Psi_k> =\frac{1}{2L} \int_{-L}^L f(x) e^{-jk\pi x/L} dx$$

Let: $$ \omega_k = k\pi /L = k \Delta \omega, \Delta \omega = \frac{\pi}{L}$$

- In order to generalize the Fourier Series to non-periodic functions, we want:

$$L \rightarrow \infty \implies \Delta \omega \rightarrow 0$$

- Thus:

$$f(x) = \lim_{ \Delta \omega \rightarrow 0}  \frac{ \Delta \omega }{2\pi} \int_{-\pi /  \Delta \omega }^{\pi /  \Delta \omega } f(\xi ) e^{-jk \Delta \omega \xi} d\xi e^{jk \Delta \omega x}$$

$$= \int_{-\infty}^{\infty}  \frac{1 }{2\pi} \underbrace{\int_{-\infty}^{\infty} f(\xi ) e^{-j\omega \xi} d\xi}_{\hat f (\omega)} e^{-jk \omega x} d\omega$$

- We get the Fourier Transform Pair

$$\hat f (\omega) = \mathcal{F}(f(x)) = \int_{-\infty}^{\infty} f(x ) e^{-j\omega x} dx$$

$$f(x)= \mathcal{F}^{-1}(\hat f (\omega))=  \frac{1 }{2\pi} \int_{-\infty}^{\infty}  \hat f (\omega) e^{jk \omega x} d\omega$$

- This Fourier Transform has special properties:

- Derivatives:

$$\mathcal{F}(\frac{d}{dx}f(x))= j\omega \mathcal{F}(f(x))$$

- Convolution Integrals:

$$\mathcal{F}(f * g)=\mathcal{F}(f)\cdot \mathcal{F}(g) = \hat f \cdot \hat g$$

- Linearity:

$$\mathcal{F}(\alpha f(x) + \beta g(x))= \mathcal{F}(\alpha f(x))+\mathcal{F}(\beta g(x))$$

- Parseval’s Theorem

$$\int_{-\infty}^{\infty}|\hat f (\omega)|^2 d\omega = 2 \pi \int_{-\infty}^{\infty}| f (x)|^2 dx$$

- Think of these integrals as the ‘energy’ in any function $$f$$

- This theorem implies that the amount of ‘energy’ in a function $$f$$ is directly proportional to its fourier transform

- Say that after Fourier Transforming a function, we have some Fourier coefficients that are close to 0, we do not know how ‘zeroing’ those coefficients out is going to affect the function

- This theorem shows if there are fourier coefficients that are negligibly small, they also contribute to the original function to the same degree

- Therefore, zeroing out the small coefficients still captures most of the original function

5. Laplace Transform

- Where the Fourier Transform was:

$$\mathcal{F}{x(t)} = X(\omega) = \int_{-\infty}^{\infty} x(t) e^{-j \omega t} dt$$

- The Laplace Transform is:

$$\mathcal{L}{x(t)} = X(S) = \int_{-\infty}^{\infty} x(t) e^{-S t} dt, S = \sigma + j \omega$$

- Thus, when $\sigma = 0 \implies S = j \omega$, the Laplace Transform reduces to the fourier transform

- Even when $$\sigma \ne 0$$, the Laplace Transform of a signal is the Fourier Transform of that signal multiplied by $$e^{-\sigma t}$$

$$X(S) = \int_{-\infty}^{\infty} x(t) e^{-S t} dt, S = \sigma + j \omega$$

$$X(S) = \int_{-\infty}^{\infty} x(t) e^{-\sigma t} e^{-j \omega t} dt$$

$$\therefore X(S) = \mathcal{F}{x(t)e^{-\sigma t}}$$

- This multiplied signal $$e^{-\sigma t}$$ is important because it allows the Laplace Transform to be performed on signals that do not go to 0 as $$t\rightarrow \infty$$

- For a certain $$\sigma$$ which is $$Re {S}$$ the signal $$x(t)$$ will converge and not others. This is defined as the region of convergence

- Properties:

- Derivatives:

$$\mathcal{L}(\frac{d}{dt}x(t))= S \mathcal{L}(x(t))$$

- Linearity:

$$\mathcal{L}(\alpha f(t) + \beta g(t))= \mathcal{L}(\alpha f(t))+\mathcal{L}(\beta g(t))$$

- Convolution Integrals:

$$f * g=\mathcal{L}(f)\cdot \mathcal{L}(g) = f(S) \cdot g(S)$$

- Extending upon the Convolution Properties:

![](https://lh7-us.googleusercontent.com/mAx0Q1fyEEJdShCv2IEMiiICXOE5QrEa3jX3QBPcM5czQYMgt-2bN6wCeG-3q4o0m67eAMhWT2W--OF3MBpkJ6JjFO88Kp2Hwu9bCqUkHUdCJZBhRrWpusXzqq4fzQWg1eroemb41g0sAlFqf5r2pA)

- Given a system defined by its impulse response, $$h(t)$$, its output to an input $$x(t)$$ is: $$y(t) = h(t)\*x(t)$$

- In the frequency domain, taking the Laplace Transform of the impulse response $$h(t)$$, gives us the system function: $$H(S)$$

$$Y(S) = H(S)\cdot X(S)$$

- For stable, causal systems all poles are on the left half of the S-plane

\*\*
