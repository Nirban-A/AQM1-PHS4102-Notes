---
title: "Compatible and Incompatible Operators"
part: 1
chapter: 2
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 2 Compatible and Incompatible Operators

## 2.1 Degeneracy and the Matrix of an Observable

Let $\hat\Omega|\omega_i\rangle=\omega_i|\omega_i\rangle$.

-   If the eigenvalue $\omega_i$ is *non-degenerate*, there is one eigenvector $|\omega_i\rangle$.

-   If it is *$s$-fold degenerate*, there are $s$ independent eigenvectors, $\hat\Omega|\omega_i,\alpha\rangle=\omega_i|\omega_i,\alpha\rangle$ with $\alpha=1,2,\dots,s$.

Any linear combination $\sum_{\alpha=1}^sc_\alpha|\omega_i,\alpha\rangle$ is again an eigenvector with the same eigenvalue. For example, if $\hat\Omega|\omega,1\rangle=\omega|\omega,1\rangle$ and $\hat\Omega|\omega,2\rangle=\omega|\omega,2\rangle$ and $|\psi\rangle=c_1|\omega,1\rangle+c_2|\omega,2\rangle$, then $\hat\Omega|\psi\rangle=\omega|\psi\rangle$.

### Matrix representation in the eigenbasis

With two non-degenerate eigenvectors, $\hat\Omega|\omega_1\rangle=\omega_1|\omega_1\rangle$, $\hat\Omega|\omega_2\rangle=\omega_2|\omega_2\rangle$ and $|\omega_1\rangle\langle\omega_1|+|\omega_2\rangle\langle\omega_2|=\mathbb 1$, the matrix of $\hat\Omega$ is

$$
\begin{array}{c|cc}
\hat\Omega&|\omega_1\rangle&|\omega_2\rangle\\\hline
\langle\omega_1|&\omega_1&0\\
\langle\omega_2|&0&\omega_2
\end{array}
$$

In its own eigenbasis the matrix is diagonal (provided there is no degeneracy).

With a degeneracy, take $\hat\Omega|\omega_1\rangle=\omega_1|\omega_1\rangle$ and a doubly degenerate level $\hat\Omega|\omega_2,1\rangle=\omega_2|\omega_2,1\rangle$, $\hat\Omega|\omega_2,2\rangle=\omega_2|\omega_2,2\rangle$. The combinations

$$
|\omega_2\rangle=\tfrac1{\sqrt2}\big(|\omega_2,1\rangle+|\omega_2,2\rangle\big),\qquad
|\omega_3\rangle=\tfrac1{\sqrt2}\big(|\omega_2,1\rangle-|\omega_2,2\rangle\big)
$$

are also orthonormal eigenvectors with eigenvalue $\omega_2$, so in the basis $\{|\omega_1\rangle,|\omega_2\rangle,|\omega_3\rangle\}$ the matrix is block diagonal: a $1\times1$ block $\omega_1$ and a $2\times2$ block belonging to the degenerate level.

!!! studynote "Study Note"

    For $\hat\Omega$ itself the $2\times2$ block is simply $\omega_2\mathbb 1_2$, so it is diagonal whatever basis is chosen inside the degenerate subspace. The block structure matters for a *second* operator $\hat B$ that commutes with $\hat\Omega$: it cannot connect different eigenvalues of $\hat\Omega$, so its matrix has the same blocks, but inside the $2\times2$ block it can have non-zero off-diagonal entries. Diagonalizing that block is exactly the step used in the proof of Theorem 2 below.

## 2.2 Definitions and the Two Theorems

!!! thm "Compatible and Incompatible Operators"

    Two operators $\hat A,\hat B$ are *compatible* if $\hat A\hat B=\hat B\hat A$, i.e. $[\hat A,\hat B]=0$, and *incompatible* if $\hat A\hat B\neq\hat B\hat A$, i.e. $[\hat A,\hat B]\neq0$.

!!! thm "Theorem 1 (simultaneous eigenvectors $\Rightarrow$ commute)"

    If two operators $\hat A$ and $\hat B$ have a complete set of simultaneous eigenvectors, then the two operators commute.

