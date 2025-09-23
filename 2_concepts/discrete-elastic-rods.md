# Discrete Elastic Rods: Problem Formulation and Equations

## 1. Problem Overview

### 1.1 Objective

Develop a discrete differential geometry approach to simulate elastic rods that:

- Preserves geometric structure of smooth Kirchhoff rod theory
- Efficiently handles stiff twisting and stretching modes through quasistatic treatment
- Enables coupling with rigid bodies and constraint enforcement
- Maintains numerical stability and convergence to analytical solutions

### 1.2 Physical System

- **Rod representation**: Curve-like elastic bodies with one large dimension (length) and small cross-section
- **Deformation modes**: Stretching, bending, and twisting
- **Key assumption**: Speed of twist waves >> speed of bending waves

## 2. Geometric Representation

### 2.1 Discrete Framed Curves

A discrete framed curve $\Gamma$ consists of:

- **Centerline**: $(n+2)$ vertices $x_0, ..., x_{n+1}$ and (n+1) edges $e^i = x_{i+1} - x_i$
- **Material frames**: $M^i = {t^i, m_1^i, m_2^i}$ per edge where $t^i = e^i/|e^j|$

### 2.2 Indexing Convention

$$
\begin{matrix}
e^0 & e^1 & e^2 & ... & e^n \\
x^0 & x^1 & x^2 & ... & x^n & x^{n+1} \\
\end{matrix}
$$

- Primal quantities (vertices): lower indices
- Dual quantities (edges): upper indices

## 3. Discrete Curvature and Geometric Quantities

### 3.1 Discrete Curvature

**Turning angle**: $\phi_i$ between consecutive edges

**Integrated curvature**: $\kappa_i = 2 \tan(\phi_i / 2)$

**Curvature binormal** (integrated quantity):
$$
(\kappa_\beta)_i = (2e_{i-1} \times e_i) / (|e_{i-1}||e_i|+e_{i-1} \cdot e_i) (eq. 1)
$$

### 3.2 Voronoi Domain

Length of domain $D_i$ associated to vertex $i$:
$$
|D_i| = l_i/2 \text{ , where } l_i = |e_{i-1}| + |e_i|
$$

## 4. Parallel Transport and Bishop Frame

### 4.1 Discrete Parallel Transport

Rotation operator $P_i$ about curvature binormal:
$P_i (t_{i-1})=t^i$
$P_i (t_{i-1} \times t^i) = t_{i-1} \times t^i$

### 4.2 Bishop Frame Construction

Starting with u⁰ ⊥ t⁰, iteratively define:

```
uⁱ = Pᵢ(uᵢ₋₁)
vⁱ = tⁱ × uⁱ
```

### 4.3 Material Frame Representation

Material frame angle θⁱ relative to Bishop frame:

```
m₁ⁱ = cos θⁱ · uⁱ + sin θⁱ · vⁱ
m₂ⁱ = -sin θⁱ · uⁱ + cos θⁱ · vⁱ
```

## 5. Energy Formulation

### 5.1 Total Elastic Energy

```
E(Γ) = Eᵦₑₙd(Γ) + Eₜwᵢₛₜ(Γ)
```

### 5.2 Bending Energy

**Material curvatures**:

```
ω̄ⱼᵢ = ((κᵦ)ᵢ · m₂ʲ, -(κᵦ)ᵢ · m₁ʲ)ᵀ for j ∈ {i-1, i}     (2)
```

**General bending energy** (anisotropic, naturally curved):

```
Eᵦₑₙd(Γ) = Σᵢ₌₁ⁿ (1/2lᵢ) Σⱼ₌ᵢ₋₁ⁱ (ω̄ⱼᵢ - ω̄̄ⱼᵢ)ᵀ Bʲ (ω̄ⱼᵢ - ω̄̄ⱼᵢ)     (3)
```

**Special case** (isotropic, naturally straight):

```
Eᵦₑₙd(Γ) = Σᵢ₌₁ⁿ α(κᵦ)ᵢ²/lᵢ
```

### 5.3 Twisting Energy

**Discrete twist**:

```
mᵢ = θⁱ - θⁱ⁻¹
```

**Twisting energy**:

```
Eₜwᵢₛₜ(Γ) = Σᵢ₌₁ⁿ β mᵢ²/lᵢ
```

## 6. Quasistatic Material Frame Treatment

### 6.1 Fundamental Assumption

Material frame minimizes elastic energy at each time step:

