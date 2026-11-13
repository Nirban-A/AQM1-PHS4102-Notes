---
title: "Cartesian Tensors: Reducible and Irreducible"
part: 3
chapter: 21
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 21 Cartesian Tensors: Reducible and Irreducible

## 21.1 Scalars, Vectors and Tensors Under a Rotation Matrix

Let $R_{ia}$ be the rotation matrix, with $R^TR=\mathbb 1$. Under a rotation of the axes:

-   **Scalars** are invariant.

-   **Vectors**: $v_i'=\sum_aR_{ia}v_a$.

-   **Tensors**: $T'_{ij}=\sum_{a,b}R_{ia}R_{jb}T_{ab}$ (rank 2), $\ T'_{ijk}=\sum_{a,b,c}R_{ia}R_{jb}R_{kc}T_{abc}$ (rank 3), and so on.

**Example: the dot product is a scalar.** Let $\varphi=v_iw_i$. Then

\begin{align*}
\varphi'&=v_i'w_i'=R_{ia}R_{ib}\,v_aw_b=R^T_{ai}R_{ib}\,v_aw_b=(R^TR)_{ab}\,v_aw_b\\
&=\delta_{ab}\,v_aw_b=v_aw_a=\varphi ,
\end{align*}

using $R^TR=\mathbb 1$. The quantity $\varphi$ remains invariant.

Now take the product $T_{ij}=v_iw_j$, which has nine components. It transforms as a rank-2 tensor:

$$
T'_{ij}=v_i'w_j'=R_{ia}R_{jb}\,v_aw_b=R_{ia}R_{jb}\,T_{ab}.
$$

## 21.2 Reducible Tensors: Decomposition of Rank 2

A Cartesian tensor of rank 2 has $3^2=9$ components but can be split into three pieces that never mix under rotation:

!!! thm "Decomposition of a Rank-2 Tensor"

    \begin{align*}
    T^{(0)}_{ij}&=\tfrac13\,\delta_{ij}\sum_{k=1}^{3}T_{kk}&&\to\ 1\ \text{component (scalar part)},\\
    T^{(1)}_{ij}&=\tfrac12\,(T_{ij}-T_{ji})&&\to\ 3\ \text{components (vector part, antisymmetric)},\\
    T^{(2)}_{ij}&=\tfrac12\,(T_{ij}+T_{ji})-T^{(0)}_{ij}&&\to\ 5\ \text{components (symmetric, traceless)}.
    \end{align*}

    Any rank-2 tensor is the sum $T=T^{(0)}+T^{(1)}+T^{(2)}$, and $1+3+5=9$.

The antisymmetric part has $3$ independent components (the diagonal vanishes and $T_{ji}=-T_{ij}$, so only $i<j$ pairs count). The symmetric part has $6$ independent components, and removing the trace (one condition) leaves $5$.

!!! solution "Complete Solution"

    *(example $T_{ij}=v_iw_j$):* The three pieces are

    \begin{align*}
    T^{(0)}_{ij}&=\tfrac13\,\delta_{ij}\,\vec v\cdot\vec w,\\
    T^{(1)}_{ij}&=\tfrac12\,(v_iw_j-v_jw_i)\ \leftrightarrow\ \tfrac12\,(\vec v\times\vec w\,)_k,\\
    T^{(2)}_{ij}&=\tfrac12\,(v_iw_j+v_jw_i)-\tfrac13\,\delta_{ij}\,\vec v\cdot\vec w .
    \end{align*}

So the nine products $v_iw_j$ split into the dot product (a scalar), the cross product (a vector) and a symmetric traceless remainder with five components.

## 21.3 Irreducible Tensors

A Cartesian tensor of rank $k$ can be decomposed into tensors of lower rank, each a linear combination of the $3^k$ components. The pieces that cannot be reduced any further are the irreducible parts.

!!! thm "Irreducible Tensor of Rank $k$"

    A set of $(2k+1)$ components that behaves as a rank-$k$ tensor and cannot be reduced is an *irreducible tensor of rank $k$*. The $(2k+1)$ components are symmetric and traceless.

The decomposition above is an example: $T^{(0)},T^{(1)},T^{(2)}$ are irreducible tensors of rank $0,1,2$ with $1,3,5$ components.

!!! intuition "Intuition"

    Irreducibility means the pieces carry independent sets of states under rotation, exactly as the $2j+1$ states $|j,m\rangle$ of a fixed $j$ never mix with those of a different $j$. That is why irreducible tensors can be matched with angular momentum states.

## 21.4 Irreducible Spherical Tensors

!!! thm "Definition (Irreducible Spherical Tensor)"

    An irreducible spherical tensor of rank $k$ ($k$ an integer) is a set of $(2k+1)$ operators $\hat T^{(k)}_q$, $q=-k,\dots,0,\dots,k$, which transform under a rotation of the axes in the same way as the angular momentum states $|k,q\rangle$.

For $k=1$:

$$
\hat T^{(1)}_{\pm1}=\mp\frac1{\sqrt2}\big(\hat A_x\pm i\hat A_y\big),\qquad\hat T^{(1)}_0=\hat A_z ,
$$

which are exactly the spherical components of a vector operator from [Section 20](20-scalar-vector-operators.md). A scalar is $k=0$ (one component, $q=0$) and a vector is $k=1$.

!!! studynote "Study Note"

    A rank-2 irreducible tensor has five components $T^{(2)}_q$, $q=-2,\dots,2$. If $\hat A,\hat B$ are two vector operators, the five combinations $\hat A_{+1}\hat B_{+1}$, $\tfrac1{\sqrt2}(\hat A_{+1}\hat B_0+\hat A_0\hat B_{+1})$, $\tfrac1{\sqrt6}(\hat A_{+1}\hat B_{-1}+2\hat A_0\hat B_0+\hat A_{-1}\hat B_{+1})$, $\tfrac1{\sqrt2}(\hat A_{-1}\hat B_0+\hat A_0\hat B_{-1})$, $\hat A_{-1}\hat B_{-1}$ form $\hat T^{(2)}_{q}$ for $q=2,1,0,-1,-2$. These are the Clebsch-Gordan combinations of two $k=1$ objects, as for two spin-1 particles coupled to total spin 2.
