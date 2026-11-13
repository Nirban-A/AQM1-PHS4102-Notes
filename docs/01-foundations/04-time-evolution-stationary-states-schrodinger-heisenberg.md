---
title: "Time Evolution: Stationary States and the Schrödinger and Heisenberg Pictures"
part: 1
chapter: 4
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 4 Time Evolution: Stationary States and the Schrödinger and Heisenberg Pictures

## 4.1 Postulate 4 and the Time-Evolution Operator

!!! thm "Postulate 4: the Schrödinger Equation"

    $$
    i\hbar\,\frac d{dt}|\psi(t)\rangle=\hat H|\psi(t)\rangle,\qquad\text{equivalently}\qquad |\dot\psi(t)\rangle=-\frac i\hbar\hat H|\psi(t)\rangle .
    $$

Solving it involves three steps: (i) set up the equation, (ii) choose a general approach to its solution, (iii) choose a basis in which to solve it. The solution is written with the *time-evolution operator* $\hat U(t)$:

$$
|\psi(t)\rangle=\hat U(t)|\psi(0)\rangle,\qquad |\dot\psi(0)\rangle=-\frac i\hbar\hat H|\psi(0)\rangle .
$$

!!! studynote "Study Note (notation)"

    The notebook writes the second relation as $|\psi(0)\rangle=-\frac i\hbar\hat H|\psi(0)\rangle$, which is not an identity; the dot (time derivative) on the left ket is the part that was lost. The correct statement is that the *rate of change* of the state at $t=0$ is $-\frac i\hbar\hat H$ acting on the state.

## 4.2 Time-Independent Hamiltonian: Solution in the Energy Basis

Suppose $\dfrac{\partial\hat H}{\partial t}=0$, i.e. $\hat H$ does not depend explicitly on time, and let $\hat H|E\rangle=E|E\rangle$. Expand the state in this basis:

$$
|\psi(t)\rangle=\sum_E|E\rangle\langle E|\psi(t)\rangle=\sum_Ea_E(t)\,|E\rangle .
$$

Insert this in $\big(i\hbar\,\partial_t-\hat H\big)|\psi(t)\rangle=0$:

$$
\sum_E\big(i\hbar\,\dot a_E(t)-E\,a_E(t)\big)|E\rangle=0\ \Longrightarrow\ i\hbar\,\dot a_E(t)=E\,a_E(t),
$$

since the $|E\rangle$ are linearly independent. The solution is $a_E(t)=a_E(0)\,e^{-iEt/\hbar}$.

!!! thm "Solution for a Time-Independent Hamiltonian"

    \begin{align*}
    \langle E|\psi(t)\rangle&=\langle E|\psi(0)\rangle\,e^{-iEt/\hbar},\qquad
    |\psi(t)\rangle=\Big[\sum_Ee^{-iEt/\hbar}|E\rangle\langle E|\Big]|\psi(0)\rangle\\
    \hat U(t)&=\sum_Ee^{-iEt/\hbar}|E\rangle\langle E|\quad(\text{non-degenerate}),\\
    \hat U(t)&=\sum_{E,\alpha}e^{-iEt/\hbar}|E,\alpha\rangle\langle E,\alpha|\quad(\text{degenerate}).
    \end{align*}

Since $\hat H|E\rangle=E|E\rangle$, we have $e^{-iEt/\hbar}|E\rangle=e^{-i\hat Ht/\hbar}|E\rangle$, and therefore

$$
\hat U(t)=\sum_Ee^{-i\hat Ht/\hbar}|E\rangle\langle E|=e^{-i\hat Ht/\hbar}\sum_E|E\rangle\langle E|=e^{-i\hat Ht/\hbar}.
$$

!!! thm "The Time-Evolution Operator"

    $$
    \hat U(t)=\exp\Big(-\frac{i\hat Ht}\hbar\Big),\qquad \hat U\hat U^\dagger=\hat U^\dagger\hat U=\mathbb 1\quad(\text{unitary}).
    $$

!!! solution "Complete Solution (unitarity)"

    Using $\langle E|E'\rangle=\delta_{EE'}$,

    $$
    \hat U^\dagger\hat U=\sum_{E,E'}e^{iEt/\hbar}e^{-iE't/\hbar}|E\rangle\langle E|E'\rangle\langle E'|=\sum_E|E\rangle\langle E|=\mathbb 1 .
    $$