```
∂E(Γ)/∂θʲ = 0     (4)
```

### 6.2 Special Case: Naturally Straight, Isotropic Rods

**Uniform twist condition**:

```
mᵢ/lᵢ = (θⁿ - θ⁰)/(2L) = constant     (5)
```

**Simplified energy**:

```
E(Γ) = Σᵢ₌₁ⁿ α(κᵦ)ᵢ²/lᵢ + β(θⁿ - θ⁰)²/(2L)     (6)
```

### 6.3 General Case: Newton's Method

**Energy gradient**:

```
∂E(Γ)/∂θʲ = ∂/∂θʲ(Wʲ + Wʲ⁺¹) + 2β(mʲ/lʲ - mʲ⁺¹/lʲ⁺¹)     (7)
```

**Hessian components**:

```
Hⱼ,ⱼ₋₁ = -2β/lʲ
Hⱼ,ⱼ₊₁ = -2β/lʲ⁺¹
Hⱼ,ⱼ = 2β/lʲ + 2β/lʲ⁺¹ + ∂²(Wʲ + Wʲ⁺¹)/∂(θʲ)²
```

## 7. Discrete Holonomy

### 7.1 Holonomy Definition

Scalar angle ψᵢ(ε) when parallel transporting adapted frame around closed loop of discrete edges.

### 7.2 Holonomy Gradients

```
∇ᵢ₋₁ψᵢ = (κᵦ)ᵢ/(2|eᵢ₋₁|)
∇ᵢ₊₁ψᵢ = -(κᵦ)ᵢ/(2|eⁱ|)     (9)
∇ᵢψᵢ = -(∇ᵢ₋₁ + ∇ᵢ₊₁)ψᵢ
```

### 7.3 Bishop Frame Variation

Total rotation angle:

```
Ψⱼ = Σᵢ₌₁ʲ ψᵢ
```

Gradient:

```
∇ᵢΨⱼ = Σₖ₌₁ʲ ∇ᵢψₖ     (10)
```

## 8. Forces and Equations of Motion

### 8.1 Force on Centerline

```
-dE(Γ)/dxᵢ = -∂E(Γ)/∂xᵢ - Σⱼ₌₀ⁿ (∂E(Γ)/∂θʲ)(∂θʲ/∂xᵢ)
```

For quasistatic case with clamped boundaries:

```
Force = -∂E/∂xᵢ + (∂E/∂θⁿ)Σⱼ₌₁ⁿ ∂ψⱼ/∂xᵢ
```

### 8.2 Special Case: Curvature Binormal Gradient

```
∇ᵢ₋₁(κᵦ)ᵢ = (2[eⁱ] + (κᵦ)ᵢ(eⁱ)ᵀ)/(|eᵢ₋₁||eⁱ| + eᵢ₋₁ · eⁱ)
∇ᵢ₊₁(κᵦ)ᵢ = (2[eᵢ₋₁] - (κᵦ)ᵢ(eᵢ₋₁)ᵀ)/(|eᵢ₋₁||eⁱ| + eᵢ₋₁ · eⁱ)
∇ᵢ(κᵦ)ᵢ = -(∇ᵢ₋₁ + ∇ᵢ₊₁)(κᵦ)ᵢ
```

### 8.3 General Case: Material-Frame Curvature Gradient

```
∇ᵢω̄ⱼₖ = ((m₂ʲ)ᵀ, -(m₁ʲ)ᵀ)∇ᵢ(κᵦ)ₖ - Jω̄ⱼₖ(∇ᵢΨⱼ)ᵀ     (11)
```

### 8.4 Equations of Motion

```
M ẍ = -dE(Γ)/dx
```

Discretized using symplectic Euler method.

## 9. Constraints

### 9.1 Inextensibility Constraints

For each edge:

```
eⁱ · eⁱ - ē̄ⁱ · ē̄ⁱ = 0
```

### 9.2 Rigid-Body Coupling Constraints

For rigid body with quaternion q and translation r:

```
q · q - 1 = 0
q x₀ q* + r - x₀ = 0
q x₁ q* + r - x₁ = 0
```

### 9.3 Constraint Enforcement

**Manifold projection method** with generalized mass matrix:

```
M̃ = [4·I   ]
     [  M·Id₃ₓ₃]
     [    M   ]
```

**Generalized velocity**:

```
y = (q⁻¹q̇, ṙ, ẋ)
```

## 10. Algorithm Structure

### Main Simulation Loop:

