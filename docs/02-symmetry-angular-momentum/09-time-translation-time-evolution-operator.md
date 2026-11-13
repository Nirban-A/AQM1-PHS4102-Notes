---
title: "Time Translation and the Time-Evolution Operator"
part: 2
chapter: 9
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 9 Time Translation and the Time-Evolution Operator

## 9.1 Definition of $\hat U(t,t_0)$

The Schrödinger equation is

$$
i\hbar\frac{\partial}{\partial t}|\psi(t)\rangle=\hat H|\psi(t)\rangle .
$$

The state at a later time $t>t_0$ is related to the initial state by a linear operator,

$$
|\psi(t)\rangle=\hat U(t,t_0)|\psi(t_0)\rangle,\qquad \hat U(t_0,t_0)=\mathbb 1 .
$$

Substituting into the Schrödinger equation, and noting that $|\psi(t_0)\rangle$ is arbitrary,

$$
i\hbar\frac{\partial}{\partial t}\hat U(t,t_0)=\hat H\,\hat U(t,t_0)
\quad\Longleftrightarrow\quad
\frac{\partial}{\partial t}\hat U(t,t_0)=-\frac i\hbar\hat H\,\hat U(t,t_0).
$$

Integrating from $t_0$ to $t$ and using $\hat U(t_0,t_0)=\mathbb 1$ gives the integral equation

$$
\hat U(t,t_0)=\mathbb 1-\frac i\hbar\int_{t_0}^{t}\hat H\,\hat U(t',t_0)\,dt' .
$$

!!! thm "Unitarity of $\hat U$"

    $$
    \langle\psi(t)|\psi(t)\rangle=\langle\psi(t_0)|\psi(t_0)\rangle\quad\Longrightarrow\quad \hat U^\dagger\hat U=\mathbb 1 .
    $$

!!! studynote "Study Note"

    The norm is conserved because $\hat H$ is Hermitian, since $\frac{d}{dt}\langle\psi|\psi\rangle=\frac{i}{\hbar}\langle\psi|(\hat H^\dagger-\hat H)|\psi\rangle=0$. A time-dependent Hermitian $\hat H$ also gives a unitary $\hat U$; only the closed form below needs $\hat H$ independent of time.

## 9.2 The Generator of Time Translation

Look at a short step $\delta t$ after $t_0$. From the differential equation,

$$
i\hbar\big[\hat U(t_0+\delta t,t_0)-\hat U(t_0,t_0)\big]=\hat H\,\hat U(t_0+\delta t,t_0)\,\delta t ,
$$

so, with $\hat U(t_0,t_0)=\mathbb 1$,

$$
\hat U(t_0+\delta t,t_0)=\mathbb 1-\frac i\hbar\hat H\Big[\hat U(t_0,t_0)+\frac{\partial\hat U}{\partial t}\Big|_{t=t_0}\delta t+\cdots\Big]\delta t=\mathbb 1-\frac i\hbar\hat H\,\delta t+O(\delta t^2).
$$

Dropping the $O(\delta t^2)$ term defines the infinitesimal time translation.

!!! thm "Hamiltonian Generates Time Translations"

    $$
    \hat U_T(\delta t)=\mathbb 1-\frac i\hbar\,\hat H\,\delta t .
    $$

Compare with $\hat U_T(\delta\vec a)=\mathbb 1-\tfrac i\hbar\,\delta\vec a\cdot\hat{\vec p}$: the Hamiltonian plays for time the role that momentum plays for space.

## 9.3 The Finite Time-Evolution Operator

Take $\hat H$ independent of time and split $t-t_0$ into $n$ steps of size $\delta t=(t-t_0)/n$:

$$
\hat U(t,t_0)=\lim_{n\to\infty}\Big[\mathbb 1-\frac i\hbar\,\frac{t-t_0}{n}\,\hat H\Big]^n .
$$

!!! thm "Time-Evolution Operator for a Time-Independent $\hat H$"

    $$
    \hat U(t,t_0)=\exp\!\Big[-\frac i\hbar\,\hat H\,(t-t_0)\Big].
    $$

## 9.4 Energy Conservation

Under a time translation the Hamiltonian transforms as

$$
\hat H'=\Big(\mathbb 1-\frac i\hbar\hat H\,\delta t\Big)\hat H\Big(\mathbb 1+\frac i\hbar\hat H\,\delta t\Big)=\hat H ,
$$

because $\hat H$ commutes with itself. Using the general rule $\frac{d}{dt}\langle\hat A\rangle=\frac1{i\hbar}\langle[\hat A,\hat H]\rangle$ with $\hat A=\hat H$,

!!! thm "Time Translation Invariance $\Rightarrow$ Energy Conservation"

    $$
    \frac{d}{dt}\langle\hat H\rangle=\frac1{i\hbar}\langle[\hat H,\hat H]\rangle=0 .
    $$

!!! intuition "Intuition"

    If the laws of physics do not change with the clock, the energy is conserved. This is the third member of the family: homogeneity of space gives momentum, isotropy gives angular momentum and homogeneity of time gives energy.

!!! memory "Memory Rule"

    The generator multiplies the parameter, always with $-\tfrac i\hbar$: $\ \hat U=\exp\!\big(-\tfrac i\hbar\ \mathrm{parameter}\times\mathrm{generator}\big)$. Space shift $\to\vec a\cdot\hat{\vec p}$, time shift $\to t\,\hat H$, rotation $\to\phi\,\hat n\cdot\hat{\vec L}$.

!!! prob "Stationary-State Evolution"

    !!! solution "Complete Solution"

        Let $\hat H|E_n\rangle=E_n|E_n\rangle$ and $|\psi(t_0)\rangle=\sum_nc_n|E_n\rangle$. Then

        $$
        |\psi(t)\rangle=e^{-i\hat H(t-t_0)/\hbar}\sum_nc_n|E_n\rangle=\sum_nc_n\,e^{-iE_n(t-t_0)/\hbar}|E_n\rangle .
        $$

    The probabilities $|c_n|^2$ do not depend on time, which is the statement that the energy distribution is conserved. A single eigenstate only picks up a phase, so every expectation value in a stationary state is constant.
