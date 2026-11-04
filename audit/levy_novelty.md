# Novelty-gate report: Lévy noise, Gaussian RKHS invariance and a diffusion limit

**Search date:** 1 November 2026.  
**Researcher:** Independent optimization/probability audit agent.  
**Corpus boundary:** Public web search, arXiv, publisher full texts and institutional repositories accessible during this session. This is a bounded review, without exhaustive MathSciNet/zbMATH coverage or author enquiries.  
**Contribution units:** Exact Lévy matrix criterion; its proof; Gaussian Fourier conjugacy; exact range; quantified invariance failure under diffusion approximation.  
**Companion fingerprint:** `target_levy.yaml`.  
**Proof location:** Section 5 (Lemma 7, Theorems 8, 9 and 11, Proposition 10) and Section 6 (Theorem 12, Proposition 13) of the revised manuscript; the original working equations (L1)--(L30) are now numbered consecutively.

## 1. Frozen claims and exclusions

For the kernel \(k_P(x,y)=\exp[-(x-y)^\top P^{-1}(x-y)]\), an invertible affine transition \(Tf(x)=\mathbb E f(Mx+b+Z)\), where \(Z\) is infinitely divisible with Gaussian covariance component \(Q\), maps \(\mathcal H_P\) into \(\mathcal H_R\) exactly when \(MRM^\top\preceq P+4Q\). Its finite norm and essential norm are \(|\det M|^{-1/2}(\det P/\det R)^{1/4}\). The jump component does not enlarge this admissible matrix region.

For \(dX=AX\,dt+dL\), the all-time condition is \(AP+PA^\top\preceq4D\), with \(D\) the Gaussian component of the driving Lévy triplet. There is no moment or drift-stability hypothesis for this statement. The proof reduces the question to a weighted Fourier multiplier and the classical subquadratic growth of the jump exponent.

The specific applied consequence is a symmetric coordinate compound-Poisson approximation to Brownian noise. At fixed time \(t=1/10\), for the stable shear \(A=[[-1,5],[0,-1]]\), \(P=I\), and the same Gaussian observable \(f(x)=e^{-8|x|^2/5}\), every prelimit output is outside \(\mathcal H_I\), whereas the Brownian output is inside. Nevertheless, prediction operators converge in \(\mathcal H_I\to C_b\) norm with exact order \(\varepsilon^2\), an explicit positive limit coefficient, and upper bound \(0.448\varepsilon^2\).

The following are excluded as originality claims:

- The affine **Gaussian** boundedness criterion, which is a verified special case of classical Gaussian-Fock theory.
- The Lévy--Khintchine representation, the integrated OU transition exponent, and the subquadratic jump-exponent lemma as new probability theorems.
- The general idea of convolution intertwinings for OU semigroups.
- The norm of an expectation functional as a kernel-mean norm, or its Fourier expression as Gaussian maximum mean discrepancy (MMD).
- Any assertion that jump noise never smooths, or that RKHS membership failure implies inaccurate prediction.
- A claim that the Lévy extension was itself explicitly posed as an open problem in the originating Gaussian paper.

## 2. Normalisation and verified translations

| Notion | Convention here | Consequence checked |
|---|---|---|
| Gaussian RKHS | \(e^{-(x-y)^\top P^{-1}(x-y)}\) | Norm Fourier weight \(e^{\xi^\top P\xi/4}\). |
| Unitary Fourier transform | \((2\pi)^{-d/2}\int e^{-ix\cdot\xi}f(x)dx\) | Norm constant \(c_P=\pi^{-d/2}(\det P)^{-1/2}\). |
| Gaussian noise component | \(\log\varphi=-\xi^\top Q\xi/2+\text{drift+jumps}\) | Squaring its modulus contributes \(-\xi^\top Q\xi\), hence the factor four. |
| Brownian covariance rate | \(\operatorname{Cov}(B_t)=tD\) | All-time slack is \(4D-AP-PA^\top\). |
| Total noise covariance | May be undefined; when finite, can include jump variance | It must not replace the Gaussian component in the criterion. |
| Pure-jump approximation | Rates \(1/(2\varepsilon^2)\) at each of \(\pm\varepsilon e_i\) | Total covariance rate is already \(I\), Gaussian component is zero, limiting Brownian component is \(I\). |
| MMD | Norm of the difference of kernel mean embeddings | Its square is \((2\pi)^{-d}c_P^{-1}\int|\varphi_1-\varphi_2|^2e^{-\xi^\top P\xi/4}d\xi\). |
| Effective diffusion | Gaussian Fourier conjugacy to unweighted \(L^2(dx)\) | Only \(D\) changes, to \(D-(AP+PA^\top)/4\); the driving jump measure and Lévy drift remain unchanged. |

