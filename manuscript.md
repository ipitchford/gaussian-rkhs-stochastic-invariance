---
title: "When Gaussian kernel spaces are invariant under stochastic dynamics"
subtitle: "Transition rigidity, a Gaussian-component noise boundary and a discontinuous diffusion limit"
author: "Anonymous"
date: "9 November 2026"
lang: en-GB
documentclass: article
fontsize: 11pt
geometry:
  - a4paper
  - margin=26mm
colorlinks: true
linkcolor: plum
urlcolor: pine
header-includes:
  - \usepackage{amsmath,amssymb,amsthm,mathtools}
  - \usepackage{microtype}
  - \usepackage{xcolor}
  - \usepackage{xurl}
  - \usepackage{needspace}
  - \definecolor{plum}{HTML}{76456D}
  - \definecolor{pine}{HTML}{386D64}
---

# Abstract {.unnumbered}

Kernel methods for stochastic Koopman operators often assume that the dynamics map a chosen Gaussian reproducing kernel Hilbert space (RKHS) into itself. We determine when this can happen. First, if a Markov transition has Gaussian conditional laws \(N(F(x),Q(x))\) with arbitrary Borel parameter fields, boundedness between two global Gaussian RKHSs forces the covariance to be constant, the mean to be affine with full column rank, and an exact matrix inequality \(MRM^\top\preceq P+4Q\). Second, for additive noise whose characteristic function has a Gaussian lower bound, which includes every infinitely divisible law with or without a Gaussian part, a Borel drift must be affine; for infinitely divisible noise only the Gaussian covariance component enters the matrix boundary. Third, a compound-Poisson approximation of a stable linear diffusion converges in operator norm from the RKHS to bounded continuous functions at sharp order \(\varepsilon^2\), while at time \(t=1/10\) every approximating transition sends one fixed Gaussian observable outside the RKHS. As an application, the Ornstein--Uhlenbeck criterion is \(AP+PA^\top\preceq4BB^\top\). Philipp et al. (2025a) proved sufficiency of \(AP+PA^\top\preceq2BB^\top\) and left necessity "as an open problem"; a stable controllable shear shows that it is not necessary. That fixed affine criterion is a specialisation of classical Gaussian-Fock operator theory, the same witness and a detailed proposed analytic derivation, including the all-time route for this witness, appeared in a public preregistration on 28 October 2026, which explicitly disclaimed a completed proof or formal verification. We also give an admissible-bandwidth rule, its consequence for an existing kernel EDMD error bound, sampling thresholds, and exact growth and finite-rank statements in the kernel norm.

**Keywords:** Koopman operator; reproducing kernel Hilbert space; Gaussian kernel; Ornstein--Uhlenbeck process; Lévy noise; covariance rigidity; kernel EDMD; bandwidth selection.

*Status.* Version 0.1.1-candidate (9 November 2026), archived at <https://doi.org/10.5281/zenodo.24089772> (all versions: <https://doi.org/10.5281/zenodo.23937399>; version 0.1.0-candidate: <https://doi.org/10.5281/zenodo.23937400>). AI-assisted research paper, not externally refereed; internal AI-assisted review only. Finite checks are supplied as scripts; no proof-assistant verification has been done.

*Changes in 0.1.1.* Wording and citations only; theorems, proofs, figures and code are unchanged. The journal numbering of Philipp et al. (2025a) is now stated (Section 1.1). Section 3 now compares Theorem 5 with Holevo (2017, Theorem 1) and Alekseev, Afonin and Bogachev (2021) precisely, and records that Sang and Zhao (2026) reproduce criterion (26) in one variable. The originality boundary for Theorem 5 in Section 1.4 now reads "covariance rigidity from RKHS boundedness".

# Introduction

## The question

Kernel methods learn the evolution of observables by approximating the linear operator \(K^tf(x)=\mathbb E[f(X_t)\mid X_0=x]\). Kernel extended dynamic mode decomposition (kEDMD) and related methods represent \(K^t\) on a reproducing kernel Hilbert space (RKHS) of functions. Much of the error analysis assumes that the RKHS is *invariant*: evolving any observable in the space gives another member of the space. Under this assumption \(K^t\) is a well-defined bounded operator from the RKHS to itself, and error bounds can be stated in terms of its norm. For example, the second estimate of Philipp et al. (2025b), Theorem 4.2, assumes \(K^t\mathcal H_{\mathcal Y}\subset\mathcal H_{\mathcal X}\). Invariance concerns every observable in an infinite-dimensional space, not only a finite dictionary used in a computation.

The Gaussian kernel is the default choice. For a positive definite matrix \(P\) we write
\[
k_P(x,y)=\exp[-(x-y)^\top P^{-1}(x-y)],
\]
and \(\mathcal H_P\) for its RKHS on the whole of \(\mathbb R^d\). This paper asks which stochastic dynamics leave \(\mathcal H_P\) invariant, or more generally map \(\mathcal H_P\) boundedly into another Gaussian RKHS \(\mathcal H_R\).

The question has a published starting point. For \(dX_t=AX_t\,dt+B\,dW_t\) with Hurwitz \(A\) and controllable \((A,B)\), Philipp et al. (2025a), Theorem 2.1, prove that \(\mathcal H_P\) is invariant under every \(K^t\) if \(AP+PA^\top\preceq2BB^\top\). Their notation is \(P=C^2\). In the arXiv version (arXiv:2405.14429v1) the abstract states: "The question of whether the sufficient Lyapunov-condition is also necessary is left as an open problem." Remark 2.2(c) reads: "It is not clear whether the condition (2.3) is also necessary for Koopman invariance of \(\mathbb H_C\). We discuss this at the end of Section 4." Remark 4.2 reads: "It is not clear whether the statement of Theorem 2.1 is actually an equivalence." We quote the arXiv version. The journal version (PAMM 25(1), e202400127) has the same numbering for Theorem 2.1, Remark 2.2(c), Proposition 3.3, Proposition 4.1 and Remark 4.2, and the same wording of the quoted sentences, except that its Remark 2.2(c) refers to the condition as (3).

## Main results in brief

The headline result is a rigidity statement. Informally:

> **Theorem A (Theorems 5 and 9).** Suppose a Markov transition maps a global Gaussian RKHS \(\mathcal H_P(\mathbb R^m)\) into a global Gaussian RKHS \(\mathcal H_R(\mathbb R^d)\). If its conditional laws are Gaussian, \(N(F(x),Q(x))\), then \(Q\) is constant and \(F\) is affine. If instead it has the form \(x\mapsto F(x)+Z\) with state-independent noise \(Z\) whose characteristic function has a Gaussian lower bound (for example any Lévy increment), then \(F\) is affine. In both cases the mean matrix \(M\) has full column rank and, for Gaussian or infinitely divisible noise with Gaussian covariance component \(Q\), boundedness holds exactly when \(MRM^\top\preceq P+4Q\).

No continuity or smoothness of \(F\) or \(Q\) is assumed. Within these two transition classes, nonlinear drift and genuinely state-dependent Gaussian covariance therefore cannot map one global Gaussian RKHS into another, at any time step. Arbitrary state-dependent non-Gaussian transitions are not covered.

Two further results describe the boundary.

* **The noise boundary (Theorems 8 and 11).** For affine maps with infinitely divisible noise, only the Gaussian covariance component determines which Gaussian bandwidths are admissible. Jumps change the image norm, but cannot repair a violation of the matrix inequality.
* **A discontinuous diffusion limit (Theorem 12, Proposition 13).** Compound-Poisson forcing with jumps \(\pm\varepsilon\) converges to Brownian forcing. For the stable shear below, the prediction operators converge in the norm from \(\mathcal H_I\) to bounded continuous functions, with sharp order \(\varepsilon^2\) and limiting constant \(\approx0.0993\). Yet at \(t=1/10\) every prelimit sends the fixed observable \(e^{-8|x|^2/5}\) outside \(\mathcal H_I\), while the Brownian limit keeps it inside.

The Ornstein--Uhlenbeck (OU) question is then an application. All-time invariance holds exactly when
\[
AP+PA^\top\preceq4BB^\top,
\]
with no stability or controllability assumption (Theorem 6). The stable controllable shear
\[
A=\begin{pmatrix}-1&5\\0&-1\end{pmatrix},\qquad B=P=I_2,
\]
satisfies this inequality but not the published sufficient condition: the slack \(2I-(A+A^\top)\) has eigenvalues \(-1\) and \(9\), while \(4I-(A+A^\top)\) has eigenvalues \(1\) and \(11\). So the published sufficient condition is not necessary.

The factor 4 has a simple source. Averaging a single kernel section over Gaussian noise \(N(0,Q)\) broadens it to the matrix \(P+2Q\). The norm of the whole image space involves the correlation of two independent noise copies, whose difference has covariance \(2Q\); this gives \(P+4Q\) (Lemma 2 and Proposition 3). Philipp et al. use the first object in their image-space inclusion; the second is the one that decides invariance. For the shear, \(I+2Q_t-M_tM_t^\top\) is indefinite at \(t=0.05\) while \(I+4Q_t-M_tM_t^\top\) is positive definite.

## What this means for kernel Koopman learning

For readers who use Gaussian-kernel Koopman models, the results say four things.

1. **Rigidity within the covered transition classes.** Within the transition classes covered here (Gaussian conditional laws, or fixed additive noise satisfying (40)) global Gaussian RKHS invariance forces an affine state map; in the Gaussian case the conditional covariance must also be constant (Theorems 5 and 9). This applies to the specified Euler--Maruyama steps and Lévy-driven Euler steps, not to arbitrary finite-time transitions of nonlinear SDEs.
2. **For linear Gaussian models there is an exact bandwidth rule.** The bandwidth matrix \(P\) is admissible at all times exactly when \(AP+PA^\top\preceq4BB^\top\). For an isotropic width \(P=\sigma^2I\) and invertible \(BB^\top\), this reads \(\sigma^2\le4/\lambda_{\max}\big((BB^\top)^{-1/2}(A+A^\top)(BB^\top)^{-1/2}\big)\) when this largest eigenvalue is positive; otherwise every \(\sigma^2>0\) is admissible. This is twice the range certified before (Section 8). The rule never binds for a stable scalar OU process, or whenever \(A+A^\top\preceq0\). It binds for strongly nonnormal stable drift such as shears, and for unstable drift. When it fails, sampling less often can restore invariance at the step used (Section 7).
3. **A positive consequence for an existing error bound.** The invariance hypothesis of Philipp et al. (2025b), Theorem 4.2, holds, under their remaining assumptions, for every multivariate OU process with square \(B\) and nondegenerate \(Q_t\) whose sampling time satisfies the exact fixed-time criterion (Corollary 18). Previously it had been verified only for the scalar OU process.
4. **In the global kernel norm, finite-rank approximation cannot help.** For a bounded square affine Gaussian transition, the distance to finite-rank operators in the \(\mathcal H_P\to\mathcal H_P\) norm equals the full operator norm (Theorem 20). Useful learning guarantees must therefore be stated in weaker norms, such as \(L^2\) of a data distribution or a compact-region supremum norm. Nothing here implies that finite-data kEDMD predictions fail.

The global Gaussian RKHS also behaves unexpectedly for stable dynamics: its operator norm grows like \(e^{-t\operatorname{tr}A/2}\) (Theorem 6). This is not a contradiction. The space contains no nonzero constants, and as stable drift contracts starting points, the predicted observable \(x\mapsto\mathbb E f(X_t)\) spreads out over a larger region of starting points, which costs kernel norm. The process is still stable in the usual sense, and \(\|K^tf\|_\infty\le\|f\|_\infty\). For learning with stable dynamics, spaces adapted to an invariant or data measure, and transfer-operator formulations that do not require invariance (for example Klus, Schuster and Muandet, 2020), may be more natural targets than invariance of the global Gaussian RKHS.

## Relation to prior work, and what is new

Much of the toolkit is established. Gaussian Fourier representations and deterministic composition rigidity are in Ikeda, Ishikawa and Sawano (2022). Ohnishi et al. (2024), Remark 3.1, state qualitatively that for a Gaussian RKHS "the only dynamics inducing bounded Koopman operators are those of affine", citing Ikeda et al.; this concerns deterministic maps and contains no noise, covariance or matrix criterion. Theorem 5 differs from it in three respects: the transition is stochastic, the conditional covariance field is shown to be constant, and the exact inequality \(MRM^\top\preceq P+4Q\), range and norm are given. The fixed affine Gaussian criterion is a specialisation of classical Gaussian-Fock operator theory (Neretin, 1990, 2011); Section 3 gives the parameter translation. We claim no priority for that criterion, and the OU answer is obtained from it by an elementary semigroup argument.

The specific negative answer for the shear was also posted publicly before this manuscript. An open GitHub issue, the-omega-institute/trureturing #23376 (opened 28 October 2026), preregisters the Philipp et al. necessity question. It quotes the same remarks, proposes the same witness \(A=\begin{pmatrix}-1&5\\0&-1\end{pmatrix}\), \(B=C=I_2\), and gives the two-noise Gram identity with \(I+4Q_t\) as a "proposed manual route". The issue states that the route is "entirely UNCOMPILED" and that it "supplies neither a proof nor a refutation, Lean result, priority claim or resolution credit". It does not state the general criterion \(AP+PA^\top\preceq4BB^\top\), the rigidity theorems or the Lévy results. The witness and a detailed proposed analytic derivation (including the all-time route for this witness, with the specialised slack \(4I-A-A^\top\)) therefore appeared in issue #23376 before this work; the issue explicitly disclaimed a completed proof or formal verification. We have not established whether the two share an upstream source.

What we regard as new, within a bounded literature search current to 4 November 2026, is: covariance-field rigidity from RKHS boundedness alone (Theorem 5); drift rigidity for additive non-Gaussian noise, including pure-jump noise (Theorem 9); the Gaussian-component noise boundary without moment assumptions (Theorems 8 and 11); and the coexistence of sharp-order prediction convergence with membership loss for one fixed observable (Theorem 12). A bounded search does not establish historical priority. The paper gives full proofs, and the companion script checks the constants, but no external peer review or formal verification is claimed.

