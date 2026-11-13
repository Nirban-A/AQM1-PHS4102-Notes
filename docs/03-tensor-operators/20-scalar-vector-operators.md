---
title: "Scalar and Vector Operators"
part: 3
chapter: 20
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 20 Scalar and Vector Operators

## 20.1 How an Operator Transforms Under a Rotation

For an infinitesimal rotation through $\delta\theta$ about the axis $\hat n$, the rotation operator is

$$
\hat U_{\hat n}(\delta\theta)=\mathbb 1-\frac i\hbar\,\delta\theta\ \hat n\cdot\hat{\vec J}.
$$

A state transforms as $|\psi'\rangle=\hat U|\psi\rangle$, and an operator transforms as

\begin{align*}
\hat A'&=\hat U^\dagger\hat A\,\hat U=\Big(\mathbb 1+\frac i\hbar\,\delta\theta\ \hat n\cdot\hat{\vec J}\Big)\hat A\Big(\mathbb 1-\frac i\hbar\,\delta\theta\ \hat n\cdot\hat{\vec J}\Big)\\
&=\hat A-\frac i\hbar\,\delta\theta\,\big[\hat A,\hat n\cdot\hat{\vec J}\,\big]+O(\delta\theta^2).
\end{align*}

This one formula fixes what “scalar”, “vector” and “tensor” mean quantum mechanically: each is defined by how $\hat A'$ must relate to $\hat A$.

## 20.2 Scalar Operators

A scalar is unchanged by a rotation, $\hat A'=\hat A$. Comparing with the expansion above:

!!! thm "Scalar Operator"

    $$
    \hat A'=\hat A\quad\Longrightarrow\quad\big[\hat A,\hat n\cdot\hat{\vec J}\,\big]=0\ \ \text{for every }\hat n,\qquad\text{i.e.}\quad[\hat A,\hat{\vec J}\,]=0 .
    $$

!!! studynote "Study Note"

    Examples are $\hat J^2$, $\hat r^2$, $\hat p^2$, $\hat{\vec L}\cdot\hat{\vec S}$ and the Hamiltonian of a central potential. A rotation-invariant Hamiltonian is exactly a scalar operator, which is the statement $[\hat H,\hat{\vec J}\,]=0$ of Part II.

## 20.3 Vector Operators

A vector operator transforms like the position vector. For $\vec r$ under an infinitesimal rotation,

$$
\vec r\,'=\vec r+\delta\theta\,(\hat n\times\vec r\,),
$$

so for a vector operator

$$
\hat{\vec A}\,'=\hat{\vec A}+\delta\theta\,(\hat n\times\hat{\vec A}).\tag{II}
$$

Equating this with the general rule, labelled (I), $\hat{\vec A}\,'=\hat{\vec A}-\frac i\hbar\delta\theta[\hat{\vec A},\hat n\cdot\hat{\vec J}\,]$:

$$
\hat{\vec A}-\frac i\hbar\,\delta\theta\,\big[\hat{\vec A},\hat n\cdot\hat{\vec J}\,\big]=\hat{\vec A}+\delta\theta\,(\hat n\times\hat{\vec A}),
\qquad\text{so}\qquad
\big[\hat{\vec A},\hat n\cdot\hat{\vec J}\,\big]=i\hbar\,(\hat n\times\hat{\vec A}).
$$

In components, $(\hat n\times\hat{\vec A})_\ell=\epsilon_{\ell mn}\,n_m\hat A_n$.

!!! thm "Vector Operator"

    $$
    \big[\hat A_\ell,\hat n\cdot\hat{\vec J}\,\big]=i\hbar\,\epsilon_{\ell mn}\,n_m\hat A_n .
    $$

## 20.4 The Cartesian Commutation Relations

Take $\ell=1$. The left side is $n_1[\hat A_1,\hat J_1]+n_2[\hat A_1,\hat J_2]+n_3[\hat A_1,\hat J_3]$, and the right side is

$$
i\hbar\,\epsilon_{1mn}n_m\hat A_n=i\hbar\,\epsilon_{123}n_2\hat A_3+i\hbar\,\epsilon_{132}n_3\hat A_2=i\hbar\,n_2\hat A_3-i\hbar\,n_3\hat A_2 .
$$

The vector $\hat n$ is arbitrary, so equating the coefficients of $n_1,n_2,n_3$ and then cycling the indices gives:

!!! thm "Defining Commutators of a Vector Operator"

    \begin{gather*}
    [\hat A_x,\hat J_x]=[\hat A_y,\hat J_y]=[\hat A_z,\hat J_z]=0,\\
    [\hat A_x,\hat J_y]=i\hbar\hat A_z,\qquad[\hat A_y,\hat J_z]=i\hbar\hat A_x,\qquad[\hat A_z,\hat J_x]=i\hbar\hat A_y .
    \end{gather*}

**Check with $\hat{\vec A}=\hat{\vec J}$:** $[\hat J_1,\hat J_2]=i\hbar\hat J_3$ and $[\hat J_1,\hat J_3]=-i\hbar\hat J_2$. This reproduces the angular momentum algebra, so $\hat{\vec J}$ itself is a vector operator. This is a consistency check on the definition: the algebra derived from rotations in Part II is the statement that the generators transform like a vector.

## 20.5 Spherical Components of a Vector Operator

Define $\hat A_\pm=\hat A_x\pm i\hat A_y$. From the identities,

$$
[\hat J_x,\hat A_\pm]=[\hat J_x,\hat A_x]\pm i[\hat J_x,\hat A_y]=\pm i\,(i\hbar\hat A_z)=\mp\hbar\hat A_z .
$$

!!! thm "Spherical Components"

    $$
    \hat A_{\pm1}=\mp\frac1{\sqrt2}\big(\hat A_x\pm i\hat A_y\big),\qquad \hat A_0=\hat A_z .
    $$

For the position vector $\vec r=r_1\hat e_1+r_2\hat e_2+r_3\hat e_3$ with $r_1=x=r\sin\theta\cos\phi$, $r_2=y=r\sin\theta\sin\phi$, $r_3=z=r\cos\theta$, the spherical components are proportional to the $\ell=1$ spherical harmonics:

\begin{align*}
r^{(1)}_{+1}&=-\tfrac1{\sqrt2}(x+iy)=-\tfrac1{\sqrt2}\,r\sin\theta\,e^{i\phi}=r\sqrt{\tfrac{4\pi}3}\,Y^{(1)}_{+1}(\theta,\phi),\\
r^{(1)}_{-1}&=\ \ \tfrac1{\sqrt2}(x-iy)=\ \ \tfrac1{\sqrt2}\,r\sin\theta\,e^{-i\phi}=r\sqrt{\tfrac{4\pi}3}\,Y^{(1)}_{-1}(\theta,\phi),\\
r^{(1)}_{0}&=z=r\cos\theta=r\sqrt{\tfrac{4\pi}3}\,Y^{(1)}_{0}(\theta,\phi).
\end{align*}

Here $r^{(1)}_q$ with $q=-1,0,1$ is the notation used from now on, where the superscript $(1)$ is the rank and the subscript $q$ labels the component. Here $Y^{(1)}_q\equiv Y_{1q}$.

!!! verification "Verification"

    Using $Y_{1,\pm1}=\mp\sqrt{3/8\pi}\sin\theta\,e^{\pm i\phi}$ and $Y_{10}=\sqrt{3/4\pi}\cos\theta$ from the earlier notes, $r\sqrt{4\pi/3}\,Y_{1,\pm1}=\mp\tfrac r{\sqrt2}\sin\theta\,e^{\pm i\phi}$, in agreement with the first two lines.

!!! solution "Complete Solution"

    The spherical components have simple commutators with $\hat J_z$. From the identities, $[\hat J_z,\hat A_x]=i\hbar\hat A_y$ and $[\hat J_z,\hat A_y]=-i\hbar\hat A_x$, so

    $$
    [\hat J_z,\hat A_\pm]=i\hbar\hat A_y\pm i(-i\hbar\hat A_x)=\pm\hbar\big(\hat A_x\pm i\hat A_y\big)=\pm\hbar\hat A_\pm,\qquad[\hat J_z,\hat A_0]=0 .
    $$

Hence $[\hat J_z,\hat A_q]=\hbar q\,\hat A_q$ for $q=-1,0,1$. Similarly $[\hat J_+,\hat A_z]=[\hat J_x,\hat A_z]+i[\hat J_y,\hat A_z]=-i\hbar\hat A_y+i(i\hbar\hat A_x)=-\hbar\hat A_+=\sqrt2\,\hbar\,\hat A_{+1}$. These are exactly the pattern that defines an irreducible tensor of rank one ([Section 22](22-irreducible-tensor-operators-their-commutation-relations.md)).
