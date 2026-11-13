---
title: "Angular Momentum: Eigenvalues and Ladder Operators"
part: 2
chapter: 11
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 11 Angular Momentum: Eigenvalues and Ladder Operators

## 11.1 $\hat J^2$ and Simultaneous Eigenstates

Define

$$
\hat J^2=\hat J_x^2+\hat J_y^2+\hat J_z^2,\qquad [\hat J^2,\hat J_x]=[\hat J^2,\hat J_y]=[\hat J^2,\hat J_z]=0 .
$$

Hence $\hat J^2$ and $\hat J_z$ have simultaneous eigenstates $|\alpha,\beta\rangle$:

$$
\hat J^2|\alpha,\beta\rangle=\hbar^2\alpha\,|\alpha,\beta\rangle,\qquad \hat J_z|\alpha,\beta\rangle=\hbar\beta\,|\alpha,\beta\rangle,\qquad \langle\alpha',\beta'|\alpha,\beta\rangle=\delta_{\alpha\alpha'}\delta_{\beta\beta'} .
$$

## 11.2 Ladder Operators

Define $\hat J_\pm=\hat J_x\pm i\hat J_y$, so that $\hat J_x=\tfrac12(\hat J_++\hat J_-)$, $\hat J_y=\tfrac1{2i}(\hat J_+-\hat J_-)$ and $\hat J_\pm^\dagger=\hat J_\mp$.

!!! thm "Ladder Operator Commutators"

    $$
    [\hat J^2,\hat J_\pm]=0,\qquad [\hat J_+,\hat J_-]=2\hbar\hat J_z,\qquad [\hat J_z,\hat J_\pm]=\pm\hbar\hat J_\pm .
    $$

!!! solution "Complete Solution"

    For the last one,

    $$
    [\hat J_z,\hat J_+]=[\hat J_z,\hat J_x]+i[\hat J_z,\hat J_y]=i\hbar\hat J_y+i(-i\hbar\hat J_x)=\hbar(\hat J_x+i\hat J_y)=\hbar\hat J_+ ,
    $$

    and the minus case is the adjoint. For the commutator $[\hat J_+,\hat J_-]$ use the products

    \begin{align*}
    \hat J_+\hat J_-&=(\hat J_x+i\hat J_y)(\hat J_x-i\hat J_y)=\hat J_x^2+\hat J_y^2+\hbar\hat J_z=\hat J^2-\hat J_z^2+\hbar\hat J_z,\tag{1}\\
    \hat J_-\hat J_+&=\hat J^2-\hat J_z^2-\hbar\hat J_z.\tag{2}
    \end{align*}

Subtracting gives $2\hbar\hat J_z$, and adding gives $\hat J^2=\tfrac12(\hat J_+\hat J_-+\hat J_-\hat J_+)+\hat J_z^2$.

Also, $\hat J_x^2=\tfrac14[\hat J_+^2+\hat J_-^2+\hat J_+\hat J_-+\hat J_-\hat J_+]$ and $\hat J_y^2=-\tfrac14[\hat J_+^2+\hat J_-^2-\hat J_+\hat J_--\hat J_-\hat J_+]$.

## 11.3 What the Ladder Operators Do

Using $[\hat J_z,\hat J_\pm]=\pm\hbar\hat J_\pm$,

$$
\hat J_z\hat J_\pm|\alpha,\beta\rangle=(\pm\hbar\hat J_\pm+\hat J_\pm\hat J_z)|\alpha,\beta\rangle=\hbar(\beta\pm1)\hat J_\pm|\alpha,\beta\rangle ,
$$

and since $\hat J^2$ commutes with $\hat J_\pm$, $\hat J^2\hat J_\pm|\alpha,\beta\rangle=\hbar^2\alpha\,\hat J_\pm|\alpha,\beta\rangle$. So $\hat J_\pm$ leave $\alpha$ alone and shift $\beta$ by $\pm1$:

$$
\hat J_\pm|\alpha,\beta\rangle=c^{\pm}_{\alpha\beta}\,|\alpha,\beta\pm1\rangle .
$$

## 11.4 Bounds and Spectrum

Since $\hat J^2-\hat J_z^2=\hat J_x^2+\hat J_y^2\ge0$,

