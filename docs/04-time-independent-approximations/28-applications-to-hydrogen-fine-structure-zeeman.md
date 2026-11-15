---
title: "Applications to Hydrogen: Fine Structure and the Zeeman Effect"
part: 4
chapter: 28
source_book: "Griffiths and Schroeter, Introduction to Quantum Mechanics (3rd ed.)"
source_section: "7.3, 7.4"
exam_asked: []
topics: []
---

# 28 Applications to Hydrogen: Fine Structure and the Zeeman Effect

## 28.1 Spin-Orbit Coupling

In the rest frame of the electron the proton circles around it and produces a magnetic field. For an electron moving with velocity $\vec v$ in the proton’s electric field $\vec E$ (Gaussian units):

$$
\vec B = -\frac1c\,\vec v\times\vec E = -\frac{1}{m_ec}\,\vec p\times\vec E = \frac{1}{m_ec}\,(\vec E\times\vec p)
$$

![](../assets/figures/28-applications-to-hydrogen-fine-structure-zeeman-fig1.svg){ .fig }

For a central potential, with $V(r) = -e\phi(r)$ and $\vec E = -\nabla\phi$:

$$
\vec E(\vec r) = \frac{1}{e}\frac{\vec r}{r}\frac{dV}{dr}
\quad\Longrightarrow\quad
\vec B = \frac{1}{e\,m_e c}\,\frac1r\frac{dV}{dr}\,(\vec r\times\vec p) = \frac{1}{m_e e c\, r}\frac{dV}{dr}\,\vec L
$$

The electron’s spin magnetic moment is $\vec\mu_s = -\dfrac{e}{m_ec}\vec S$, and the interaction energy $-\vec\mu_s\cdot\vec B$ gives the spin-orbit Hamiltonian

!!! thm "Spin-Orbit Hamiltonian"

    $$
    \hat H_{\text{soc}} = \lambda\,\hat{\vec L}\cdot\hat{\vec S}, \qquad \lambda = \lambda(r) = \frac{1}{2m_e^2c^2}\frac1r\frac{dV}{dr}\ \xrightarrow{\,V=-e^2/r\,}\ \frac{e^2}{2m_e^2c^2}\frac{1}{r^3}
    $$

!!! studynote "Study Note"

    The naive calculation above gives a prefactor $1/(m_e^2c^2)$; the factor $\tfrac12$ in $\lambda$ is the **Thomas precession** correction (the electron’s rest frame is accelerating). The notebook uses the correct final form $\lambda = e^2/(2m_e^2c^2r^3)$. In SI units replace $e^2\to e^2/4\pi\varepsilon_0$.

The hydrogen problem with spin-orbit coupling is

$$
\hat H = \underbrace{\frac{\hat p^2}{2m_e} - \frac{e^2}{r}}_{\hat H^0} + \underbrace{\frac{e^2}{2m_e^2c^2r^3}\,\hat{\vec L}\cdot\hat{\vec S}}_{\hat H_{\text{soc}}} = \hat H^0 + \hat H'
$$

## 28.2 Choice of Basis: Which States Are Good?

-   **Uncoupled basis** $|n,l,s,m_l,m_s\rangle$, eigenstates of $\{\hat L^2,\hat S^2,\hat L_z,\hat S_z\}$. This is **not good**: $\hat{\vec L}\cdot\hat{\vec S}$ does not commute with $\hat L_z$ or $\hat S_z$, so $\hat H_{\text{soc}}$ is not diagonal in it and the degenerate levels are mixed.

-   **Coupled basis** $|n,j,m_j,l,s\rangle$, eigenstates of $\{\hat J^2,\hat J_z,\hat L^2,\hat S^2\}$ with $\hat{\vec J} = \hat{\vec L}+\hat{\vec S}$. This is **good**: $\hat J^2$ and $\hat J_z$ commute with $\hat H^0$ and with $\hat H_{\text{soc}}$, so by the theorem of [Section 27](27-time-independent-perturbation-theory-degenerate-case.md) the off-diagonal elements between different $j,m_j$ vanish.

Using $\hat{\vec L}\cdot\hat{\vec S} = \tfrac12\big(\hat J^2 - \hat L^2 - \hat S^2\big)$, the first-order energy is

