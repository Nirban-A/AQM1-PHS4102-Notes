---
title: "Time Translation and Conservation of Energy"
part: 5
chapter: 39
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 39 Time Translation and Conservation of Energy

## 39.1 The Time-Translation Operator

The Hamiltonian generates translations in time. For an infinitesimal step $\delta t$,

$$
\hat U_T(\delta t)=\Big(\mathbb 1-\frac i\hbar\hat H\,\delta t\Big)
$$

Starting a short step $\epsilon$ from two different times $t_1$ and $t_2$:

\begin{align*}
|\psi(t_1+\epsilon)\rangle&=\Big(\mathbb 1-\frac{i\epsilon}{\hbar}\hat H(t_1)\Big)|\psi_0\rangle\\
|\psi(t_2+\epsilon)\rangle&=\Big(\mathbb 1-\frac{i\epsilon}{\hbar}\hat H(t_2)\Big)|\psi_0\rangle
\end{align*}

If $\hat H$ has no explicit time dependence, $\hat H(t_1)=\hat H(t_2)$ and the same operator evolves the state no matter when the step starts: the physics is invariant under **time translation**.

!!! studynote "Study Note"

    Here $|\psi_0\rangle$ stands for the state at the start of each short interval. The infinitesimal form is just the Schrödinger equation, $|\psi(t+\delta t)\rangle=|\psi(t)\rangle+\delta t\,\partial_t|\psi\rangle=\big(\mathbb 1-\frac i\hbar\hat H\delta t\big)|\psi(t)\rangle$, and repeating it gives $e^{-i\hat Ht/\hbar}$.

## 39.2 Conservation of Energy

The expectation value of an observable $\hat\Omega$ (with no explicit time dependence) obeys

$$
i\hbar\,\frac d{dt}\langle\hat\Omega\rangle=\big\langle[\hat\Omega,\hat H]\big\rangle
$$

Choose $\hat\Omega=\hat H$. Since $[\hat H,\hat H]=0$,

!!! thm "Conservation of Energy"

    $$
    i\hbar\,\frac d{dt}\langle\hat H\rangle=0\quad\Longrightarrow\quad\text{energy is conserved}
    $$

!!! solution "Complete Solution (the commutator rule)"

    With $i\hbar|\dot\psi\rangle=\hat H|\psi\rangle$ and $-i\hbar\langle\dot\psi|=\langle\psi|\hat H$,

    $$
    \frac d{dt}\langle\psi|\hat\Omega|\psi\rangle=\langle\dot\psi|\hat\Omega|\psi\rangle+\langle\psi|\hat\Omega|\dot\psi\rangle=\frac i\hbar\langle\hat H\hat\Omega-\hat\Omega\hat H\rangle=-\frac i\hbar\langle[\hat\Omega,\hat H]\rangle
    $$

    which is $i\hbar\,\frac d{dt}\langle\hat\Omega\rangle=\langle[\hat\Omega,\hat H]\rangle$ .

!!! studynote "Study Note (link to the rest of the chapter)"

    Time-translation invariance ($\hat H$ time-independent) is equivalent to conservation of energy. A time-dependent perturbation breaks the invariance: in general $\frac d{dt}\langle\hat H\rangle=\big\langle\frac{\partial\hat H}{\partial t}\big\rangle\neq0$, and the atom exchanges energy with the driving field. For a harmonic perturbation the exchanged amount is exactly $\hbar\omega$, which is the content of the $\delta(E_f-E_i\mp\hbar\omega)$ in Fermi’s golden rule; for a constant perturbation ($\omega=0$) the same rule gives $E_f=E_i$.

!!! memory "Memory Rule"

    Time-independent $\hat H\Rightarrow$ energy conserved; periodic perturbation of frequency $\omega\Rightarrow$ energy changes only in quanta $\hbar\omega$.
