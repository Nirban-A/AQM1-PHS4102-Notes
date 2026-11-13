---
title: "Clebsch-Gordan Tables"
part: 2
chapter: 17
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 17 Clebsch-Gordan Tables

## 17.1 Construction Strategy

The recipe, used in both examples below, is:

1.  Start from the top state $|j_{\max},j_{\max}\rangle$, which has a single term in the product basis ($m_1=j_1$, $m_2=j_2$).

2.  Fix its phase by the **sign convention** $\langle j_1,j_2,j_1,(j-j_1)|j,j\rangle$ real and positive.

3.  Apply $\hat J_-=\hat J_{1-}+\hat J_{2-}$ repeatedly to get the other $m$ values of $j_{\max}$.

4.  For the next $j$, find the state with $m=j$ orthogonal to the one already built, fix its sign by the convention, and lower again.

## 17.2 Spin-$\tfrac12\otimes$ Spin-$\tfrac12$

Here $j_1=j_2=\tfrac12$, the space is $2\times2=4$ dimensional, and $|j_1-j_2|=0\le j\le1$: $m=0$ for $j=0$ (dim 1) and $m=1,0,-1$ for $j=1$ (dim 3), with total dimension $3\oplus1=4$. The $j=1$ states are the *spin triplet* and the $j=0$ state is the *spin singlet*.

Use the notation $|m_1,m_2\rangle\equiv|\tfrac12,\tfrac12,m_1,m_2\rangle$. The top state $|1,1\rangle$ contains only $m_1=m_2=\tfrac12$, so $\langle\tfrac12\tfrac12\tfrac12\tfrac12|1,1\rangle^2=1$, and by the sign convention

$$
|1,1\rangle=|\tfrac12,\tfrac12\rangle .
$$

Lower with $\hat J_-|j,m\rangle=\hbar\sqrt{(j+m)(j-m+1)}\,|j,m-1\rangle$ and $\hat J_-=\hat J_{1-}+\hat J_{2-}$:

$$
\hat J_-|1,1\rangle=\hbar\sqrt2\,|1,0\rangle=\hbar\big(|-\tfrac12,\tfrac12\rangle+|\tfrac12,-\tfrac12\rangle\big)\ \Rightarrow\ |1,0\rangle=\tfrac1{\sqrt2}|\tfrac12,-\tfrac12\rangle+\tfrac1{\sqrt2}|-\tfrac12,\tfrac12\rangle .
$$

Lowering once more,

$$
\hat J_-|1,0\rangle=\hbar\sqrt2\,|1,-1\rangle=\tfrac\hbar{\sqrt2}\big(|-\tfrac12,-\tfrac12\rangle+|-\tfrac12,-\tfrac12\rangle\big)\ \Rightarrow\ |1,-1\rangle=|-\tfrac12,-\tfrac12\rangle .
$$

For the singlet write $|0,0\rangle=a|\tfrac12,-\tfrac12\rangle+b|-\tfrac12,\tfrac12\rangle$. Orthogonality to $|1,0\rangle$ gives $\tfrac a{\sqrt2}+\tfrac b{\sqrt2}=0$, normalisation gives $a^2+b^2=1$, and the sign convention $\langle\tfrac12\tfrac12\tfrac12,-\tfrac12|0,0\rangle>0$ gives $a>0$. Hence $a=\tfrac1{\sqrt2}$, $b=-\tfrac1{\sqrt2}$.