$$
\langle\alpha,\beta|\hat J^2-\hat J_z^2|\alpha,\beta\rangle=\hbar^2(\alpha-\beta^2)\ge0\quad\Longrightarrow\quad\alpha\ge\beta^2 .
$$

So for a fixed $\alpha$ there is a maximum $\beta_{\max}$, and the ladder must terminate: $\hat J_+|\alpha,\beta_{\max}\rangle=0$. Applying $\hat J_-$ and using (2):

$$
\hat J_-\hat J_+|\alpha,\beta_{\max}\rangle=0\ \Rightarrow\ (\hat J^2-\hat J_z^2-\hbar\hat J_z)|\alpha,\beta_{\max}\rangle=0\ \Rightarrow\ \alpha=\beta_{\max}(\beta_{\max}+1).
$$

Likewise there is a minimum with $\hat J_-|\alpha,\beta_{\min}\rangle=0$, and using (1):

$$
\hat J_+\hat J_-|\alpha,\beta_{\min}\rangle=0\ \Rightarrow\ \alpha=\beta_{\min}(\beta_{\min}-1).
$$

Equating the two expressions for $\alpha$:

$$
\beta_{\max}^2+\beta_{\max}=\beta_{\min}^2-\beta_{\min}\quad\Longrightarrow\quad \beta_{\min}=-\beta_{\max}.
$$

Applying $\hat J_-$ a total of $n$ times to $|\alpha,\beta_{\max}\rangle$ reaches $|\alpha,\beta_{\min}\rangle$, so $\beta_{\max}=\beta_{\min}+n$, hence $\beta_{\max}=n/2\equiv j$. Writing $\beta\equiv m$ and $\alpha=j(j+1)$:

!!! thm "Angular Momentum Spectrum"

    \begin{gather*}
    \hat J^2|j,m\rangle=\hbar^2j(j+1)|j,m\rangle,\qquad \hat J_z|j,m\rangle=\hbar m|j,m\rangle,\\
    -j\le m\le j\ \ (\text{steps of }1),\qquad j=0,\tfrac12,1,\tfrac32,\dots,\qquad \langle j',m'|j,m\rangle=\delta_{jj'}\delta_{mm'}.
    \end{gather*}

    Each $j$ is $(2j+1)$-fold degenerate. For $j=1$, $m=-1,0,1$ (three-fold degenerate).

!!! studynote "Study Note"

    Because $n=2j$ is an integer, $j$ can be half-integer, and the algebra alone does not forbid it. For *orbital* angular momentum single-valuedness of the wavefunction restricts $\ell$ to integers (see [Section 15](15-orbital-angular-momentum-spherical-harmonics.md)); half-integers appear only for spin.

## 11.5 Matrix Elements of the Ladder Operators

Write $\hat J_+|j,m\rangle=c^+_{jm}|j,m+1\rangle$. Then $\langle j,m|\hat J_+^\dagger\hat J_+|j,m\rangle=|c^+_{jm}|^2$ with $\hat J_+^\dagger=\hat J_-$, and by (2),

$$
|c^+_{jm}|^2=\langle j,m|\hat J^2-\hat J_z^2-\hbar\hat J_z|j,m\rangle=\hbar^2\big[j(j+1)-m^2-m\big]=\hbar^2\big[j(j+1)-m(m+1)\big].
$$

The case of $\hat J_-$ follows from (1). Choosing the phases real and positive:

!!! thm "Action of $\hat J_\pm$"

    $$
    \hat J_\pm|j,m\rangle=\hbar\sqrt{j(j+1)-m(m\pm1)}\;|j,m\pm1\rangle=\hbar\sqrt{(j\mp m)(j\pm m+1)}\;|j,m\pm1\rangle .
    $$

!!! verification "Verification"

    Both forms agree, since $j(j+1)-m(m\pm1)=(j\mp m)(j\pm m+1)$. At the ends of the ladder the square root vanishes ($m=j$ for $\hat J_+$, $m=-j$ for $\hat J_-$), as it must.

The cases $j=0$ ($|0,0\rangle$), $j=\tfrac12$ ($|\tfrac12,\pm\tfrac12\rangle$), and so on, give the representations in the following sections.
