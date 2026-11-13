---
title: "Postulates of Quantum Mechanics and Dirac Notation"
part: 1
chapter: 1
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 1 Postulates of Quantum Mechanics and Dirac Notation

## 1.1 Classical versus Quantum Postulates

We study non-relativistic quantum mechanics of a single particle. The four postulates are stated side by side with their classical counterparts.

|     | **Classical mechanics**                                                                                                                             | **Quantum mechanics**                                                                                                                                                                                                                                        |
|:----|:----------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | The state of a particle at a given time is specified by two variables $x(t),\,p(t)$.                                                                   | The state of a particle is represented by a vector $\vert \psi(t)\rangle$ in a Hilbert space.                                                                                                                                                                            |
| 2   | Every dynamical variable $\omega$ is a function of $x,p$, e.g. $E=\dfrac{p^2}{2m}+V(x)$.                                                                   | The variables $x,p$ are replaced by Hermitian operators $\hat x,\hat p$, with $\langle x\vert \hat x\vert x'\rangle=x\,\delta(x-x')$ and $\langle x\vert \hat p\vert x'\rangle=-i\hbar\,\delta'(x-x')$.                                                                                                                                                     |
| 3   | If the particle is in a state given by $x$ and $p$, measuring $\omega$ yields the value $\omega(x,p)$ and the state is unaffected. | If the particle is in a state $\vert \psi\rangle$, measuring $\omega\to\hat\Omega$ yields one of the eigenvalues $\omega_i$ of $\hat\Omega$ with probability $P(\omega_i)\propto\vert \langle\omega_i\vert \psi\rangle\vert ^2$, where $\hat\Omega\vert \omega_i\rangle=\omega_i\vert \omega_i\rangle$. The state changes from $\vert \psi\rangle$ to $\vert \omega_i\rangle$ as a result of the measurement. |
| 4   | The state variables change in time according to Hamilton’s equations, $\dot x=\dfrac{\partial H_c}{\partial p}$, $\dot p=-\dfrac{\partial H_c}{\partial x}$.                                                     | The state vector evolves as $i\hbar\dfrac{\partial}{\partial t}\vert \psi\rangle=\hat H\vert \psi\rangle$, with $\hat H=H_c(x\to\hat x,\ p\to\hat p)$.                                                                                                                                                                                                   |

Postulates 1 to 3 describe the state at a given time; Postulate 4 describes how the state evolves in time.

!!! thm "Operator Postulate: Matrix Elements in the Position Basis"

    $$
    \hat x|x\rangle=x|x\rangle,\qquad \hat p|x\rangle\neq p|x\rangle,\qquad
    \langle x|\hat x|x'\rangle=x\,\delta(x-x'),\qquad \langle x|\hat p|x'\rangle=-i\hbar\,\delta'(x-x'),
    $$

    with $\delta'(x-x')=\dfrac{d}{dx}\delta(x-x')$.

!!! intuition "Intuition"

    Classically a particle *is* at a point of phase space. Quantum mechanically a state is a vector, and numbers such as position and momentum are what you obtain by *measuring* operators on it. The position kets are eigenvectors of $\hat x$, but they are not eigenvectors of $\hat p$: a state with a sharp position has no sharp momentum.

## 1.2 Vectors, Kets and Bras: the Finite-Dimensional Picture

Recall the notation for an ordinary vector. In three dimensions, $\vec A=A_1\hat e_1+A_2\hat e_2+A_3\hat e_3$ with $\hat e_i\cdot\hat e_j=\delta_{ij}$ and $\hat e_i\cdot\vec A=A_i$. Dirac notation carries this over to any dimension:

\begin{align*}
|A\rangle&=\sum_{i=1}^nA_i|e_i\rangle\ \ (\text{ket}), &
\langle A|&=\sum_{i=1}^nA_i^*\langle e_i|\ \ (\text{bra}),\\
\langle e_i|e_j\rangle&=\delta_{ij}\ \ (\text{orthonormality}), &
\langle e_k|A\rangle&=A_k .
\end{align*}

For a general state in a finite-dimensional space, $|\psi\rangle=\sum_{j=1}^n\psi_j|a_j\rangle$ and $\langle a_k|\psi\rangle=\sum_j\psi_j\langle a_k|a_j\rangle=\sum_j\psi_j\delta_{kj}=\psi_k$.

### Matrix representation and projection operators

In the basis $\{|e_i\rangle\}$ the kets are column vectors, $|e_1\rangle=(1,0,0)^T$, $|e_2\rangle=(0,1,0)^T$, $|e_3\rangle=(0,0,1)^T$, and the bras are row vectors. Then $\langle e_1|e_1\rangle=(1\ 0\ 0)(1\ 0\ 0)^T=1$ and

$$
|e_1\rangle\langle e_1|=\begin{pmatrix}1&0&0\\0&0&0\\0&0&0\end{pmatrix},\qquad
|e_1\rangle\langle e_1|+|e_2\rangle\langle e_2|+|e_3\rangle\langle e_3|=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}.
$$