!!! thm "C-G Table for $\tfrac12\otimes\tfrac12$ (Triplet and Singlet)"

    $$
    \begin{array}{c|cccc}
    (m_1,m_2)\ \backslash\ (j,m) & (1,1) & (1,0) & (0,0) & (1,-1) \\
    \hline (\tfrac12,\tfrac12) & 1 & 0 & 0 & 0 \\
    (\tfrac12,-\tfrac12) & 0 & \tfrac1{\sqrt2} & \tfrac1{\sqrt2} & 0 \\
    (-\tfrac12,\tfrac12) & 0 & \tfrac1{\sqrt2} & -\tfrac1{\sqrt2} & 0 \\
    (-\tfrac12,-\tfrac12) & 0 & 0 & 0 & 1
    \end{array}
    $$

    $$
    |1,1\rangle=|\!\uparrow\uparrow\rangle,\quad |1,0\rangle=\tfrac1{\sqrt2}\big(|\!\uparrow\downarrow\rangle+|\!\downarrow\uparrow\rangle\big),\quad |1,-1\rangle=|\!\downarrow\downarrow\rangle,\quad |0,0\rangle=\tfrac1{\sqrt2}\big(|\!\uparrow\downarrow\rangle-|\!\downarrow\uparrow\rangle\big).
    $$

The transformation matrix is block diagonal, with a $1\times1$ block for each of $m=\pm1$ and a $2\times2$ block for $m=0$. It is an *orthogonal* matrix since the coefficients are real and the change of basis is unitary.

!!! studynote "Study Note"

    The notebook’s table has the $|1,0\rangle$ and $|0,0\rangle$ columns in the $2\times2$ block, with $\tfrac1{\sqrt2},\tfrac1{\sqrt2}$ and $\tfrac1{\sqrt2},-\tfrac1{\sqrt2}$ down the rows $(\tfrac12,-\tfrac12)$ and $(-\tfrac12,\tfrac12)$, exactly as above. The triplet is symmetric under interchange of the two spins and the singlet is antisymmetric.

## 17.3 Spin-$1\otimes$ Spin-$\tfrac12$

This is the example the notebook sets up with $j_1=1$ ($m_1=1,0,-1$) and $j_2=\tfrac12$ ($m_2=\pm\tfrac12$): a 6-dimensional space with $j=\tfrac32$ ($m=\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$) and $j=\tfrac12$ ($m=\pm\tfrac12$). The table in the notebook is left empty; it is completed here. Write $|m_1,m_2\rangle$ for $|1,\tfrac12,m_1,m_2\rangle$.

!!! solution "Complete Solution"

    **Step 1.** $|\tfrac32,\tfrac32\rangle=|1,\tfrac12\rangle$ (sign convention).

**Step 2.** Lower: $\hat J_-|\tfrac32,\tfrac32\rangle=\hbar\sqrt3\,|\tfrac32,\tfrac12\rangle$, and $\hat J_{1-}|1,1\rangle=\hbar\sqrt2|1,0\rangle$, $\hat J_{2-}|\tfrac12,\tfrac12\rangle=\hbar|\tfrac12,-\tfrac12\rangle$, so

$$
\sqrt3\,|\tfrac32,\tfrac12\rangle=\sqrt2\,|0,\tfrac12\rangle+|1,-\tfrac12\rangle\quad\Rightarrow\quad |\tfrac32,\tfrac12\rangle=\sqrt{\tfrac23}\,|0,\tfrac12\rangle+\sqrt{\tfrac13}\,|1,-\tfrac12\rangle .
$$

**Step 3.** The $j=\tfrac12$ state: $|\tfrac12,\tfrac12\rangle=a|1,-\tfrac12\rangle+b|0,\tfrac12\rangle$ is orthogonal to the one above, so $a\sqrt{\tfrac13}+b\sqrt{\tfrac23}=0$, with $a^2+b^2=1$. The convention $\langle j_1,j_2,j_1,(j-j_1)|j,j\rangle=\langle1,\tfrac12;1,-\tfrac12|\tfrac12,\tfrac12\rangle=a>0$ gives

$$
|\tfrac12,\tfrac12\rangle=\sqrt{\tfrac23}\,|1,-\tfrac12\rangle-\sqrt{\tfrac13}\,|0,\tfrac12\rangle .
$$

