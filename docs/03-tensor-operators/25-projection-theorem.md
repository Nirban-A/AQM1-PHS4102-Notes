---
title: "The Projection Theorem"
part: 3
chapter: 25
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 25 The Projection Theorem

## 25.1 Statement

Within a multiplet of fixed $j$, any vector operator $\hat{\vec V}$ behaves like a multiple of $\hat{\vec J}$.

!!! thm "Projection Theorem"

    $$
    \langle j,m'|\hat V_q|j,m\rangle=\frac{\langle j,m|\hat{\vec J}\cdot\hat{\vec V}|j,m\rangle}{\hbar^2j(j+1)}\ \langle j,m'|\hat J_q|j,m\rangle .
    $$

The numerator is the expectation of the scalar $\hat{\vec J}\cdot\hat{\vec V}$ in $|j,m\rangle$, so ([Section 23](23-wigner-eckart-theorem.md)) it does not depend on $m$. The theorem says: replace $\hat{\vec V}$ by its projection onto $\hat{\vec J}$.

## 25.2 Proof

**Step 1: the scalar product in spherical components.** With $\hat J_{\pm1}=\mp\tfrac1{\sqrt2}(\hat J_x\pm i\hat J_y)=\mp\tfrac1{\sqrt2}\hat J_\pm$ and $\hat J_0=\hat J_z$,

$$
\hat{\vec J}\cdot\hat{\vec V}=\hat J_0\hat V_0-\hat J_{+1}\hat V_{-1}-\hat J_{-1}\hat V_{+1}.
$$

!!! verification "Verification"

    $\hat J_{+1}\hat V_{-1}+\hat J_{-1}\hat V_{+1}=-\tfrac12\big[(J_x+iJ_y)(V_x-iV_y)+(J_x-iJ_y)(V_x+iV_y)\big]=-(J_xV_x+J_yV_y)$, so the right side is $J_zV_z+J_xV_x+J_yV_y$.

**Step 2: diagonal matrix element.** The operators $\hat J_q$ never change $j$, so only matrix elements of $\hat V$ inside the multiplet appear. Using $\langle j,m|\hat J_+=\hbar\sqrt{(j+m)(j-m+1)}\,\langle j,m-1|$ and $\langle j,m|\hat J_-=\hbar\sqrt{(j-m)(j+m+1)}\,\langle j,m+1|$:

\begin{align*}
\langle j,m|\hat{\vec J}\cdot\hat{\vec V}|j,m\rangle&=m\hbar\,\langle j,m|\hat V_0|j,m\rangle+\frac\hbar{\sqrt2}\sqrt{(j+m)(j-m+1)}\ \langle j,m-1|\hat V_{-1}|j,m\rangle\\
&\quad-\frac\hbar{\sqrt2}\sqrt{(j-m)(j+m+1)}\ \langle j,m+1|\hat V_{+1}|j,m\rangle .
\end{align*}

!!! studynote "Study Note"

    The notebook writes the factor $\hbar/2$ in front of the two square roots. With the matrix elements of the spherical components $\hat V_{\mp1}$ as above the coefficient is $\hbar/\sqrt2$ (it would be $\hbar/2$ for the Cartesian combinations $\hat V_x\mp i\hat V_y$, which differ from $\hat V_{\mp1}$ by $\sqrt2$). The slip does not affect the argument, which only uses that the bracket below is a number.

**Step 3: apply Wigner-Eckart.** With $k=1$ and $j'=j$,

\begin{gather*}
\langle j,m|\hat V_0|j,m\rangle=C^{jm}_{jm,10}\langle j\|\hat V\|j\rangle,\\
\langle j,m-1|\hat V_{-1}|j,m\rangle=C^{j,m-1}_{jm,1,-1}\langle j\|\hat V\|j\rangle,\\
\langle j,m+1|\hat V_{+1}|j,m\rangle=C^{j,m+1}_{jm,1,1}\langle j\|\hat V\|j\rangle .
\end{gather*}

Substituting,

$$
\langle j,m|\hat{\vec J}\cdot\hat{\vec V}|j,m\rangle=\mathcal C_{jm}\,\langle j\|\hat V\|j\rangle,\tag{1}
$$

where $\mathcal C_{jm}$ is the bracket of Clebsch-Gordan coefficients and square roots, a pure number. If $\hat{\vec V}=\hat{\vec J}$ the same steps give

$$
\langle j,m|\hat J^2|j,m\rangle=\mathcal C_{jm}\,\langle j\|\hat J\|j\rangle.\tag{2}
$$

Dividing (1) by (2),

$$
\frac{\langle j,m|\hat{\vec J}\cdot\hat{\vec V}|j,m\rangle}{\langle j,m|\hat J^2|j,m\rangle}=\frac{\langle j\|\hat V\|j\rangle}{\langle j\|\hat J\|j\rangle}.\tag{3}
$$

**Step 4: ratio of components.** For any $m,m',q$,

$$
\langle j,m'|\hat V_q|j,m\rangle=C^{jm'}_{jm,1q}\langle j\|\hat V\|j\rangle,\qquad
\langle j,m'|\hat J_q|j,m\rangle=C^{jm'}_{jm,1q}\langle j\|\hat J\|j\rangle ,
$$

and dividing the two,

$$
\frac{\langle j,m'|\hat V_q|j,m\rangle}{\langle j,m'|\hat J_q|j,m\rangle}=\frac{\langle j\|\hat V\|j\rangle}{\langle j\|\hat J\|j\rangle}.\tag{4}
$$

From (3) and (4), and $\langle j,m|\hat J^2|j,m\rangle=\hbar^2j(j+1)$,