| Result | Status in this paper | Originality boundary |
|---|---|---|
| Gaussian transition rigidity (Thm 5) | Complete proof for arbitrary Borel mean and covariance fields, rectangular dimensions | Covariance rigidity from RKHS boundedness proposed as new; the affine Gaussian form is known under Gaussian-preservation premises (Section 3); deterministic affine rigidity is known |
| Additive-noise rigidity (Thm 9) | Complete proof for noise with a Gaussian lower bound on its characteristic function | Proposed as new; open for faster-decaying or vanishing characteristic functions |
| Infinitely divisible noise boundary (Thms 8, 11) | Exact matrix boundary, image space and norm | Lévy--Khintchine machinery is standard; only the Gaussian component controls the boundary |
| Diffusion approximation (Thm 12, Prop 13) | One fixed membership-loss observable, sharp order, explicit constants | Coexistence result proposed; the norm identity is standard kernel-mean duality |
| Fixed affine criterion and OU answer (Prop 3, Thm 6) | Explicit Fock translation and separating example | Contained in Gaussian-Fock theory; witness publicly proposed in #23376 |
| Bandwidths, kEDMD, sampling, spectra, growth, finite rank (Secs 7--9) | Consequences in the specified spaces | Imported spectral theorem and kEDMD bound are attributed |

## Reading guide

Section 2 sets up the Fourier description of Gaussian RKHSs, gives the exact image of an affine Gaussian transition (Proposition 3) and proves Gaussian transition rigidity (Theorem 5). Section 3 shows how the affine criterion follows from classical Fock-space theory. Section 4 derives the OU criterion and the separating example. Section 5 treats additive infinitely divisible noise and proves additive-noise rigidity (Theorem 9). Section 6 contains the discontinuous diffusion limit. Section 7 gives exact sampling thresholds and Section 8 the bandwidth rule and its kEDMD consequence. Section 9 collects consequences of an isometry to a classical OU semigroup: spectrum, growth of each observable and the finite-rank barrier. Section 10 summarises and lists open problems, and Section 11 describes the checks and the scope of the claims. A reader interested only in the OU answer can read Sections 2.1--2.3 and 4.

**Notation.**

| Symbol | Meaning |
|---|---|
| \(P\), \(R\) | Source and target kernel matrices, \(k_P(x,y)=e^{-(x-y)^\top P^{-1}(x-y)}\) |
| \(\mathcal H_P\), \(\|\cdot\|_P\), \(c_P\) | Gaussian RKHS on \(\mathbb R^d\), its norm, \(c_P=\pi^{-d/2}(\det P)^{-1/2}\) |
| \(F\), \(M\), \(b\) | Conditional mean map; its matrix and shift when affine |
| \(Q\) | Gaussian (conditional or noise) covariance; \(Q_t\) its OU value at time \(t\) |
| \(S\), \(E\) | \(S=P+4Q\) and \(E=(M^\top S^{-1}M)^{-1}\), the exact image matrix |
| \(D\) | Brownian covariance rate (\(D=BB^\top\) for \(B\,dW\)) |
| \(D_{\rm eff}\), \(\Sigma\) | \(D-\frac14(AP+PA^\top)\); stationary covariance \(\int_0^\infty e^{As}De^{A^\top s}ds\) |
| \(\varphi\), \(j\), \(\nu\) | Noise characteristic function, real jump exponent, Lévy measure |

All covariances are probabilistic: standard Brownian motion at time \(t\) has covariance \(tI\). The order \(\preceq\) is the Loewner order.

# Gaussian transitions between Gaussian RKHSs

## Scope

For \(P\in\mathbb S_{++}^m\), \(\mathcal H_P(\mathbb R^m)\) is the complex RKHS with kernel \(k_P\). We consider
\[
(Tf)(x)=\int_{\mathbb R^m}f(u)\,\mathcal N(F(x),Q(x))(du),
\qquad x\in\mathbb R^d,
\tag{1}
\]
where \(F:\mathbb R^d\to\mathbb R^m\) and \(Q:\mathbb R^d\to\mathbb S_+^m\) are Borel maps. Degenerate Gaussian laws are allowed. Since every \(f\in\mathcal H_P\) is bounded, (1) is defined at every state.

## Fourier representation and exact Gaussian smoothing

We use the unitary Fourier transform \(\widehat f(\xi)=(2\pi)^{-m/2}\int e^{-iu\cdot\xi}f(u)\,du\). The Fourier characterisation of a translation-invariant RKHS gives
\[
\begin{split}
\mathcal H_P
&=\left\{f\in L^2(\mathbb R^m):
  \int|\widehat f(\xi)|^2e^{\xi^\top P\xi/4}\,d\xi<\infty\right\},\\
\|f\|_P^2
&=c_P\int|\widehat f(\xi)|^2e^{\xi^\top P\xi/4}\,d\xi,\qquad c_P=\pi^{-m/2}(\det P)^{-1/2}.
\end{split}
\tag{2}
\]
Functions are taken in their continuous versions. The normalisation follows from \(\widehat{k_P(\,\cdot\,,0)}(\xi)=2^{-m/2}\sqrt{\det P}\,e^{-\xi^\top P\xi/4}\).

Two consequences are used repeatedly. First, \(\|f\|_\infty\le\|f\|_P\), because \(k_P(x,x)=1\). Second,
\[
\mathcal H_P\subset C_0(\mathbb R^m),
\tag{3}
\]
because kernel sections vanish at infinity, their span is dense, and RKHS convergence implies uniform convergence. In particular, nonzero constants do not belong to \(\mathcal H_P\).

**Lemma 1 (Gaussian inclusions).**
For positive definite \(E,R\) of the same dimension, \(\mathcal H_E\subseteq\mathcal H_R\) if and only if \(E\succeq R\). When the inclusion holds, its norm is
\[
\|\iota:\mathcal H_E\to\mathcal H_R\|=\left(\frac{\det E}{\det R}\right)^{1/4}.
\tag{4}
\]

**Proof.**
The ratio of the Fourier weights in (2) is \((\det E/\det R)^{1/2}\exp[\frac14\xi^\top(R-E)\xi]\). Its supremum is finite exactly when \(R\preceq E\), and then equals the prefactor; Fourier mass near the origin shows sharpness. Setwise inclusion implies bounded inclusion by the closed graph theorem. \(\square\)

This inclusion is also Philipp et al. (2025a), Proposition 3.3. The Fourier proof gives the norm and explicit failure witnesses.

**Lemma 2 (exact smoothing range).**
Let \(Q\succeq0\), \(Z\sim\mathcal N(0,Q)\) and \((S_Qf)(u)=\mathbb E f(u+Z)\). Then
\[
S_Q(\mathcal H_P)=\mathcal H_{P+4Q},
\qquad
\|S_Qf\|_{P+4Q}^2=\left(\frac{\det P}{\det(P+4Q)}\right)^{1/2}\|f\|_P^2.
\tag{5}
\]

**Proof.**
\(\widehat{S_Qf}(\xi)=e^{-\xi^\top Q\xi/2}\widehat f(\xi)\). Substitution into (2) proves the norm identity. For \(g\in\mathcal H_{P+4Q}\), \(\widehat f=e^{\xi^\top Q\xi/2}\widehat g\) defines \(f\in\mathcal H_P\) with \(S_Qf=g\), also when \(Q\) is singular. \(\square\)

The factor four comes from squaring the Fourier multiplier \(e^{-\xi^\top Q\xi/2}\) in a Hilbert-space norm.

## Exact affine range and norm

**Proposition 3 (affine Gaussian transitions).**
Let \(P\in\mathbb S_{++}^m\), \(R\in\mathbb S_{++}^d\), \(Q\in\mathbb S_+^m\), \(M\in\mathbb R^{m\times d}\), and
\[
(Tf)(x)=\mathbb E f(Mx+b+Z),\qquad Z\sim\mathcal N(0,Q).
\tag{6}
\]
If \(M\) has full column rank, set \(S=P+4Q\) and \(E=(M^\top S^{-1}M)^{-1}\). Then \(T(\mathcal H_P)=\mathcal H_E\). Moreover, \(T:\mathcal H_P\to\mathcal H_R\) is bounded exactly when
\[
M^\top S^{-1}M\preceq R^{-1},
\quad\text{equivalently}\quad
MRM^\top\preceq S,
\tag{7}
\]
and then
\[
\|T\|_{\mathcal H_P\to\mathcal H_R}
=\left(\frac{\det P}{\det S}\right)^{1/4}\left(\frac{\det E}{\det R}\right)^{1/4}.
\tag{8}
\]
If \(M\) does not have full column rank, \(T\) does not map \(\mathcal H_P\) into \(\mathcal H_R\).

**Proof.**
Let \(\eta_x=\mathbb E\,k_P(\,\cdot\,,Mx+b+Z)\in\mathcal H_P\). The section map \(u\mapsto k_P(\cdot,u)\) is norm-continuous and takes values in the separable space \(\mathcal H_P\). It is therefore strongly measurable, and its constant unit norm makes it Bochner integrable. The operator has the feature representation \(Tf(x)=\langle f,\eta_x\rangle_P\), with the inner product linear in its first argument.

Let \(V\) be the closed span of the \(\eta_x\), and \(Jf(x)=\langle f,\eta_x\rangle_P\) on \(V\). By the standard description of the range of a feature map (Aronszajn, 1950; Paulsen and Raghupathi, 2016), \(J\) is an isometry of \(V\) onto the RKHS with kernel
\[
L(x,y)=\langle\eta_y,\eta_x\rangle_P=\mathbb E_{Z,Z'}\,k_P(Mx+b+Z,My+b+Z'),
\tag{9}
\]
with \(Z,Z'\) independent, and \(T=J\Pi_V\) maps \(\mathcal H_P\) onto that RKHS with the quotient norm. Since \(Z-Z'\sim\mathcal N(0,2Q)\), Gaussian integration gives
\[
L(x,y)=c\,\exp[-(x-y)^\top M^\top S^{-1}M(x-y)]=c\,k_E(x,y),\qquad c=\left(\frac{\det P}{\det S}\right)^{1/2}.
\tag{10}
\]
Thus \(T:\mathcal H_P\to\mathcal H_E\) is \(\sqrt c\) times a coisometry, which proves \(T(\mathcal H_P)=\mathcal H_E\). Lemma 1 then gives (7) and (8). The two forms of (7) are equivalent because \(S^{-1/2}MR^{1/2}\) and its transpose have the same nonzero singular values.

If \(Mv=0\) for some \(v\ne0\), take a positive kernel section \(f\). Then \(Tf>0\) and \(Tf(x+tv)=Tf(x)\) for all real \(t\), contradicting (3). \(\square\)

**Corollary 4 (equal dimensions).**
If \(m=d\), boundedness requires \(M\) invertible, \(E=M^{-1}(P+4Q)M^{-\top}\), and
\[
\|T\|_{\mathcal H_P\to\mathcal H_R}=\left(\frac{\det P}{\det R}\right)^{1/4}|\det M|^{-1/2}.
\tag{11}
\]
Directly from (2), \(\widehat{Tf}(\eta)=|\det M|^{-1}e^{ib\cdot M^{-\top}\eta}e^{-(M^{-\top}\eta)^\top Q(M^{-\top}\eta)/2}\widehat f(M^{-\top}\eta)\). After \(\eta=M^\top\xi\), the ratio of squared-norm integrands is
\[
\left(\frac{\det P}{\det R}\right)^{1/2}|\det M|^{-1}\exp\!\left[\tfrac14\xi^\top(MRM^\top-P-4Q)\xi\right].
\tag{12}
\]
This gives the sharp matrix condition and the norm, and shows that \(T\) is injective, so the minimal-preimage norm in Proposition 3 is the norm of the unique preimage. Noise controls high-frequency admissibility; the norm is set by frequencies near zero.

## An explicit observable when the matrix condition fails

Suppose \(m=d\), \(M\) is invertible, and \(\Delta=MRM^\top-P-4Q\) has a positive eigenvalue. For positive definite \(G\), (2) shows
\[
k_G(\,\cdot\,,0)\in\mathcal H_P\iff 2G-P\succ0,
\qquad
\|k_G(\,\cdot\,,0)\|_P^2=\frac{\det G}{\sqrt{\det P\,\det(2G-P)}}.
\tag{13}
\]
Choose \(0<\varepsilon<\lambda_{\max}(\Delta)\) and \(f_\varepsilon=k_{G_\varepsilon}(\cdot,0)\) with \(G_\varepsilon=(P+\varepsilon I)/2\). Then \(f_\varepsilon\in\mathcal H_P\), and \(Tf_\varepsilon\) is a nonzero multiple of a translated Gaussian with matrix \(M^{-1}(G_\varepsilon+2Q)M^{-\top}\). Its membership in \(\mathcal H_R\) would require \(2G_\varepsilon+4Q-MRM^\top=\varepsilon I-\Delta\succ0\), which the choice of \(\varepsilon\) excludes. Hence
\[
f_\varepsilon\in\mathcal H_P,\qquad Tf_\varepsilon\notin\mathcal H_R.
\tag{14}
\]
The companion script checks the scalar instance \(M=3\), \(Q=P=R=1\), \(f=e^{-x^2}\).

## Rigidity of state-dependent Gaussian transitions

**Theorem 5 (Gaussian transition rigidity).**
Let \(T\) be given by (1), \(P\in\mathbb S_{++}^m\) and \(R\in\mathbb S_{++}^d\). The following are equivalent:

1. \(T(\mathcal H_P)\subseteq\mathcal H_R\).
2. \(T:\mathcal H_P\to\mathcal H_R\) is bounded.
3. There are a constant \(Q_0\succeq0\), a full-column-rank \(M\in\mathbb R^{m\times d}\) and \(b\in\mathbb R^m\) with
   \[
   Q(x)=Q_0,\qquad F(x)=Mx+b\quad\text{for every }x,\qquad MRM^\top\preceq P+4Q_0.
   \tag{15}
   \]