!!! thm "Completeness and Projection Operators"

    \begin{gather*}
    \sum_i|e_i\rangle\langle e_i|=\mathbb 1\quad(\text{completeness}),\qquad
    \hat P_i=|e_i\rangle\langle e_i|\quad(\text{projection operator}),\\
    \int dx\,|x\rangle\langle x|=\mathbb 1\quad(\text{continuum}).
    \end{gather*}

!!! studynote "Study Note"

    $\hat P_i$ acting on $|A\rangle$ gives $|e_i\rangle\langle e_i|A\rangle=A_i|e_i\rangle$, the component of $|A\rangle$ along $|e_i\rangle$. Inserting $\mathbb 1=\sum_i|e_i\rangle\langle e_i|$ anywhere in an expression is the single most used trick in this formalism.

### Infinite-dimensional case

In the infinite-dimensional (function) space, with the position kets $|x\rangle$ as basis,

$$
|\psi\rangle=\int dx\,\psi(x)\,|x\rangle,\qquad
\langle x'|\psi\rangle=\int dx\,\psi(x)\langle x'|x\rangle=\int dx\,\psi(x)\,\delta(x-x')=\psi(x').
$$

!!! studynote "Study Note"

    The wavefunction $\psi(x)=\langle x|\psi\rangle$ is just the set of components of the abstract ket $|\psi\rangle$ in the position basis. The last step uses $\langle x'|x\rangle=\delta(x-x')$, which is derived in [Section 3](03-dirac-delta-function-position-momentum-bases.md).

### Expansion in the eigenbasis of an operator

If $\hat\Omega|\omega_i\rangle=\omega_i|\omega_i\rangle$ with a complete orthonormal set,

$$
\sum_{i=1}^n|\omega_i\rangle\langle\omega_i|=\mathbb 1,\qquad
|\psi\rangle=\sum_i\psi_i|\omega_i\rangle,\qquad
\langle\omega_k|\psi\rangle=\sum_i\langle\omega_k|\omega_i\rangle\psi_i=\psi_k,\qquad
\text{Prob}=|\langle\omega_k|\psi\rangle|^2=|\psi_k|^2 .
$$

## 1.3 Consequences of the Postulates

### (I) The principle of superposition

If $|\psi\rangle$ and $|\psi'\rangle$ both represent states of a particle, then so does $\alpha|\psi\rangle+\beta|\psi'\rangle$. This is the *principle of superposition*.

### (II) Observables and measurement probabilities

A classical observable $\omega(x,p)$ becomes an operator $\hat\Omega(x\to\hat x,\,p\to\hat p)$. It is Hermitian, so its eigenvectors satisfy

$$
\hat\Omega|\omega_i\rangle=\omega_i|\omega_i\rangle,\qquad
\hat\Omega=\hat\Omega^\dagger,\qquad
\sum_i|\omega_i\rangle\langle\omega_i|=\mathbb 1,\qquad
\langle\omega_i|\omega_j\rangle=\delta_{ij},
$$

