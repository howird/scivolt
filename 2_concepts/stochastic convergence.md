---
---
# Stochastic Convergence
#math/stats 

thm 1. Central Limit Theorem
$$
(sum X_i - n mu)/sqrt(n) ->^D N(, sigma^2)
$$
thm 2. Law of Iterated Logarithm (LIL)

- have iid random variables with mean and variance
- then, rather than scaling it the way you 
$$
lim sup_(n->infinity) (sum X_i - n mu)/sqrt(2n log log (n)) ->^D sigma \
lim inf_(n->infinity) (sum X_i - n mu)/sqrt(2n log log (n)) ->^D -sigma \
$$

LIL can be treated as a refinement of SLLN
- we kow that $1/n (sum X_i - mu) = o(n)$ by SLLN
- the LIL improves this order to $O(sqrt(n log log(n)))$n addition provides the proportionality constant 
LIL also provides an illus of the diff betw

since $Z_n->^p 0$ then with high prob, Z_n is contained in an arbitrary interval (-epsilon, epsilon) eventually for an epsilon
this seems ti cintradict LIL which says that Z_n reaches the interval ()

thm3 cramer-wold device
let ${X_n, n>=1}$ be a seqence of p-dimensional random vectirs. THen
$$
X_n ->^cal(D) X "as" n-> infinity "iff for any" a in RR, a^top X_n ->^cal(D) a^top X
$$

thm4 multivar clt
let ${X_n, n>=1}$ be a iid p-dimensional random vector with $E(X)=sigma$. THen
$$
->^cal(D) 
$$

