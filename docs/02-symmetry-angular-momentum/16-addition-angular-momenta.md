---
title: "Addition of Angular Momenta"
part: 2
chapter: 16
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 16 Addition of Angular Momenta

## 16.1 Two Angular Momenta

Consider two angular momenta $\hat{\vec J}_1,\hat{\vec J}_2$ whose components belong to two different subspaces. They arise either from two different particles, or from the same system carrying two different angular momenta (such as $\hat{\vec L}+\hat{\vec S}$). Each obeys the algebra,

$$
[\hat J_{1x},\hat J_{1y}]=i\hbar\hat J_{1z},\ \dots\qquad [\hat J_{2x},\hat J_{2y}]=i\hbar\hat J_{2z},\ \dots\qquad [\hat J_{1j},\hat J_{2k}]=0\ \ (j,k=x,y,z),
$$

the last because they act on different subspaces.

## 16.2 The Uncoupled (Product) Basis

The operators $\hat J_1^2,\hat J_{1z},\hat J_2^2,\hat J_{2z}$ all commute, so they have simultaneous eigenstates. Separately,

$$
\hat J_1^2|j_1,m_1\rangle=\hbar^2j_1(j_1+1)|j_1,m_1\rangle,\ \ \hat J_{1z}|j_1,m_1\rangle=\hbar m_1|j_1,m_1\rangle\quad\big[(2j_1+1)\text{-dim.\ space}\big],
$$

and similarly for $\hat J_2$ on a $(2j_2+1)$-dimensional space. The composite eigenstates are tensor products:

!!! thm "Composite (Uncoupled) Basis"

    $$
    |j_1,j_2,m_1,m_2\rangle\equiv|j_1,m_1\rangle\otimes|j_2,m_2\rangle,\qquad\text{a }(2j_1+1)(2j_2+1)\text{-dimensional space,}
    $$

    \begin{gather*}
    \hat J_1^2|j_1,j_2,m_1,m_2\rangle=\hbar^2j_1(j_1+1)|\dots\rangle,\quad \hat J_{1z}|\dots\rangle=\hbar m_1|\dots\rangle,\\
    \hat J_2^2|\dots\rangle=\hbar^2j_2(j_2+1)|\dots\rangle,\quad \hat J_{2z}|\dots\rangle=\hbar m_2|\dots\rangle,\\
    \sum_{m_1=-j_1}^{j_1}\sum_{m_2=-j_2}^{j_2}|j_1,j_2,m_1,m_2\rangle\langle j_1,j_2,m_1,m_2|=\mathbb 1,\\
    \langle j_1',j_2',m_1',m_2'|j_1,j_2,m_1,m_2\rangle=\delta_{j_1'j_1}\delta_{j_2'j_2}\delta_{m_1'm_1}\delta_{m_2'm_2}.
    \end{gather*}

    Here $j_1,j_2$ are fixed for the problem and only $m_1,m_2$ vary.

The ladder operators act as $\hat J_{1\pm}|j_1,j_2,m_1,m_2\rangle=\hbar\sqrt{(j_1\mp m_1)(j_1\pm m_1+1)}\,|j_1,j_2,m_1\pm1,m_2\rangle$, and similarly for $\hat J_{2\pm}$.

## 16.3 Total Angular Momentum

Define

$$
\hat{\vec J}=\hat{\vec J}_1+\hat{\vec J}_2,\qquad \hat J_z=\hat J_{1z}+\hat J_{2z},\qquad [\hat J_x,\hat J_y]=i\hbar\hat J_z .
$$

$\hat J^2,\hat J_z$ are the *total* (composite) operators, and $\hat J_1^2,\hat J_2^2,\hat J_{1z},\hat J_{2z}$ the separate ones. Expand

$$
\hat J^2=(\hat{\vec J}_1+\hat{\vec J}_2)^2=\hat J_1^2+\hat J_2^2+2\hat{\vec J}_1\cdot\hat{\vec J}_2=\hat J_1^2+\hat J_2^2+2\hat J_{1z}\hat J_{2z}+2\big(\hat J_{1x}\hat J_{2x}+\hat J_{1y}\hat J_{2y}\big).
$$