**Proof.** Let $\hat A|n,\mu\rangle=a_n|n,\mu\rangle$ and $\hat B|n,\mu\rangle=b_{n\mu}|n,\mu\rangle$, with $\sum_{n,\mu}|n,\mu\rangle\langle n,\mu|=\mathbb 1$. Then

$$
\hat B\hat A|n,\mu\rangle=a_nb_{n\mu}|n,\mu\rangle,\qquad \hat A\hat B|n,\mu\rangle=b_{n\mu}a_n|n,\mu\rangle .
$$

Subtracting, $(\hat A\hat B-\hat B\hat A)|n,\mu\rangle=0$ for every vector of a complete set, hence $[\hat A,\hat B]=0$ on the whole space. $\blacksquare$

!!! studynote "Study Note (correction)"

    The notebook writes $\hat B|n,\mu\rangle=b_n|n,\mu\rangle$ with the same label $n$ as for $\hat A$. When $\hat A$ is degenerate the $\hat B$ eigenvalue depends on the extra label $\mu$ as well, so $b_{n\mu}$ is written here. The proof is unchanged because the $b$’s are just numbers.

!!! thm "Theorem 2 (commuting $\Rightarrow$ simultaneous eigenvectors)"

    If two operators commute, we can find for them a complete set of simultaneous eigenvectors.

**Proof, Case 1: $\hat A$ non-degenerate.** Let $\hat A|m\rangle=a_m|m\rangle$ with $[\hat A,\hat B]=0$. Then

$$
\hat A\big(\hat B|m\rangle\big)=\hat B\hat A|m\rangle=a_m\big(\hat B|m\rangle\big),
$$

so $\hat B|m\rangle$ is an eigenvector of $\hat A$ with the same eigenvalue $a_m$. There is no degeneracy, so $\hat B|m\rangle$ must be proportional to $|m\rangle$: $\hat B|m\rangle=\lambda_m|m\rangle$. Hence $|m\rangle$ is an eigenvector of both operators. $\blacksquare$

**Proof, Case 2: $\hat A$ degenerate.** Let $\hat A|n,k\rangle=a_n|n,k\rangle$, $k=1,\dots,s$. As above,

$$
\hat A\big(\hat B|n,k\rangle\big)=\hat B\hat A|n,k\rangle=a_n\big(\hat B|n,k\rangle\big),
$$

so $\hat B|n,k\rangle$ is also an eigenvector of $\hat A$ with eigenvalue $a_n$: it lies in the $s$-dimensional eigenspace, so

$$
\hat B|n,k\rangle=\sum_{l=1}^sc_{kl}|n,l\rangle\equiv|\psi\rangle .
$$

Inside this eigenspace $\hat B$ acts as an $s\times s$ matrix $(c_{kl})$. Choosing the basis of the eigenspace to diagonalize it gives a unique set of eigenvectors $\hat B|n,\mu\rangle=b_{n\mu}|n,\mu\rangle$ ($\mu=1,\dots,s$). Any combination of the $|n,k\rangle$ is still an eigenvector of $\hat A$, so also $\hat A|n,\mu\rangle=a_n|n,\mu\rangle$. These are simultaneous eigenvectors of $\hat A$ and $\hat B$. $\blacksquare$

!!! intuition "Intuition"

    A commuting partner $\hat B$ cannot move a state out of an eigenspace of $\hat A$; it can only rotate it inside the eigenspace. Diagonalizing $\hat B$ within each eigenspace of $\hat A$ then yields common eigenvectors. When $\hat A$ and $\hat B$ do *not* commute, $\hat B|n,k\rangle$ leaves the eigenspace and no common eigenbasis exists.

