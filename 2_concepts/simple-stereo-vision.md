---
tags:
  - note
  - math/lin-alg
  - comp-methods/vision
  - cs684
status: done
---
# Stereo Vision

![stereo vision diagram](2_concepts/media/Pasted%20image%2020241021223917.png)

- Given two cameras offset by a baseline, $b$, how can we get the __world coordinates of a point__ if we know the __image coordinates__ of the point on both cameras?
- Using the [perspective projection](2_concepts/camera-calibration.md) equations:

$$
\displaylines{
u_l = f_x \frac xz + o_x \\
v_l = f_y \frac yz + o_y \\

u_r = f_x \frac {x-b}z + o_x \\
v_r = f_y \frac yz + o_y
}
$$

- solving for $(x, y, z)$:

![equations for x, y, z](2_concepts/media/Pasted%20image%2020241022142725.png)
