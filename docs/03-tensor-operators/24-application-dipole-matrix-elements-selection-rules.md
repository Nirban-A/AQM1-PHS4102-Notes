---
title: "Application: Dipole Matrix Elements and Selection Rules"
part: 3
chapter: 24
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 24 Application: Dipole Matrix Elements and Selection Rules

## 24.1 The $2s\to2p$ Dipole Matrix Element

Take hydrogen-like states $|n,\ell,m\rangle$. The dipole operator is a rank-1 tensor operator, $\hat r^{(1)}_q$. Consider the $2s\to2p$ transition: the dipole term contributes to the transition if

$$
\langle n'=2,\ell'=1,m'=0|\,\hat r^{(1)}_0\,|n=2,\ell=0,m=0\rangle\neq0 .
$$

By the Wigner-Eckart theorem with $\ell=0$, $m=0$, $k=1$, $q=0$, $\ell'=1$, $m'=0$:

$$
\langle\ell',m'|\hat r^{(1)}_0|\ell=0,m=0\rangle=C^{\ell'm'}_{\ell m,kq}\,\langle\ell'\|\hat r^{(1)}\|\ell\rangle=C^{10}_{00,10}\,\langle1\|\hat r^{(1)}\|0\rangle=\langle1\|\hat r^{(1)}\|0\rangle,
$$

since coupling $\ell=0$ with $k=1$ gives $C^{10}_{00,10}=1$. The reduced element is built from the radial integral of the hydrogen functions

$$
R_{2s}=\frac1{\sqrt{2a_0^3}}\Big(1-\frac r{2a_0}\Big)e^{-r/2a_0},\qquad R_{2p}=\frac1{\sqrt{24a_0^3}}\,\frac r{a_0}\,e^{-r/2a_0}.
$$

!!! solution "Complete Solution"

    The radial integral, with $x=r/a_0$, is

    \begin{align*}
    \int_0^\infty R_{2p}\,r\,R_{2s}\,r^2\,dr&=\frac{a_0}{\sqrt{48}}\int_0^\infty x^4\Big(1-\frac x2\Big)e^{-x}\,dx=\frac{a_0}{\sqrt{48}}\big(4!-\tfrac12\,5!\big)\\
    &=-\frac{36}{\sqrt{48}}\,a_0=-3\sqrt3\,a_0\approx-5.196\,a_0 .
    \end{align*}

The angular part supplies a factor $\int Y_{10}^*\cos\theta\,Y_{00}\,d\Omega=1/\sqrt3$, so the full matrix element is

$$
\langle2,1,0|\,z\,|2,0,0\rangle=\langle1\|\hat r^{(1)}\|0\rangle=-\frac{3\sqrt3}{\sqrt3}\,a_0=-3\,a_0 .
$$

!!! studynote "Study Note"

    The notebook identifies the reduced element with the radial integral $\langle R_{2p}|r|R_{2s}\rangle$ and quotes $2.106\,a_0$. That number does not match the integral above, which is exactly $-3\sqrt3\,a_0$, and the reduced element in the convention used here also contains the angular factor $1/\sqrt3$, giving $-3a_0$. Only the non-vanishing of the matrix element matters for the selection-rule argument, so the conclusion is unaffected.

## 24.2 Selection Rules

!!! thm "Dipole Selection Rules"

    For the dipole operator $\hat r^{(1)}_q$ ($k=1$, $q=0,\pm1$):

    $$
    \Delta m=m'-m=q\in\{0,\pm1\},\qquad |\ell-1|\le\ell'\le\ell+1,\qquad\text{and in fact}\quad\Delta\ell=\pm1 .
    $$

!!! solution "Complete Solution"

    The triangle rule allows $\ell'=\ell-1,\ell,\ell+1$. The case $\ell'=\ell$ is removed by parity: $\hat r$ is odd under $\vec r\to-\vec r$ and $Y_{\ell m}$ has parity $(-1)^\ell$, so $\langle\ell'm'|\hat r_q|\ell m\rangle=0$ unless $(-1)^{\ell+\ell'+1}=+1$, i.e. $\ell+\ell'$ is odd. Hence $\Delta\ell=\pm1$.

## 24.3 The Magnetic Selection Rule in the Example

For the same initial state $|2,0,0\rangle$ consider the $q=+1$ component:

$$
\langle\ell',m'|\hat r^{(1)}_{1}|\ell,m\rangle=C^{10}_{00,11}\,\langle\ell'\|\hat r^{(1)}\|\ell\rangle=0,
$$

since $C^{10}_{00,11}=0$: the final state $(\ell',m')=(1,0)$ does not satisfy $m'=m+q=1$. For the $q=+1$ component the allowed final state is $m'=+1$.

!!! prob "Relative Strengths of $2s\to2p$ Components"

    !!! solution "Complete Solution"

        For an initial $s$ state ($\ell=0$, $m=0$) the coupling $0\otimes1$ has a single outcome, so $C(0,1,1|0,q,m')=\delta_{m'q}$ for $q=-1,0,1$. By the theorem,

        $$
        \langle2,1,m'|\hat r^{(1)}_q|2,0,0\rangle=\delta_{m'q}\,\langle1\|\hat r^{(1)}\|0\rangle=-3a_0\,\delta_{m'q}.
        $$

    Each of the three polarisation components connects $2s$ to the corresponding $2p,m'=q$ state with the same magnitude $3a_0$. A spherical $s$ state has no preferred direction, so no component of the dipole operator is favoured. This is the *geometric* content: all the dependence on $q$ sits in the Clebsch-Gordan factor, all the physics in $\langle1\|\hat r^{(1)}\|0\rangle$.