The exact range and norm are then those of Proposition 3. In particular, if \(m<d\) no transition of the form (1) has the mapping property.

*Idea of the proof.* Kernel sections \(k_P(\cdot,w)\) extend to complex centres \(w\), and functions in \(\mathcal H_R\) extend to entire functions with controlled growth. Applying \(T\) to complex-centred sections gives an entire function \(\Phi(z,w)\) of the state along a line and of the centre. Along the real axis \(\Phi\) is an explicit Gaussian in the centre, with coefficients given by \(F\) and \(Q\). Boundedness gives a uniform bound over real centres, which forces the quadratic coefficient to have nonnegative real part; a Cayley transform and Liouville's theorem make it constant. A second growth bound makes the imaginary part of the continued mean grow at most linearly, so the mean is affine.

**Proof.**
*Boundedness from inclusion.* Suppose \(f_n\to f\) in \(\mathcal H_P\) and \(Tf_n\to g\) in \(\mathcal H_R\). Both imply uniform convergence, and \(\|T(f_n-f)\|_\infty\le\|f_n-f\|_\infty\), so \(g=Tf\). The closed graph theorem gives boundedness.

*Holomorphic extensions.* By (2), each \(f\in\mathcal H_R\) extends to an entire function on \(\mathbb C^d\) with
\[
|f(z)|\le\|f\|_R\exp[2(\operatorname{Im}z)^\top R^{-1}(\operatorname{Im}z)].
\tag{16}
\]
For \(w\in\mathbb C^m\) let \(\kappa_w(u)=\exp[-(u-w)^\top P^{-1}(u-w)]\). Its Fourier transform is \(2^{-m/2}\sqrt{\det P}\,e^{-\xi^\top P\xi/4-iw\cdot\xi}\); this and its \(w\)-derivatives are locally dominated in the weighted \(L^2\) space of (2), so \(w\mapsto\kappa_w\) is an entire \(\mathcal H_P\)-valued map with
\[
\|\kappa_w\|_P=\exp[2(\operatorname{Im}w)^\top P^{-1}(\operatorname{Im}w)].
\tag{17}
\]
Completing the square proves (17), and Cauchy--Schwarz proves (16).

Fix \(x_0,v\in\mathbb R^d\), \(v\ne0\), and let
\[
\Phi(z,w)=(T\kappa_w)(x_0+zv),\qquad (z,w)\in\mathbb C\times\mathbb C^m.
\]
Since \(T\) is bounded and linear, \(w\mapsto T\kappa_w\) is an entire \(\mathcal H_R\)-valued map. Evaluation at the complex point \(x_0+zv\) is a bounded functional on \(\mathcal H_R\) by (16), represented by an element depending antiholomorphically on \(z\) (the complex-centred kernel section of \(\mathcal H_R\)). Hence \(\Phi\) is separately holomorphic in \(z\) and in \(w\), and locally bounded, so it is jointly entire by Hartogs' theorem. By (16) and \(\|\kappa_y\|_P=1\) for real \(y\),
\[
|\Phi(z,y)|\le\|T\|\exp[2(\operatorname{Im}z)^2v^\top R^{-1}v],\qquad y\in\mathbb R^m,
\tag{18}
\]
uniformly over all real centres. For real \(t\) and real \(y\), Gaussian integration gives
\[
\Phi(t,y)=a(t)\exp[-(F(x_0+tv)-y)^\top C(t)(F(x_0+tv)-y)],
\tag{19}
\]
with \(C(t)=(P+2Q(x_0+tv))^{-1}\succ0\) and \(a(t)=\sqrt{\det P/\det(P+2Q(x_0+tv))}>0\). For fixed real \(t\), both sides of (19) are entire in the centre once \(y\) is replaced by \(w\in\mathbb C^m\) (the right side by the same formula), and they agree for real \(w\), so they agree for all \(w\). In particular the \(w\)-derivatives at \(w=0\) can be computed from (19).

Let \(g(z)=\Phi(z,0)\). Since \(g>0\) on \(\mathbb R\), its zero set \(\mathcal Z\) is discrete, and \(\Omega=\mathbb C\setminus\mathcal Z\) is connected and contains \(\mathbb R\). On \(\Omega\) define holomorphic coefficients
\[
L_i(z)=\frac{\partial_{w_i}\Phi(z,0)}{2g(z)},\qquad
\mathcal C_{ij}(z)=-\frac12\left[\frac{\partial_{w_i}\partial_{w_j}\Phi(z,0)}{g(z)}-\frac{\partial_{w_i}\Phi(z,0)\,\partial_{w_j}\Phi(z,0)}{g(z)^2}\right].
\tag{20}
\]
By (19), \(\mathcal C(t)=C(t)\) and \(L(t)=C(t)F(x_0+tv)\) for real \(t\). For fixed real \(y\), both sides of
\[
\Phi(z,y)=g(z)\exp[2L(z)\cdot y-y^\top\mathcal C(z)y]
\tag{21}
\]
are holomorphic on \(\Omega\) and agree on \(\mathbb R\), so (21) holds on \(\Omega\). No logarithm is needed.

*Constancy of the covariance.* Fix \(z\in\Omega\) and nonzero \(u\in\mathbb R^m\), and put \(y=ru\) in (21). The bound (18) as \(|r|\to\infty\) forces \(\operatorname{Re}(u^\top\mathcal C(z)u)\ge0\). So \(h_u(z)=u^\top\mathcal C(z)u\) has \(\operatorname{Re}(h_u+1)\ge1\) on \(\Omega\); the denominator of the Cayley transform
\[
b_u(z)=\frac{h_u(z)-1}{h_u(z)+1}
\]
never vanishes, \(|b_u|\le1\), and \(b_u\ne1\) everywhere. The bounded function \(b_u\) extends across the discrete set \(\mathcal Z\), so it is constant by Liouville's theorem. The constant is not \(1\) (on \(\mathbb R\), \(h_u(t)>0\) is finite), so inverting the Cayley transform makes \(h_u\) constant. Taking \(u=e_i\) and \(u=e_i+e_j\) shows that \(\mathcal C\) is a constant matrix \(C\succ0\) on the line. Hence \(Q(x_0+tv)\) is constant in \(t\). Every two real states lie on a line, so \(Q(x)=Q_0\) for all \(x\).

*Affineness of the mean.* Now \(C\) and \(a=\sqrt{\det P/\det(P+2Q_0)}\) are constant on the line. Each \(L_i\) is meromorphic on \(\mathbb C\), with possible poles only on \(\mathcal Z\). With \(y=e_i\), (21) reads \(\Phi(z,e_i)=g(z)e^{2L_i(z)-C_{ii}}\). A pole of \(L_i\) would give the right side an essential singularity that a finite-order zero of \(g\) cannot cancel, while the left side is entire. So \(\mathcal F(z)=C^{-1}L(z)\) is entire and equals \(F(x_0+tv)\) for real \(z=t\). The identity \(g(t)=a\exp[-\mathcal F(t)^\top C\mathcal F(t)]\) extends to all \(z\), so \(g\) has no zeros. In (21) choose the real centre \(y=\operatorname{Re}\mathcal F(z)\). Then (18) gives
\[
a\exp\!\left[(\operatorname{Im}\mathcal F(z))^\top C(\operatorname{Im}\mathcal F(z))\right]\le\|T\|\exp[2(\operatorname{Im}z)^2v^\top R^{-1}v].
\tag{22}
\]
Each component of \(\operatorname{Im}(C^{1/2}\mathcal F(z))\) is an entire harmonic function of at most linear growth, hence affine: interior derivative estimates on disks of radius \(r\) bound its second derivatives by a constant times \(r^{-2}(1+r)\to0\). By the Cauchy--Riemann equations \(\mathcal F\) is affine, with real coefficients because it is real on \(\mathbb R\). So \(F\) is affine on every real line. Linewise affineness implies global affineness without any continuity assumption: after subtracting \(F(0)\) it gives real homogeneity and the midpoint identity, hence additivity. Therefore \(F(x)=Mx+b\).

Full column rank and the matrix condition follow from Proposition 3. \(\square\)

**Consequence for Euler--Maruyama steps.** For a step \(X^+=x+h\,b(x)+\sqrt h\,\sigma(x)Z\), \(Z\sim\mathcal N(0,I)\), \(h>0\), Theorem 5 gives a complete equal-dimensional criterion: the step maps \(\mathcal H_P\) into \(\mathcal H_R\) exactly when
\[
b(x)=Ax+c,\quad \sigma(x)\sigma(x)^\top=D\ \text{for every }x,\quad
I+hA\ \text{invertible},\quad (I+hA)R(I+hA)^\top\preceq P+4hD.
\tag{23}
\]
The factor \(\sigma(x)\) may vary by orthogonal transformations; only \(\sigma\sigma^\top\) matters. Theorem 9 below extends the drift conclusion to Euler steps driven by non-Gaussian Lévy increments. Finite-time transition laws of nonlinear SDEs are generally not Gaussian, so (23) concerns the numerical step, not arbitrary nonlinear diffusions.

# The affine criterion as a classical Fock-space specialisation

This section records the formula-level overlap behind the attribution in the introduction. Take equal dimensions and invertible \(M\). Changes of coordinates whiten both kernels to \(I\); the mean matrix and noise covariance become
\[
L=P^{-1/2}MR^{1/2},\qquad Q_0=P^{-1/2}QP^{-1/2}.
\]
Real translations are unitary on a translation-invariant Gaussian RKHS, so \(b\) does not affect boundedness. The identity \(e^{-|x-y|^2}=e^{-|x|^2}e^{2x\cdot y}e^{-|y|^2}\) identifies \(\mathcal H_I\) isometrically with the standard Fock space through \(f(x)=e^{-|x|^2}\mathsf F(\sqrt2x)\). Gaussian integration turns the centred transition into a Fock integral operator with kernel
\[
\det(I+2Q_0)^{-1/2}\exp\!\left[\tfrac12 z^\top(I-L^\top WL)z+z^\top L^\top W\bar w+\tfrac12\bar w^\top(I-W)\bar w\right],\qquad W=(I+2Q_0)^{-1},
\tag{24}
\]
with real symmetric block matrix
\[
\Gamma=\begin{pmatrix}I-L^\top WL&L^\top W\\WL&I-W\end{pmatrix}.
\tag{25}
\]
The Olshanski criterion, as stated in Neretin (1990) and Neretin (2011, Chapter 5, Proposition 1.3 and Theorem 1.4), requires \(\|\Gamma\|\le1\) together with strict norm bounds on the two diagonal blocks. Here \(I-\Gamma=\begin{pmatrix}L^\top\\-I\end{pmatrix}W\begin{pmatrix}L&-I\end{pmatrix}\succeq0\). The Schur complement of \(2I-W\succ0\) in \(I+\Gamma\), with \(W(2I-W)^{-1}=(I+4Q_0)^{-1}\), gives
\[
I+\Gamma\succeq0\iff L^\top(I+4Q_0)^{-1}L\preceq I\iff LL^\top\preceq I+4Q_0.
\tag{26}
\]
Under this inequality the diagonal-block conditions hold: \(0\preceq I-W\prec I\), \(L^\top WL\succ0\) since \(L\) is invertible, and \(W^{1/2}LL^\top W^{1/2}\preceq W^{1/2}(I+4Q_0)W^{1/2}\prec2I\) gives \(L^\top WL\prec2I\). Undoing the coordinate changes yields exactly \(MRM^\top\preceq P+4Q\).

So the fixed affine criterion is an exact specialisation of an established theorem. The Fourier proof is a short route that makes the norm and the comparison with Philipp et al. transparent. Deterministic composition restrictions are also discussed by Gonzalez et al. (2024) and Middelkamp (2024, Section 4.4.2). Theorem 5 has a different premise from the characterisations of Gaussian-to-Gaussian maps in De Palma et al. (2015), Holevo (2017) and Alekseev et al. (2021). Holevo (2017, Theorem 1, p. 712) assumes a Feller endomorphism of the bounded signed measures on \(\mathbb R^n\) that maps every Gaussian probability measure to a Gaussian measure, and concludes that it is a Markov operator with transition law \(N(K_0x+y_0,\Upsilon_0)\): the same affine-Gaussian conclusion as Theorem 5, from a different premise. Alekseev et al. (2021, Theorems 1--2) extend this to locally convex spaces and need Gaussian images only of Gaussian measures concentrated on affine lines; their pushforward under \(x\mapsto x^3\) shows that Gaussian images of Dirac measures alone do not suffice, and their Remark 1 shows that the Feller condition, which their Theorems 3--4 weaken, cannot be dropped. In Theorem 5 only the image of each Dirac measure \(\delta_x\), the conditional law \(N(F(x),Q(x))\), is assumed Gaussian; nothing is assumed about the images of non-degenerate Gaussian input laws, and no Feller or continuity condition is imposed. Boundedness between Gaussian RKHSs supplies the restriction instead. Conversely, those theorems make no RKHS hypothesis, keep input and output dimensions equal, and give no rank condition or matrix inequality. The premises are incomparable; a posteriori the transitions of Theorem 5 lie in Holevo's class, so Theorem 5 is a new route to that conclusion, not a larger class. As a cross-check in one complex variable, Sang and Zhao (2026, Theorem 1.1 with \(p=q=2\)) characterise bounded Gaussian integral operators on the Fock space; with the parameters of (24) at \(d=1\) their condition reduces to (26), and their compactness criterion never holds for these operators, in agreement with Theorem 20. John and Parthasarathy (2021, Definition V.1) define their class by an already quadratic-exponential coherent generating function; their structural results do not derive that property from our hypotheses. These premise differences are material, but they are not by themselves proof of historical novelty.

# The sharp Ornstein--Uhlenbeck criterion

Let \(A\in\mathbb R^{d\times d}\) and \(B\in\mathbb R^{d\times r}\), with no stability or controllability assumption, and
\[
dX_t=AX_t\,dt+B\,dW_t,\qquad M_t=e^{At},\qquad Q_t=\int_0^te^{As}BB^\top e^{A^\top s}\,ds.
\tag{27}
\]