**Step 4.** Lower again: $\hat J_-|\tfrac32,\tfrac12\rangle=2\hbar|\tfrac32,-\tfrac12\rangle$, with $\hat J_-|1,-\tfrac12\rangle=\hbar\sqrt2\,|0,-\tfrac12\rangle$ and $\hat J_-|0,\tfrac12\rangle=\hbar\big(\sqrt2\,|-1,\tfrac12\rangle+|0,-\tfrac12\rangle\big)$:

$$
2|\tfrac32,-\tfrac12\rangle=\sqrt{\tfrac23}\big(\sqrt2|-1,\tfrac12\rangle+|0,-\tfrac12\rangle\big)+\sqrt{\tfrac13}\sqrt2|0,-\tfrac12\rangle\ \Rightarrow\ |\tfrac32,-\tfrac12\rangle=\sqrt{\tfrac23}\,|0,-\tfrac12\rangle+\sqrt{\tfrac13}\,|-1,\tfrac12\rangle .
$$

And $\hat J_-|\tfrac12,\tfrac12\rangle=\hbar|\tfrac12,-\tfrac12\rangle$ gives

$$
|\tfrac12,-\tfrac12\rangle=\sqrt{\tfrac13}\,|0,-\tfrac12\rangle-\sqrt{\tfrac23}\,|-1,\tfrac12\rangle,\qquad |\tfrac32,-\tfrac32\rangle=|-1,-\tfrac12\rangle .
$$

!!! thm "C-G Table for $1\otimes\tfrac12$"

    $$
    \begin{array}{c|cccccc}
    (m_1,m_2)\ \backslash\ (j,m) & (\tfrac32,\tfrac32) & (\tfrac32,\tfrac12) & (\tfrac12,\tfrac12) & (\tfrac32,-\tfrac12) & (\tfrac12,-\tfrac12) & (\tfrac32,-\tfrac32) \\
    \hline (1,\tfrac12) & 1 & 0 & 0 & 0 & 0 & 0 \\
    (1,-\tfrac12) & 0 & \sqrt{\tfrac13} & \sqrt{\tfrac23} & 0 & 0 & 0 \\
    (0,\tfrac12) & 0 & \sqrt{\tfrac23} & -\sqrt{\tfrac13} & 0 & 0 & 0 \\
    (0,-\tfrac12) & 0 & 0 & 0 & \sqrt{\tfrac23} & \sqrt{\tfrac13} & 0 \\
    (-1,\tfrac12) & 0 & 0 & 0 & \sqrt{\tfrac13} & -\sqrt{\tfrac23} & 0 \\
    (-1,-\tfrac12) & 0 & 0 & 0 & 0 & 0 & 1
    \end{array}
    $$

!!! verification "Verification"

    Each column has squared entries summing to $1$, each row has squared entries summing to $1$ (the two orthogonality relations), and the sign convention holds: the entry with $m_1=j_1$ in each $j$-column is positive. The numbers were also checked against a computer-algebra evaluation of the Clebsch-Gordan coefficients.

## 17.4 Properties of C-G Coefficients

!!! thm "Properties"

    1.  $\langle j_1,j_2,m_1,m_2|j,m\rangle$ is real.

    2.  $|j_1-j_2|\le j\le j_1+j_2$ (triangle rule).

    3.  $m_1+m_2=m$.

    4.  $\langle j_1,j_2,m_1=j_1,m_2=j-j_1|j,j\rangle$ is real and positive (sign convention).

    5.  $\langle j_1,j_2,m_1,m_2|j,m\rangle=(-1)^{\,j-j_1-j_2}\langle j_2,j_1,m_2,m_1|j,m\rangle$.

!!! verification "Verification (property v)"

    For the spin-$\tfrac12$ pair, the triplet has $j-j_1-j_2=0$, so the coefficient is unchanged on swapping the spins, while the singlet has $j-j_1-j_2=-1$ and changes sign, as in the table.

!!! examtip "Exam Tip"

    When building a table, check the three things the notes list: the $m$ rule (zeros off the blocks), the triangle rule (which columns exist), and the positive sign of the corner coefficient. Most sign errors come from the orthogonal partner state (the $j=\tfrac12$ states above).