1. **Precompute**: ω̄ⱼᵢ using equation (2)
2. **Set quasistatic material frame** (solve equation 4)
3. **While simulating**:
    - Apply torque to rigid-body
    - Integrate rigid-body
    - Compute forces on centerline
    - Integrate centerline
    - Enforce inextensibility and rigid-body coupling
    - Collision detection and response
    - Update Bishop frame
    - Update quasistatic material frame

### Key Parameters:

- **α**: Bending modulus
- **β**: Twisting modulus
- **B**: Anisotropic bending matrix (2×2)
- **M**: Mass matrix
- **I**: Moment of inertia tensor

This formulation provides a complete discrete treatment that preserves the geometric structure of Kirchhoff rod theory while enabling efficient simulation of complex rod dynamics with rigid-body coupling.
# Discrete Elastic Rods: Detailed Implementation Pipeline

## Pipeline Overview

The discrete elastic rods simulation follows Algorithm 1 from the paper, with each stage carefully handling tensor operations and geometric computations.

---

## Stage 0: Initialization and Preprocessing

### Stage 0.1: Geometric Setup
**Purpose**: Initialize rod geometry and material properties

**Inputs**:
- `x_rest`: Rest positions of centerline vertices, shape $(n+2, 3)$
- `u_0`: Initial Bishop frame vector at edge 0, shape $(3,)$
- `alpha`: Bending modulus (scalar)
- `beta`: Twisting modulus (scalar) 
- `B`: Anisotropic bending matrix, shape $(2, 2)$ per edge
- `boundary_conditions`: Type and values for boundary constraints

**Outputs**:
- `x`: Current centerline positions, shape $(n+2, 3)$
- `x_dot`: Centerline velocities, shape $(n+2, 3)$
- `e`: Edge vectors $e^i = x_{i+1} - x_i$, shape $(n+1, 3)$
- `t`: Unit tangent vectors $t^i = e^i/|e^i|$, shape $(n+1, 3)$
- `l`: Voronoi lengths $l_i = |e^{i-1}| + |e^i|$, shape $(n,)$

### Stage 0.2: Precompute Reference Quantities
**Purpose**: Compute rest configuration geometric quantities

**Inputs**:
- `x_rest`: Rest centerline positions, shape $(n+2, 3)$
- `u_0`: Reference Bishop vector, shape $(3,)$

**Mathematical Operations**:
$$
\bar{e}^i = x_{i+1}^{\text{rest}} - x_i^{\text{rest}} \\
\bar{t}^i = \bar{e}^i / |\bar{e}^i| \\
(\bar{\kappa}_b)_i = \frac{2\bar{e}^{i-1} \times \bar{e}^i}{|\bar{e}^{i-1}||\bar{e}^i| + \bar{e}^{i-1} \cdot \bar{e}^i}
$$

**Outputs**:
- `e_bar`: Rest edge vectors, shape $(n+1, 3)$
- `t_bar`: Rest tangent vectors, shape $(n+1, 3)$
- `kappa_b_bar`: Rest curvature binormals, shape $(n, 3)$
- `u_bar`: Rest Bishop frame u-vectors, shape $(n+1, 3)$
- `v_bar`: Rest Bishop frame v-vectors, shape $(n+1, 3)$
- `omega_bar`: Rest material curvatures $\bar{\omega}^j_i$, shape $(n, 2, 2)$

---

## Stage 1: Precompute $\omega^j_i$ (Algorithm Step 1)

### Stage 1.1: Current Geometry Update
**Purpose**: Compute current geometric quantities from centerline positions

**Inputs**:
- `x`: Current centerline positions, shape $(n+2, 3)$

**Mathematical Operations**:
$$
e^i = x_{i+1} - x_i \\
t^i = e^i / |e^i| \\
\phi_i = \arccos(t^{i-1} \cdot t^i) \\
(\kappa_b)_i = \frac{2e^{i-1} \times e^i}{|e^{i-1}||e^i| + e^{i-1} \cdot e^i}
$$

**Outputs**:
- `e`: Current edge vectors, shape $(n+1, 3)$
- `t`: Current tangent vectors, shape $(n+1, 3)$
- `phi`: Turning angles, shape $(n,)$
- `kappa_b`: Curvature binormals, shape $(n, 3)$

### Stage 1.2: Bishop Frame Update
**Purpose**: Update Bishop frame via parallel transport

**Inputs**:
- `t`: Current tangent vectors, shape $(n+1, 3)$
- `u_0`: Bishop vector at edge 0, shape $(3,)$