**Theorem 6 (fixed-time and all-time invariance).**
For \(P\succ0\) and \(t\ge0\),
\[
K^t(\mathcal H_P)\subseteq\mathcal H_P\iff e^{At}Pe^{A^\top t}\preceq P+4Q_t,
\tag{28}
\]
and then \(\|K^t\|_{\mathcal H_P\to\mathcal H_P}=e^{-t\operatorname{tr}A/2}\). Furthermore,
\[
\boxed{\quad K^t(\mathcal H_P)\subseteq\mathcal H_P\ \text{for every }t\ge0\iff AP+PA^\top\preceq4BB^\top.\quad}
\tag{29}
\]

**Proof.**
The transition is \(\mathcal N(M_tx,Q_t)\) with \(M_t\) invertible, so Corollary 4 gives (28) and the norm. For the all-time statement use
\[
P+4Q_t-e^{At}Pe^{A^\top t}=\int_0^te^{As}(4BB^\top-AP-PA^\top)e^{A^\top s}\,ds.
\tag{30}
\]
Positivity of the integrand proves sufficiency; dividing by \(t\) and letting \(t\downarrow0\) proves necessity. \(\square\)

Theorem 6 keeps the normalisation of Philipp et al. (2025a) and also covers non-stable drift. Their sufficient condition
\[
AP+PA^\top\preceq2BB^\top
\tag{31}
\]
remains valid, and is strictly stronger than necessary. Their image-space inclusion uses \(P+2Q_t\); the exact image matrix is \(e^{-At}(P+4Q_t)e^{-A^\top t}\). Remark 4.2 of Philipp et al. notes that a converse would follow if invariance implied the inclusion \(\mathcal H_{C_t}\hookrightarrow\mathcal H_C\) for their \(C_t^2=e^{-At}(C^2+2Q_t)e^{-A^\top t}\); the example below shows that invariance does not imply this inclusion. The scalar stable baseline is also in Philipp et al. (2025b), Theorem D.2, with the same norm bound.

**In one dimension the condition never binds for a stable process.** For \(dX=aX\,dt+\beta\,dW\) and \(P=p>0\), (29) reads \(2ap\le4\beta^2\). It holds for every \(p\) when \(a\le0\), and means \(p\le2\beta^2/a\) when \(a>0\). The constraint therefore matters only for unstable or nonnormal multivariate drift.

## A stable controllable example separating the two conditions

Take
\[
A=\begin{pmatrix}-1&5\\0&-1\end{pmatrix},\qquad B=I_2,\qquad P=I_2.
\tag{32}
\]
\(A\) is Hurwitz with double eigenvalue \(-1\), and \((A,B)\) is controllable because \(B\) is invertible. The slack in (31) is \(2I-(A+A^\top)\), with eigenvalues \(-1\) and \(9\), so (31) fails. The sharp slack \(4I-(A+A^\top)\) has eigenvalues \(1\) and \(11\). So every \(K^t\) preserves \(\mathcal H_I\), and
\[
\|K^t\|=e^{t}.
\tag{33}
\]
This example satisfies all assumptions of the originating question. The same matrices were proposed as a witness in the public issue #23376 discussed in the introduction.

**Why the norm grows although the process is stable.** The growth in (33) concerns the global Gaussian RKHS norm. That norm penalises spatial spread: it is a Fourier weight \(e^{\xi^\top P\xi/4}\) that is small only for functions concentrated in a region of size about \(\sqrt P\), and it excludes constants. As the stable drift pulls starting points together, \(x\mapsto\mathbb E f(X_t)\) varies over a larger set of starting points, so its kernel norm grows, while its supremum norm decreases and it converges pointwise to the stationary mean. The space is different from the invariant-probability \(L^2\) space on which the Markov semigroup is a contraction. Section 9 shows that every nonzero observable grows at exactly the rate \(e^{-t\operatorname{tr}A/2}\).

# Additive Lévy noise and the Gaussian-component boundary

In this section the noise is additive and state-independent. We first treat affine maps, where only the Gaussian covariance component of the noise matters, and then show that a nonlinear drift is impossible.

## The part of the characteristic exponent that decides invariance

Let \(Z\in\mathbb R^m\) be infinitely divisible with characteristic function \(\varphi\) and Lévy--Khintchine representation
\[
\log\varphi(\xi)=i\ell\cdot\xi-\tfrac12\xi^\top Q\xi+\int_{\mathbb R^m\setminus\{0\}}\left(e^{i\xi\cdot z}-1-i\xi\cdot z\,\mathbf1_{\{|z|\le1\}}\right)\nu(dz),
\tag{34}
\]
with \(Q\succeq0\) the Gaussian covariance component and \(\int(1\wedge|z|^2)\nu(dz)<\infty\). The matrix \(Q\) need not be the total covariance of \(Z\), which need not exist. Define
\[
j(\xi)=\int(1-\cos(\xi\cdot z))\,\nu(dz),\qquad |\varphi(\xi)|^2=e^{-\xi^\top Q\xi-2j(\xi)}.
\tag{35}
\]
For the use of (34) in linear stochastic transitions, see Sarkar (2026), Section 6, equations (6.2)--(6.4).

**Lemma 7 (subquadratic jump exponent).** For every Lévy measure, \(j(\xi)=o(|\xi|^2)\) as \(|\xi|\to\infty\), uniformly in direction.

**Proof.** With \(r=|\xi|\), the small-jump part satisfies \(r^{-2}\int_{|z|\le1}(1-\cos(\xi\cdot z))\nu(dz)\le\int_{|z|\le1}\min\{2/r^2,|z|^2/2\}\nu(dz)\to0\) by dominated convergence. The large-jump part is at most \(2\nu(|z|>1)/r^2\). Neither bound depends on direction. \(\square\)

In particular, for every \(\epsilon>0\) there is \(C_\epsilon\) with \(2j(\xi)\le\epsilon|\xi|^2+C_\epsilon\), so
\[
|\varphi(\xi)|\ge e^{-C_\epsilon/2}\,e^{-\xi^\top(Q+\epsilon I)\xi/2}.
\tag{36}
\]

**Theorem 8 (affine infinitely divisible transitions).** Let \(P,R\succ0\) in dimension \(d\), \(M\in GL(d,\mathbb R)\), and \((Tf)(x)=\mathbb E f(Mx+b+Z)\). The following are equivalent: (1) \(T(\mathcal H_P)\subseteq\mathcal H_R\); (2) \(T:\mathcal H_P\to\mathcal H_R\) is bounded; (3) \(MRM^\top\preceq P+4Q\). When they hold,
\[
\|T\|=\|T\|_{\rm ess}=|\det M|^{-1/2}\left(\frac{\det P}{\det R}\right)^{1/4}.
\tag{37}
\]
If \(M\) is singular, the mapping property fails for every \(R\).

**Proof.** Fourier transformation gives \(\widehat{Tf}(\eta)=|\det M|^{-1}e^{ib\cdot M^{-\top}\eta}\varphi(M^{-\top}\eta)\widehat f(M^{-\top}\eta)\), valid in \(L^2\) because Jensen's inequality gives \(\|Tf\|_{L^2}\le|\det M|^{-1/2}\|f\|_{L^2}\), and pointwise because \(\widehat f\in L^1\). Changing variables \(\eta=M^\top\xi\),
\[
\|Tf\|_R^2=|\det M|^{-1}c_R\int|\widehat f(\xi)|^2e^{\xi^\top P\xi/4}\exp\!\left[-\tfrac14\xi^\top(P+4Q-MRM^\top)\xi-2j(\xi)\right]d\xi,
\tag{38}
\]
read as \(+\infty\) when \(Tf\notin\mathcal H_R\). If the matrix in parentheses is positive semidefinite, the last factor is at most one and tends to one at the origin, which proves (37) for the norm. If \(\Delta=MRM^\top-P-4Q\) has an eigenvalue \(\lambda>0\), take \(0<\delta<\lambda/8\) and \(\widehat f(\xi)=\exp[-\xi^\top P\xi/8-\delta|\xi|^2]\), so \(f\in\mathcal H_P\). Up to a constant, the integrand in (38) is \(\exp[\frac14\xi^\top\Delta\xi-2\delta|\xi|^2-2j(\xi)]\). On an open cone around a top eigenvector the quadratic part exceeds \(a|\xi|^2\) for some \(a>0\); by Lemma 7 the exponent exceeds \(a|\xi|^2/2\) for large \(|\xi|\) there, and the integral diverges. For the essential norm, conjugate by the weighted Fourier isometries; the remaining multiplier has modulus close to its supremum on a small ball around the origin, which supports an infinite orthonormal sequence on which the image norm is close to \(\|T\|\). Compact operators send it to a null sequence, so their distance from \(T\) is at least \(\|T\|\). Finally, if \(Mv=0\), \(v\ne0\), a positive kernel section has an image that is positive and constant along \(v\), contradicting (3). \(\square\)

The theorem covers asymmetric and infinite-activity jumps without large-jump moments. It concerns the specified Gaussian Fourier weight; jump noise may smooth substantially in other spaces.

## Rigidity of additive-noise transitions with nonlinear drift

Theorem 5 uses the exp-quadratic form (19), which is not available for jump noise. We now treat additive state-independent noise with a nonlinear Borel drift, working on the Fourier side: every real kernel section is mapped to a *translate of one fixed function*, translates correspond to characters, and characters can be continued in the state variable.

Let \(Z\in\mathbb R^m\) have characteristic function \(\varphi(\eta)=\mathbb E e^{i\eta\cdot Z}\), let \(F:\mathbb R^d\to\mathbb R^m\) be Borel, and
\[
(Tf)(x)=\mathbb E f(F(x)+Z),\qquad x\in\mathbb R^d.
\tag{39}
\]
We say \(Z\) satisfies the *Gaussian lower bound* if there are \(c>0\) and \(\gamma\ge0\) with
\[
|\varphi(\eta)|\ge c\,e^{-\gamma|\eta|^2}\qquad(\eta\in\mathbb R^m).
\tag{40}
\]
By (36), every infinitely divisible law satisfies (40), with or without a Gaussian component and without moment assumptions.

**Theorem 9 (additive-noise rigidity).**
Let \(P\in\mathbb S_{++}^m\), \(R\in\mathbb S_{++}^d\) and \(T\) as in (39).

1. If \(Z\) satisfies (40) and \(T(\mathcal H_P)\subseteq\mathcal H_R\), then \(F(x)=Mx+b\) with \(M\in\mathbb R^{m\times d}\) of full column rank. In particular \(m\ge d\).
2. If \(Z\) is infinitely divisible with Gaussian covariance component \(Q\) and \(F(x)=Mx+b\) with \(M\) of full column rank, then
\[
T(\mathcal H_P)\subseteq\mathcal H_R\iff T:\mathcal H_P\to\mathcal H_R\ \text{is bounded}\iff MRM^\top\preceq P+4Q.
\tag{41}
\]
Then \(\|T\|\) is at most the norm (8) of the Gaussian transition with covariance \(Q\), and equals (37) when \(m=d\).

Hence, for infinitely divisible \(Z\), the mapping property, boundedness, and "\(F=Mx+b\), \(\operatorname{rank}M=d\), \(MRM^\top\preceq P+4Q\)" are equivalent. The Gaussian component \(Q\) may be zero; then \(MRM^\top\preceq P\) is required. Theorem 9 contains Theorem 8 and, for constant covariance, the drift part of Theorem 5.

*Idea of the proof.* The Riesz representer of evaluation of \(Tf\) at a state is, after conjugation, a translate of the fixed function \(k_P(\cdot,0)*\operatorname{law}(Z)\) by \(F(x)\). Dividing its Fourier transform by the nonvanishing factor coming from \(\varphi\) leaves the character \(e^{-i\eta\cdot F(x)}\). Along a line of states this character continues holomorphically and remains multiplicative in \(\eta\), so it has the form \(e^{-i\eta\cdot\mathcal F(z)}\) with \(\mathcal F\) entire. The Gaussian lower bound turns the growth bound from \(\mathcal H_R\) into linear growth of \(\operatorname{Im}\mathcal F\), and the last step of Theorem 5 applies.

**Proof.** *Boundedness.* The closed-graph argument of Theorem 5 uses only \(\|Tf\|_\infty\le\|f\|_\infty\), so \(T\) is bounded.

*Representers.* Fix \(x_0,v\in\mathbb R^d\), \(v\ne0\), put \(\beta=v^\top R^{-1}v\) and \(p(t)=F(x_0+tv)\). By (16), for \(z\in\mathbb C\) the functional \(f\mapsto(Tf)(x_0+zv)\) is bounded on \(\mathcal H_P\) with norm at most \(\|T\|e^{2\beta(\operatorname{Im}z)^2}\). Let \(\rho_z\in\mathcal H_P\) be its Riesz representer and \(\psi_z=\overline{\rho_z}\). Since \(k_P\) is real, \(\psi_z\in\mathcal H_P\) with \(\|\psi_z\|_P=\|\rho_z\|_P\), and by (2)
\[
(Tf)(x_0+zv)=c_P\int\widehat f(\eta)\,\widehat{\psi_z}(-\eta)\,e^{\eta^\top P\eta/4}\,d\eta.
\]
The left side is entire in \(z\) for every \(f\). Since \(\widehat f\) ranges over all of \(L^2(e^{\eta^\top P\eta/4}d\eta)\), these pairings separate points, so \(z\mapsto\widehat{\psi_z}\) is weakly holomorphic, hence holomorphic, into this weighted space, and locally bounded. For real \(t\) and \(y\in\mathbb R^m\), with \(\widetilde G(y)=\mathbb E\,k_P(y-Z,0)\),
\[
\psi_t(y)=(Tk_P(\cdot,y))(x_0+tv)=\mathbb E\,k_P(p(t)+Z,y)=\widetilde G(y-p(t)),
\]
a translate of one fixed function. Since \(\widetilde G=k_P(\cdot,0)*\operatorname{law}(Z)\),
\[
\widehat{\psi_t}(\eta)=\alpha(\eta)\,e^{-i\eta\cdot p(t)},\qquad \alpha(\eta)=2^{-m/2}\sqrt{\det P}\,e^{-\eta^\top P\eta/4}\,\overline{\varphi(\eta)}.
\tag{42}
\]