These translations were verified directly in the proof, rather than inferred from similar titles.

## 3. Fingerprints

This is a continuous operator classification, not a newly generated finite matrix or combinatorial sequence. The relevant exact objects are recorded in the YAML. Three scalar transition instances are: \(M=1/2,Q=0\), always admissible on \(\mathcal H_1\); \(M=2,Q=3/4\), exactly on the boundary; and \(M=2,Q=0\), inadmissible for every pure-jump law. Their finite norms, when admissible, are \(\sqrt2\) and \(1/\sqrt2\).

The shear has trace \(-2\), determinant \(1\), and characteristic polynomial \((\lambda+1)^2\). Its symmetric part \(A+A^\top\) has eigenvalues \(3,-7\), and the Brownian slack \(4I-A-A^\top\) has eigenvalues \(1,11\). At the selected time,
\[
e^{tA}e^{tA^\top}=e^{-1/5}
\begin{pmatrix}5/4&1/2\\1/2&1\end{pmatrix},
\qquad
v^\top e^{tA}e^{tA^\top}v=(13/8)e^{-1/5}>5/4.
\]

The compound-Poisson characteristic exponent has the familiar cosine expansion
\[
\varepsilon^{-2}(\cos(\varepsilon u)-1)
=-u^2/2+\varepsilon^2u^4/24-\varepsilon^4u^6/720+\cdots.
\]
Its coefficient sequence is classical and is not an originality target. There is no unidentified rational or algebraic generating function requiring an OEIS search.

## 4. Cross-disciplinary aliases

| Discipline | Aliases searched or inspected |
|---|---|
| Harmonic analysis | Gaussian Fourier-weighted \(L^2\), weighted composition, ultra-analytic regularity, Gelfand--Shilov smoothing, Gaussian convolution. |
| Probability | Lévy--OU transition, skew convolution, infinitely divisible noise, Brownian component, compound-Poisson diffusion approximation. |
| Mathematical physics | Fock-space second quantisation, Gaussian integral operators, bosonic semigroups. |
| Statistics and machine learning | Gaussian RKHS invariance, kernel Koopman operator, kernel mean embedding, Gaussian MMD. |
| Generating-function language | Poissonization and cosine exponent; the identified classical cosine series does not itself suggest a new enumeration problem. |

## 5. Reproducible search log

All queries below were run on 1 November 2026. The two available web search engines were used in separate calls. The log records query text, including negative or low-quality retrieval, rather than describing every result as absent.

| Corpus | Query or query family | Material examined and consequence |
|---|---|---|
| Web, routine engine | `"Lévy" "Gaussian RKHS"`; `"Levy" "Gaussian RKHS" invariance` | No matching Lévy invariance theorem located. Results were largely Gaussian-process RKHSs and rough-path material. |
| Web, routine engine | `"Gaussian" "reproducing kernel" "infinitely divisible" operator` | Found second-quantisation literature and kernel-mean literature; distinctions below. |
| Web, routine engine | `"Gaussian" "RKHS" "compound Poisson"` | No matching invariance or same-observable result located. |
| Web, routine engine | `"Ornstein Uhlenbeck" "Gelfand-Shilov" Levy` | Retrieved Obiedat--Moyo on a different dual-space OU problem; its function-space definitions were inspected. |
| Web, stronger engine | `"Gaussian RKHS" "jump" Koopman` | Retrieved the original Gaussian paper and Middelkamp's thesis. Root separately inspected the latter's deterministic-only characterization. |
| Web, stronger engine | `"Gaussian RKHS" "diffusion approximation"` | No matching result located; unrelated Stein/RKHS material returned. |
| Web, stronger engine | `"Gaussian" "Fourier weight" "Lévy"` | No matching exact matrix classification located. |
| Web, routine engine | `"Gaussian RKHS" "Brownian component"`; `"MPM" "Levy" Gaussian kernel` | No matching formula located. Literal matrix-string query had poor precision and is weak negative evidence. |
| Web, routine engine | `"Gaussian kernel" "compound Poisson" "operator"` | Retrieved kernel statistics and potential theory; no inspected collision. |
| Web, stronger engine | `"Lévy" "ultra-analytic" semigroup`; `"Gaussian" "weighted composition" "infinitely divisible"`; `"Gaussian reproducing" "jump" "invariance"` | No exact statement located. Adjacent nonlocal smoothing and Besov-space results use different norms. |
| Primary-source inspection | Sarkar, arXiv:2502.15183v4, Sections 6--7 | Integrated characteristic exponent is established machinery; convolution intertwinings are prior work. The inspected results use invariant-measure \(L^p\) spaces, rather than this Gaussian RKHS. |
| Primary-source inspection | Nishiyama--Fukumizu, JMLR 17(180), Lemma 2.5 and introductory Gaussian convolution calculation | Kernel-mean convolution formulas are prior work; exact prediction norm is an MMD/duality identity. |
| Single-source follow-up | `"Second quantisation for skew convolution products of infinitely divisible measures" pdf` | Author-uploaded full arXiv v2 became accessible through ResearchGate; Proposition 2.1, the Section 3 space definitions, the standing hypotheses and Theorem 3.7 were inspected. The specific full-text gap was closed. |
| Web, routine engine, after MMD identification | `"maximum mean discrepancy" "compound Poisson" Gaussian`; `"kernel mean" "diffusion approximation"`; `"maximum mean discrepancy" "Brownian" "Poisson" approximation`; `"MMD" "Poisson" "Edgeworth"` | No exact same-observable invariance discontinuity or displayed asymptotic was located. Retrieval was sparse and often irrelevant; no exhaustive CLT/MMD priority conclusion follows. |

