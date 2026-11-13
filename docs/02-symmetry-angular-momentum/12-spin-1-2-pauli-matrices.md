---
title: "Spin-1/2 and the Pauli Matrices"
part: 2
chapter: 12
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 12 Spin-$\tfrac12$ and the Pauli Matrices

## 12.1 Spin Operators on a Two-Dimensional Space

Spin is described by a two-dimensional Hilbert space with basis kets $|+\rangle,|-\rangle$ and

$$
\langle+|+\rangle=\langle-|-\rangle=1,\qquad\langle+|-\rangle=0,\qquad |+\rangle\langle+|+|-\rangle\langle-|=\mathbb 1 .
$$

Construct the operators

\begin{align*}
\hat S_x&=\frac\hbar2\big\{|-\rangle\langle+|+|+\rangle\langle-|\big\},\\
\hat S_y&=\frac{i\hbar}2\big\{|-\rangle\langle+|-|+\rangle\langle-|\big\},\\
\hat S_z&=\frac\hbar2\big\{|+\rangle\langle+|-|-\rangle\langle-|\big\}.
\end{align*}

Then

$$
\hat S_x\hat S_y=\frac{i\hbar^2}4\big\{-|-\rangle\langle-|+|+\rangle\langle+|\big\},\qquad
\hat S_y\hat S_x=\frac{i\hbar^2}4\big\{-|+\rangle\langle+|+|-\rangle\langle-|\big\},
$$

so that

$$
\hat S_x\hat S_y-\hat S_y\hat S_x=\frac{i\hbar^2}4\cdot2\big\{|+\rangle\langle+|-|-\rangle\langle-|\big\}=\frac{i\hbar^2}4\cdot2\cdot\frac2\hbar\hat S_z=i\hbar\hat S_z .
$$

By the same calculation for the other pairs,

$$
[\hat S_i,\hat S_j]=i\hbar\,\epsilon_{ijk}\hat S_k ,
$$

the angular momentum algebra, but with *no classical analogue*. Hence $\hat{\vec S}$ generates rotations in spin space: $\hat U_z(\phi)=\exp(-i\phi\hat S_z/\hbar)$.

## 12.2 Pauli Two-Component Formalism

Represent the basis kets and bras as

$$
|+\rangle=\begin{pmatrix}1\\0\end{pmatrix},\ \ |-\rangle=\begin{pmatrix}0\\1\end{pmatrix},\ \ \langle+|=(1\ \ 0),\ \ \langle-|=(0\ \ 1).
$$

For example,

$$
\hat S_z=\frac\hbar2\Big\{\begin{pmatrix}1\\0\end{pmatrix}(1\ \ 0)-\begin{pmatrix}0\\1\end{pmatrix}(0\ \ 1)\Big\}=\frac\hbar2\begin{pmatrix}1&0\\0&-1\end{pmatrix}=\frac\hbar2\hat\sigma_3 ,
$$

and likewise $\hat S_x=\tfrac\hbar2\hat\sigma_1$, $\hat S_y=\tfrac\hbar2\hat\sigma_2$.

!!! thm "Pauli Matrices"

    $$
    \hat\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
    \hat\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
    \hat\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
    $$

    Properties: $\hat\sigma_i^2=\mathbb 1$; $\hat\sigma_i\hat\sigma_j+\hat\sigma_j\hat\sigma_i=0$ for $i\ne j$, i.e. $\{\hat\sigma_i,\hat\sigma_j\}=2\delta_{ij}\mathbb 1$; $[\hat\sigma_i,\hat\sigma_j]=2i\epsilon_{ijk}\hat\sigma_k$; $\hat\sigma_i^\dagger=\hat\sigma_i$; $\det\hat\sigma_i=-1$; $\mathrm{Tr}\,\hat\sigma_i=0$.

## 12.3 The $j=\tfrac12$ Basis

For $j=\tfrac12$ the allowed values are $m=\pm\tfrac12$, with $\hat J_z|\tfrac12,\pm\tfrac12\rangle=\pm\tfrac\hbar2|\tfrac12,\pm\tfrac12\rangle$, so in this basis $\hat J_z=\tfrac\hbar2\hat\sigma_3$. The action of $\hat J_\pm$ ([Section 11](11-angular-momentum-eigenvalues-ladder-operators.md)) then gives $\hat J_x=\tfrac\hbar2\hat\sigma_x$ and $\hat J_y=\tfrac\hbar2\hat\sigma_y$. The usual nomenclature is

