---
title: "The j=1 Representation and the Angular Momentum Uncertainty Relation"
part: 2
chapter: 13
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 13 The $j=1$ Representation and the Angular Momentum Uncertainty Relation

## 13.1 Matrices for $j=1$

In the basis $|1,-1\rangle,|1,0\rangle,|1,1\rangle$ the operator $\hat J_z|j,m\rangle=\hbar m|j,m\rangle$ is diagonal. Using $\hat J_\pm|1,m\rangle=\hbar\sqrt{2-m(m\pm1)}\,|1,m\pm1\rangle$, whose nonzero coefficients are all $\hbar\sqrt2$, and $\hat J_x=\tfrac12(\hat J_++\hat J_-)$, $\hat J_y=\tfrac1{2i}(\hat J_+-\hat J_-)$:

!!! thm "Spin-1 (j=1) Matrices"

    $$
    \hat J_z=\hbar\begin{pmatrix}-1&0&0\\0&0&0\\0&0&1\end{pmatrix},\quad
    \hat J_x=\frac\hbar{\sqrt2}\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix},\quad
    \hat J_y=\frac\hbar{\sqrt2}\begin{pmatrix}0&i&0\\-i&0&i\\0&-i&0\end{pmatrix}.
    $$

!!! verification "Verification"

    $[\hat J_x,\hat J_y]=i\hbar\hat J_z$ holds for these matrices, and $\hat J^2=\hat J_x^2+\hat J_y^2+\hat J_z^2=2\hbar^2\,\mathbb 1=\hbar^2j(j+1)\mathbb 1$ with $j=1$. The $\hat J_y$ matrix is the notebook’s table completed.

The same construction gives the matrices for any $j$: the dimension is $2j+1$ and $\hat J_z$ is always diagonal with entries $\hbar m$.

## 13.2 Uncertainty Relation for Angular Momentum

For Hermitian operators $[\hat A,\hat B]=i\hat C$, the general uncertainty relation is

$$
\Delta\hat A\,\Delta\hat B\ \ge\ \frac{|\langle\hat C\rangle|}2 .
$$

Applying this to $[\hat J_x,\hat J_y]=i\hbar\hat J_z$ (so that $\hat C=\hbar\hat J_z$):

!!! thm "Angular Momentum Uncertainty"

    $$
    \Delta\hat J_x\,\Delta\hat J_y\ \ge\ \frac\hbar2\,|\langle\hat J_z\rangle| .
    $$

!!! intuition "Intuition"

    In an eigenstate $|j,m\rangle$ with $m\neq0$ one component is sharp while the other two are fuzzy: their uncertainty product cannot vanish. For $m=0$ the right-hand side is zero, so the bound is empty (and it is saturated by $|j,j\rangle$ with $\Delta J_x=\Delta J_y$).

!!! verification "Verification"

    For $|j,j\rangle$, $\langle\hat J_x^2\rangle=\langle\hat J_y^2\rangle=\tfrac12\hbar^2 j$ and $\langle\hat J_x\rangle=\langle\hat J_y\rangle=0$, so $\Delta J_x\Delta J_y=\tfrac12\hbar^2j=\tfrac\hbar2\langle\hat J_z\rangle$. The bound is attained.