To express the last bracket by ladder operators,

\begin{align*}
\hat J_{1+}\hat J_{2-}&=(\hat J_{1x}+i\hat J_{1y})(\hat J_{2x}-i\hat J_{2y})=\hat J_{1x}\hat J_{2x}+\hat J_{1y}\hat J_{2y}-i(\hat J_{1x}\hat J_{2y}-\hat J_{1y}\hat J_{2x}),\\
\hat J_{1-}\hat J_{2+}&=\hat J_{1x}\hat J_{2x}+\hat J_{1y}\hat J_{2y}+i(\hat J_{1x}\hat J_{2y}-\hat J_{1y}\hat J_{2x}),
\end{align*}

so that $\hat J_{1+}\hat J_{2-}+\hat J_{1-}\hat J_{2+}=2(\hat J_{1x}\hat J_{2x}+\hat J_{1y}\hat J_{2y})$.

!!! thm "Total $\hat J^2$ in Terms of Separate Operators"

    $$
    \hat J^2=\hat J_1^2+\hat J_2^2+2\hat J_{1z}\hat J_{2z}+\hat J_{1+}\hat J_{2-}+\hat J_{1-}\hat J_{2+}.
    $$

!!! studynote "Study Note"

    The cross terms $\hat J_{1+}\hat J_{2-}$ and $\hat J_{1-}\hat J_{2+}$ change $m_1$ and $m_2$ in opposite directions, and are the reason that $\hat J^2$ is not diagonal in the product basis.

## 16.4 Commutation Relations and the Coupled Basis

$$
[\hat J^2,\hat J_1^2]=0,\quad[\hat J^2,\hat J_2^2]=0,\quad[\hat J^2,\hat J_z]=0,\qquad\text{but}\qquad [\hat J^2,\hat J_{1z}]\neq0,\quad[\hat J^2,\hat J_{2z}]\neq0 .
$$

Hence $\{\hat J^2,\hat J_z,\hat J_1^2,\hat J_2^2\}$ is a second commuting set of operators, with new (coupled) basis states.

!!! thm "Coupled Basis"

    \begin{gather*}
    \hat J_1^2|j_1,j_2,j,m\rangle=\hbar^2j_1(j_1+1)|\dots\rangle,\qquad \hat J_2^2|j_1,j_2,j,m\rangle=\hbar^2j_2(j_2+1)|\dots\rangle,\\
    \hat J^2|j_1,j_2,j,m\rangle=\hbar^2j(j+1)|\dots\rangle,\qquad \hat J_z|j_1,j_2,j,m\rangle=\hbar m|\dots\rangle,\qquad m=-j,\dots,j,\\
    \sum_j\sum_m|j,m\rangle\langle j,m|=\mathbb 1,\qquad \langle j',m'|j,m\rangle=\delta_{jj'}\delta_{mm'},\qquad |j_1,j_2,j,m\rangle\equiv|j,m\rangle .
    \end{gather*}

    Now $j$ is not fixed (it varies) while $j_1,j_2$ stay fixed. The dimension of the space is $(2j_1+1)(2j_2+1)$ in either basis.

## 16.5 The Clebsch-Gordan Transformation

Insert the completeness relation of the product basis in front of $|j,m\rangle$:

$$
|j,m\rangle=\sum_{m_1=-j_1}^{j_1}\sum_{m_2=-j_2}^{j_2}\underbrace{\langle j_1,j_2,m_1,m_2|j,m\rangle}_{\text{C-G coefficients}}\ |j_1,j_2,m_1,m_2\rangle .
$$

The notation $\langle j_1,j_2,m_1,m_2|j,m\rangle\equiv\begin{pmatrix}j_1&j_2&j\\m_1&m_2&m\end{pmatrix}$ is also used. With the standard phase convention (fixed in [Section 17](17-clebsch-gordan-tables.md)) the coefficients are *real*, so $\langle j,m|j_1,j_2,m_1,m_2\rangle=\langle j_1,j_2,m_1,m_2|j,m\rangle$.