$$
E_{\text{soc}} = \langle n,j,m_j,l,s|\,\lambda\hat{\vec L}\cdot\hat{\vec S}\,|n,j,m_j,l,s\rangle
= \frac{e^2\hbar^2}{4m_e^2c^2}\Big[j(j+1) - l(l+1) - s(s+1)\Big]\Big\langle n l\Big|\frac1{r^3}\Big|n l\Big\rangle
$$

with $s(s+1)=\tfrac34$ and the standard hydrogen expectation value

$$
\Big\langle n l\Big|\frac{1}{r^3}\Big|n l\Big\rangle = \frac{2}{n^3\,l(l+1)(2l+1)\,a_0^3}
$$

!!! thm "Spin-Orbit Energy of Hydrogen"

    \begin{align*}
    E_{nlj} &= -\frac{e^2}{2a_0}\frac1{n^2} + E_{\text{soc}}\\
    E^{\text{soc}}_n &= \frac{e^2\hbar^2}{2m_e^2c^2}\left[\frac{j(j+1)-l(l+1)-\tfrac34}{n^3\,l(l+1)(2l+1)\,a_0^3}\right]\\
    &= \frac{|E_n^{(0)}|}{n}\,\alpha^2\left[\frac{j(j+1)-l(l+1)-\tfrac34}{l(l+1)(2l+1)}\right]
    \end{align*}

    with $E_n^{(0)} = -\dfrac{e^2}{2a_0n^2} = -\dfrac{\alpha^2m_ec^2}{2n^2}$, fine-structure constant $\alpha = \dfrac{\hbar}{m_eca_0} = \dfrac{e^2}{\hbar c}\simeq\dfrac1{137}$, and Bohr radius $a_0 = \dfrac{\hbar^2}{m_ee^2}$.

!!! studynote "Study Note (sign)"

    In the notebook the last form is written with $E_n^{(0)}$ (a negative number) in front. With $E_n^{(0)}<0$ that would make $E_n^{\text{soc}}$ negative for $j=l+\tfrac12$, which contradicts the first form (positive for $j=l+\frac12$). The correct prefactor is $|E_n^{(0)}| = -E_n^{(0)}$, as written above. Check: $|E_n^{(0)}|\alpha^2/n = \alpha^4m_ec^2/(2n^3)$, and $\frac{e^2\hbar^2}{2m_e^2c^2a_0^3} = |E_1^{(0)}|\alpha^2$.

!!! studynote "Study Note"

    For $l=0$ the expression is $0/0$ but there is no spin-orbit energy ($\hat{\vec L}=0$, so $\hat H_{\text{soc}}=0$). The relative size is $\sim\alpha^2\approx 5\times10^{-5}$ of $E_n^{(0)}$, which is why it is called *fine* structure.

## 28.3 Relativistic Correction

The kinetic energy is $\hat T = \sqrt{\hat p^2c^2 + m_e^2c^4} - m_ec^2 = m_ec^2\sqrt{1+\dfrac{\hat p^2}{m_e^2c^2}} - m_ec^2$. Expanding in $p/m_ec$:

$$
\hat T = \frac{\hat p^2}{2m_e} - \frac18\frac{\hat p^4}{m_e^3c^2} + \cdots
$$

so the Hamiltonian with relativistic correction is

$$
\hat H = \underbrace{\frac{\hat p^2}{2m_e} - \frac{e^2}{r}}_{\hat H^0} \underbrace{-\,\frac{\hat p^4}{8m_e^3c^2}}_{\hat H_R} = \hat H^0 + \hat H_R
$$

First-order perturbation correction:

$$
E'_{\text{Rel}} = \Big\langle n\,l\,s\,j\,m_j\Big|\hat p^4\Big|n\,l\,s\,j\,m_j\Big\rangle\Big(-\frac{1}{8m_e^3c^2}\Big) = -\frac{\alpha^4m_ec^2}{8n^4}\Big(\frac{8n}{2l+1}-3\Big)
$$

!!! studynote "Study Note (sign)"

    The notebook shows the same quantity once more as $\frac{\alpha^2|E_n^{(0)}|}{4n^2}\big(\frac{8n}{2l+1}-3\big)$ without the minus sign. Since $\frac{\alpha^2|E_n^{(0)}|}{4n^2}=\frac{\alpha^4m_ec^2}{8n^4}$, the correct form is $E'_{\text{Rel}} = -\dfrac{\alpha^2|E_n^{(0)}|}{4n^2}\Big(\dfrac{8n}{2l+1}-3\Big)$, always negative (relativistic effects lower the energy).