*Normalised symbols.* By (40), \(\alpha\) has no zeros. Let \(U(z,\eta)=\widehat{\psi_z}(\eta)/\alpha(\eta)\) and define the finite measure
\[
\mu(d\eta)=c_P|\alpha(\eta)|^2e^{\eta^\top P\eta/4}d\eta=\pi^{-m/2}2^{-m}\sqrt{\det P}\;e^{-\eta^\top P\eta/4}|\varphi(\eta)|^2\,d\eta.
\]
Then \(z\mapsto U(z,\cdot)\) is entire into \(L^2(\mu)\), with
\[
\|U(z,\cdot)\|_{L^2(\mu)}=\|\psi_z\|_P\le\|T\|e^{2\beta(\operatorname{Im}z)^2},
\tag{43}
\]
and \(U(t,\eta)=e^{-i\eta\cdot p(t)}\) for almost every \(\eta\) when \(t\) is real. The density of \(\mu\) is continuous, positive and even, so \(L^2(\mu)\subset L^2_{\rm loc}\), and every pairing \(\langle U(z,\cdot),\chi\rangle=\int U(z,\eta)\chi(\eta)\,d\eta\) with bounded compactly supported \(\chi\) is entire in \(z\).

*Multiplicativity.* For \(\chi\in C_c^\infty(\mathbb R^{2m})\), the functions \(z\mapsto\iint U(z,\eta_1)U(z,\eta_2)\chi\,d\eta_1d\eta_2\) and \(z\mapsto\iint U(z,\eta_1+\eta_2)\chi\,d\eta_1d\eta_2=\int U(z,\zeta)\big(\int\chi(\eta,\zeta-\eta)d\eta\big)d\zeta\) are entire and agree on \(\mathbb R\). By the identity theorem,
\[
U(z,\eta_1+\eta_2)=U(z,\eta_1)U(z,\eta_2)\quad\text{for a.e. }(\eta_1,\eta_2),\ \text{for every }z\in\mathbb C.
\tag{44}
\]

*Exponential form.* Fix \(z\), and suppose \(\chi\in C_c^\infty(\mathbb R^m)\) has \(c_\chi(z):=\langle U(z,\cdot),\chi\rangle\ne0\). Testing (44) against \(\theta(\eta_1)\chi(\eta_2)\) for arbitrary test functions \(\theta\) gives \(U(z,\cdot)=\Lambda_\chi(z,\cdot)/c_\chi(z)\) almost everywhere, with the smooth function \(\Lambda_\chi(z,\eta)=\int U(z,\zeta)\chi(\zeta-\eta)\,d\zeta\). Its continuous version \(\widetilde U_z\) satisfies (44) everywhere, so \(\widetilde U_z(0)\in\{0,1\}\), and \(\widetilde U_z(0)=0\) would force \(U(z,\cdot)=0\). Therefore \(\widetilde U_z\) is a continuous homomorphism \((\mathbb R^m,+)\to(\mathbb C^\times,\cdot)\), so \(\widetilde U_z(\eta)=e^{\lambda(z)\cdot\eta}\) for a unique \(\lambda(z)\in\mathbb C^m\), with \(\lambda_k(z)=\partial_{\eta_k}\widetilde U_z(0)=-\langle U(z,\cdot),\partial_k\chi\rangle/c_\chi(z)\), holomorphic near \(z\).