**Mathematical Operations**:
$$
P_i: \mathbb{R}^3 \to \mathbb{R}^3 \text{ (parallel transport rotation)} \\
u^i = P_i(u^{i-1}) \\
v^i = t^i \times u^i
$$

**Implementation**:
```python
def parallel_transport(u_prev, t_prev, t_curr):
    if torch.allclose(t_prev, t_curr):
        return u_prev
    
    # Rotation axis and angle
    axis = torch.cross(t_prev, t_curr)
    axis = axis / torch.norm(axis)
    cos_angle = torch.dot(t_prev, t_curr)
    angle = torch.acos(torch.clamp(cos_angle, -1, 1))
    
    # Rodrigues rotation formula
    return rodrigues_rotation(u_prev, axis, angle)
```

**Outputs**:
- `u`: Bishop u-vectors, shape $(n+1, 3)$
- `v`: Bishop v-vectors, shape $(n+1, 3)$

### Stage 1.3: Material Curvature Computation
**Purpose**: Compute $\omega^j_i$ using Equation (2)

**Inputs**:
- `kappa_b`: Curvature binormals, shape $(n, 3)$
- `m1`: Material frame vectors $m_1^j$, shape $(n+1, 3)$
- `m2`: Material frame vectors $m_2^j$, shape $(n+1, 3)$

**Mathematical Operations**:
$$
\omega^j_i = \begin{pmatrix}
(\kappa_b)_i \cdot m_2^j \\
-(\kappa_b)_i \cdot m_1^j
\end{pmatrix} \quad \text{for } j \in \{i-1, i\}
$$

**Outputs**:
- `omega`: Material curvatures, shape $(n, 2, 2)$ where `omega[i, :, j]` = $\omega^{i+j-1}_i$

---

## Stage 2: Set Quasistatic Material Frame (Algorithm Step 2)

### Stage 2.1: Energy Gradient Computation
**Purpose**: Compute $\partial E/\partial \theta^j$ using Equation (7)

**Inputs**:
- `omega`: Current material curvatures, shape $(n, 2, 2)$
- `omega_bar`: Rest material curvatures, shape $(n, 2, 2)$
- `B`: Bending matrices, shape $(n+1, 2, 2)$
- `theta`: Current material frame angles, shape $(n+1,)$
- `l`: Voronoi lengths, shape $(n,)$
- `beta`: Twisting modulus (scalar)

**Mathematical Operations**:
$$
\frac{\partial E}{\partial \theta^j} = \frac{\partial}{\partial \theta^j}(W^j + W^{j+1}) + 2\beta\left(\frac{m^j}{l^j} - \frac{m^{j+1}}{l^{j+1}}\right)
$$

where:
$$
W^i = \frac{1}{2l_i} \sum_{j=i-1}^i (\omega^j_i - \bar{\omega}^j_i)^T B^j (\omega^j_i - \bar{\omega}^j_i)
$$

**Outputs**:
- `grad_E`: Energy gradient, shape $(n+1,)$

### Stage 2.2: Energy Hessian Computation
**Purpose**: Compute Hessian matrix for Newton's method

**Mathematical Operations**:
$$
H_{j,j-1} = -\frac{2\beta}{l^j}, \quad H_{j,j+1} = -\frac{2\beta}{l^{j+1}} \\
H_{j,j} = \frac{2\beta}{l^j} + \frac{2\beta}{l^{j+1}} + \frac{\partial^2(W^j + W^{j+1})}{\partial(\theta^j)^2}
$$

**Outputs**:
- `hessian`: Tridiagonal Hessian matrix, shape $(n+1, n+1)$

### Stage 2.3: Newton Iteration
**Purpose**: Solve for optimal $\theta^j$ values

**Mathematical Operations**:
$$
\theta^{\text{new}} = \theta^{\text{old}} - \alpha_{\text{line}} H^{-1} \nabla E
$$

**Implementation**:
```python
def newton_step_with_line_search(theta, grad_E, hessian, energy_func):
    # Solve tridiagonal system
    delta_theta = solve_tridiagonal(hessian, -grad_E)
    
    # Line search
    alpha = backtracking_line_search(theta, delta_theta, energy_func)
    
    return theta + alpha * delta_theta
```

**Outputs**:
- `theta`: Updated material frame angles, shape $(n+1,)$
- `m1, m2`: Updated material frame vectors, shape $(n+1, 3)$ each