!!! solution "Complete Solution"

    *(evaluating $\langle\hat p^4\rangle$):* From $\hat H^0|\psi\rangle = E_n|\psi\rangle$ we have $\hat p^2 = 2m_e(E_n + e^2/r)$ on the state, so

    $$
    \langle\hat p^4\rangle = 4m_e^2\Big\langle\Big(E_n+\frac{e^2}{r}\Big)^2\Big\rangle = 4m_e^2\Big[E_n^2 + 2E_ne^2\Big\langle\frac1r\Big\rangle + e^4\Big\langle\frac1{r^2}\Big\rangle\Big]
    $$

    with $\langle 1/r\rangle = \dfrac{1}{n^2a_0}$ and $\langle 1/r^2\rangle = \dfrac{1}{(l+\frac12)\,n^3a_0^2}$, $E_n=-\dfrac{e^2}{2a_0n^2}$:

    $$
    E'_{\text{Rel}} = -\frac{1}{2m_ec^2}\,\frac{e^4}{a_0^2}\Big[\frac1{4n^4} - \frac1{n^4} + \frac{2}{n^3(2l+1)}\Big]
    = -\frac{e^4}{8m_ec^2a_0^2n^4}\Big(\frac{8n}{2l+1}-3\Big)
    $$

    and $e^4/a_0^2 = \alpha^4m_e^2c^4$ gives the result above.

!!! studynote "Study Note"

    $\hat p^4$ is a scalar and commutes with $\hat L^2,\hat L_z$, so the hydrogen states $|n,l,m\rangle$ are already good states and no degenerate diagonalization is required.

## 28.4 Fine Structure

Spin-orbit coupling plus the relativistic correction together form the **fine structure**:

!!! thm "Fine-Structure Correction to the Energy"

    $$
    E^{(1)}_{\text{FS}} = \frac{\alpha^4m_ec^2}{2n^3}\left[\frac{j(j+1)-l(l+1)-\tfrac34}{l(l+1)(2l+1)}\right] - \frac{\alpha^4m_ec^2}{8n^4}\left[\frac{8n}{2l+1}-3\right]
    $$

!!! solution "Complete Solution (simplification)"

    For $j=l+\tfrac12$ the bracket $j(j+1)-l(l+1)-\frac34$ equals $l$; for $j=l-\tfrac12$ it equals $-(l+1)$. In both cases the two terms combine to

    $$
    E^{(1)}_{\text{FS}} = -\frac{\alpha^4m_ec^2}{8n^4}\Big(\frac{4n}{j+\frac12}-3\Big) = -\frac{(E_n^{(0)})^2}{2m_ec^2}\Big(\frac{4n}{j+\frac12}-3\Big)
    $$

Check for $j=l+\tfrac12$: spin-orbit term $\frac{\alpha^4m_ec^2}{2n^3(l+1)(2l+1)}$; combining with the relativistic term gives $\frac{8n}{2l+1}-3-\frac{4n}{(l+1)(2l+1)} = \frac{4n}{l+1}-3 = \frac{4n}{j+1/2}-3$.

!!! studynote "Study Note (the case $l=0$ and the Darwin term)"

    The simplification above uses $j(j+1)-l(l+1)-\frac34=l$ for $j=l+\frac12$ and then cancels a factor $l$ against the denominator, which is only legitimate for $l\ge1$. For an $s$ state there is no spin-orbit energy, and the relativistic term alone gives $-\frac{\alpha^4m_ec^2}{8n^4}(8n-3)$, not $-\frac{\alpha^4m_ec^2}{8n^4}(4n-3)$. The difference, $+\frac{\alpha^4m_ec^2}{2n^3}$, is supplied by the **Darwin term** $\hat H_D=\frac{\pi e^2\hbar^2}{2m_e^2c^2}\delta^3(\vec r)$ (Gaussian units), whose expectation value in an $s$ state is $\frac{\pi e^2\hbar^2}{2m_e^2c^2}|\psi_{n00}(0)|^2=\frac{\alpha^4m_ec^2}{2n^3}$ since $|\psi_{n00}(0)|^2=1/\pi n^3a_0^3$. So the formula in terms of $n$ and $j$ holds for $s$ states too, but only after the Darwin term is included.