Earlier queries during the exploratory stage also combined Gaussian RKHS with jump-driven Koopman invariance, heat-transform conjugacy, and Lévy approximation. The explicit rerun above provides a reproducible bounded search after the final formula simplification.

## 6. Inspected primary sources and their exact relation

### Sarkar: classical Lévy--OU representation and intertwining

Rohan Sarkar, *Spectral theory of non-local Ornstein--Uhlenbeck operators*, arXiv:2502.15183v4, 13 April 2026, https://arxiv.org/html/2502.15183v4 . Equations (6.2)--(6.4) give the integrated characteristic exponent; Section 7 develops convolution intertwinings on invariant-measure spaces. These are acknowledged ingredients. No Gaussian-RKHS matrix criterion was found in the inspected sections or the full-text search.

### Nishiyama--Fukumizu: exact kernel-mean identity

Yu Nishiyama and Kenji Fukumizu (2016), *Characteristic Kernels and Infinitely Divisible Distributions*, JMLR 17(180), 1--28. Full PDF: https://jmlr.csail.mit.edu/papers/volume17/14-132/14-132.pdf . Lemma 2.5 expresses kernel means and their inner products as convolutions. Applied to the difference of two noise laws and the Gaussian spectral density, it gives the MMD integral in (L28). At any starting state the expectation-difference functional is a common translation of that mean-embedding difference; translation is an isometry. Thus the operator-norm identity is a direct consequence of established kernel-mean theory, not a new discrepancy.

### Neretin/Olshanski: verified Gaussian special-case collision

Neretin, *Lectures on Gaussian Integral Operators and Classical Groups* (EMS, 2011), Chapter 5, Proposition 1.3 and Theorem 1.4, author PDF https://www.mat.univie.ac.at/~neretin/lectures/ems.pdf . The Gaussian-Fock boundedness theorem, attributed there to Olshanski, reproduces the pure Gaussian affine matrix criterion after the explicit conjugation in the main novelty report. The added nonquadratic Lévy exponent is not a Gaussian integral kernel, so this source does not directly prove the full Lévy statement. This observation does not establish novelty of the extension.

### Adjacent smoothing source

Hamed M. Obiedat and Lloyd Edgar S. Moyo, *Ornstein--Uhlenbeck Semigroup on the Dual Space of Gelfand--Shilov Spaces of Beurling Type*, Bol. Soc. Paran. Mat. 39(1) (2021), 71--80, DOI 10.5269/bspm.40348. Full PDF: https://periodicos.uem.br/ojs/index.php/BSocParanMat/article/download/40348/751375150871/ . Its definition in Theorem 2.1 uses a Fréchet family of spatial and Fourier seminorms and studies the dual; it is not the fixed Gaussian Fourier Hilbert norm in (L1). This inspection excludes a superficial title-level collision only.

### Second quantisation: full-text lead closed

David Applebaum and Jan van Neerven (2015), *Second quantisation for skew convolution products of infinitely divisible measures*, Infinite Dimensional Analysis, Quantum Probability and Related Topics 18(1), 1550003, DOI 10.1142/S0219025715500034. The author-uploaded arXiv:1405.1276v2 is available at https://www.researchgate.net/publication/262108763_Second_quantisation_for_skew_convolution_products_of_infinitely_divisible_measures . This full version, rather than merely its abstract, was inspected.

