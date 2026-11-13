---
title: "Orbital Angular Momentum and Spherical Harmonics"
part: 2
chapter: 15
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 15 Orbital Angular Momentum and Spherical Harmonics

## 15.1 Projection to Real Space

For orbital angular momentum $\vec L=\vec r\times\vec p$ (so $\hat L_i=\epsilon_{ijk}\hat r_j\hat p_k$), the eigenvalue equations are

$$
\hat L^2|\ell,m\rangle=\hbar^2\ell(\ell+1)|\ell,m\rangle,\qquad \hat L_z|\ell,m\rangle=\hbar m|\ell,m\rangle .
$$

In Cartesian coordinates,

$$
\hat L_z=\hat x\hat p_y-\hat y\hat p_x=-i\hbar\Big(x\frac\partial{\partial y}-y\frac\partial{\partial x}\Big),
$$

and $\hat L_x,\hat L_y$ follow by cyclic permutation.

!!! solution "Complete Solution"

    The cyclic permutations are

    $$
    \hat L_x=-i\hbar\Big(y\frac\partial{\partial z}-z\frac\partial{\partial y}\Big),\qquad \hat L_y=-i\hbar\Big(z\frac\partial{\partial x}-x\frac\partial{\partial z}\Big).
    $$

In spherical coordinates $(r,\theta,\phi)$ with $x=r\sin\theta\cos\phi$, $y=r\sin\theta\sin\phi$, $z=r\cos\theta$:

!!! thm "$\hat L_z$ and $\hat L^2$ in Spherical Coordinates"

    $$
    \hat L_z=-i\hbar\frac{\partial}{\partial\phi},\qquad
    \hat L^2=-\hbar^2\Big[\frac1{\sin\theta}\frac\partial{\partial\theta}\Big(\sin\theta\frac\partial{\partial\theta}\Big)+\frac1{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\Big].
    $$

## 15.2 Spherical Harmonics

Write $Y_{\ell m}(\theta,\phi)=\langle\theta,\phi|\ell,m\rangle$. Then

$$
\hat L^2Y_{\ell m}(\theta,\phi)=\hbar^2\ell(\ell+1)Y_{\ell m}(\theta,\phi),\qquad \hat L_zY_{\ell m}(\theta,\phi)=\hbar m\,Y_{\ell m}(\theta,\phi),
$$

with the solution

$$
Y_{\ell m}(\theta,\phi)=N_{\ell m}\,P_\ell^m(\cos\theta)\,e^{im\phi},
$$

where $P_\ell^m$ are the associated Legendre functions and $N_{\ell m}$ is a normalisation constant.

!!! intuition "Intuition"

    $L_z=-i\hbar\partial_\phi$ makes the $\phi$-dependence $e^{im\phi}$. Single-valuedness under $\phi\to\phi+2\pi$ requires $m$ to be an integer, and since $m$ runs from $-\ell$ to $\ell$ in integer steps, $\ell$ must be an integer. Half-integer $j$ cannot be orbital.

|            | $Y_{\ell m}(\theta,\phi)$  | $Y_{\ell m}(x,y,z)$  |
|:-----------|:-----------:|:-----------:|
| $Y_{00}$ | $\dfrac1{\sqrt{4\pi}}$  | $\dfrac1{\sqrt{4\pi}}$  |
| $Y_{10}$ | $\sqrt{\dfrac3{4\pi}}\cos\theta$  | $\sqrt{\dfrac3{4\pi}}\,\dfrac zr$  |
| $Y_{1,\pm1}$ | $\mp\sqrt{\dfrac3{8\pi}}\sin\theta\,e^{\pm i\phi}$ | $\mp\sqrt{\dfrac3{8\pi}}\,\dfrac{x\pm iy}r$ |

using $x/r=\sin\theta\cos\phi$, $y/r=\sin\theta\sin\phi$, $z/r=\cos\theta$.

!!! studynote "Study Note"

    The Cartesian column of the notebook omits the $\mp$ sign that the angular column carries. Both columns describe the same function, and the Condon-Shortley phase convention puts the factor $(-1)^m$ on $Y_{\ell m}$ for $m>0$, so the sign must appear in both.

!!! verification "Verification"

    $Y_{10}\propto z/r$ is an eigenfunction of $\hat L_z$ with $m=0$ since it does not depend on $\phi$, and $\hat L^2(z/r)=2\hbar^2(z/r)$ matches $\ell=1$, $\hbar^2\ell(\ell+1)=2\hbar^2$.
