---
title: "The Interaction Picture"
part: 5
chapter: 32
source_book: "Griffiths and Schroeter, Introduction to Quantum Mechanics (3rd ed.)"
source_section: "11.1.2"
exam_asked: []
topics: []
---

# 32 The Interaction Picture

## 32.1 From the Schrödinger Picture to the Interaction Picture

In the Schrödinger picture the states evolve in time with the full Hamiltonian. For a time-independent $\hat H$ the evolution operator is

$$
\hat U = \exp\Big(-\frac i\hbar\hat Ht\Big), \qquad |\psi(t)\rangle = \hat U|\psi(0)\rangle = \exp\Big(-\frac i\hbar\hat Ht\Big)|\psi(0)\rangle
$$

Expanding $|\psi(0)\rangle=\sum_n c_n(0)|n\rangle$ in the eigenstates, $\hat H|n\rangle=E_n|n\rangle$,

$$
|\psi(t)\rangle = \exp\Big(-\frac i\hbar\hat Ht\Big)\sum_nc_n|n\rangle = \sum_n\exp\Big(-\frac i\hbar E_nt\Big)c_n|n\rangle,
\qquad
i\hbar\frac\partial{\partial t}|\psi(t)\rangle_S = \hat H|\psi(t)\rangle_S
$$

The Schrödinger picture is not convenient for a time-dependent perturbation: the large, known evolution due to $\hat H^0$ is mixed with the small effect of $\hat V(t)$. We therefore switch to the **interaction picture**. With

$$
\hat H = \hat H^0 + \hat V(t)
$$

define the interaction-picture state

$$
|\psi(t)\rangle_I = \exp\Big(\frac i\hbar\hat H^0t\Big)|\psi(t)\rangle_S, \qquad\text{with}\quad |\psi(0)\rangle_I=|\psi(0)\rangle_S\ \text{at } t=0
$$

Differentiate and use the Schrödinger equation $i\hbar\,\partial_t|\psi\rangle_S=\hat H|\psi\rangle_S$:

\begin{align*}
i\hbar\frac\partial{\partial t}|\psi(t)\rangle_I &= i\hbar\Big[\frac{i\hat H^0}{\hbar}e^{\frac i\hbar\hat H^0t}|\psi(t)\rangle_S + e^{\frac i\hbar\hat H^0t}\,\partial_t|\psi(t)\rangle_S\Big]\\
&= -\hat H^0e^{\frac i\hbar\hat H^0t}|\psi(t)\rangle_S + e^{\frac i\hbar\hat H^0t}\hat H|\psi(t)\rangle_S
= e^{\frac i\hbar\hat H^0t}\big[\hat H-\hat H^0\big]|\psi(t)\rangle_S\\
&= e^{\frac i\hbar\hat H^0t}\,\hat V(t)\,|\psi(t)\rangle_S
= e^{\frac i\hbar\hat H^0t}\,\hat V(t)\,e^{-\frac i\hbar\hat H^0t}\,|\psi(t)\rangle_I
\end{align*}

!!! thm "Schrödinger Equation in the Interaction Picture"

    $$
    i\hbar\frac\partial{\partial t}|\psi(t)\rangle_I = \hat V_I(t)\,|\psi(t)\rangle_I, \qquad
    \hat V_I(t) = \exp\Big(\frac i\hbar\hat H^0t\Big)\,\hat V(t)\,\exp\Big(-\frac i\hbar\hat H^0t\Big)
    $$

In the interaction picture **both operators and states have time dependence**.

!!! intuition "Intuition"

    The factor $e^{\frac i\hbar\hat H^0t}$ “undoes” the fast, exactly known evolution of the unperturbed system. What is left evolves only because of the perturbation, and it is driven by $\hat V_I(t)$ alone, which is small. This is exactly why a power series in $\hat V$ makes sense.

!!! memory "Memory Rule"

    Operators evolve with $\hat H^0$ (that is the factor $e^{\pm i\hat H^0t/\hbar}$ in $\hat V_I$); states evolve only under $\hat V_I$. If $\hat V=0$ the interaction-picture state is constant.

!!! studynote "Study Note"

    The two pictures give the same physics: the probability $|c_n|^2$ of finding the system in the eigenstate $|n\rangle$ of $\hat H^0$ is identical in both, because $e^{\frac i\hbar\hat H^0t}$ is unitary and only multiplies each $|n\rangle$ by a phase $e^{iE_nt/\hbar}$.

## 32.2 Equation for the Coefficients

Expand the interaction-picture state in the eigenstates of $\hat H^0$ (with $\hat H^0|n\rangle=E_n|n\rangle$):

$$
|\psi(t)\rangle_I = \sum_nc_n(t)|n\rangle
$$

Insert in $i\hbar\,\partial_t|\psi\rangle_I=\hat V_I|\psi\rangle_I$:

$$
i\hbar\sum_n\dot c_n(t)|n\rangle = \exp\Big(\frac i\hbar\hat H^0t\Big)\hat V(t)\exp\Big(-\frac i\hbar\hat H^0t\Big)\sum_nc_n(t)|n\rangle
$$

Take the inner product with $\langle m|$ and use $\langle m|e^{\frac i\hbar\hat H^0t}=e^{\frac i\hbar E_mt}\langle m|$:

$$
i\hbar\,\dot c_m(t) = \sum_n\exp\Big(\frac i\hbar(E_m-E_n)t\Big)\langle m|\hat V(t)|n\rangle\,c_n(t)
$$

Define the matrix element and the transition frequency

$$
V_{mn}(t)=\langle m|\hat V(t)|n\rangle, \qquad \hbar\omega_{mn}=E_m-E_n, \qquad \omega_{nm}=-\omega_{mn}
$$

!!! thm "Coupled Equations for the Amplitudes in the Interaction Picture"

    $$
    i\hbar\,\dot c_m(t) = \sum_nV_{mn}(t)\,e^{i\omega_{mn}t}\,c_n(t)
    $$

!!! studynote "Study Note (consistency with Section 1)"

    For two levels $a,b$ with $\omega_{ba}=\omega_0$ this gives $\dot c_b=-\frac i\hbar V_{ba}e^{i\omega_0t}c_a$ and $\dot c_a=-\frac i\hbar V_{ab}e^{-i\omega_0t}c_b$, the same equations that were derived directly in [Section 31](31-time-dependent-perturbation-theory-two-level.md).

!!! examtip "Exam Tip"

    This set of equations is the starting point for *every* problem in this chapter: truncate the sum to the relevant levels and solve (exactly for two levels, iteratively in general).

!!! book "See also: Griffiths, Introduction to Quantum Mechanics (3rd ed.), section 11.1.2"

    Griffiths does not introduce the interaction picture by name. He writes the state directly as $\sum_nc_n(t)\,e^{-iE_nt/\hbar}|\psi_n\rangle$, so his $c_n(t)$ are exactly the coefficients of the interaction-picture state used here, and the factors $e^{i\omega_{mn}t}$ appear in the equations for $\dot c_m$ from the start. The multi-level equation of [Section 32.2](#322-equation-for-the-coefficients) is Problem 11.24(a).