!!! book "See also: Shankar, Principles of Quantum Mechanics (2nd ed.), section 20.2"

    The Darwin term is derived from the Dirac equation in Shankar's section 20.2 (Eqs. 20.2.37 and 20.2.38, p. 573), where $\langle n00|\hat H_D|n00\rangle=\frac{\alpha^4m_ec^2}{2n^3}$ as used above. Shankar also notes that the spin-orbit expression, applied formally at $l=0$, happens to reproduce exactly this shift.

!!! examtip "Exam Tip"

    The fine-structure shift depends only on $n$ and $j$, not on $l$ separately (e.g. the $2S_{1/2}$ and $2P_{1/2}$ levels stay degenerate at this order).

## 28.5 Anomalous Zeeman Effect

In a magnetic field the Hamiltonian acquires

$$
\hat H_B = -\vec\mu_L\cdot\vec B - \vec\mu_s\cdot\vec B = \frac{e}{2m_ec}\,\vec L\cdot\vec B + \frac{e}{m_ec}\,\vec S\cdot\vec B
$$

Take $\vec B = B_0\hat e_z$. Then

$$
\hat H_B = \frac{eB_0}{2m_ec}\big(\hat L_z + 2\hat S_z\big) = \frac{eB_0}{2m_ec}\big(\hat J_z + \hat S_z\big) = \frac{\mu_BB_0}{\hbar}\big(\hat J_z+\hat S_z\big), \qquad \mu_B = \frac{e\hbar}{2m_ec}\ (\text{Bohr magneton})
$$

and the full Hamiltonian is

$$
\boxed{\hat H = \hat H^0 + \hat H_{\text{soc}} + \hat H_R + \hat H_B}
$$

Two limiting regimes are treated (the relativistic term is neglected in the first):

1.  **Strong field, $\hat H_B \gg \hat H_{\text{soc}}$:** $\hat H = \hat H^0+\hat H_B$, use the uncoupled basis $|n,l,s,m_l,m_s\rangle$:

    $$
    E^{(1)}_B = \frac{eB_0}{2m_ec}\langle n l s m_l m_s|(\hat L_z+2\hat S_z)|n l s m_l m_s\rangle = \frac{eB_0\hbar}{2m_ec}\,(m_l+2m_s)
    $$

    !!! thm "Paschen-Back Effect"

        $$
        E^{\prime}_{(B)} = \frac{eB_0\hbar}{2m_ec}\,(m_l + 2m_s)
        $$

2.  **Weak field, $\hat H_{FS}=\hat H_{\text{soc}}+\hat H_R \gg \hat H_B$:** $\hat H = \hat H^0+\hat H_{FS}+\hat H_B$, use the coupled basis $|n,j,m_j,l,s\rangle$:

    $$
    E^{(1)}_B = \frac{eB_0}{2m_ec}\Big[\hbar m_j + \langle n l s j m_j|\hat S_z|n l s j m_j\rangle\Big]
    $$

    By the projection theorem

    $$
    \langle\hat S_z\rangle = \frac{\langle\hat{\vec J}\cdot\hat{\vec S}\rangle}{\hbar^2j(j+1)}\,\langle\hat J_z\rangle, \qquad \hat{\vec J}\cdot\hat{\vec S} = \tfrac12\big(\hat J^2+\hat S^2-\hat L^2\big)
    $$

    which gives the Landé result:

    !!! thm "Weak-Field Zeeman Energy and the Landé $g$-Factor"

        $$
        E^{(1)}_B = \frac{eB_0\hbar}{2m_ec}\,g_J\,m_j, \qquad g_J = 1 + \frac{j(j+1) - l(l+1) + s(s+1)}{2j(j+1)}
        $$