and the last two properties are guaranteed for quantum mechanics (Hermiticity gives real eigenvalues, orthogonal eigenvectors, and completeness). Expand the state in this eigenbasis, $|\psi\rangle=\sum_i|\omega_i\rangle\langle\omega_i|\psi\rangle=\sum_i\psi_i|\omega_i\rangle$. The probability that a measurement yields the eigenvalue $\omega$ is

$$
p(\omega)\propto|\langle\omega|\psi\rangle|^2=\langle\omega|\psi\rangle^*\langle\omega|\psi\rangle=\langle\psi|\omega\rangle\langle\omega|\psi\rangle .
$$

The constant of proportionality is fixed by requiring $\sum_ip(\omega_i)=1$.

!!! thm "Measurement Probability"

    $$
    p(\omega_i)=\frac{|\langle\omega_i|\psi\rangle|^2}{\sum_j|\langle\omega_j|\psi\rangle|^2}=\frac{|\langle\omega_i|\psi\rangle|^2}{\langle\psi|\psi\rangle}
    $$

    and, for a normalized state $(\langle\psi|\psi\rangle=1)$, $p(\omega_i)=|\langle\omega_i|\psi\rangle|^2$.

!!! verification "Verification"

    The denominator is $\sum_j\langle\psi|\omega_j\rangle\langle\omega_j|\psi\rangle=\langle\psi|\Big(\sum_j|\omega_j\rangle\langle\omega_j|\Big)|\psi\rangle=\langle\psi|\psi\rangle$, using completeness. So the total probability is $1$ for any state, normalized or not.

Two special cases follow at once. If $|\psi\rangle=|\omega_k\rangle$ then $p(\omega_k)=1$ and all others vanish. If $|\psi\rangle=\alpha|\omega_1\rangle+\beta|\omega_2\rangle$ with $|\omega_1\rangle,|\omega_2\rangle$ eigenfunctions of $\hat\Omega$ with different eigenvalues, normalization $\langle\psi|\psi\rangle=1$ gives

$$
|\psi\rangle=\frac{\alpha|\omega_1\rangle+\beta|\omega_2\rangle}{\sqrt{|\alpha|^2+|\beta|^2}},\qquad
p(\omega_1)=\frac{|\alpha|^2}{|\alpha|^2+|\beta|^2},\qquad
p(\omega_2)=\frac{|\beta|^2}{|\alpha|^2+|\beta|^2}.
$$

## 1.4 Complications of Quantum Measurement

### (1) Ordering ambiguity: symmetrization

Classically $\omega=xp=px$. Quantum mechanically $\hat x\hat p\neq\hat p\hat x$, so the observable is taken to be the symmetrized product

$$
\hat\Omega=\frac{\hat x\hat p+\hat p\hat x}{2}.
$$

!!! solution "Complete Solution (why symmetrize)"

    Using $[\hat x,\hat p]=i\hbar$, $(\hat x\hat p)^\dagger=\hat p^\dagger\hat x^\dagger=\hat p\hat x=\hat x\hat p-i\hbar\neq\hat x\hat p$, so $\hat x\hat p$ alone is not Hermitian and cannot be an observable. The symmetrized combination satisfies $\hat\Omega^\dagger=\tfrac12(\hat p\hat x+\hat x\hat p)=\hat\Omega$, so it is Hermitian, with real eigenvalues.

### (2) Degenerate eigenvalues: the projection operator

Suppose two eigenvectors share one eigenvalue, $\hat\Omega|\omega_1\rangle=\omega|\omega_1\rangle$ and $\hat\Omega|\omega_2\rangle=\omega|\omega_2\rangle$. The probability of obtaining $\omega$ is the sum over the degenerate states,