Consequently

$$
\langle\psi(t)|\psi(t)\rangle=\langle\psi(0)|\hat U^\dagger\hat U|\psi(0)\rangle=\langle\psi(0)|\psi(0)\rangle,
$$

so the total probability does not change in time. Unitarity is the mathematical form of probability conservation.

### Stationary states

If the system starts in a single energy eigenstate (including the degenerate case), $|\psi(0)\rangle=|E\rangle$, then

$$
|\psi(t)\rangle=|\psi(0)\rangle\,e^{-iEt/\hbar},\qquad
|\langle E|\psi(t)\rangle|^2=\big|\langle E|\psi(0)\rangle\,e^{-iEt/\hbar}\big|^2=|\langle E|\psi(0)\rangle|^2 .
$$

The probabilities of all measurements are independent of time. These are the *stationary states*. Only the phase $e^{-iEt/\hbar}$ changes, and a global phase has no physical consequence.

!!! intuition "Intuition"

    A general state is a superposition of energy eigenstates, each rotating in the complex plane at its own angular frequency $E/\hbar$. Interference between components with different $E$ is what produces genuine time dependence; a single component alone gives a frozen probability distribution.

!!! studynote "Study Note (choice of basis)"

    For a Hamiltonian such as $\hat H=\dfrac{\hat p^2}{2m}+\dfrac1{\cosh^2x}$, the potential is a function of position, so solving in the $x$-basis (a differential equation) is easier than in any basis where $\hat x$ is not diagonal. Choose the basis in which the Hamiltonian is simplest.

!!! examtip "Exam Tip"

    To find $|\psi(t)\rangle$: (1) find the eigenstates $|E\rangle$ of $\hat H$, (2) expand $|\psi(0)\rangle=\sum_Ec_E|E\rangle$ with $c_E=\langle E|\psi(0)\rangle$, (3) attach $e^{-iEt/\hbar}$ to each term. Probabilities of measuring energy $E$ never change; probabilities of measuring other observables generally do.

## 4.3 The Schrödinger Picture

In the Schrödinger picture the state vectors depend on time and the operators are time independent:

$$
i\hbar\frac d{dt}|\psi(t)\rangle=\hat H|\psi(t)\rangle,\qquad |\psi(t)\rangle=\hat U(t)|\psi(0)\rangle=\hat U(t,t_0)|\psi(t_0)\rangle,\qquad \hat U(t)=e^{-i\hat Ht/\hbar},\ \ \hat U^\dagger\hat U=\mathbb 1 .
$$

## 4.4 The Heisenberg Picture

Invert the evolution: $|\psi(0)\rangle=\hat U^\dagger(t)|\psi(t)\rangle$. Define the Heisenberg state

$$
|\psi\rangle_H\equiv|\psi(0)\rangle=e^{i\hat Ht/\hbar}|\psi(t)\rangle ,
$$

which is *frozen in time*. The expectation value of an operator $\hat A$ (which is time independent in the Schrödinger picture) is

$$
\langle\psi(t)|\hat A|\psi(t)\rangle=\langle\psi(0)|\,e^{i\hat Ht/\hbar}\hat A\,e^{-i\hat Ht/\hbar}\,|\psi(0)\rangle=\langle\psi(0)|\hat A_H|\psi(0)\rangle=\ _H\langle\psi|\hat A_H|\psi\rangle_H ,
$$

which defines the time-dependent Heisenberg operator.

!!! thm "Heisenberg Operator"

    $$
    \hat A_H(t)=\hat U^\dagger\hat A\,\hat U=e^{i\hat Ht/\hbar}\,\hat A\,e^{-i\hat Ht/\hbar}\qquad\Big(\text{with }\frac{\partial\hat A}{\partial t}=0\Big).
    $$

To find its equation of motion, note $\hat U^\dagger=e^{i\hat Ht/\hbar}$ and $\hat U=e^{-i\hat Ht/\hbar}$ give

$$
\frac{\partial\hat U^\dagger}{\partial t}=\hat U^\dagger\,\frac i\hbar\hat H,\qquad
\frac{\partial\hat U}{\partial t}=-\hat U\,\frac i\hbar\hat H .
$$

Then