!!! solution "Complete Solution (fine structure on top of the Paschen-Back levels) || Griffiths, Eq. 7.86 (Problem 7.26)"

    The strong-field energy above keeps only $\hat H^0+\hat H_B$. The fine-structure terms can be added as a first-order correction, because the states $|n,l,m_l,m_s\rangle$ are also good states for them: $\hat H_{FS}$ commutes with $\hat L^2$ and $\hat J_z$, and by the theorem of [Section 27.4](27-time-independent-perturbation-theory-degenerate-case.md) these two operators separate the states that share the same $m_l+2m_s$.

    For the spin-orbit term, $|l,m_l\rangle|s,m_s\rangle$ is a product state with $\langle\hat L_x\rangle=\langle\hat L_y\rangle=\langle\hat S_x\rangle=\langle\hat S_y\rangle=0$, so $\langle\hat{\vec L}\cdot\hat{\vec S}\rangle=\hbar^2m_lm_s$. With $\langle1/r^3\rangle=1/\big(n^3l(l+\tfrac12)(l+1)a_0^3\big)$ and $\frac{e^2\hbar^2}{2m_e^2c^2a_0^3}=|E_1^{(0)}|\alpha^2$,

    $$
    E_{\text{so}}=\frac{|E_1^{(0)}|\,\alpha^2}{n^3}\,\frac{m_lm_s}{l(l+\frac12)(l+1)}
    $$

    The relativistic term of [Section 28.3](#283-relativistic-correction) can be rewritten with $\alpha^4m_ec^2/8n^4=|E_1^{(0)}|\alpha^2/4n^4$:

    $$
    E_{\text{rel}}=-\frac{|E_1^{(0)}|\,\alpha^2}{4n^4}\Big(\frac{8n}{2l+1}-3\Big)=\frac{|E_1^{(0)}|\,\alpha^2}{n^3}\Big[\frac3{4n}-\frac{l(l+1)}{l(l+\frac12)(l+1)}\Big]
    $$

    Adding the two,

    $$
    E^{(1)}_{\text{FS}}=\frac{|E_1^{(0)}|\,\alpha^2}{n^3}\left\{\frac3{4n}-\frac{l(l+1)-m_lm_s}{l(l+\frac12)(l+1)}\right\}
    $$

    The total strong-field energy is $-\dfrac{13.6\ \text{eV}}{n^2}+\mu_BB_0(m_l+2m_s)+E^{(1)}_{\text{FS}}$. The fraction is indeterminate for $l=0$; once the Darwin term is included its value there is $1$ (see the Study Note in [Section 28.4](#284-fine-structure) and Griffiths Problem 7.28).

!!! studynote "Study Note (sign in the Landé factor)"

    The notebook prints the numerator as $j(j+1)-l(l+1)-s(s+1)$. Since $\langle\hat{\vec J}\cdot\hat{\vec S}\rangle = \frac{\hbar^2}{2}[j(j+1)+s(s+1)-l(l+1)]$, the $s(s+1)$ term carries a **plus** sign. Check: for $l=0$, $j=s=\tfrac12$ the free electron must give $g=2$: $1+\frac{3/4+3/4}{3/2}=2$ (the printed sign would give $g=1$).

!!! studynote "Study Note (regimes)"

    The notebook labels the second regime as “$H_{soc}\sim H_B$”; the computation with $|n,j,m_j,l,s\rangle$ as good states is valid when $\hat H_B$ is small compared with the fine structure (weak field). If $\hat H_B$ is comparable to $\hat H_{FS}$, $\hat H_B+\hat H_{FS}$ must be diagonalized inside each $m_j$ subspace.

!!! examtip "Exam Tip"

    Quick values for hydrogen with $n=2$: $2S_{1/2}$: $g_J=2$; $2P_{1/2}$: $g_J=\frac23$; $2P_{3/2}$: $g_J=\frac43$. Weak-field levels split into $2j+1$ equally spaced lines (spacing $g_J\mu_BB_0$).

!!! mistakes "Common mistakes"

    \(a\) using the uncoupled basis when spin-orbit coupling is present, (b) writing $m_l+m_s$ instead of $m_l+2m_s$ (the spin $g$-factor is 2), (c) forgetting that $g_J$ depends on $l$, $s$ and $j$, (d) using $E_n^{(0)}$ instead of $|E_n^{(0)}|$ in the spin-orbit prefactor.

!!! book "See also: Griffiths, Introduction to Quantum Mechanics (3rd ed.), sections 7.4.3 and 7.5"

    Two things the notes do not work out. In the intermediate-field regime ($\hat H_B$ comparable to $\hat H_{FS}$, section 7.4.3) the good states are mixtures of $|j=l\pm\frac12,m_j\rangle$ with the same $m_j$, so $\hat H_B+\hat H_{FS}$ is diagonalized in a $2\times2$ block for each $m_j$ (for $n=2$, Problems 7.29 and 7.30). Section 7.5 treats the hyperfine splitting of hydrogen, the origin of the 21 cm line.