Such a \(\chi\) exists at every \(z\). Choose \(\chi_0\ge0\), \(\chi_0\ne0\), supported in \(\{|\zeta|<\delta\}\) with \(\delta|p(0)|<\pi/2\). Then \(\operatorname{Re}c_{\chi_0}(0)>0\), so the zeros of \(c_{\chi_0}\) form a discrete set \(\mathcal Z_0\). For \(z'\notin\mathcal Z_0\), evenness of \(\mu\) and \(\cosh\ge1\) give \(\|U(z',\cdot)\|^2_{L^2(\mu)}=\int e^{2\eta\cdot\operatorname{Re}\lambda(z')}\mu(d\eta)\ge\mu(\mathbb R^m)\). By continuity of \(z\mapsto U(z,\cdot)\) this holds for every \(z\), so \(U(z,\cdot)\ne0\) and some \(\chi\) has \(c_\chi(z)\ne0\). Thus \(\lambda\) is entire. Put \(\mathcal F=i\lambda\). For real \(t\), the continuous functions \(e^{\lambda(t)\cdot\eta}\) and \(e^{-i\eta\cdot p(t)}\) agree almost everywhere, hence everywhere, so \(\mathcal F(t)=F(x_0+tv)\).

*Growth and affineness.* Since \(|e^{-i\eta\cdot\mathcal F(z)}|=e^{\eta\cdot\operatorname{Im}\mathcal F(z)}\), (43) and (40) give, with \(N=P/4+2\gamma I\) and \(\omega=\operatorname{Im}\mathcal F(z)\),
\[
c^2\,2^{-m}\sqrt{\det P}\,(\det N)^{-1/2}\,e^{\omega^\top N^{-1}\omega}\le\int e^{2\eta\cdot\omega}\mu(d\eta)\le\|T\|^2e^{4\beta(\operatorname{Im}z)^2}.
\tag{45}
\]
Hence \(|\operatorname{Im}\mathcal F(z)|\le C(1+|\operatorname{Im}z|)\), the analogue of (22). As in Theorem 5, each component of \(\operatorname{Im}\mathcal F\) is an entire harmonic function of at most linear growth, hence affine, so \(\mathcal F\) is affine with real coefficients, \(F\) is affine on every line, and \(F(x)=Mx+b\) globally. If \(Mv=0\) with \(v\ne0\), then \(Tk_P(\cdot,0)\) is positive and constant along \(v\), contradicting (3). This proves part 1.

*Part 2.* Write \(Z=Z_G+Z_J\) with independent \(Z_G\sim\mathcal N(\ell,Q)\) and jump part \(Z_J\). Then \(T=T_G\circ S_J\), where \(S_Jf=\mathbb E f(\cdot+Z_J)\) is the Fourier multiplier \(\varphi_J\) on \(\mathcal H_P\), a contraction since \(|\varphi_J|\le1\), and \(T_G\) is the Gaussian transition (6) with shift \(b+\ell\). If \(MRM^\top\preceq P+4Q\), Proposition 3 gives boundedness and the norm bound.

Conversely, suppose \(T\) is bounded. Let \(r_x\in\mathcal H_P\) represent \(f\mapsto(Tf)(x)\); by the computation above \(\overline{r_x}=\widetilde G(\cdot-(Mx+b))\). By Aronszajn's range-inclusion criterion (Aronszajn, 1950; Paulsen and Raghupathi, 2016), \(\|T\|^2k_R(x,x')-\langle r_{x'},r_x\rangle_P\) is a positive kernel, where \(\langle r_{x'},r_x\rangle_P=\int e^{i\eta\cdot M(x-x')}\mu(d\eta)\). Both terms are translation invariant on \(\mathbb R^d\), so by Bochner's theorem the push-forward \((M^\top)_\#\mu\) is dominated by \(\|T\|^2\) times the spectral measure of \(k_R\), whose density is \(\pi^{-d/2}2^{-d}\sqrt{\det R}\,e^{-\zeta^\top R\zeta/4}\). By (36), \(|\varphi|^2\ge c_\epsilon e^{-\eta^\top(Q+\epsilon I)\eta}\) for every \(\epsilon>0\), so, with \(S_\epsilon=P+4Q+4\epsilon I\) and \(E_\epsilon=(M^\top S_\epsilon^{-1}M)^{-1}\), \(\mu\) has density at least a positive constant times \(e^{-\eta^\top S_\epsilon\eta/4}\), and \((M^\top)_\#\mu\) has density at least a positive constant times the Gaussian marginal \(\exp[-\tfrac14\zeta^\top E_\epsilon\zeta]\). Domination by \(e^{-\zeta^\top R\zeta/4}\) for large \(\zeta\) forces \(E_\epsilon\succeq R\), that is \(M^\top S_\epsilon^{-1}M\preceq R^{-1}\). Letting \(\epsilon\downarrow0\) gives \(M^\top(P+4Q)^{-1}M\preceq R^{-1}\), equivalent to \(MRM^\top\preceq P+4Q\). For \(m=d\) the norm is (37). \(\square\)

**Scope.** Part 1 covers Cauchy, stable, compound-Poisson and tempered noises, and so Euler and splitting steps \(x\mapsto x+hb(x)+\Delta L_h\) for every Lévy-driven SDE with additive noise: such a step preserves no pair of global Gaussian RKHSs unless the drift is affine. The proof uses (40) twice: to divide by \(\alpha\), and in (45). For laws whose characteristic function vanishes on an open set, or decays faster than every Gaussian, we do not know whether rigidity persists. State-dependent non-Gaussian noise \(Z=Z(x)\) is not covered, because the translate structure (42) is lost. The companion script checks (42), the identity \(\mu(\mathbb R)=\|\widetilde G\|_P^2\) and the lower bound in (45) numerically for one-dimensional Cauchy noise, which is pure-jump and has no moments.

## The exact image space

The jump component affects the image norm below quadratic scale. In equal dimensions with invertible \(M\), let \(E=M^{-1}(P+4Q)M^{-\top}\).

**Proposition 10 (range of an affine infinitely divisible transition).** \(T\) is injective on \(\mathcal H_P\), and its range consists of the continuous versions of \(g\in L^2(\mathbb R^d)\) with
\[
\int|\widehat g(\eta)|^2\exp\!\left[\tfrac14\eta^\top E\eta+2j(M^{-\top}\eta)\right]d\eta<\infty.
\tag{46}
\]
The norm transported from the unique preimage is \(|\det M|c_P\) times this integral. Consequently \(\mathcal H_{E+\rho I}\subseteq T(\mathcal H_P)\subseteq\mathcal H_E\) for every \(\rho>0\), and if \(\nu\) is finite then \(T(\mathcal H_P)=\mathcal H_E\) with equivalent norms.

**Proof.** Infinitely divisible characteristic functions have no zeros. Solving the Fourier identity in the proof of Theorem 8 for \(\widehat f\) and substituting into (2) gives (46), its norm and injectivity. Since \(j\ge0\), the upper inclusion follows. By Lemma 7, \(2j(M^{-\top}\eta)\le\rho|\eta|^2/4+C_\rho\), which gives the lower inclusion. For finite \(\nu\), \(0\le j\le2\nu(\mathbb R^d\setminus\{0\})\). \(\square\)

## Linear dynamics with Lévy forcing

Let \(L_t\) be a Lévy process with triplet \((\ell,D,\nu)\), truncation as in (34), and
\[
dX_t=AX_t\,dt+dL_t,\qquad K_tf(x)=\mathbb E_xf(X_t).
\]
The solution has state map \(M_t=e^{tA}\) and infinitely divisible noise with exponent \(\Psi_t(\xi)=\int_0^t\Psi(e^{sA^\top}\xi)\,ds\), where \(\Psi\) is the exponent of \(L_1\); no moment assumption is needed. Its Gaussian component and jump exponent are
\[
Q_G(t)=\int_0^te^{sA}De^{sA^\top}\,ds,\qquad j_t(\xi)=\int_0^tj(e^{sA^\top}\xi)\,ds.
\tag{47}
\]
Lemma 7 applies to \(j_t\) without hidden uniformity: with \(C_t=\max_{0\le s\le t}\|e^{sA}\|\),
\[
\frac{j_t(\xi)}{|\xi|^2}\le t\int_{|z|\le1}\min\left\{\frac2{|\xi|^2},\frac{C_t^2|z|^2}{2}\right\}\nu(dz)+\frac{2t\nu(|z|>1)}{|\xi|^2}\longrightarrow0.
\]

**Theorem 11 (sharp Lévy--OU invariance).** For every \(t\ge0\),
\[
K_t(\mathcal H_P)\subseteq\mathcal H_P\iff e^{tA}Pe^{tA^\top}\preceq P+4Q_G(t),
\]
and invariance for every time is equivalent to
\[
\boxed{\quad AP+PA^\top\preceq4D.\quad}
\tag{48}
\]
At every admissible time, \(\|K_t\|=\|K_t\|_{\rm ess}=e^{-t\operatorname{tr}A/2}\). No stability of \(A\), stationary law or large-jump moment is required.

**Proof.** Apply Theorem 8 to the transition at time \(t\), and use \(P+4Q_G(t)-e^{tA}Pe^{tA^\top}=\int_0^te^{sA}(4D-AP-PA^\top)e^{sA^\top}ds\) as in Theorem 6. \(\square\)

Under (48), the Fourier isometry of Section 9 conjugates \(K_t\) to the Lévy--OU semigroup on Lebesgue \(L^2\) with the same \(A\), drift \(\ell\) and jump measure \(\nu\), and Gaussian rate \(D_{\rm eff}=D-\frac14(AP+PA^\top)\succeq0\): the conjugation replaces \(Q_G(t)\) by \(Q_G(t)+(P-M_tPM_t^\top)/4=\int_0^te^{sA}D_{\rm eff}e^{sA^\top}ds\) and leaves the drift and jump factors unchanged. Convolution intertwinings for Lévy--OU operators are established (Sarkar, 2026, Section 7); the point here is this particular unitary identification of the global Gaussian RKHS.

# A diffusion approximation that changes RKHS membership

Convergence of noise laws need not preserve Gaussian RKHS invariance. We show that the failure persists even when prediction operators converge in a strong uniform sense, and that one fixed observable witnesses it for every approximating process.

For \(\varepsilon>0\) let
\[
L_t^\varepsilon=\varepsilon\sum_{i=1}^d\big(N_i^+(t)-N_i^-(t)\big)e_i,
\tag{49}
\]
with independent Poisson processes of rate \(1/(2\varepsilon^2)\). Then \(\Psi_\varepsilon(\xi)=\varepsilon^{-2}\sum_i[\cos(\varepsilon\xi_i)-1]\to-\frac12|\xi|^2\), so the limit is standard Brownian motion. Each prelimit has zero Gaussian component, although its total covariance rate is already \(I_d\). Let \(K_t^\varepsilon\) be the transition of \(dX_t=AX_t\,dt+dL_t^\varepsilon\) and \(K_t^0\) its Brownian counterpart. In dimension two take
\[
A=\begin{pmatrix}-1&5\\0&-1\end{pmatrix},\qquad P=I_2,\qquad t_*=\frac1{10},\qquad f(x)=e^{-(8/5)|x|^2}.
\tag{50}
\]

**Theorem 12 (fixed-observable membership loss with uniform prediction convergence).** The function \(f\) in (50) belongs to \(\mathcal H_I\), and
\[
K_{t_*}^\varepsilon f\notin\mathcal H_I\ \text{for every }\varepsilon>0,\qquad K_{t_*}^0f\in\mathcal H_I.
\tag{51}
\]
Nevertheless, for every \(t\ge0\),
\[
\|K_t^\varepsilon-K_t^0\|_{\mathcal H_I\to C_b(\mathbb R^2)}\le\frac{2\sqrt6}{9}(e^{6t}-1)\varepsilon^2,
\tag{52}
\]
and at \(t=t_*\) the coefficient is \(0.4475\ldots<0.448\).

**Proof of (51).** Since \(A+A^\top\) has eigenvalues \(3\) and \(-7\), the Brownian rate \(I\) satisfies (48), while every pure-jump prelimit fails it. For the fixed time and observable, \(M=e^{t_*A}=e^{-1/10}\begin{pmatrix}1&1/2\\0&1\end{pmatrix}\) and \(MM^\top=e^{-1/5}\begin{pmatrix}5/4&1/2\\1/2&1\end{pmatrix}\). For \(v=(1,1)^\top/\sqrt2\),
\[
v^\top MM^\top v=\tfrac{13}{8}e^{-1/5}=1.330\ldots>1.25.
\tag{53}
\]
The observable is \(f=k_G(\cdot,0)\) with \(G=\frac58I\); by (13), \(f\in\mathcal H_I\) with \(\|f\|_I^2=25/16\). Its Fourier transform is a constant times \(e^{-5|\xi|^2/32}\), so the prelimit output norm requires integrating
\[
\exp\left[\tfrac14\xi^\top(MM^\top-\tfrac54I)\xi-2j_{\varepsilon,t_*}(\xi)\right].
\]
The compound-Poisson exponent satisfies \(0\le j_{\varepsilon,t_*}\le2dt_*/\varepsilon^2\), so for fixed \(\varepsilon\) the damping is bounded below by a positive constant. By (53) the quadratic form is positive on a cone, and the integral diverges. For the Brownian limit the Gaussian component is \(Q_{t_*}\), and (48) with \(D=I\) gives \(I+4Q_{t_*}-MM^\top\succeq0\), so \(\tfrac54I+4Q_{t_*}-MM^\top\succeq\tfrac14I\succ0\). The output is a Gaussian with matrix \(M^{-1}(G+2Q_{t_*})M^{-\top}\), and twice this matrix minus \(I\) is congruent to \(\frac54I+4Q_{t_*}-MM^\top\succ0\); by (13) it lies in \(\mathcal H_I\).

**Proof of (52).** The argument works in every dimension and for every \(P\succ0\). For (49),
\[
j_{\varepsilon,t}(\xi)=\varepsilon^{-2}\int_0^t\sum_i\left[1-\cos\big(\varepsilon(e^{sA^\top}\xi)_i\big)\right]ds,\qquad
j_{0,t}(\xi)=\tfrac12\int_0^t|e^{sA^\top}\xi|^2ds.
\]
The inequalities \(0\le u^2/2-(1-\cos u)\le u^4/24\) give
\[
0\le j_{0,t}(\xi)-j_{\varepsilon,t}(\xi)\le\frac{\varepsilon^2H_t}{24}|\xi|^4,\qquad H_t=\int_0^t\|e^{sA}\|^4ds.
\tag{54}
\]
The transition characteristic functions are \(e^{-j_{\varepsilon,t}}\) and \(e^{-j_{0,t}}\), and \(|e^{-a}-e^{-b}|\le|a-b|\) for \(a,b\ge0\). Fourier inversion and Cauchy--Schwarz give
\[
\|K_t^\varepsilon-K_t^0\|_{\mathcal H_P\to C_b}\le C_{P,t}\varepsilon^2,\qquad
C_{P,t}=\frac{(2\pi)^{-d/2}H_t}{24\sqrt{c_P}}\left(\int|\xi|^8e^{-\xi^\top P\xi/4}\,d\xi\right)^{1/2}.
\tag{55}
\]
For (50), \(\lambda_{\max}((A+A^\top)/2)=3/2\), so \(\|e^{sA}\|\le e^{3s/2}\) and \(H_t\le(e^{6t}-1)/6\). Polar integration gives \(\int_{\mathbb R^2}|\xi|^8e^{-|\xi|^2/4}d\xi=24576\pi\), and \((2\pi)^{-1}c_I^{-1/2}\sqrt{24576\pi}=32\sqrt6\). This gives (52). \(\square\)

## Exact prediction norm and the sharp order

**Proposition 13 (exact norm into bounded continuous functions).** If \(T_if(x)=\mathbb E f(Mx+Z_i)\), \(i=1,2\), with noise characteristic functions \(\varphi_i\), then
\[
\|T_1-T_2\|_{\mathcal H_P\to C_b}=\frac{(2\pi)^{-d/2}}{\sqrt{c_P}}\left(\int|\varphi_1(\xi)-\varphi_2(\xi)|^2e^{-\xi^\top P\xi/4}\,d\xi\right)^{1/2}.
\tag{56}
\]
For (49), every \(t>0\) satisfies
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-2}\|K_t^\varepsilon-K_t^0\|_{\mathcal H_P\to C_b}=\Gamma_{P,t},\qquad
\Gamma_{P,t}=\frac{(2\pi)^{-d/2}}{24\sqrt{c_P}}\left(\int a_t(\xi)^2e^{-2j_{0,t}(\xi)-\xi^\top P\xi/4}\,d\xi\right)^{1/2}\in(0,\infty),
\tag{57}
\]
where \(a_t(\xi)=\int_0^t\sum_i|(e^{sA^\top}\xi)_i|^4ds\).

**Proof.** At fixed \(x\), Fourier inversion writes the difference as \(f\mapsto(2\pi)^{-d/2}\int\widehat f(\xi)e^{i(Mx)\cdot\xi}[\varphi_1-\varphi_2](\xi)\,d\xi\). Its norm on (2) is the right side of (56), independently of \(x\), and Cauchy--Schwarz is attained at \(x=0\) by a multiple of the function with Fourier transform \(\overline{\varphi_1-\varphi_2}\,e^{-\xi^\top P\xi/4}\). For fixed \(\xi\), \(\varepsilon^{-2}(e^{-j_{\varepsilon,t}}-e^{-j_{0,t}})\to e^{-j_{0,t}}a_t/24\). By (54) the left side is bounded by \(H_t|\xi|^4/24\), square-integrable against the weight, and dominated convergence gives (57). For \(t>0\), \(a_t(\xi)>0\) when \(\xi\ne0\). \(\square\)

The norm (56) is the Gaussian-kernel maximum mean discrepancy between the two noise laws, the norm of their mean-embedding difference; this identity is standard kernel-mean duality in the normalisation of (2) (Nishiyama and Fukumizu, 2016, Lemma 2.5).

**The constants of the example.** For (50), \(\Gamma_{I,1/10}=0.0993\) (more precisely \(0.099254\)), computed from (57) by exact radial integration and one-dimensional angular quadrature. Direct evaluation of (56) gives \(\varepsilon^{-2}\|K^\varepsilon_{t_*}-K^0_{t_*}\|=0.09921\) at \(\varepsilon=0.2\) and \(0.09925\) at \(\varepsilon=0.1\). The explicit coefficient \(0.4475\) in (52) is therefore about \(4.5\) times the true limiting constant; even with the exact value \(H_{1/10}=0.13661\) in place of its bound \(0.13702\), (55) gives \(0.4462\). The bound establishes the order \(\varepsilon^2\), and (57) shows that this order is sharp; the coefficient in (52) is not sharp.

**How to read the discontinuity.** The membership statement concerns the global norm of \(\mathcal H_I\), which requires the Fourier transform of an output to decay like a Gaussian of a prescribed width. A pure-jump prelimit has no Gaussian damping at high frequency, so once Theorem 8 is known, failure of membership is immediate. The convergence statement uses the much weaker norm into \(C_b\). There is no contradiction between the two, in the same way that smooth functions can converge uniformly to a nonsmooth limit. The point of Theorem 12 is practical: the global RKHS norm is exactly the norm in which the invariance hypothesis \(K^t\mathcal H\subset\mathcal H\) of kEDMD error bounds is formulated (Philipp et al., 2025b, Theorem 4.2), so prediction convergence alone does not transfer that hypothesis from a diffusion model to its jump approximations, even when prediction is uniformly accurate over the whole unit ball and globally in the starting point.

# Sampling intervals and exact thresholds

Fixed-time invariance differs from invariance at every time. Write \(D=BB^\top\) and \(Q_t=\int_0^te^{As}De^{A^\top s}ds\).

**Proposition 14 (eventual invariance).** If \(A\) is Hurwitz, then for every \(P\succ0\) and \(D\succeq0\) there is \(T_0<\infty\) such that \(K_t\mathcal H_P\subseteq\mathcal H_P\) for all \(t\ge T_0\). The admissible times form a closed additive subsemigroup of \([0,\infty)\).

**Proof.** As \(t\to\infty\), \(M_t\to0\) and \(Q_t\to\Sigma\), so \(P+4Q_t-M_tPM_t^\top\to P+4\Sigma\succ0\). Continuity gives closedness and \(K_{s+t}=K_sK_t\) additivity. \(\square\)

**Proposition 15 (shear sampling boundary).** Let \(A_s=\begin{pmatrix}-1&s\\0&-1\end{pmatrix}\), \(D=qI_2\), \(P=I_2\), \(q\ge0\), \(h=1+2q\). For \(t>0\), \(K_t\) preserves \(\mathcal H_I\) if and only if
\[
\frac{\sinh t}{t}\ge r_{s,q}:=\frac{|s|h}{2\sqrt{h^2+s^2q(1+q)}}.
\tag{58}
\]
If \(|s|\le2+4q\), every \(t>0\) is admissible. Otherwise the admissible positive times are exactly \([T_{s,q},\infty)\), where \(\sinh T_{s,q}/T_{s,q}=r_{s,q}\).

**Proof.** With \(e=e^{-2t}\) and \(G_t=I+4Q_t-M_tM_t^\top\), direct integration gives \((G_t)_{22}=h(1-e)\), \((G_t)_{12}=s\{q(1-e)-hte\}\) and \((G_t)_{11}=h(1-e)+s^2\{q[1-e(1+2t)]-ht^2e\}\). Since \((G_t)_{22}>0\), positivity is equivalent to
\[
\det G_t=[h^2+s^2q(1+q)](1-e)^2-s^2h^2t^2e\ge0.
\tag{59}
\]
The identity \((1-e^{-2t})^2=4e^{-2t}\sinh^2t\) gives (58). \(\sinh t/t\) increases strictly from one to infinity, and \(r_{s,q}\le1\) is equivalent to \(s^2\le4h^2\). \(\square\)

For \(q=1\) the old sufficient threshold is \(|s|\le4\) and the sharp all-time threshold \(|s|\le6\), so \(s=5\) is not an isolated case. At \(s=7\) the sampling threshold is \(0.3000561741\), at \(s=10\) it is \(0.4721567642\), and as \(|s|\to\infty\) it tends to the solution of \(\sinh T/T=3/(2\sqrt2)\), \(0.5979259925\). For fixed \(|s|>2\), the least isotropic Brownian covariance rate permitting invariance is \(q=(|s|-2)/4\), half the rate required by the earlier sufficient condition; the noise amplitudes differ by \(\sqrt2\).

For practice, the admissible sampling times \([T_{s,q},\infty)\) are a lower bound on the lag time at which a Gaussian-kernel Koopman model of such a system has an invariant RKHS. Lag selection is routine in kEDMD and related methods, and Proposition 15 shows that very short lags can be the ones that break the invariance hypothesis.

![Exact formulas evaluated numerically. Left: the sampling boundary for the shear family with Brownian covariance rate \(I\); the dotted and dashed lines mark the earlier sufficient threshold \(s=4\) and the sharp all-time threshold \(s=6\). Right: the norm of the fixed observable \(e^{-|x|^2}\) for the shear \(s=5\), after removing the growth factor \(e^t\). The plot illustrates the formulas; the proofs do not depend on it.](figures/invariance_and_norm.pdf){width=100%}

# Admissible bandwidths and kernel EDMD

Throughout this section \(A\in\mathbb R^{d\times d}\), \(B\in\mathbb R^{d\times n}\), \(\mathcal L_A(P)=AP+PA^\top\) and \(G=BB^\top\). By Theorem 6 the set of Gaussian bandwidths preserved by the whole OU semigroup is
\[
\operatorname{Adm}(A,B)=\{P\succ0:\ AP+PA^\top\preceq4BB^\top\}.
\tag{60}
\]
Write \(\operatorname{Adm}_2(A,B)\) for the set defined with \(2BB^\top\), certified by Philipp et al. (2025a), Theorem 2.1. Theorem 6 needs no stability or controllability, so (60) is meaningful for every pair \((A,B)\). Checking \(P\in\operatorname{Adm}\) is a linear matrix inequality, and searching for an admissible \(P\) is a semidefinite feasibility problem.

**Proposition 16 (structure of the admissible set).**

(a) \(\operatorname{Adm}(A,B)\) is convex, and \(cP\in\operatorname{Adm}(A,B)\) whenever \(P\in\operatorname{Adm}(A,B)\) and \(0<c\le1\).

(b) \(\operatorname{Adm}(A,B)=2\operatorname{Adm}_2(A,B)\supseteq\operatorname{Adm}_2(A,B)\). The inclusion is strict as soon as some \(P\in\operatorname{Adm}\) has \(AP+PA^\top\not\preceq0\), for example for the shear (32).

(c) If \((A,B)\) is stabilisable, there is \(P\succ0\) with \(AP+PA^\top\prec4BB^\top\). Conversely, if \(\operatorname{Adm}(A,B)\ne\varnothing\), every eigenvalue \(\lambda\) of \(A\) with a left eigenvector \(w\) such that \(w^*B=0\) has \(\operatorname{Re}\lambda\le0\).

(d) If \(\lambda\) is an eigenvalue of \(A\) with \(\operatorname{Re}\lambda>0\) and left eigenvector \(w\), every \(P\in\operatorname{Adm}(A,B)\) satisfies
\[
w^*Pw\le\frac{2|B^\top w|^2}{\operatorname{Re}\lambda}.
\tag{61}
\]
Unstable modes cap the admissible bandwidth in their left-eigenvector directions.

(e) If \(\operatorname{Adm}(A,B)\ne\varnothing\), the recession directions of the closure of \(\operatorname{Adm}(A,B)\) are \(\{D\succeq0:AD+DA^\top\preceq0\}\). If \(A\) is Hurwitz and \(\Sigma_\infty=\int_0^\infty e^{As}BB^\top e^{A^\top s}ds\succ0\), then \(c\Sigma_\infty\in\operatorname{Adm}(A,B)\) for every \(c>0\). If \(A\) is marginally stable (spectrum in the closed left half-plane, imaginary-axis eigenvalues semisimple), there is \(P\succ0\) with \(cP\in\operatorname{Adm}(A,B)\) for all \(c>0\).

**Proof.** (a) \(\mathcal L_A\) is linear, and \(\mathcal L_A(cP)=c\mathcal L_A(P)\preceq4cG\preceq4G\) for \(c\le1\). (b) \(\mathcal L_A(P)\preceq4G\iff\mathcal L_A(P/2)\preceq2G\). If \(\operatorname{Adm}=\operatorname{Adm}_2\), then \(\operatorname{Adm}\) is closed under doubling, so \(\mathcal L_A(2^kP)\preceq4G\) for all \(k\) and \(\mathcal L_A(P)\preceq0\); for (32), \(\mathcal L_A(I)=A+A^\top\not\preceq0\). (c) Let \(A+BK\) be Hurwitz and \((A+BK)P+P(A+BK)^\top=-I\) with \(P\succ0\). For \(\mu>0\), \(-BKP-PK^\top B^\top\preceq\mu BB^\top+\mu^{-1}PK^\top KP\); choosing \(\mu\) with \(\mu^{-1}PK^\top KP\preceq\frac12I\) gives \(AP+PA^\top\preceq-\frac12I+\mu BB^\top\prec\mu BB^\top\), so \((4/\mu)P\) works. Conversely, \(w^*\mathcal L_A(P)w=2\operatorname{Re}\lambda\,w^*Pw\le4|B^\top w|^2=0\) with \(w^*Pw>0\). (d) The same identity gives \(2\operatorname{Re}\lambda\,w^*Pw\le4|B^\top w|^2\). (e) Let \(C=\{P\succeq0:\mathcal L_A(P)\preceq4G\}\). If \(P_0\in\operatorname{Adm}\), then for \(P\in C\) and \(0<\theta\le1\), \((1-\theta)P+\theta P_0\in\operatorname{Adm}\) by convexity, so \(C\) is the closure of \(\operatorname{Adm}\) (nonemptiness is needed: \(A=1\), \(B=0\) gives \(\operatorname{Adm}=\varnothing\) but \(C=\{0\}\)). The recession cone of the closed convex set \(C\) is obtained by deleting \(4G\). For Hurwitz \(A\), \(\mathcal L_A(c\Sigma_\infty)=-cBB^\top\preceq4BB^\top\). For marginally stable \(A\) the Lyapunov theorem gives \(P\succ0\) with \(\mathcal L_A(P)\preceq0\). \(\square\)

Loewner cofinality of the admissible set can hold even without an admissible positive-definite ray. A ray \(cP\in\operatorname{Adm}\) for all \(c>0\) forces \(AP+PA^\top\preceq0\), which excludes nontrivial imaginary-axis Jordan blocks; nevertheless, for \(A=\begin{pmatrix}0&1\\0&0\end{pmatrix}\) and \(B=I\), \(P=\begin{pmatrix}p_{11}&p_{12}\\p_{12}&p_{22}\end{pmatrix}\) is admissible exactly when \(4(4-2p_{12})\ge p_{22}^2\), and with \(p_{12}=2-p_{22}^2/8\) and \(p_{11}\) large this contains matrices above any prescribed \(R\succ0\), although no positive-definite ray is admissible. We have no exact characterisation of nonemptiness for non-stabilisable pairs beyond (c).

**Proposition 17 (exact isotropic bandwidth rule).** Let \(S_A=A+A^\top\). For \(P=\sigma^2I\),
\[
K^t(\mathcal H_{\sigma^2I})\subseteq\mathcal H_{\sigma^2I}\ \text{for all }t\ge0\iff\sigma^2\le\sigma_\star^2:=4\inf_{x^\top S_Ax>0}\frac{|B^\top x|^2}{x^\top S_Ax},
\tag{62}
\]
with \(\sigma_\star^2=+\infty\) when \(S_A\preceq0\). If \(G=BB^\top\succ0\) and \(\lambda_{\max}(G^{-1/2}S_AG^{-1/2})>0\),
\[
\sigma_\star^2=\frac{4}{\lambda_{\max}\big(G^{-1/2}S_AG^{-1/2}\big)}.
\tag{63}
\]
The threshold for the published sufficient condition (31) is exactly \(\sigma_\star^2/2\).

**Proof.** \(4G-\sigma^2S_A\succeq0\) means \(\sigma^2x^\top S_Ax\le4|B^\top x|^2\) for all \(x\); vectors with \(x^\top S_Ax\le0\) impose nothing. If \(G\succ0\), substitute \(x=G^{-1/2}y\). Replacing \(4\) by \(2\) halves the infimum. \(\square\)

In one dimension, (62) reads \(\sigma^2\le2\beta^2/a\) for \(dX=aX\,dt+\beta\,dW\) with \(a>0\), and imposes nothing for \(a\le0\). For the shear (32), \(S_A\) has eigenvalues \(3\) and \(-7\), so \(\sigma_\star^2=4/3\), against \(2/3\) under (31). With the single noise channel \(B=e_2\), \(\sigma_\star^2=8/21\), positive although \(BB^\top\) is singular. By (11) the operator norm \(e^{-t\operatorname{tr}A/2}\) does not depend on \(P\); the choice of bandwidth affects admissibility, not the growth rate.

## Consequence for kernel EDMD error bounds

For Philipp, Schaller, Worthmann, Peitz and Nüske (2025b) we cite arXiv:2312.10460v1; theorem, remark and equation numbers below refer to it. Their Theorem 4.2 bounds the kEDMD prediction error for SDEs of the form (3.1) there. Its second estimate, their (4.2), holds under the additional hypothesis \(K^t\mathcal H_{\mathcal Y}\subset\mathcal H_{\mathcal X}\), where \(\mathcal H_{\mathcal X}\) and \(\mathcal H_{\mathcal Y}\) are the RKHSs of the kernel restricted to \(\mathcal X\subset\mathcal Y\):
\[
\|K^t-\widehat K^{m,t}_r\|_{\mathcal H_{\mathcal Y}\to L^2(\mathcal X;\mu)}\le\sqrt{\lambda_{r+1}}\,\|K^t\|_{\mathcal H_{\mathcal Y}\to\mathcal H_{\mathcal X}}+c_r\varepsilon,
\]
with probability at least \(1-\delta\). Their Remark 4.3 and Theorem D.2 verify the hypothesis for the scalar process \(dX=-\alpha X\,dt+dW\) with \(\mathcal Y=\mathbb R\). Their bound (5.9) for deterministic control-affine systems uses the same hypothesis and is not addressed here.

**Corollary 18 (multivariate OU in kEDMD).** Let \(B\in\mathbb R^{d\times d}\), so that \(dX=AX\,dt+B\,dW\) has the form (3.1) of Philipp et al. (2025b). Take the kernel \(k_P\), \(\mathcal Y=\mathbb R^d\) and \(\mathcal X=\overline\Omega\) with \(\Omega\) bounded, connected and open. Assume all standing, measure, sampling, spectral-gap and sample-size hypotheses of their Theorem 4.2 (among them finite mass on \(\mathcal Y\), \(\mu(\mathcal X)=1\), uniform transition-measure domination over the horizon, simple Mercer eigenvalues through \(r+1\), \(0<\varepsilon<\delta_r\), \(0<\delta<1\), \(m\ge\max\{r,8\|k\|_\infty^2\log(4/\delta)/\varepsilon^2\}\), and their estimator and data construction). For each fixed sampling time \(t>0\) with \(Q_t\succ0\),
\[
K^t\mathcal H_{\mathcal Y}\subset\mathcal H_{\mathcal X}\iff e^{At}Pe^{A^\top t}\preceq P+4Q_t,
\tag{64}
\]
and in that case their estimate (4.2) holds with \(\|K^t\|_{\mathcal H_{\mathcal Y}\to\mathcal H_{\mathcal X}}\le e^{-t\operatorname{tr}A/2}\). In particular, for each fixed sampling time, their (4.2) holds whenever \(AP+PA^\top\preceq4BB^\top\).

**Proof.** \(\mathcal H_{\mathcal Y}=\mathcal H_P\), and restriction \(\mathcal H_P\to\mathcal H_{\mathcal X}\) is a contraction onto \(\mathcal H_{\mathcal X}\) (Aronszajn, 1950). If the right side of (64) holds, Theorem 6 gives the inclusion and the norm bound. Conversely, suppose \(K^tf|_{\mathcal X}=g|_{\mathcal X}\) with \(g\in\mathcal H_P\). Functions in \(\mathcal H_P\) are real-analytic by (16), and so is \(K^tf(x)=\int f(y)\,\phi_{Q_t}(y-e^{At}x)\,dy\), because \(f\) is bounded and the Gaussian density \(\phi_{Q_t}\) extends to an entire function of \(x\) with locally uniform integrable bounds. Since they agree on the open set \(\Omega\), the identity theorem on \(\mathbb R^d\) gives \(K^tf=g\in\mathcal H_P\). Hence \(K^t\mathcal H_P\subseteq\mathcal H_P\), and (28) applies. \(\square\)

Corollary 18 only checks the RKHS hypothesis of an existing theorem. It does not tighten their constants, and \(\|K^t\|\) still grows like \(e^{-t\operatorname{tr}A/2}\) for stable drift. The square-\(B\) assumption follows their setting; a non-square \(B\) can be replaced by a square root of \(BB^\top\).

**Table 1.** Exact matrix computations for the shear (32), \(B=I\), \(P=\sigma^2I\). The columns give the published sufficient condition (31), the sharp all-time rule (29), and the sampling times among \(t=0.05,0.1,0.25,0.5,1,2,3\) at which the fixed-time criterion (28), and hence the hypothesis of Corollary 18, holds. At every invariant entry the exact norm (8) equals \(e^t\).

| \(\sigma^2\) | (31) | (29) | Fixed-time invariance |
|---|---|---|---|
| 0.5 | yes | yes | all |
| 2/3 | yes | yes | all |
| 1 | no | yes | all |
| 4/3 | no | yes | all |
| 1.5 | no | no | \(t\ge0.5\) |
| 2 | no | no | \(t\ge1\) |
| 4 | no | no | \(t\ge2\) |

Table 1 is a demonstration of the hypothesis, not a fitted kEDMD model: a finite-data fit cannot detect membership in the global RKHS, which is exactly why the hypothesis needs a criterion.

# Consequences of an exact isometry

This section collects consequences of one identity. Assume \(AP+PA^\top\preceq4D\), put \(D_{\rm eff}=D-\frac14(AP+PA^\top)\succeq0\), and let \(\Sigma=\int_0^\infty e^{As}De^{A^\top s}ds\) when \(A\) is Hurwitz.

**Theorem 19 (isometry, spectrum and growth).**

(a) *Isometry.* The map \(U_P:\mathcal H_P\to L^2(\mathbb R^d,dx)\), \(\widehat{U_Pf}(\xi)=c_P^{1/2}e^{\xi^\top P\xi/8}\widehat f(\xi)\), is unitary and onto. It conjugates \(K_t\) to the OU transition on Lebesgue \(L^2\) with drift \(A\) and Brownian covariance rate \(D_{\rm eff}\), whose finite-time covariance is
\[
Q_{\rm eff}(t)=Q_t+\tfrac14(P-M_tPM_t^\top)=\int_0^te^{As}D_{\rm eff}e^{A^\top s}ds.
\tag{65}
\]
In particular the invariant semigroup is strongly continuous on \(\mathcal H_P\).

(b) *Spectrum.* If \(A\) is Hurwitz, put \(a=-\operatorname{tr}A/2>0\) and let \(\mathcal L_P\) be the generator on \(\mathcal H_P\). Then
\[
\operatorname{spec}(\mathcal L_P)=\{z:\operatorname{Re}z\le a\},\qquad\operatorname{spec}(K_t)=\{z:|z|\le e^{at}\}\quad(t>0).
\tag{66}
\]

(c) *Growth of each observable.* If \(A\) is Hurwitz, every nonzero \(f\in\mathcal H_P\) satisfies
\[
e^{t\operatorname{tr}A}\|K_tf\|_P^2\ \downarrow\ c_P\int|\widehat f(\xi)|^2e^{-\xi^\top\Sigma\xi}\,d\xi>0,
\qquad
\lim_{t\to\infty}\frac1t\log\|K_tf\|_P=-\frac12\operatorname{tr}A,
\tag{67}
\]
and \(\|K_tf\|_P<e^{at}\|f\|_P\) for \(t>0\). Neither \(K_t\) (\(t>0\)) nor the generator has eigenvalues on \(\mathcal H_P\).

**Proof.** (a) The Gaussian RKHS norm gives unitarity, and multiplication by the reciprocal Gaussian gives surjectivity. In the affine Fourier formula at \(\eta=M_t^\top\xi\), the transformed multiplier is \(\exp\{-\xi^\top[Q_t+(P-M_tPM_t^\top)/4]\xi/2\}\) and the determinant factor is \(|\det M_t|^{-1}\), which is the Fourier formula for the stated Lebesgue-space transition. Integrating the derivative of \(e^{At}Pe^{A^\top t}\) gives the second equality in (65). This is an identity of bounded semigroups, not only of generators.

(b) The effective stationary Gramian is \(\int_0^\infty e^{As}D_{\rm eff}e^{A^\top s}ds=\Sigma+P/4\succ0\), so the effective pair is controllable even when \(D_{\rm eff}\) is singular: a vanishing Gramian quadratic form would force \(D_{\rm eff}^{1/2}e^{A^\top s}v=0\) for all \(s\), and analyticity would make \(v\) orthogonal to every controllability direction. Fornaro, Metafune, Pallara and Schnaubelt (2021), Theorems 2.9 and 4.1, treat the operator \(\mathcal Lu=\operatorname{Tr}(QD^2u)+\langle Bx,Du\rangle\) on \(L^p(\mathbb R^d,dx)\), with \(D\) the gradient. With their \(B=A\), \(Q=D_{\rm eff}/2\) and \(p=2\), they give the half-plane and disc in (66) on Lebesgue \(L^2\), and the unitary \(U_P\) transfers them to \(\mathcal H_P\).

(c) With \(G_t=P+4Q_t-M_tPM_t^\top\), the exact affine norm formula is \(e^{t\operatorname{tr}A}\|K_tf\|_P^2=c_P\int|\widehat f|^2e^{\xi^\top P\xi/4}e^{-\xi^\top G_t\xi/4}d\xi\). The matrices \(G_t\) increase from zero to \(P+4\Sigma\), and dominated convergence gives (67). By (a) and (b), \(G_t=4Q_{\rm eff}(t)\succ0\) for \(t>0\), which gives the strict inequality. If \(K_tf=\mu f\) with \(f\ne0\), injectivity gives \(\mu\ne0\); (67) at times \(nt\) forces \(|\mu|=e^{at}\), contradicting the strict inequality. An eigenfunction of the generator would be one of every \(K_t\). \(\square\)

Part (b) is a transfer of an existing spectral theorem; the contribution is the explicit isometry and the verification of the effective hypotheses. The target of \(U_P\) is \(L^2\) for **Lebesgue measure**, not for the invariant Gaussian measure, which is why the spectrum is a half-plane. Hermite polynomials from stationary Gaussian \(L^2\) do not belong to the global Gaussian RKHS.

**Theorem 20 (essential norm and finite-rank approximation).** For any bounded affine Gaussian transition \(T:\mathcal H_P(\mathbb R^d)\to\mathcal H_R(\mathbb R^d)\) with invertible \(M\),
\[
\|T\|_{\rm ess}=\|T\|=\left(\frac{\det P}{\det R}\right)^{1/4}|\det M|^{-1/2},
\qquad
\inf_{\operatorname{rank}F<\infty}\|T-F\|=\|T\|.
\tag{68}
\]

**Proof.** Fourier isometries and the unitary change of variables for \(M\) turn \(T\) into a multiple of multiplication by a function of supremum one, whose modulus tends to one near the origin, followed by a unitary. For \(\epsilon>0\), a ball on which the modulus exceeds \(1-\epsilon\) supports an infinite orthonormal sequence. Compact operators send this weakly null sequence to a null sequence, so their distance from \(T\) is at least \((1-\epsilon)\|T\|\). The zero operator gives the reverse inequality. \(\square\)

The same holds for outputs restricted to a region with nonempty interior **when the target norm is the restricted Gaussian RKHS norm**: restriction is then isometric, because a function orthogonal to all kernel sections centred in the region vanishes on an open set and hence everywhere. Theorem 20 is an exact barrier for one operator norm. It neither contradicts nor replaces guarantees in \(L^\infty\) on a compact region, in \(L^2\) of a data distribution, or on a fixed finite family of observables, where kEDMD error analyses work (Philipp et al., 2025b; Hertel et al., 2026).

| Norm or property | What the results establish |
|---|---|
| Global Gaussian RKHS membership | Exact invariance criteria; membership fails for one fixed observable in every jump prelimit |
| Operator norm \(\mathcal H_P\to C_b\) | Jump transitions approximate the Brownian transition at sharp order \(\varepsilon^2\) |
| Operator norm \(\mathcal H_P\to\mathcal H_R\) | Finite-rank approximation error equals the full norm for bounded square affine Gaussian transitions |
| Data-weighted or compact-region norms | No impossibility conclusion follows from the global obstruction |

# Conclusion and open problems

Global Gaussian RKHS invariance is a rigid property. Gaussian conditional laws must have constant covariance and affine mean, and additive noise with a Gaussian lower bound on its characteristic function forces an affine drift. For linear dynamics the admissible bandwidths are given exactly by \(MRM^\top\preceq P+4Q\), or \(AP+PA^\top\preceq4BB^\top\) for all times, with only the Gaussian part of the noise counting. This settles the necessity question of Philipp et al. (2025a) through a classical Fock-space criterion, and it doubles the certified bandwidth range for kEDMD. Prediction convergence in a weaker norm does not carry the property across a diffusion approximation.

Open problems:

1. **State-dependent non-Gaussian transitions.** Can a Markov kernel whose conditional laws are neither Gaussian nor a fixed additive noise map one global Gaussian RKHS into another, for example a state-dependent Lévy kernel or a Gaussian mixture? The translate structure used in Theorem 9 is then lost.
2. **Noise without a Gaussian lower bound.** Does drift rigidity persist when the characteristic function vanishes on an open set or decays faster than every Gaussian?
3. **Weaker or weighted norms.** Is there a weighted Gaussian RKHS, for example one adapted to the stationary law, in which stable OU semigroups are invariant and contractive under a sharp condition? What are the analogues of Theorems 5 and 12 in norms used by kEDMD error analyses?
4. **Nonemptiness of the admissible set.** Characterise exactly when \(\operatorname{Adm}(A,B)\ne\varnothing\) for non-stabilisable pairs.

# Reproducibility and claim boundaries

The companion script `code/verify.py` (run as `python3 -I -B code/verify.py --output-dir OUT`) writes only to the chosen output directory and stops with an error if any check fails, also under `python -O`. It derives the slack eigenvalues, effective diffusion, isotropic thresholds and witness norms of the separating example in exact rational arithmetic from the entered matrices. It compares the closed shear formulas with numerical quadrature at 140 parameter settings (largest discrepancies about \(10^{-13}\) for entries and \(10^{-12}\) for determinants) and the effective-covariance identity at 24 noncommuting instances. For Section 6 it computes \(H_{1/10}\), the moment integral, the coefficient \(0.4475\), the witness inequality, the Brownian membership margin \(\frac14\), the limiting constant \(\Gamma_{I,1/10}\approx0.0993\), and the exact norms (56) at four values of \(\varepsilon\), with an independent Cartesian-grid check. It checks Theorem 9 numerically for Cauchy noise and reproduces Table 1 and the thresholds of Section 8. These computations test constants, normalisations and implementation; the proofs establish the theorems. The figure uses exact formulas evaluated numerically, and no simulated data enter any proof.

Scope restrictions matter. Theorem 5 concerns Gaussian conditional laws and Theorem 9 additive state-independent noise, both on global analytic kernel spaces; mean matrices may be rectangular but must have full column rank. The Lévy, spectral and growth results concern equal dimensions, additive noise and linear drift. The spectral statements describe a particular RKHS, not a space-independent spectrum of the process. No improvement in computational cost, data requirements or empirical prediction accuracy is claimed.

The originating sufficient condition, the Fourier characterisation of Gaussian RKHSs, deterministic Gaussian composition rigidity, general bounded Gaussian-Fock operators, the classical Lebesgue-space OU spectrum and the kEDMD error bound are prior work. The separating witness and a detailed proposed analytic derivation appeared in GitHub issue #23376; the issue explicitly disclaimed a completed proof or formal verification. The literature search was bounded, current to 4 November 2026, and included a GitHub issue search; it does not establish priority. Internal checks do not constitute external peer review or formal proof verification.

# References {.unnumbered}

Alekseev, G. A., Afonin, K. A., & Bogachev, V. I. (2021). On Gaussian transition operators. *Doklady Mathematics, 104*(2), 229–233. <https://doi.org/10.1134/S1064562421050021>

Aronszajn, N. (1950). Theory of reproducing kernels. *Transactions of the American Mathematical Society, 68*(3), 337–404. <https://doi.org/10.1090/s0002-9947-1950-0051437-7>

De Palma, G., Mari, A., Giovannetti, V., & Holevo, A. S. (2015). Normal form decomposition for Gaussian-to-Gaussian superoperators. *Journal of Mathematical Physics, 56*(5), 052202. <https://doi.org/10.1063/1.4921265>

Fornaro, S., Metafune, G., Pallara, D., & Schnaubelt, R. (2021). \(L^p\)-spectrum of degenerate hypoelliptic Ornstein–Uhlenbeck operators. *Journal of Functional Analysis, 280*(2), 108807. <https://doi.org/10.1016/j.jfa.2020.108807>

Gonzalez, E., Abudia, M., Jury, M., Kamalapurkar, R., & Rosenfeld, J. A. (2024). The kernel perspective on dynamic mode decomposition. *Transactions on Machine Learning Research*. <https://arxiv.org/abs/2106.00106v3>

Hertel, M., Philipp, F. M., Schaller, M., & Worthmann, K. (2026). *Koopman for stochastic dynamics: Error bounds for kernel extended dynamic mode decomposition* (Version 2). arXiv. <https://arxiv.org/abs/2512.20247v2>

Holevo, A. S. (2017). On a characterization of Gaussian transition operators. *Theory of Probability & Its Applications, 61*(4), 712–718. <https://doi.org/10.1137/S0040585X97T988435>

Ikeda, M., Ishikawa, I., & Sawano, Y. (2022). Boundedness of composition operators on reproducing kernel Hilbert spaces with analytic positive definite functions. *Journal of Mathematical Analysis and Applications, 511*(1), 126048. <https://doi.org/10.1016/j.jmaa.2022.126048>

John, T. C., & Parthasarathy, K. R. (2021). A common parametrization for finite mode Gaussian states, their symmetries, and associated contractions with some applications. *Journal of Mathematical Physics, 62*(2), 022102. <https://doi.org/10.1063/5.0019413>

Klus, S., Schuster, I., & Muandet, K. (2020). Eigendecompositions of transfer operators in reproducing kernel Hilbert spaces. *Journal of Nonlinear Science, 30*(1), 283–315. <https://doi.org/10.1007/s00332-019-09574-z>

loning (2026, October 28). *Preregister: whole Gaussian-OU Gaussian-RKHS necessity question — arXiv:2405.14429v1 Remarks 2.2(c)/4.2* (Issue #23376, the-omega-institute/trureturing). GitHub. Unreviewed preregistration with a proposed derivation; disclaims a completed proof or formal verification. <https://github.com/the-omega-institute/trureturing/issues/23376>

Middelkamp, T. P. (2024). *A unifying framework for estimation of the Koopman operator between reproducing kernel Hilbert spaces* [Master's thesis, University of Twente]. <https://essay.utwente.nl/essays/104793>

Neretin, Y. A. (1990). A semigroup of operators in the boson Fock space. *Functional Analysis and Its Applications, 24*(2), 135–144. <https://doi.org/10.1007/BF01077706>

Neretin, Y. A. (2011). *Lectures on Gaussian integral operators and classical groups*. European Mathematical Society. <https://www.mat.univie.ac.at/~neretin/lectures/ems.pdf>

Nishiyama, Y., & Fukumizu, K. (2016). Characteristic kernels and infinitely divisible distributions. *Journal of Machine Learning Research, 17*(180), 1–28. <https://www.jmlr.org/papers/v17/14-132.html>

Ohnishi, M., Ishikawa, I., Lowrey, K., Ikeda, M., Kakade, S., & Kawahara, Y. (2024). Koopman spectrum nonlinear regulators and efficient online learning. *Transactions on Machine Learning Research*. <https://openreview.net/forum?id=thfoUZugvS> ; inspected version <https://arxiv.org/abs/2106.15775v2>

Paulsen, V. I., & Raghupathi, M. (2016). *An introduction to the theory of reproducing kernel Hilbert spaces*. Cambridge University Press. <https://doi.org/10.1017/cbo9781316219232>

Philipp, F. M., Schaller, M., Worthmann, K., Peitz, S., & Nüske, F. (2025a). Invariance of Gaussian RKHSs under Koopman operators of stochastic differential equations with constant matrix coefficients. *PAMM, 25*(1), e202400127. <https://doi.org/10.1002/pamm.202400127> ; quoted version <https://arxiv.org/abs/2405.14429v1>

Philipp, F. M., Schaller, M., Worthmann, K., Peitz, S., & Nüske, F. (2025b). Error analysis of kernel EDMD for prediction and control in the Koopman framework. *Journal of Nonlinear Science, 35*(5), 92. <https://doi.org/10.1007/s00332-025-10182-3> ; numbering cited from <https://arxiv.org/abs/2312.10460v1>

Sang, Y., & Zhao, L. (2026). Boundedness and compactness of Gaussian integral operators between Fock spaces. arXiv:2610.28279v1. <https://arxiv.org/abs/2610.28279v1>

Sarkar, R. (2026). *Spectral theory of non-local Ornstein–Uhlenbeck operators* (Version 4). arXiv. <https://arxiv.org/abs/2502.15183v4>