\begin{align*}
\frac{d\hat A_H}{dt}&=\frac{\partial\hat U^\dagger}{\partial t}\hat A\hat U+\hat U^\dagger\hat A\frac{\partial\hat U}{\partial t}
=\frac i\hbar\,\hat U^\dagger\hat H\hat A\hat U-\frac i\hbar\,\hat U^\dagger\hat A\hat U\hat H\\
&=\frac i\hbar\Big[\hat U^\dagger\hat H\hat U\ \hat U^\dagger\hat A\hat U-\hat U^\dagger\hat A\hat U\ \hat U^\dagger\hat H\hat U\Big]
=\frac i\hbar\big[\hat H,\hat A_H\big]=\frac1{i\hbar}\big[\hat A_H,\hat H\big],
\end{align*}

where we inserted $\hat U\hat U^\dagger=\mathbb 1$ and used $\hat U^\dagger\hat H\hat U=\hat H$.

!!! thm "Heisenberg Equation of Motion"

    $$
    \frac{d\hat A_H}{dt}=\frac1{i\hbar}\big[\hat A_H,\hat H\big]\qquad\text{and}\qquad\frac d{dt}\langle\hat A\rangle=\frac1{i\hbar}\big\langle[\hat A,\hat H]\big\rangle .
    $$

**Note:** A unitary transformation by $\hat U=e^{-i\hat Ht/\hbar}$ does not change the Hamiltonian, since $\hat U^\dagger\hat H\hat U=\hat U^\dagger\hat U\hat H=\hat H$ (it commutes with its own exponential).

!!! intuition "Intuition"

    In the Schrödinger picture the state moves and the measuring apparatus is fixed; in the Heisenberg picture the state is fixed and the operators rotate. Both give identical expectation values and probabilities. The Heisenberg form is the quantum counterpart of the classical equation $\dot A=\{A,H\}$ with the Poisson bracket replaced by $\frac1{i\hbar}[\ ,\ ]$.

!!! solution "Complete Solution (conservation laws)"

    If $[\hat A,\hat H]=0$ then $d\langle\hat A\rangle/dt=0$ and $\hat A$ is conserved. For $\hat A=\hat H$ itself, $[\hat H,\hat H]=0$, so $\langle\hat H\rangle$ (the energy) is conserved when $\hat H$ has no explicit time dependence.

!!! prob "Worked Example: Free Particle in the Heisenberg Picture"

    Find $\hat x_H(t)$ and $\hat p_H(t)$ for $\hat H=\hat p^2/2m$.

!!! solution "Complete Solution"

    Since $[\hat p,\hat H]=0$, $\dfrac{d\hat p_H}{dt}=0$, so $\hat p_H(t)=\hat p$. For the position, $[\hat x,\hat p^2]=\hat p[\hat x,\hat p]+[\hat x,\hat p]\hat p=2i\hbar\hat p$, hence

    $$
    \frac{d\hat x_H}{dt}=\frac1{i\hbar}\frac{[\hat x,\hat p^2]}{2m}=\frac{\hat p}m\quad\Longrightarrow\quad \hat x_H(t)=\hat x+\frac{\hat p}m\,t .
    $$

!!! verification "Verification"

    This is the classical straight-line motion $x=x_0+(p/m)t$, and $[\hat x_H(t),\hat p_H(t)]=[\hat x,\hat p]=i\hbar$ is preserved at all times, as it must be for a unitary transformation.

|                   | **Schrödinger picture** | **Heisenberg picture**       |
|:------------------|:------------------------|:-----------------------------|
| State             | $\vert \psi(t)\rangle=\hat U(t)\vert \psi(0)\rangle$              | $\vert \psi\rangle_H=\vert \psi(0)\rangle$ (frozen)          |
| Operator          | $\hat A$ (fixed)      | $\hat A_H(t)=\hat U^\dagger\hat A\hat U$                   |
| Equation          | $i\hbar\,\partial_t\vert \psi\rangle=\hat H\vert \psi\rangle$              | $\dot{\hat A}_H=\frac1{i\hbar}[\hat A_H,\hat H]$                   |
| Expectation value | $\langle\psi(t)\vert \hat A\vert \psi(t)\rangle$              | $\ _H\langle\psi\vert \hat A_H(t)\vert \psi\rangle_H$ (the same number) |