!!! thm "Orthogonality Relations"

    Unitarity of the change of basis ($\langle j',m'|j,m\rangle=\delta_{jj'}\delta_{mm'}$ and the completeness of the product basis) gives

    \begin{gather*}
    \sum_{m_1,m_2}\langle j_1,j_2,m_1,m_2|j',m'\rangle\langle j_1,j_2,m_1,m_2|j,m\rangle=\delta_{jj'}\delta_{mm'},\\
    \sum_{j,m}\langle j_1,j_2,m_1',m_2'|j,m\rangle\langle j_1,j_2,m_1,m_2|j,m\rangle=\delta_{m_1'm_1}\delta_{m_2'm_2}.
    \end{gather*}

    In particular $\displaystyle\sum_{m_1,m_2}\langle j_1,j_2,m_1,m_2|j,m\rangle^2=1$ and $\displaystyle\sum_{j,m}\langle j_1,j_2,m_1,m_2|j,m\rangle^2=1$.

## 16.6 Selection Rules

!!! thm "$m$ Selection Rule"

    $\langle j_1,j_2,m_1,m_2|j,m\rangle$ vanishes unless $m=m_1+m_2$.

!!! solution "Complete Solution"

    Since $\hat J_z=\hat J_{1z}+\hat J_{2z}$,

    $$
    \langle j_1,j_2,m_1,m_2|\hat J_z-\hat J_{1z}-\hat J_{2z}|j,m\rangle=0\ \Rightarrow\ \hbar(m-m_1-m_2)\langle j_1,j_2,m_1,m_2|j,m\rangle=0 ,
    $$

    so either the coefficient vanishes or $m=m_1+m_2$.

## 16.7 Allowed Values of $j$

The largest $m$ is $(m_1)_{\max}+(m_2)_{\max}=j_1+j_2$, and $|m|\le j$, so

$$
j_{\max}=j_1+j_2 .
$$

To find $j_{\min}$ count the states: the total number of $|j,m\rangle$ states must equal the number of product states,

$$
\sum_{j=j_{\min}}^{j_{\max}}(2j+1)=(2j_1+1)(2j_2+1).
$$

The sum is $(2j_{\min}+1)+(2j_{\min}+3)+\cdots+(2j_{\max}+1)$, an arithmetic series with $j_{\max}-j_{\min}+1$ terms, so adding the series to itself reversed,

$$
2S=2\big[(j_1+j_2+1)+j_{\min}\big]\big[j_1+j_2-j_{\min}+1\big]\ \Rightarrow\ S=\big[(j_1+j_2+1)+j_{\min}\big]\big[(j_1+j_2+1)-j_{\min}\big].
$$

Setting $S=(2j_1+1)(2j_2+1)$ and expanding, $(j_1+j_2+1)^2-j_{\min}^2=4j_1j_2+2j_1+2j_2+1$, which simplifies to $j_{\min}^2=(j_1-j_2)^2$.

!!! thm "Triangle Rule"

    $$
    j_{\min}=|j_1-j_2|,\qquad\text{so}\qquad |j_1-j_2|\le j\le j_1+j_2,\qquad j\ \text{in integer steps.}
    $$

Together with $m=m_1+m_2$, these two conditions comprise the selection rules for C-G coefficients.

!!! prob "Example: $j_1=\tfrac12,\ j_2=1$"

    !!! solution "Complete Solution"

        $m_1=\pm\tfrac12$ and $m_2=-1,0,1$ give a $2\times3=6$ dimensional space. The total angular momentum takes $j_{\max}=\tfrac32$ (a 4-dimensional block with $m=\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$) and $j_{\min}=|j_1-j_2|=\tfrac12$ (a 2-dimensional block with $m=\pm\tfrac12$). The dimensions match: $6=4\oplus2$.

!!! intuition "Intuition"

    Think of the vector model: two vectors of lengths $\sqrt{j_1(j_1+1)}\hbar$ and $\sqrt{j_2(j_2+1)}\hbar$ can add to a resultant of length anywhere from $|j_1-j_2|$ (antiparallel) to $j_1+j_2$ (parallel), in quantised integer steps. That is the triangle rule.
