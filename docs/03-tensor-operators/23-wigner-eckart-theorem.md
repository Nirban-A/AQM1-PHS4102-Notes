---
title: "The Wigner-Eckart Theorem"
part: 3
chapter: 23
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 23 The Wigner-Eckart Theorem

## 23.1 Idea of the Derivation

The matrix elements $\langle j',m'|\hat T^{(k)}_q|j,m\rangle$ obey the linear recursion (A) of [Section 22](22-irreducible-tensor-operators-their-commutation-relations.md). The Clebsch-Gordan coefficients for coupling the angular momenta $j$ and $k$ into $j'$ obey a recursion of the same form. If two sets of numbers satisfy the same homogeneous recursion, they are proportional. The proportionality constant cannot depend on $m,q,m'$, which is the content of the theorem.

## 23.2 Coupling $j$ and $k$

Consider the product states $|j,m,k,q\rangle=|j,m\rangle\otimes|k,q\rangle$, and couple $j$ with $k$ to a total $j'$ (any value allowed by the triangle rule $|j-k|\le j'\le j+k$). The conservation $m'=m+q$ holds, and

$$
|j',m'\rangle=\sum_{m,q}\langle j,m,k,q|j',m'\rangle\,|j,m,k,q\rangle\equiv\sum_{m,q}C(j,k,j'\,|\,m,q,m')\,|j,m,k,q\rangle .
$$

Apply the total lowering operator $\hat J_-'=\hat J_-+\hat K_-$, where $\hat K_-$ acts on the $|k,q\rangle$ part. The left side is

\begin{align*}
\hat J_-'|j',m'\rangle&=\hbar\sqrt{(j'+m')(j'-m'+1)}\,|j',m'-1\rangle\\
&=\hbar\sqrt{(j'+m')(j'-m'+1)}\sum_{m,q}C(jkj'|m,q,m'-1)\,|j,m,k,q\rangle ,
\end{align*}

and the right side is

$$
\sum_{m,q}C(jkj'|m,q,m')\Big[\hbar\sqrt{(j+m)(j-m+1)}\,|j,m-1,k,q\rangle+\hbar\sqrt{(k+q)(k-q+1)}\,|j,m,k,q-1\rangle\Big].
$$

In the first term replace $m\to m+1$ and in the second $q\to q+1$, so that all kets read $|j,m,k,q\rangle$ (labelled (B) and (B$'$) in the notes). The kets are linearly independent, so their coefficients must match:

!!! thm "Recursion for the Clebsch-Gordan Coefficients"

    \begin{align*}
    \sqrt{(j'+m')(j'-m'+1)}\ C(jkj'|m,q,m'-1)&=\sqrt{(j+m+1)(j-m)}\ C(jkj'|m+1,q,m')\\
    &\quad+\sqrt{(k+q+1)(k-q)}\ C(jkj'|m,q+1,m').\tag{C}
    \end{align*}

## 23.3 Comparison with the Tensor Recursion

Place (A) and (C) side by side. They are identical in form under the correspondence

\begin{gather*}
\langle j',m'-1|\hat T^{(k)}_q|j,m\rangle\leftrightarrow C(jkj'|m,q,m'-1),\\
\langle j',m'|\hat T^{(k)}_q|j,m+1\rangle\leftrightarrow C(jkj'|m+1,q,m'),\\
\langle j',m'|\hat T^{(k)}_{q+1}|j,m\rangle\leftrightarrow C(jkj'|m,q+1,m').
\end{gather*}

Therefore

$$
\langle j',m'|\hat T^{(k)}_q|j,m\rangle\ \propto\ C(jkj'|m,q,m').
$$

!!! studynote "Study Note"

    The notebook states “we can take $j'=j+k$” before building $|j',m'\rangle$. Nothing in the argument depends on that choice: relation (C) holds for each allowed $j'$ separately, and the proportionality constant is allowed to depend on $j,j',k$ (and on any other labels such as $n$), but not on $m,q,m'$.

!!! thm "Wigner-Eckart Theorem"

    $$
    \boxed{\ \langle j',m'|\hat T^{(k)}_q|j,m\rangle=\langle j'\|\hat T^{(k)}\|j\rangle\ \cdot\ C(jkj'|m,q,m')\ }
    $$

    The first factor, the **reduced matrix element**, is the *dynamical factor*: it depends on the operator and the physical system but not on $m,q,m'$. The second factor, the Clebsch-Gordan coefficient, is the *geometric factor*: it depends only on the rotational symmetry.

## 23.4 Notations

The Clebsch-Gordan coefficient appears in the notes in several forms,

$$
C(jkj'|m,q,m')\ \equiv\ C^{\,j'm'}_{\,jm,\,kq}\ \equiv\ \begin{pmatrix}j&k&j'\\m&q&m'\end{pmatrix}.
$$

!!! studynote "Study Note"

    The last symbol (the Wigner $3j$ symbol) is closely related to the Clebsch-Gordan coefficient but not identical: it differs by a normalisation factor $\sqrt{2j'+1}$ and a phase, so reduced matrix elements quoted with a $3j$ symbol differ from those used here by that factor. Always check which convention a formula uses.

## 23.5 Consequences

1.  **Magnetic selection rule:** $m'=m+q$.

2.  **Triangle selection rule:** $\langle j',m'|\hat T^{(k)}_q|j,m\rangle=0$ unless $|j-k|\le j'\le j+k$, since otherwise the Clebsch-Gordan coefficient vanishes.

3.  **Fixed ratios:** within a pair of multiplets $(j,j')$, the ratio of any two matrix elements of $\hat T^{(k)}_q$ equals the ratio of two Clebsch-Gordan coefficients, regardless of the physics inside the reduced element.

## 23.6 Scalar Operators

For a scalar operator $k=0$ and $q=0$. The coupling $j\otimes0$ gives only $j'=j$, $m'=m$, so

$$
C(j,0,j'|m,0,m')=\delta_{jj'}\delta_{mm'},
$$

and

$$
\langle j',m'|\hat T^{(0)}_0|j,m\rangle=\delta_{jj'}\delta_{mm'}\,\langle j'\|\hat T^{(0)}\|j\rangle .
$$

!!! thm "Scalar Operator Matrix Elements"

    A scalar operator is diagonal in $j$ and $m$, and its diagonal element does not depend on $m$.

This agrees with [Section 20](20-scalar-vector-operators.md): $[\hat A,\hat{\vec J}\,]=0$ means $\hat A$ cannot change $j$ or $m$.