$$
p(\omega)\propto|\langle\omega_1|\psi\rangle|^2+|\langle\omega_2|\psi\rangle|^2 .
$$

Define the projection operator $\hat P_\omega=|\omega_1\rangle\langle\omega_1|+|\omega_2\rangle\langle\omega_2|$. Then

$$
p(\omega)\propto\langle\psi|\hat P_\omega|\psi\rangle=\langle\psi|\hat P_\omega^2|\psi\rangle=\langle\hat P_\omega\psi|\hat P_\omega\psi\rangle,\qquad
\hat P_\omega=\hat P_\omega^2=\hat P_\omega^\dagger .
$$

!!! verification "Verification"

    *($\hat P_\omega^2=\hat P_\omega$):* $\hat P_\omega^2=\sum_{a,b=1}^2|\omega_a\rangle\langle\omega_a|\omega_b\rangle\langle\omega_b|=\sum_a|\omega_a\rangle\langle\omega_a|=\hat P_\omega$ by orthonormality. The probability is the squared length of the part of $|\psi\rangle$ that lies in the degenerate subspace.

### (3) Continuous spectra: probability density

For a continuous eigenvalue $\omega$ the sums become integrals,

$$
|\psi\rangle=\sum_i|\omega_i\rangle\langle\omega_i|\psi\rangle\ \longrightarrow\ |\psi\rangle=\int d\omega\,|\omega\rangle\langle\omega|\psi\rangle=\int d\omega\,\psi(\omega)|\omega\rangle,
$$

and $p(\omega)=|\psi(\omega)|^2=|\langle\omega|\psi\rangle|^2$ is a *probability density*. It is correctly normalized, since

$$
\int p(\omega)\,d\omega=\int d\omega\,\langle\psi|\omega\rangle\langle\omega|\psi\rangle=\langle\psi|\psi\rangle=1,\qquad\text{because}\ \int d\omega\,|\omega\rangle\langle\omega|=\mathbb 1 .
$$

## 1.5 Collapse of the State

Let $|\psi\rangle$ be the state and $\hat\Omega$ an observable with $\hat\Omega|\omega_i\rangle=\omega_i|\omega_i\rangle$. Writing $|\psi\rangle=\sum_i|\omega_i\rangle\langle\omega_i|\psi\rangle$ (basis kets times components), a measurement gives $\omega_i$ with probability $p(\omega_i)=|\langle\omega_i|\psi\rangle|^2$, and the state *collapses* to $|\omega_i\rangle$. To test this, take an ensemble of $N$ identically prepared particles in the state $|\psi\rangle$ and measure $\hat\Omega$ on each: the fraction giving $\omega_i$ approaches $p(\omega_i)$.

!!! prob "Worked Example: Preparing and Measuring a Superposition"

    An operator $\hat\Lambda$ has eigenvalues $\lambda_1,\lambda_2$ with eigenstates $|\lambda_1\rangle,|\lambda_2\rangle$. A state is prepared as $|\omega\rangle=\dfrac1{\sqrt3}|\lambda_1\rangle+\dfrac2{\sqrt3}|\lambda_2\rangle$. Find the measurement probabilities and the state after a measurement.

!!! solution "Complete Solution"

    As written, $\langle\omega|\omega\rangle=\tfrac13+\tfrac43=\tfrac53\neq1$, so the state is not normalized. Using the normalized form $|\omega\rangle=(|\lambda_1\rangle+2|\lambda_2\rangle)/\sqrt5$, the probabilities are

    $$
    p(\lambda_1)=\frac15,\qquad p(\lambda_2)=\frac45,\qquad p(\lambda_1)+p(\lambda_2)=1 .
    $$

If the result is $\lambda_2$, the state becomes $|\lambda_2\rangle$, and an immediate second measurement of $\hat\Lambda$ returns $\lambda_2$ with probability $1$. (If the intended coefficients were $1/\sqrt3$ and $\sqrt{2/3}$, the probabilities would be $\tfrac13$ and $\tfrac23$; the notebook example stops before the numbers.)

