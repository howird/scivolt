# Pmf

cdf: $F_x (x) = P(X <= x)$
pmf: $P_x (x_i) = P(X = x_i)$
pdf: $P(a <= X <= b) = integral_a^b f_x (x) d x$


pdf is a densidty function
![[image.png]]
$$
P(X=0) = integral_(0^-)^(0^+) f_x (x) d x = integral_(0^-)^(0^+) p(x)  delta(x) d x
$$

a pmf of a continuous rv is always zero

one can represent a pdf of a discrete variable using the $delta$ function

$$
P(X = x_1) &= integral_(x_1^-) ^(x_1^+) f_x (x) d x \
&= integral_(x_1^-) ^(x_1^+) sum_(x_i in R_x) p_x (x_i) delta(x - x_i) d x \
&= sum_(x_i in R_x) integral_(x_1^-) ^(x_1^+) p_x (x_i) delta(x - x_i) d x \
&= sum_cancel(x_i in R_x) integral_(x_1^-) ^(x_1^+) p_x (cancel(x_i)) delta(x - x_i) d x \
$$

multivariate rvs
marginal distributions:
consider a bivariate rv = $Z = (X, Y)$
for a marginal distribution, we only consider a subset of the variables
in this case choose $X$
cdf: $F_x (x) = P (X<=x) = P(X<=x, Y<infinity) = F_(x y) (x, infinity)$
pmf: $p_x (x) = P(X=x) = P(X=x, (Y=y_1) union (Y=y_2) union ... union (Y=y_j))$ 

pdf:

$$
d/(d x) [ integral^x_(-infinity) integral^infinity_(-infinity) f_(x, y) ( u, v) d v d u] \
= integral^x_(-infinity) d/(d x) [integral^infinity_(-infinity) f_(x, y) ( u, v) d v] d u + integral^infinity_(-infinity) f_(x, y) (x, v) d v dot (d x)/(d y) - integral^infinity_(-infinity) f_(x, y) (-infinity,x
$$

Note: All marginal distributions are determined by the joint distribution, but the converse is not true, due to lack of information about dependencies.

conditional distributions
consider a bivariate rv = $Z = (X, Y)$
![](2_concepts/media/Pasted%20image%2020250917114624.png)

iid rv:
iid distributions ahve maximal 'randomness', since given information about one variable, the independence does not give you information on the others

