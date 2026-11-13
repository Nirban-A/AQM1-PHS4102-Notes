---
title: "Irreducible Tensor Operators and Their Commutation Relations"
part: 3
chapter: 22
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 22 Irreducible Tensor Operators and Their Commutation Relations

## 22.1 Definition

An irreducible tensor operator is written $\hat T^{(k)}_q$, where $k$ is the **rank** and $q$ labels the $2k+1$ **components**, $q=-k,\dots,k$. For $k=1$, $q=-1,0,1$, and

$$
\hat T^{(1)}_{\pm1}=\mp\frac1{\sqrt2}\big(\hat A_x\pm i\hat A_y\big),\qquad \hat T^{(1)}_0=\hat A_z .
$$

## 22.2 The Commutation Relations

Requiring $\hat T^{(k)}_q$ to transform under rotations like the angular momentum states $|k,q\rangle$ is equivalent to the following commutators with $\hat{\vec J}$.

!!! thm "Defining Relations of an Irreducible Tensor Operator"

    \begin{align*}
    [\hat J_z,\hat T^{(k)}_q]&=\hbar q\,\hat T^{(k)}_q,\tag{I}\\
    [\hat J_\pm,\hat T^{(k)}_q]&=\hbar\sqrt{(k\mp q)(k\pm q+1)}\ \hat T^{(k)}_{q\pm1},\tag{II}\\
    \sum_i\big[\hat J_i,[\hat J_i,\hat T^{(k)}_q]\big]&=\hbar^2k(k+1)\,\hat T^{(k)}_q,
    \end{align*}

    where $\hat J_\pm=\hat J_x\pm i\hat J_y$.

!!! intuition "Intuition"

    Compare with $\hat J_z|k,q\rangle=\hbar q|k,q\rangle$ and $\hat J_\pm|k,q\rangle=\hbar\sqrt{(k\mp q)(k\pm q+1)}\,|k,q\pm1\rangle$. The operator $[\hat J_z,\,\cdot\,]$ acts on $\hat T^{(k)}_q$ as $\hat J_z$ acts on $|k,q\rangle$, and the double commutator is the analogue of $\hat J^2$. So $\hat T^{(k)}_q$ “behaves as an angular momentum state” under the adjoint action.

!!! verification "Verification (rank 1)"

    The relations (I) and (II) agree with the vector results of [Section 20](20-scalar-vector-operators.md): $[\hat J_z,\hat A_q]=\hbar q\hat A_q$, and $[\hat J_+,\hat A_0]=\sqrt2\,\hbar\hat A_{+1}$, which is (II) with $k=1$, $q=0$, since $\sqrt{(1-0)(1+0+1)}=\sqrt2$.

## 22.3 Selection Rule on $m$

Take the matrix element of relation (I) between angular momentum states:

\begin{align*}
\langle j',m'|[\hat J_z,\hat T^{(k)}_q]|j,m\rangle&=\langle j',m'|\hat J_z\hat T^{(k)}_q-\hat T^{(k)}_q\hat J_z|j,m\rangle=\hbar(m'-m)\langle j',m'|\hat T^{(k)}_q|j,m\rangle,\\
&=\hbar q\,\langle j',m'|\hat T^{(k)}_q|j,m\rangle .
\end{align*}

Therefore $(m'-m-q)\langle j',m'|\hat T^{(k)}_q|j,m\rangle=0$.

!!! thm "$m$ Selection Rule"

    $$
    \langle j',m'|\hat T^{(k)}_q|j,m\rangle\neq0\quad\text{only if}\quad m'=m+q .
    $$

!!! intuition "Intuition"

    The operator $\hat T^{(k)}_q$ carries $q$ units of angular momentum about $z$. Acting on a state with $J_z=\hbar m$ it creates a state with $J_z=\hbar(m+q)$.

## 22.4 A Recursion Relation for the Matrix Elements

Now take the matrix element of (II) with the raising operator:

$$
\langle j',m'|[\hat J_+,\hat T^{(k)}_q]|j,m\rangle=\hbar\sqrt{(k-q)(k+q+1)}\ \langle j',m'|\hat T^{(k)}_{q+1}|j,m\rangle .
$$

The left side is $\langle j',m'|\hat J_+\hat T^{(k)}_q-\hat T^{(k)}_q\hat J_+|j,m\rangle$. Use, for the first term,

$$
\langle j',m'|\hat J_+=\big[\hat J_-|j',m'\rangle\big]^\dagger=\hbar\sqrt{(j'+m')(j'-m'+1)}\,\langle j',m'-1|,
$$

and, for the second term,

$$
\hat J_+|j,m\rangle=\hbar\sqrt{(j-m)(j+m+1)}\,|j,m+1\rangle .
$$

Cancelling the common $\hbar$:

!!! thm "Recursion for Matrix Elements of $\hat T^{(k)}_q$"

    \begin{align*}
    \sqrt{(j'+m')(j'-m'+1)}\ \langle j',m'-1|\hat T^{(k)}_q|j,m\rangle&-\sqrt{(j-m)(j+m+1)}\ \langle j',m'|\hat T^{(k)}_q|j,m+1\rangle\\
    &=\sqrt{(k-q)(k+q+1)}\ \langle j',m'|\hat T^{(k)}_{q+1}|j,m\rangle .\tag{A}
    \end{align*}

This linear relation connects matrix elements with different values of $m,q,m'$. The next section shows that the Clebsch-Gordan coefficients satisfy the *same* relation, which forces the matrix elements to be proportional to them.