!!! solution "Complete Solution"

    *(explicit $2$-fold example):* For $\hat A|n,1\rangle=a_n|n,1\rangle$, $\hat A|n,2\rangle=a_n|n,2\rangle$ one has $\hat A[\alpha|n,1\rangle+\beta|n,2\rangle]=a_n[\alpha|n,1\rangle+\beta|n,2\rangle]$ for all $\alpha,\beta$. If $\hat B$ acts as the $2\times2$ matrix $\begin{pmatrix}c_{11}&c_{12}\\c_{21}&c_{22}\end{pmatrix}$ on this pair, its two eigenvectors $(\alpha,\beta)$ and eigenvalues $b_{n1},b_{n2}$ come from the secular equation $\det(c-b\mathbb 1)=0$, and the resulting pair labels the two states $|n,1\rangle',|n,2\rangle'$ uniquely.

## 2.3 Complete Set of Commuting Operators

!!! thm "Complete (Maximal) Set of Commuting Operators"

    Start from $\hat A|n\rangle=a_n|n\rangle$ (non-degenerate) or $\hat A|n,\mu\rangle=a_n|n,\mu\rangle$ (degenerate). Add an operator $\hat B$ with $[\hat A,\hat B]=0$ to resolve the degeneracy, so the common eigenvectors are $|n,\nu\rangle$. If a degeneracy remains, add $\hat C$ with $\hat A\hat C=\hat C\hat A$ and $\hat B\hat C=\hat C\hat B$, giving eigenvectors $|n,\nu,\delta\rangle$ that are simultaneously eigenvectors of $\hat A,\hat B,\hat C$. When the eigenvalues of the set label every state uniquely, the set is *complete* (or *maximal*).

!!! studynote "Study Note"

    A complete set of commuting operators is a coordinate system for the Hilbert space: the list of eigenvalues, e.g. $(a_n,b_\nu,c_\delta)$, is the address of one basis vector. Later sections use sets such as $\{\hat H,\hat L^2,\hat L_z\}$ in exactly this sense.

## 2.4 Incompatible Operators and the Uncertainty Relation

Let $[\hat A,\hat B]=i\hat C$, i.e. $\hat A\hat B-\hat B\hat A=i\hat C$, with $\hat A,\hat B,\hat C$ Hermitian. Define the shifted operators

$$
\Delta\hat A=\hat A-\langle\hat A\rangle\mathbb 1,\qquad \Delta\hat B=\hat B-\langle\hat B\rangle\mathbb 1,\qquad \langle\hat A\rangle=\langle\psi|\hat A|\psi\rangle .
$$

Since $\langle\hat A\rangle$ is a number, $[\Delta\hat A,\Delta\hat B]=[\hat A,\hat B]=i\hat C$. Also $\langle(\Delta\hat A)^2\rangle=\langle\hat A^2\rangle-\langle\hat A\rangle^2$ and likewise for $\hat B$.

Introduce, for a real number $\gamma$, the operator and the vector

$$
\hat P=\Delta\hat A+i\gamma\,\Delta\hat B,\qquad |\varphi\rangle=\hat P|\psi\rangle .
$$

The squared norm of any vector is non-negative:

\begin{align*}
0\le\langle\varphi|\varphi\rangle&=\langle\psi|\big(\Delta\hat A-i\gamma\Delta\hat B\big)\big(\Delta\hat A+i\gamma\Delta\hat B\big)|\psi\rangle\\
&=\langle(\Delta\hat A)^2\rangle+\gamma^2\langle(\Delta\hat B)^2\rangle+i\gamma\,\langle\Delta\hat A\Delta\hat B-\Delta\hat B\Delta\hat A\rangle\\
&=\langle(\Delta\hat A)^2\rangle+\gamma^2\langle(\Delta\hat B)^2\rangle-\gamma\langle\hat C\rangle ,
\end{align*}

where the last step uses $\langle[\Delta\hat A,\Delta\hat B]\rangle=i\langle\hat C\rangle$, so $i\gamma\cdot i\langle\hat C\rangle=-\gamma\langle\hat C\rangle$. For $\gamma>0$ divide by $\gamma$:

$$
\frac1\gamma\langle(\Delta\hat A)^2\rangle+\gamma\langle(\Delta\hat B)^2\rangle\ \ge\ \langle\hat C\rangle .
$$

