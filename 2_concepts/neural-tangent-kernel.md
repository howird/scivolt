---
aliases:
  - ntk
---
# Neural Tangent Kernel

1-hidden layer

$$
f(x^alpha; theta) = 1/sqrt(n) W_1 phi (W_0 x^alpha) \
W_(l_(i j)) sim^"iid" N(0, 1) \
theta(t) = {W_1(t), W_0(t)}
$$

Data
$$
(x^alpha, y^alpha)^m_(alpha=1) sim^"iid" P
$$

Loss
$$
cal(L)(theta) = 1/(2m) sum^m_(beta = 1) (f(x^beta; theta) - y^beta)^2
$$

Gradient Flow
$$
diff_t theta(t) &= - nabla_theta cal(L)(theta(t)) \
&= 1/m sum^m_(beta = 1) (f(x^beta; theta) - y^beta) \
$$

important: something about angle brackets, this is clearly a tangent, the residual is a tangent or something
the fact that there is a regime where the training is so simple is what is important

$$
diff_t f(x^alpha; theta(t)) &= lr(< Delta_theta f(x^alpha; theta(t)), diff_t theta(t) >) \
diff_t underbrace((f^alpha - y^alpha), "residual") &= -1/m sum_(beta=1)^m lr(< nabla_theta f^alpha, nabla_theta f^beta >) \
&= underbrace(K_t^((n)) (x^alpha, x^beta), "NTK")
$$
- $n$ width, $t$ time


$$
f coloneqq [f^alpha]^m_(alpha=1), y : = [y^beta]^m_(beta=1) \

$$

example side tangent on eigenvalues?

$$
&sum_(alpha, beta) u^alpha K^(alpha beta) u^beta \
=& sum_(alpha, beta) u^alpha lambda^alpha delta_(alpha beta) u^beta \
=& sum_(alpha) lambda^alpha (u^beta)^2 \
<=& sum_(alpha) lambda_max (u^beta)^2 \
>=& sum_(alpha) lambda_min (u^beta)^2 \
$$

$$
(-1)/m^2 (f-y)^top K(f-y) \
<= (-lambda_min (K))/(2m) norm(f-y)^2 \
<= (-2lambda_min )/(m) cal(L)(theta(t))
$$

gronwall's inequality
$$
diff_t cal(L)(theta(t)) <= (-lambda_min)/(2m) cal(L)(theta(t)) \
=> cal(L)(theta(t)) <= exp((-lambda_min)/(2m)) cal(L)(theta(0))
$$

equality case
$$
diff_t U(t) = -c U(t) \
=> U(t) = exp(-c t) U(0)
$$

corollary
as $n-> infinity$, if $lambda_min (k) >= lambda_min > 0$
$$
"then" cal(L) (theta(0)) <= exp((-lambda_min)/(2m)) cal(L)(theta(0))
$$

the minimum eigenvalue of the is positive and therefore we have exponential convergence
today this remains the most general case we understand about NNs
Remark, this implies NN training converges!
- this regime is infinite width $n$, finite sample $m$, $n_0$ data dimension, $d$ depth, $t$ training time


Exercise
$$
diff_t f^alpha = -1/m sum_beta K^((n))_t (x^alpha, x^beta) (f^beta - y^beta) \
K^((n))_t (x^alpha, x^beta) = 1/n lr(langle phi(W_0 x^alpha) ", " phi(W_0 x^beta) rangle) + 1/n lr(<"diag"(phi^prime (x^alpha W_1)^top)(W_0 x^alpha)", " dot.c >)
$$

first term is the GP kernel Phi(x^alpha, x^beta) 
second term 