$$
\frac{\langle j,m|\hat{\vec J}\cdot\hat{\vec V}|j,m\rangle}{\hbar^2j(j+1)}=\frac{\langle j,m'|\hat V_q|j,m\rangle}{\langle j,m'|\hat J_q|j,m\rangle}
\quad\Longrightarrow\quad
\langle j,m'|\hat V_q|j,m\rangle=\frac{\langle j,m|\hat{\vec J}\cdot\hat{\vec V}|j,m\rangle}{\hbar^2j(j+1)}\langle j,m'|\hat J_q|j,m\rangle.\qquad\blacksquare
$$

!!! intuition "Intuition"

    Inside one $j$-multiplet the only vector direction available is $\hat{\vec J}$. Any other vector operator can only have a component along $\hat{\vec J}$ that survives; its perpendicular part averages out, like the classical vector $\vec S$ precessing about $\vec J$ and keeping only $(\vec S\cdot\hat J)\hat J$.

## 25.3 Example: the Spin Operator

Take $\hat{\vec V}=\hat{\vec S}$ with $\hat{\vec J}=\hat{\vec L}+\hat{\vec S}$. Then

\begin{align*}
\hat{\vec J}\cdot\hat{\vec S}&=(\hat{\vec L}+\hat{\vec S})\cdot\hat{\vec S}=\hat{\vec L}\cdot\hat{\vec S}+\hat S^2=\tfrac12\big(\hat J^2-\hat L^2-\hat S^2\big)+\hat S^2\\
&=\tfrac12\big(\hat J^2-\hat L^2+\hat S^2\big).
\end{align*}

Using the projection theorem with $q=0$, $m'=m$:

$$
\langle j,m|\hat S_z|j,m\rangle=\langle j,m|\hat J_z|j,m\rangle\ \frac{\langle j,m|\hat{\vec J}\cdot\hat{\vec S}|j,m\rangle}{\hbar^2j(j+1)}
=m\hbar\cdot\frac{\tfrac12\hbar^2\big[j(j+1)-\ell(\ell+1)+s(s+1)\big]}{\hbar^2j(j+1)}.
$$

!!! thm "Matrix Element of $\hat S_z$ in $|j,m,\ell,s\rangle$"

    $$
    \langle j,m|\hat S_z|j,m\rangle=\frac{m\hbar}{2j(j+1)}\Big[j(j+1)-\ell(\ell+1)+s(s+1)\Big].
    $$

!!! prob "$p$ Electron: $\ell=1$, $s=\tfrac12$"

    !!! solution "Complete Solution"

        For $j=\tfrac32$: $\ j(j+1)=\tfrac{15}4$, so the bracket is $\tfrac{15}4-2+\tfrac34=\tfrac52$ and

        $$
        \langle\hat S_z\rangle=\frac{m\hbar}{2\cdot\frac{15}4}\cdot\frac52=\frac{m\hbar}3 .
        $$

    For $j=\tfrac12$: $\ j(j+1)=\tfrac34$, the bracket is $\tfrac34-2+\tfrac34=-\tfrac12$, and

    $$
    \langle\hat S_z\rangle=\frac{m\hbar}{2\cdot\frac34}\cdot\Big(-\frac12\Big)=-\frac{m\hbar}3 .
    $$

    So in the state $|j=\tfrac32,m=\tfrac12\rangle$ the spin component is $+\hbar/6$, while in $|j=\tfrac12,m=\tfrac12\rangle$ it is $-\hbar/6$. The $j=\tfrac12$ state has the spin mostly antiparallel to the orbital motion.

## 25.4 Application: the Landé Factor

!!! solution "Complete Solution"

    In a weak magnetic field the Zeeman Hamiltonian of a sodium atom is proportional to $\hat L_z+2\hat S_z=\hat J_z+\hat S_z$. The vector operator in question is $\hat{\vec V}=\hat{\vec L}+2\hat{\vec S}=\hat{\vec J}+\hat{\vec S}$, so by the projection theorem

    $$
    \langle j,m'|\hat V_q|j,m\rangle=\frac{\langle\hat{\vec J}\cdot(\hat{\vec J}+\hat{\vec S})\rangle}{\hbar^2j(j+1)}\langle j,m'|\hat J_q|j,m\rangle=\Big[1+\frac{\langle\hat{\vec J}\cdot\hat{\vec S}\rangle}{\hbar^2j(j+1)}\Big]\langle j,m'|\hat J_q|j,m\rangle .
    $$

With $\langle\hat{\vec J}\cdot\hat{\vec S}\rangle=\tfrac12\hbar^2[j(j+1)-\ell(\ell+1)+s(s+1)]$ the bracket is the Landé factor:

!!! thm "Landé $g$-Factor"

    $$
    g_J=1+\frac{j(j+1)-\ell(\ell+1)+s(s+1)}{2j(j+1)},\qquad \Delta E=g_J\,\mu_B\,B\,m .
    $$

For sodium $3P_{3/2}$: $g_J=\tfrac43$. For $3P_{1/2}$: $g_J=\tfrac23$. For $3S_{1/2}$ ($\ell=0$): $g_J=2$. This explains the $\Delta E=g_J\mu_BBm$ statement made without proof in the sodium Zeeman limit.

!!! examtip "Exam Tip"

    The projection theorem is the shortcut whenever a question asks for “the expectation of a vector operator in a state of definite $j$, $m$”. Compute $\langle\hat{\vec J}\cdot\hat{\vec V}\rangle$ with the identity $\hat{\vec J}\cdot\hat{\vec V}=\tfrac12(\hat J^2+\hat V^2-\ldots)$ for the system at hand, and multiply by $m\hbar/\hbar^2j(j+1)$.
