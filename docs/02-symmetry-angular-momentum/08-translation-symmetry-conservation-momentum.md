---
title: "Translation Symmetry and Conservation of Momentum"
part: 2
chapter: 8
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 8 Translation Symmetry and Conservation of Momentum

## 8.1 How States Transform Under a Translation

Let $\vec r$ be a dynamical variable. A translation by $\vec a$ moves a point according to

$$
\vec r'=\hat T(\vec a)\vec r=\vec r+\vec a,\qquad \vec r=\hat T(\vec a)^{-1}\vec r'=\vec r'-\vec a .
$$

The state vector transforms as $|\psi'\rangle=\hat U_T(\vec a)|\psi\rangle$. Because space is homogeneous, the value of the wavefunction is carried along with the point, so

$$
\psi'(\vec r')=\psi(\vec r)\quad\Longrightarrow\quad \hat U_T(\vec a)\psi(\vec r')=\psi\big(\hat T(\vec a)^{-1}\vec r'\big)=\psi(\vec r'-\vec a).
$$

Renaming the dummy variable gives the defining action

$$
\hat U_T(\vec a)\,\psi(\vec r)=\psi(\vec r-\vec a).
$$

## 8.2 The Generator of Translations

Take an infinitesimal translation $\delta\vec a$ and Taylor expand:

\begin{align*}
\hat U_T(\delta\vec a)\psi(\vec r)&=\psi(\vec r-\delta\vec a)=\psi(\vec r)-\delta\vec a\cdot\vec\nabla\psi(\vec r)\\
&=\psi(\vec r)-\frac{i}{\hbar}\,\delta\vec a\cdot\hat{\vec p}\,\psi(\vec r)=\Big[\mathbb 1-\frac i\hbar\,\delta\vec a\cdot\hat{\vec p}\Big]\psi(\vec r),
\end{align*}

using $\hat{\vec p}=-i\hbar\vec\nabla$.

!!! thm "Momentum Generates Translations"

    $$
    \hat U_T(\delta\vec a)=\mathbb 1-\frac i\hbar\,\delta\vec a\cdot\hat{\vec p}.
    $$

Build a finite translation from $n$ small ones, $\delta\vec a=\vec a/n$:

$$
\hat U_T(\vec a)=\lim_{n\to\infty}\Big[\mathbb 1-\frac i\hbar\,\frac{\vec a}{n}\cdot\hat{\vec p}\Big]^n.
$$

!!! thm "Finite Translation Operator"

    $$
    \hat U_T(\vec a)=\exp\!\Big(-\frac i\hbar\,\vec a\cdot\hat{\vec p}\Big).
    $$

If $|\psi\rangle$ is an eigenstate of momentum, $\hat{\vec p}|\psi\rangle=\vec p\,|\psi\rangle$, then

$$
|\psi'\rangle=\hat U_T(\vec a)|\psi\rangle=\exp\!\Big(-\frac i\hbar\,\vec a\cdot\vec p\Big)|\psi\rangle .
$$

The state acquires only a phase. Two consequences follow: a momentum eigenstate is unchanged (up to a phase) by a translation, and conversely a state that does not change under translation must be an eigenstate of the momentum operator.

!!! intuition "Intuition"

    A plane wave $e^{i\vec p\cdot\vec r/\hbar}$ looks the same everywhere, so sliding it sideways changes nothing physical. That is exactly why it can be an eigenstate of the translation generator.

## 8.3 Invariance of the Hamiltonian

Operators transform as $\hat H'=\hat U_T\hat H\hat U_T^\dagger$. For an infinitesimal translation,

\begin{align*}
\hat H'&=\Big[\mathbb 1-\frac i\hbar\,\delta\vec a\cdot\hat{\vec p}\Big]\hat H\Big[\mathbb 1+\frac i\hbar\,\delta\vec a\cdot\hat{\vec p}\Big]\\
&=\hat H-\frac i\hbar\,\delta\vec a\cdot\hat{\vec p}\,\hat H+\frac i\hbar\,\hat H\,\delta\vec a\cdot\hat{\vec p}
=\hat H+\frac i\hbar\,\delta\vec a\cdot[\hat H,\hat{\vec p}\,].
\end{align*}

If the Hamiltonian is invariant under translation, $\hat H'=\hat H$, then $[\hat H,\hat{\vec p}\,]=0$.

For any observable $\hat A$ without explicit time dependence,

$$
\frac{d}{dt}\langle\hat A\rangle=\frac1{i\hbar}\langle[\hat A,\hat H]\rangle ,
$$

so $[\hat A,\hat H]=0$ implies that $\langle\hat A\rangle$ is conserved.

!!! thm "Homogeneity of Space $\Rightarrow$ Momentum Conservation"

    $$
    [\hat H,\hat{\vec p}\,]=0\quad\Longrightarrow\quad \frac{d}{dt}\langle\hat{\vec p}\,\rangle=0 .
    $$

!!! studynote "Study Note"

    The recipe used throughout this chapter is the same each time. (i) Find the unitary operator for the symmetry, $\hat U=\exp(-\tfrac i\hbar\,\text{parameter}\times\text{generator})$. (ii) Require $\hat U\hat H\hat U^\dagger=\hat H$, which is equivalent to $[\hat H,\text{generator}]=0$. (iii) Conclude that the expectation value of the generator is conserved. Translation gives $\hat{\vec p}$, time translation will give $\hat H$ and rotation will give $\hat{\vec L}$.

!!! examtip "Exam Tip"

    The sign in $\hat U_T(\vec a)\psi(\vec r)=\psi(\vec r-\vec a)$ is a frequent source of errors. The state is moved by $+\vec a$, so the new wavefunction at $\vec r$ takes the old value from $\vec r-\vec a$.