This holds for every $\gamma$, so it holds at the value that minimizes the left side. Differentiating with respect to $\gamma$,

$$
-\frac1{\gamma^2}\langle(\Delta\hat A)^2\rangle+\langle(\Delta\hat B)^2\rangle=0
\quad\Longrightarrow\quad
\gamma^2=\frac{\langle(\Delta\hat A)^2\rangle}{\langle(\Delta\hat B)^2\rangle}.
$$

Substituting this $\gamma$ makes both terms on the left equal to $\sqrt{\langle(\Delta\hat A)^2\rangle\langle(\Delta\hat B)^2\rangle}$, so $2\sqrt{\langle(\Delta\hat A)^2\rangle\langle(\Delta\hat B)^2\rangle}\ge\langle\hat C\rangle$.

!!! thm "Generalized Uncertainty Relation"

    $$
    \sqrt{\langle(\Delta\hat A)^2\rangle\langle(\Delta\hat B)^2\rangle}\ \ge\ \frac{|\langle\hat C\rangle|}{2},
    \qquad\text{i.e.}\qquad \Delta A\,\Delta B\ \ge\ \frac{|\langle\hat C\rangle|}2\qquad\text{for }[\hat A,\hat B]=i\hat C .
    $$

    For $[\hat x,\hat p]=i\hbar\,\mathbb 1$ (so $\hat C=\hbar\mathbb 1$):

    $$
    \boxed{\ \Delta x\,\Delta p\ \ge\ \frac\hbar2\ }
    $$

!!! studynote "Study Note (corrections)"

    \(i\) In the last line of the notebook derivation, $2\langle\Delta\hat A\rangle$ should read $2\langle(\Delta\hat A)^2\rangle$: with $\gamma=\sqrt{\langle(\Delta A)^2\rangle/\langle(\Delta B)^2\rangle}$ the inequality $\langle(\Delta A)^2\rangle+\gamma^2\langle(\Delta B)^2\rangle\ge\gamma\langle C\rangle$ becomes $2\langle(\Delta A)^2\rangle\ge\sqrt{\langle(\Delta A)^2\rangle/\langle(\Delta B)^2\rangle}\,\langle C\rangle$, and cancelling the common factor gives the boxed result. (ii) The notebook states the result with $\langle C\rangle$ rather than $|\langle C\rangle|$. Dividing by $\gamma>0$ assumed $\langle C\rangle\ge0$; for $\langle C\rangle<0$ repeat with $\gamma<0$, which gives the absolute value.

!!! solution "Complete Solution (the discriminant route, which handles the sign automatically)"

    The quantity $\langle(\Delta A)^2\rangle+\gamma^2\langle(\Delta B)^2\rangle-\gamma\langle C\rangle\ge0$ is a quadratic in $\gamma$ that is non-negative for *all* real $\gamma$. Hence its discriminant cannot be positive: $\langle C\rangle^2-4\langle(\Delta A)^2\rangle\langle(\Delta B)^2\rangle\le0$, which is $\Delta A\,\Delta B\ge|\langle C\rangle|/2$.

!!! intuition "Intuition"

    Incompatible observables have no common eigenvectors, so no state can have a sharp value of both. The right-hand side $|\langle C\rangle|/2$ quantifies the unavoidable trade-off. For $\hat x,\hat p$ the bound $\hbar/2$ does not depend on the state; for other pairs (e.g. components of angular momentum) it depends on the state through $\langle\hat C\rangle$.

!!! examtip "Exam Tip"

    To quote or prove an uncertainty relation: (1) compute $[\hat A,\hat B]=i\hat C$, (2) write $\Delta A\,\Delta B\ge|\langle\hat C\rangle|/2$, (3) evaluate $\langle\hat C\rangle$ in the given state. A relation holds for *any* state; it becomes an equality only for special (minimum-uncertainty) states, such as the oscillator ground state and the coherent states of [Section 7](07-classical-limit-oscillator-coherent-states.md).