Proposition 2.1 assumes infinitely divisible \(\lambda_i=\gamma_i*\pi_i\) and a Borel linear map \(T\). The standing assumption before Lemma 3.5 is \(T_\#\lambda_1*\rho=\lambda_2\), with an infinitely divisible skew factor \(\rho\). Theorem 3.7 represents the contraction \(P_T:L^2(\lambda_2)\to L^2(\lambda_1)\) through \(\Gamma(H_{\gamma,i}\oplus L^2(\nu_i))\). Section 3 defines \(H_\gamma\) by its isometry onto the first Wiener--Itô chaos.

The distinction is mathematical: this \(H_\gamma\) is the Gaussian measure's Cameron--Martin space, not the Gaussian-kernel observable RKHS. Their theorem concerns probability-measure \(L^2\) contractions under a skew-convolution compatibility hypothesis. It does not state our criterion between fixed translation-invariant kernel spaces, exact range, or diffusion-limit membership failure. No direct collision was identified. The White Rose PDF also became accessible, but is an earlier short draft with different numbering; the adjudication uses v2.

## 7. Missingness and negative-evidence limits

Search engines do not index displayed formulas reliably. Literal matrix queries had low precision. The present search does not cover every literature on ultra-analytic spaces, skew convolution, Fock representations of Lévy noise, or rates of convergence in MMD. The specific Applebaum--van Neerven full-text lead was subsequently inspected and closed as documented above. No author correspondence was sent. The independent proof establishes the stated mathematics, but none of these checks establishes historical priority.

## 8. Outcome by contribution unit

| Unit | Outcome | Permitted language | Forbidden language |
|---|---|---|---|
| Affine Gaussian matrix criterion | COLLISION with classical Gaussian-Fock theory | Explicit translation resolving the inspected RKHS question. | First general Gaussian operator criterion. |
| Lévy matrix criterion and exact range | BOUNDED UNCERTAINTY | We prove the displayed Lévy extension; no matching statement was found in this search. | Previously unknown, first, or exhaustive classification across all prior literature. |
| Proof method | Standard ingredients with a complete direct argument | Weighted Fourier multiplication and the subquadratic jump exponent give a self-contained proof. | New operator calculus or new Lévy--Khintchine theorem. |
| Unitary Lévy--OU conjugacy | BRIDGE within the recorded search, with priority uncertainty | Explicit Gaussian-RKHS identification with the displayed effective Brownian part. | First convolution intertwining for Lévy OU. |
| Exact prediction norm (Proposition 13) | COLLISION / standard RKHS duality | Gaussian MMD expressed as this expectation-operator norm. | New probability metric or new general norm identity. |
| Same-observable invariance failure plus sharp \(\varepsilon^2\) convergence | BOUNDED UNCERTAINTY | The explicit theorem and proof; the combination was not found in the bounded search. | First known discontinuity of any smooth function-space property under a CLT. |
| Numerical constants and exact witness | Verified computation attached to the proof | Explicit witness and independently checked upper-bound coefficient. | Computations establish priority or replace proof. |

## 9. Decision and permitted manuscript claim

**BOUNDED UNCERTAINTY, with established subcomponents explicitly attributed.** The result is mathematically tractable and the manuscript supplies a complete proof. The central proposed contribution is the Gaussian-component-only boundary and its concrete consequence for diffusion surrogates, rather than originality of the Fourier, Lévy, or MMD tools.

Permitted summary: “For additive infinitely divisible noise, we prove an exact Gaussian-RKHS invariance criterion controlled only by the Gaussian component. An explicit diffusion approximation has uniformly convergent prediction operators while every prelimit sends one fixed observable outside the RKHS.”

## 10. Rerun triggers

A fresh formula-level gate is needed if the result is generalized to nonlinear state maps or state-dependent jump laws, claimed as a theorem on a named ultra-analytic space, identified with a second-quantisation theorem, or framed as a new MMD central-limit result. The last simplification to the MMD identity has already been rerun and the norm identity relabelled as established machinery.

## Revision addendum (4 November 2026)

- The limiting constant of the worked example is now reported: \(\Gamma_{I,1/10}\approx0.0993\) (0.099254), against the explicit uniform coefficient 0.4475, about 4.5 times larger. The bound proves the order \(\varepsilon^2\), and the positive limit shows the order is sharp; the coefficient of the bound is not sharp. `code/verify.py` computes both and evaluates the exact norm at four values of \(\varepsilon\).
- The manuscript now states explicitly that membership loss is a statement about the global RKHS norm, and that this is the norm in which the kEDMD invariance hypothesis is formulated.
- Theorem 9 (additive-noise rigidity) extends the affine Lévy criterion to Borel drifts and rectangular mean matrices: a nonlinear drift is impossible for every infinitely divisible noise, including pure-jump noise. This removes the earlier exclusion "No ... nonlinear drift classification" for additive state-independent noise; state-dependent Lévy jump kernels remain open.
- GitHub issue the-omega-institute/trureturing #23376 (28 Oct 2026) concerns only the Gaussian OU question and does not state any Lévy result.