---

## Stage 3: Main Simulation Loop

### Stage 3.1: Rigid-Body Integration (Algorithm Step 4-5)

**Inputs**:
- `rigid_body_state`: Position, orientation, linear/angular velocities
- `torque`: Torque from rod coupling, shape $(3,)$
- `dt`: Time step (scalar)

**Mathematical Operations**:
$$
\tau = |\tau| t^0 \quad \text{where } |\tau| = \frac{\partial E}{\partial \theta^0}
$$

**Outputs**:
- `rigid_body_state`: Updated rigid body state
- `boundary_theta`: Updated boundary material frame angle

### Stage 3.2: Centerline Force Computation (Algorithm Step 6)

**Purpose**: Compute forces on centerline vertices

**Inputs**:
- `x`: Centerline positions, shape $(n+2, 3)$
- `omega`: Material curvatures, shape $(n, 2, 2)$
- `kappa_b`: Curvature binormals, shape $(n, 3)$
- `theta`: Material frame angles, shape $(n+1,)$

#### Stage 3.2.1: Curvature Binormal Gradients

**Mathematical Operations**:
$$
\nabla_{i-1}(\kappa_b)_i = \frac{2[e^i] + (\kappa_b)_i (e^i)^T}{|e^{i-1}||e^i| + e^{i-1} \cdot e^i} \\
\nabla_{i+1}(\kappa_b)_i = \frac{2[e^{i-1}] - (\kappa_b)_i (e^{i-1})^T}{|e^{i-1}||e^i| + e^{i-1} \cdot e^i}
$$

where $[e]$ is the skew-symmetric matrix s.t. $[e] \cdot x = e \times x$.

**Outputs**:
- `grad_kappa_b`: Gradients of curvature binormals, shape $(n, 3, 3)$

#### Stage 3.2.2: Holonomy Gradients

**Mathematical Operations**:
$$
\nabla_{i-1} \psi_i = \frac{(\kappa_b)_i}{2|e^{i-1}|}, \quad \nabla_{i+1} \psi_i = -\frac{(\kappa_b)_i}{2|e^i|}
$$

**Outputs**:
- `grad_psi`: Holonomy gradients, shape $(n, 3)$

#### Stage 3.2.3: Total Force Assembly

**Mathematical Operations**:
For special case (isotropic, naturally straight):
$$
F_i = -\sum_{j=i-1}^{i+1} \frac{2\alpha}{l^j} (\nabla_i (\kappa_b)_j)^T (\kappa_b)_j + \frac{\beta(\theta^n - \theta^0)}{L} \nabla_i \psi_j
$$

For general case:
$$
F_i = -\sum_{k=1}^n \frac{1}{l_k} \sum_{j=k-1}^k (\nabla_i \omega^j_k)^T B^j (\omega^j_k - \bar{\omega}^j_k)
$$

**Outputs**:
- `forces`: Forces on centerline vertices, shape $(n+2, 3)$

### Stage 3.3: Centerline Integration (Algorithm Step 7)

**Purpose**: Integrate equations of motion using symplectic Euler

**Inputs**:
- `x`: Positions, shape $(n+2, 3)$
- `x_dot`: Velocities, shape $(n+2, 3)$
- `forces`: Forces, shape $(n+2, 3)$
- `M`: Mass matrix, shape $(n+2, 3, 3)$ (typically diagonal)
- `dt`: Time step (scalar)

**Mathematical Operations**:
$$
\dot{x}^{n+1} = \dot{x}^n + dt \cdot M^{-1} F^n \\
x^{n+1} = x^n + dt \cdot \dot{x}^{n+1}
$$

**Outputs**:
- `x`: Updated positions, shape $(n+2, 3)$
- `x_dot`: Updated velocities, shape $(n+2, 3)$

### Stage 3.4: Constraint Enforcement (Algorithm Step 8)

#### Stage 3.4.1: Constraint Violation Computation

**Inputs**:
- `x`: Current positions, shape $(n+2, 3)$
- `rigid_body_state`: Rigid body position/orientation
- `e_bar`: Rest edge lengths, shape $(n+1,)$

**Mathematical Operations**:
$$
C_{\text{inext}}^i = e^i \cdot e^i - \bar{e}^i \cdot \bar{e}^i \\
C_{\text{rigid}} = \begin{pmatrix} q \cdot q - 1 \\ q x_0 q^* + r - x_0 \\ q x_1 q^* + r - x_1 \end{pmatrix}
$$