$$
|\tfrac12,\tfrac12\rangle=|\!\uparrow\rangle\equiv\begin{pmatrix}1\\0\end{pmatrix},\qquad
|\tfrac12,-\tfrac12\rangle=|\!\downarrow\rangle\equiv\begin{pmatrix}0\\1\end{pmatrix}.
$$

## 12.4 Identities

!!! thm "Two Pauli Identities"

    For numbers (not operators) $a_1,a_2,a_3$ and $\vec a=(a_1,a_2,a_3)$,

    $$
    \hat{\vec\sigma}\cdot\vec a=\hat\sigma_1a_1+\hat\sigma_2a_2+\hat\sigma_3a_3=\begin{pmatrix}a_3&a_1-ia_2\\a_1+ia_2&-a_3\end{pmatrix},
    $$

    $$
    (\hat{\vec\sigma}\cdot\vec a)(\hat{\vec\sigma}\cdot\vec b)=\vec a\cdot\vec b+i\,\hat{\vec\sigma}\cdot(\vec a\times\vec b).
    $$

!!! solution "Complete Solution"

    Split the product into commutator and anticommutator,

    \begin{align*}
    (\hat{\vec\sigma}\cdot\vec a)(\hat{\vec\sigma}\cdot\vec b)&=\sum_{j,k}a_jb_k\hat\sigma_j\hat\sigma_k=\sum_{j,k}a_jb_k\,\tfrac12\Big([\hat\sigma_j,\hat\sigma_k]+\{\hat\sigma_j,\hat\sigma_k\}\Big)\\
    &=\sum_{j,k}a_jb_k\big(\delta_{jk}+i\epsilon_{jk\ell}\hat\sigma_\ell\big)=\vec a\cdot\vec b+i\,\hat{\vec\sigma}\cdot(\vec a\times\vec b).
    \end{align*}

For $\vec a=\vec b$ this gives $(\hat{\vec\sigma}\cdot\vec a)^2=|\vec a|^2$, so for a unit vector $\hat n$, $(\hat n\cdot\hat{\vec\sigma})^m=\mathbb 1$ for even $m$ and $=\hat n\cdot\hat{\vec\sigma}$ for odd $m$.

## 12.5 Rotation of a Spin: the Rotation Operator

!!! thm "Spin-$\tfrac12$ Rotation Operator"

    $$
    \hat U_{\hat n}(\phi)=e^{-\frac i\hbar\phi\,\hat n\cdot\hat{\vec S}}=e^{-\frac i2\phi\,\hat n\cdot\hat{\vec\sigma}}=\mathbb 1\cos\frac\phi2-i\,\hat{\vec\sigma}\cdot\hat n\,\sin\frac\phi2,\qquad \hat n=(n_x,n_y,n_z),\ n_x^2+n_y^2+n_z^2=1 .
    $$

!!! solution "Complete Solution"

    Expand the exponential and use $(\hat n\cdot\hat{\vec\sigma})^2=\mathbb 1$:

    $$
    e^{-\frac i2\phi\,\hat n\cdot\hat{\vec\sigma}}=\Big[\mathbb 1-\frac{(\hat n\cdot\hat{\vec\sigma})^2}{2!}\Big(\frac\phi2\Big)^2+\frac{(\hat n\cdot\hat{\vec\sigma})^4}{4!}\Big(\frac\phi2\Big)^4-\cdots\Big]-i\Big[(\hat{\vec\sigma}\cdot\hat n)\frac\phi2-\frac{(\hat{\vec\sigma}\cdot\hat n)^3}{3!}\Big(\frac\phi2\Big)^3+\cdots\Big],
    $$

    and the two brackets sum to $\cos(\phi/2)$ and $\hat{\vec\sigma}\cdot\hat n\,\sin(\phi/2)$. As a matrix,

    $$
    \hat U_{\hat n}(\phi)=\begin{pmatrix}\cos\frac\phi2-in_z\sin\frac\phi2&(-in_x-n_y)\sin\frac\phi2\\(-in_x+n_y)\sin\frac\phi2&\cos\frac\phi2+in_z\sin\frac\phi2\end{pmatrix}.
    $$