!!! examtip "Exam Tip"

    Always check normalization before reading off probabilities. If the coefficients are not normalized, divide $|c_i|^2$ by $\sum_j|c_j|^2$.

## 1.6 Expectation Value and Uncertainty

For an ensemble of particles in the state $|\psi\rangle$,

\begin{align*}
\langle\hat\Omega\rangle&=\sum_ip(\omega_i)\,\omega_i\ \ (\text{discrete})\ =\int d\omega\,\omega\,p(\omega)\ \ (\text{continuous}),
\end{align*}

and the discrete sum is evaluated as

\begin{align*}
\langle\hat\Omega\rangle&=\sum_i\langle\omega_i|\psi\rangle^*\langle\omega_i|\psi\rangle\,\omega_i
=\sum_i\langle\psi|\omega_i\rangle\,\omega_i\,\langle\omega_i|\psi\rangle
=\sum_i\langle\psi|\hat\Omega|\omega_i\rangle\langle\omega_i|\psi\rangle
=\langle\psi|\hat\Omega\Big(\sum_i|\omega_i\rangle\langle\omega_i|\Big)|\psi\rangle .
\end{align*}

!!! thm "Expectation Value"

    $$
    \langle\hat\Omega\rangle=\langle\psi|\hat\Omega|\psi\rangle,\qquad\text{and if }\hat\Omega|\psi\rangle=\omega|\psi\rangle\text{ then }\langle\hat\Omega\rangle=\omega\ \ (\langle\psi|\psi\rangle=1).
    $$

!!! thm "Uncertainty (Standard Deviation) of an Observable"

    \begin{align*}
    \Delta\hat\Omega&=\Big\langle\big(\hat\Omega-\mathbb 1\langle\hat\Omega\rangle\big)^2\Big\rangle^{1/2},\\
    \langle(\Delta\hat\Omega)^2\rangle&=\sum_ip(\omega_i)\big(\omega_i-\langle\hat\Omega\rangle\big)^2\ \ \Big(\text{or }\int d\omega\,p(\omega)(\omega-\langle\hat\Omega\rangle)^2\Big)\\
    &=\langle\psi|\big(\hat\Omega-\mathbb 1\langle\hat\Omega\rangle\big)^2|\psi\rangle .
    \end{align*}

!!! studynote "Study Note (correction)"

    The notebook writes $\Delta\hat\Omega=[(\hat\Omega-\mathbb 1\langle\hat\Omega\rangle)^2]^{1/2}$ without the outer expectation value. The brackets $\langle\ \rangle$ around the squared operator are required: an operator has no single numerical spread, only its expectation value in a state does.

!!! solution "Complete Solution (the working formula)"

    Expanding the square, $\langle(\hat\Omega-\langle\hat\Omega\rangle)^2\rangle=\langle\hat\Omega^2\rangle-2\langle\hat\Omega\rangle\langle\hat\Omega\rangle+\langle\hat\Omega\rangle^2=\langle\hat\Omega^2\rangle-\langle\hat\Omega\rangle^2$. This is the form used for $\Delta x$ and $\Delta p$ in the oscillator sections below. For an eigenstate, $\Delta\hat\Omega=0$.

!!! memory "Memory Rule"

    “Mean of the square minus square of the mean.” It is never negative, and it vanishes only when $|\psi\rangle$ is an eigenstate of the operator.

### Summary of the formalism so far

1.  The state is a vector $|\psi\rangle$ in a Hilbert space.

2.  Observables are Hermitian operators, e.g. $\hat\Omega$: eigenvalues are real and eigenvectors are orthogonal.

3.  A measurement gives an eigenvalue with probability $|\langle\omega_i|\psi\rangle|^2$ and collapses the state to $|\omega_i\rangle$.

4.  Between measurements, the state evolves by the Schrödinger equation ([Section 4](04-time-evolution-stationary-states-schrodinger-heisenberg.md)).