**Outputs**:
- `C`: Constraint violations, shape $(n+1+4,)$ (inextensibility + rigid body)

#### Stage 3.4.2: Fast Manifold Projection

**Purpose**: Project configuration onto constraint manifold

**Inputs**:
- `y`: Generalized velocities $(q^{-1}\dot{q}, \dot{r}, \dot{x})$, shape $(3+3+(n+2) \times 3,)$
- `M_tilde`: Generalized mass matrix, shape $(3+3+(n+2) \times 3, 3+3+(n+2) \times 3)$
- `C`: Constraint violations, shape $(n+1+4,)$

**Mathematical Operations**:
$$
\tilde{M} = \begin{pmatrix}
4 \cdot I & & \\
& M \cdot \text{Id}_{3 \times 3} & \\
& & M
\end{pmatrix}
$$

Newton iteration:
$$
\begin{pmatrix} \tilde{M} & J_C^T \\ J_C & 0 \end{pmatrix} \begin{pmatrix} \Delta y \\ \lambda \end{pmatrix} = \begin{pmatrix} 0 \\ -C \end{pmatrix}
$$

**Implementation**:
```python
def fast_projection_step(y, M_tilde, C, J_C):
    # Assemble system matrix
    n_dof = y.shape[0]
    n_constraints = C.shape[0]
    
    system_matrix = torch.zeros(n_dof + n_constraints, n_dof + n_constraints)
    system_matrix[:n_dof, :n_dof] = M_tilde
    system_matrix[:n_dof, n_dof:] = J_C.T
    system_matrix[n_dof:, :n_dof] = J_C
    
    rhs = torch.cat([torch.zeros(n_dof), -C])
    
    # Solve system
    solution = torch.linalg.solve(system_matrix, rhs)
    delta_y = solution[:n_dof]
    lambda_mult = solution[n_dof:]
    
    return y + delta_y, lambda_mult
```

**Outputs**:
- `y`: Projected generalized velocities, shape $(3+3+(n+2) \times 3,)$
- `x`: Projected positions, shape $(n+2, 3)$
- `rigid_body_state`: Projected rigid body state

### Stage 3.5: Collision Detection and Response (Algorithm Step 9)

**Purpose**: Handle rod self-contact and external collisions

**Inputs**:
- `x`: Centerline positions, shape $(n+2, 3)$
- `radius`: Rod radius (scalar)

**Outputs**:
- `x`: Collision-corrected positions, shape $(n+2, 3)$
- `x_dot`: Collision-corrected velocities, shape $(n+2, 3)$

### Stage 3.6: Final Updates (Algorithm Steps 10-11)

#### Stage 3.6.1: Bishop Frame Update
**Purpose**: Maintain Bishop frame adaptation to centerline

**Mathematical Operations**:
$$
u^0_{\text{new}} = P_{\text{time}}(u^0_{\text{old}})
$$
where $P_{\text{time}}$ is parallel transport in time.

#### Stage 3.6.2: Quasistatic Material Frame Update
**Purpose**: Re-solve for optimal material frame

**Outputs**:
- `theta`: Updated material frame angles, shape $(n+1,)$
- `m1, m2`: Updated material frame vectors, shape $(n+1, 3)$ each

---

## Data Flow Summary

```
Input: x_rest(n+2,3), u_0(3), alpha, beta → Initialize
    ↓
x(n+2,3), x_dot(n+2,3) → Precompute omega^j_i
    ↓
omega(n,2,2) → Quasistatic Solve
    ↓
theta(n+1) → Force Computation
    ↓
forces(n+2,3) → Integration
    ↓
x_new(n+2,3) → Constraint Projection
    ↓
x_projected(n+2,3) → Update Frames
    ↓
Repeat Simulation Loop
```

## Computational Complexity

- **Per time step**: $O(n)$ for most operations
- **Newton solve**: $O(n)$ due to tridiagonal structure
- **Constraint projection**: $O(n^3)$ for dense system solve
- **Overall**: $O(n^3)$ per time step due to constraint projection

## Key Implementation Notes

1. **Numerical Stability**: Use Rodrigues rotation formula for parallel transport
2. **Singularity Handling**: Check for collinear edges in curvature binormal computation
3. **Line Search**: Essential for Newton convergence in quasistatic solve
4. **Constraint Tolerance**: Typically $10^{-8}$ for constraint satisfaction
5. **Time Step**: Limited by CFL condition for bending waves