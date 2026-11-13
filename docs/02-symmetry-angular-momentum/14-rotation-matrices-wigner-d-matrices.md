---
title: "Rotation Matrices (Wigner D-Matrices)"
part: 2
chapter: 14
source_book: 
source_section: 
exam_asked: []
topics: []
---

# 14 Rotation Matrices (Wigner $D$-Matrices)

## 14.1 Rotations Do Not Change $j$

Let $\chi(\hat{\vec J}\,)$ be any function of the angular momentum operator. Since $\hat J^2$ commutes with every component, $[\hat J^2,\chi(\hat{\vec J}\,)]=0$, and so

$$
\langle j,m|[\hat J^2,\chi]|j',m'\rangle=\hbar^2\big[j(j+1)-j'(j'+1)\big]\langle j,m|\chi(\hat{\vec J}\,)|j',m'\rangle=0 .
$$

!!! thm "Block Structure"

    $$
    \langle j,m|\chi(\hat{\vec J}\,)|j',m'\rangle=\delta_{jj'}\,\langle j,m|\chi(\hat{\vec J}\,)|j,m'\rangle .
    $$

The rotation operator $\hat U_{\hat n}(\phi)=\exp(-\tfrac i\hbar\phi\,\hat n\cdot\hat{\vec J})$ is such a function, so it only mixes states of the same $j$.

## 14.2 Definition of the $D$-Matrix

!!! thm "Wigner $D$-Matrix"

    $$
    \hat U|j,m\rangle=\sum_{m'}|j,m'\rangle\,D^j_{m'm}(\hat U),\qquad D^j_{m'm}(\hat U)=\langle j,m'|\hat U|j,m\rangle ,
    $$

    a $(2j+1)\times(2j+1)$ unitary matrix. ($D$ is for *Drehung*, German for rotation.)

!!! studynote "Study Note"

    The notebook writes the indices as $D^j_{mm'}=\langle j,m'|\hat U|j,m\rangle$ in one place and as $\langle j,m|\hat U|j,m'\rangle$ in another. Here the standard placement $D^j_{m'm}=\langle j,m'|\hat U|j,m\rangle$ (row $m'$, column $m$) is used throughout, so that $D$ is literally the matrix of $\hat U$.

For $j=\tfrac12$ and rotation by $\phi$ about $\hat n$, with $\hat U_{\hat n}(\phi)=\mathbb 1\cos\frac\phi2-i\hat{\vec\sigma}\cdot\hat n\sin\frac\phi2$,

$$
D^{1/2}_{m'm}(\hat n,\phi)=\cos\frac\phi2\,\delta_{m'm}-i\sin\frac\phi2\,\langle m'|\hat{\vec\sigma}\cdot\hat n|m\rangle=
\begin{pmatrix}\cos\frac\phi2-in_z\sin\frac\phi2&(-in_x-n_y)\sin\frac\phi2\\(-in_x+n_y)\sin\frac\phi2&\cos\frac\phi2+in_z\sin\frac\phi2\end{pmatrix}.
$$

## 14.3 Euler Angles

Any rotation can be built from three rotations: about $z$ by $\alpha$, about the new $y$ by $\beta$ and about $z$ by $\gamma$. In terms of the operators,

$$
\hat U(\alpha,\beta,\gamma)=\hat U(z,\alpha)\,\hat U(y,\beta)\,\hat U(z,\gamma).
$$

Its matrix elements are

\begin{align*}
D^j_{m'm}(\alpha,\beta,\gamma)&=\langle j,m'|\hat U(z,\alpha)\hat U(y,\beta)\hat U(z,\gamma)|j,m\rangle\\
&=\sum_{m_1,m_2}\langle j,m'|\hat U(z,\alpha)|j,m_1\rangle\ \langle j,m_1|\hat U(y,\beta)|j,m_2\rangle\ \langle j,m_2|\hat U(z,\gamma)|j,m\rangle .
\end{align*}

The $z$-rotations are diagonal because $\hat J_z|j,m\rangle=\hbar m|j,m\rangle$:

$$
\langle j,m'|e^{-i\hat J_z\alpha/\hbar}|j,m_1\rangle=e^{-im'\alpha}\delta_{m'm_1},\qquad
\langle j,m_2|e^{-i\hat J_z\gamma/\hbar}|j,m\rangle=e^{-im\gamma}\delta_{m_2m}.
$$

Defining the reduced matrix $d^j_{m'm}(\beta)=\langle j,m'|\hat U(y,\beta)|j,m\rangle$,

!!! thm "Euler-Angle Form of the $D$-Matrix"

    $$
    D^j_{m'm}(\alpha,\beta,\gamma)=e^{-im'\alpha}\,d^j_{m'm}(\beta)\,e^{-im\gamma}.
    $$

!!! studynote "Study Note"

    The notebook writes $\hat U(y,\alpha)$ in the middle factor; the second rotation is through the angle $\beta$, which is what the following line of the notebook uses.

For $j=\tfrac12$, $\hat d^{1/2}(\beta)=e^{-i\beta\hat J_y/\hbar}=e^{-\frac i2\beta\hat\sigma_y}$, so

$$
\hat d^{1/2}(\beta)=\mathbb 1\cos\frac\beta2-i\hat\sigma_y\sin\frac\beta2=\begin{pmatrix}\cos\frac\beta2&-\sin\frac\beta2\\ \sin\frac\beta2&\cos\frac\beta2\end{pmatrix}.
$$

!!! solution "Complete Solution"

    For $j=1$ (using $\hat J_y$ from [Section 13](13-j-1-representation-angular-momentum-uncertainty.md)), in the basis $m=1,0,-1$,

    $$
    d^1(\beta)=\begin{pmatrix}\frac{1+\cos\beta}2&-\frac{\sin\beta}{\sqrt2}&\frac{1-\cos\beta}2\\[2pt]\frac{\sin\beta}{\sqrt2}&\cos\beta&-\frac{\sin\beta}{\sqrt2}\\[2pt]\frac{1-\cos\beta}2&\frac{\sin\beta}{\sqrt2}&\frac{1+\cos\beta}2\end{pmatrix}.
    $$

!!! memory "Memory Rule"

    $z$-rotations only give phases $e^{-im\,(\text{angle})}$. All the mixing among different $m$ sits in the single middle matrix $d^j(\beta)$.