!!! studynote "Study Note"

    The notebook’s matrix drops the factor $i$ in the diagonal term $-in_z\sin\frac\phi2$ (top-left); the form above is the one that follows from $\mathbb 1\cos\frac\phi2-i\hat{\vec\sigma}\cdot\hat n\sin\frac\phi2$.

A rotation through $\phi=2\pi$ gives $\hat U_{\hat n}(2\pi)=-\mathbb 1$: the spinor changes sign. This is the signature of a double-valued (spinor) representation. Only a $4\pi$ rotation returns the state itself, while all expectation values are unaffected.

## 12.6 Expectation Values Under a Rotation (Hausdorff Identity)

Let $|\alpha'\rangle=\hat U_z(\phi)|\alpha\rangle$. Then

$$
\langle\hat S_x'\rangle=\langle\alpha'|\hat S_x|\alpha'\rangle=\langle\alpha|e^{i\phi\hat S_z/\hbar}\,\hat S_x\,e^{-i\phi\hat S_z/\hbar}|\alpha\rangle .
$$

The operator inside is evaluated with the Hausdorff identity:

!!! thm "Hausdorff Identity"

    $$
    e^{i\hat G\lambda}\hat Ae^{-i\hat G\lambda}=\hat A+i\lambda[\hat G,\hat A]+\frac{i^2\lambda^2}{2!}\big[\hat G,[\hat G,\hat A]\big]+\cdots
    $$

Use $\hat A=\hat S_x$, $\hat G=\hat S_z$, $\lambda=\phi/\hbar$ and $[\hat S_z,\hat S_x]=i\hbar\hat S_y$, $[\hat S_z,\hat S_y]=-i\hbar\hat S_x$:

\begin{align*}
e^{i\phi\hat S_z/\hbar}\hat S_xe^{-i\phi\hat S_z/\hbar}&=\hat S_x+\frac{i\phi}\hbar[\hat S_z,\hat S_x]+\frac1{2!}\Big(\frac{i\phi}\hbar\Big)^2\big[\hat S_z,[\hat S_z,\hat S_x]\big]+\cdots\\
&=\hat S_x\Big[1-\frac{\phi^2}{2!}+\cdots\Big]-\hat S_y\Big[\phi-\frac{\phi^3}{3!}+\cdots\Big]=\cos\phi\,\hat S_x-\sin\phi\,\hat S_y .
\end{align*}

Therefore, and similarly for $\hat S_y$,

\begin{gather*}
\langle\hat S_x'\rangle=\cos\phi\,\langle\hat S_x\rangle-\sin\phi\,\langle\hat S_y\rangle,\qquad
\langle\hat S_y'\rangle=\sin\phi\,\langle\hat S_x\rangle+\cos\phi\,\langle\hat S_y\rangle,\qquad
\langle\hat S_z'\rangle=\langle\hat S_z\rangle .
\end{gather*}

This is exactly how the components of an ordinary vector rotate about $z$, so the spin expectation value $\langle\hat{\vec S}\rangle$ behaves as a classical vector under rotations of the spin space.

!!! prob "Rotate a Spin Pointing Along $+x$ About $z$ by $90^\circ$"

    !!! solution "Complete Solution"

        The state $|\hat x;+\rangle=\tfrac1{\sqrt2}(1,1)^T$ has $\langle\hat{\vec S}\rangle=(\hbar/2,0,0)$. With $\hat n=\hat z$, $\phi=\pi/2$,

        $$
        \hat U_z(\tfrac\pi2)=\mathrm{diag}\big(e^{-i\pi/4},e^{i\pi/4}\big),\qquad
        \hat U_z(\tfrac\pi2)\tfrac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}=\tfrac{e^{-i\pi/4}}{\sqrt2}\begin{pmatrix}1\\i\end{pmatrix}.
        $$

    This is the $+y$ eigenstate: $\langle\hat S_y'\rangle=\sin\tfrac\pi2\cdot\tfrac\hbar2=\tfrac\hbar2$ and $\langle\hat S_x'\rangle=0$, in agreement with the formulas above.
