# Formula-level novelty and claim audit

**Review date:** 1 November 2026.  
**Status:** final synthesis for the accompanying manuscript.  
**Method:** the novelty-gate protocol, rerun after the fixed affine formula, the covariance-field extension, the Lévy extension, and the maximum-mean-discrepancy interpretation.  
**Boundary:** a substantial but bounded public-literature search and theorem-level comparison. This is neither an exhaustive priority search nor external peer review.

## 1. What has actually been proved

The manuscript contains complete arguments for three principal statements:

1. A Gaussian conditional transition \(N(F(x),Q(x))\), with arbitrary Borel parameter fields, maps one global translation-invariant Gaussian RKHS into another if and only if \(Q\) is constant, \(F(x)=Mx+b\), \(M\) has full column rank, and \(MRM^\top\preceq P+4Q\). Exact range and norm are supplied, including rectangular dimensions.
2. For an affine transition with infinitely divisible additive noise, the Gaussian covariance component alone determines the same matrix boundary. The jump exponent is uniformly subquadratic at high frequency. For Lévy-driven linear dynamics, all-time invariance is equivalent to \(AP+PA^\top\preceq4D_G\), with no stability or large-jump moment assumption.
3. A stable two-dimensional shear driven by symmetric compound-Poisson noise approximates its Brownian counterpart in \(\mathcal H_I\to C_b\) operator norm with sharp order \(\varepsilon^2\). Nevertheless, every prelimit at \(t=1/10\) sends the same explicitly given Gaussian observable outside \(\mathcal H_I\), while the Brownian operator preserves the whole space.

The Gaussian specialisation answers the necessity question in Philipp et al. (2025a), published Remark 2.2(c) and the end of Section 4. The published sufficient condition with \(2BB^\top\) remains valid. Its proposed necessity is false; the exact replacement has \(4BB^\top\), in the same normalisation. The arXiv version additionally labels the closing discussion Remark 4.2.

## 2. Normalisation and identifying formulas

The kernel is \(k_P(x,y)=\exp[-(x-y)^\top P^{-1}(x-y)]\). In the originating article \(P=C^2\). Standard Brownian motion has covariance \(tI\), and the SDE contains \(B\,dW\), without an additional \(\sqrt2\).

With the unitary Fourier transform,
\[
\|f\|_P^2=\pi^{-d/2}(\det P)^{-1/2}
\int|\widehat f(\xi)|^2e^{\xi^\top P\xi/4}\,d\xi.
\]
The equal-dimensional affine squared-norm multiplier is
\[
|\det M|^{-1}(\det P/\det R)^{1/2}
\exp\!\left[\xi^\top(MRM^\top-P-4Q)\xi/4-2j(\xi)\right].
\]
The term \(j\) is zero for Gaussian noise and is the real jump exponent for infinitely divisible noise. The exact Gaussian range is \(\mathcal H_{M^{-1}(P+4Q)M^{-\top}}\). The semigroup slack identity is
\[
P+4Q_G(t)-e^{At}Pe^{A^\top t}
=\int_0^t e^{As}(4D_G-AP-PA^\top)e^{A^\top s}\,ds.
\]

Sanity-check fingerprints are the shear \(A=[[-1,5],[0,-1]]\), \(B=P=I\), old slack eigenvalues \(-1,9\), sharp slack eigenvalues \(1,11\), and exact norm \(e^t\). The common jump-noise failure observable is \(\exp(-8|x|^2/5)\), with squared RKHS norm \(25/16\).

## 3. Verified overlap, by contribution

| Manuscript unit | Closest inspected prior work | Decision and permitted claim |
|---|---|---|
| Fixed affine Gaussian boundedness | Olshanski's Gaussian Fock-operator criterion, stated in Neretin (1990; 2011) | **Verified mathematical overlap.** The manuscript supplies the block-matrix transform and Schur complement. This is a classical specialisation, not a new general Gaussian-operator theorem. |
| Deterministic mean affineness | Ikeda et al. (2022), Theorems 1.1–1.2; Gonzalez et al. (2024); Middelkamp (2024), Section 4.4.2 | **Known special case.** The self-contained analytic proof recovers it. |
| Qualitative affine restriction in stochastic Koopman discussion | Ohnishi et al. (2024), Remark 3.1 | **Prior qualitative assertion.** No first-observation claim is permitted. |
| Sharp answer to the specific OU necessity question | Philipp et al. (2025a), Theorem 2.1 and open-question discussion; GitHub issue the-omega-institute/trureturing #23376 (28 Oct 2026) | **Exact resolution of the inspected question**, using a classical affine criterion translated to this setting and an admissible separating example. The same witness and Gram identity were posted earlier, without proof, in #23376. |
| Constancy of arbitrary Gaussian conditional covariance | De Palma et al. (2015), Theorem III.2; Alekseev et al. (2021), Theorems 1–3 | **Different inspected hypotheses.** Those sources preserve Gaussian input measures. Our hypothesis is boundedness on specified observable RKHSs. Historical novelty remains provisional. |
| Gaussian coherent-state preserver interpretation | John and Parthasarathy (2021), Sections IV–V | Their class is defined by an already quadratic-exponential coherent generating function; the inspected results do not derive it from arbitrary Borel conditional parameters and RKHS boundedness. |
| Lévy matrix boundary and image description | Sarkar (2026), Sections 6–7; Applebaum and van Neerven, arXiv:1405.1276v2 | Existing linear Lévy formulas and second-quantisation machinery are credited. The latter concerns \(L^2\) of infinitely divisible measures and Gaussian first-chaos/Cameron–Martin spaces. No direct Gaussian-kernel observable-space classification was found in the inspected theorems. |
| Exact norm into \(C_b\) | Kernel-mean duality / maximum mean discrepancy; Nishiyama and Fukumizu (2016), Lemma 2.5 | **Established machinery.** It is the Gaussian-kernel MMD of the additive-noise laws. The claim concerns its quantified coexistence with loss of RKHS membership. |
| Stable OU spectral half-plane and semigroup disk | Fornaro et al. (2021), Theorems 2.9 and 4.1 | **Imported spectral theorem**, transferred by an explicit isometry after checking controllability. |
| Essential norm and finite-rank barrier | Multiplication operators on nonatomic \(L^2\) | **Standard operator-theoretic consequence** of the explicit representation, not new compactness theory. |

The exact Fock overlap is significant: after whitening, the block matrix
\[
\Gamma=\begin{pmatrix}I-L^\top SL&L^\top S\\SL&I-S\end{pmatrix},
\qquad S=(I+2Q_0)^{-1},
\]
satisfies the classical criterion exactly when \(LL^\top\preceq I+4Q_0\). This matches the present affine inequality after undoing coordinates. The originality case cannot be built on the factor-four calculation alone.

## 4. Searches and source inspection

The searches used two public web engines, arXiv HTML/PDF, publisher pages, institutional repositories and author-uploaded manuscripts. Primary sources were preferred. Exact query logs and theorem comparisons are in the state-covariance and Lévy supplements. Representative query groups included:

- Gaussian RKHS, stochastic Koopman, necessity, Lyapunov inequality, Gaussian convolution, exact image, and the formulas \(P+4Q\) and \(4BB^\top\).
- Gaussian native spaces, Weierstrass transforms, Bargmann–Fock integral operators, Olshanski semigroups, coherent vectors, squeezed states and Gaussian-preserving maps.
- State-dependent and heteroscedastic Gaussian covariance, bounded conditional-mean embeddings, Gaussian transition operators, affine rigidity and Liouville arguments.
- Lévy–OU, pure-jump smoothing, Gaussian Fourier weights, subquadratic jump exponents, skew convolution, second quantisation, diffusion approximation and Gaussian maximum mean discrepancy.

The late thesis lead was read at the actual relevant section. Middelkamp (2024), printed pp. 50–51, characterises deterministic composition maps; it does not provide the stochastic covariance-field or Lévy result. The John–Parthasarathy paper was checked at its structural definitions and theorems, rather than classified by its title. The Russian original of Alekseev et al. was located and read after initial English-access failures; this closed a material hypothesis-comparison gap.

The skew-convolution lead arXiv:1405.1276 was also inspected in its complete author-uploaded v2. Proposition 2.1 assumes a linear skew map satisfying \(T_\#\lambda_1*\rho=\lambda_2\), and Theorem 3.7 uses Fock space built from the Gaussian first-chaos RKHS and \(L^2(\nu)\). That RKHS is not the global translation-invariant Gaussian kernel space of observables used here. This is a verified distinction, not merely an abstract-based judgement.

## 5. What remains uncertain

Holevo (2017) was accessible through its abstract, publication metadata and the statement of its principal result reproduced in later primary literature. Its full variants for unnormalised Gaussian measures were not inspected directly. A previously published bounded-operator theorem about coherent vectors could still subsume the covariance classification under a different vocabulary. The two-engine search and selected references cannot exclude that possibility.

No article was found in the inspected corpus stating the combined Lévy invariance boundary, common-observable diffusion-limit failure and sharp global prediction norm rate. Failed searches are not affirmative evidence of priority. The outcome for these strengthened claims is therefore **bounded uncertainty**, with a complete candidate proof and a moderate-confidence originality assessment.

The source question is a focused problem in kernel operator learning and stochastic dynamics. We have not established that it is the most important open problem in applied mathematics. Selection balanced a published open statement, a foundational modelling assumption, tractability, and scope for a substantial extension.

## 6. Final claim policy

It is defensible to say that the manuscript proves a sharp answer to the inspected necessity question and provides a complete Gaussian conditional-transition classification and Lévy extension with the stated proofs. The manuscript's proposed new contribution lies primarily in the covariance-field rigidity and the combined jump/diffusion result.

It is not defensible to say that a classical Gaussian integral-operator criterion has been discovered for the first time, that all nonlinear stochastic Koopman operators have been classified, that all finite-data kernel prediction methods fail, that a global priority search is complete, or that the shear witness was first proposed here.

Any quality assessment of the manuscript must remain conditional on expert verification and the bounded novelty evidence. The accompanying reproducibility checks test constants and examples; they do not mechanically verify the analytic proofs.

## 7. Sources

Complete APA-style references and visible links are included in the manuscript and the detailed audit supplements. The principal records are:

- Philipp et al. (2025a): https://doi.org/10.1002/pamm.202400127
- Neretin (1990): https://doi.org/10.1007/BF01077706
- Neretin (2011), Chapter 5: https://www.mat.univie.ac.at/~neretin/lectures/ems.pdf
- Ikeda et al. (2022): https://doi.org/10.1016/j.jmaa.2022.126048
- De Palma et al. (2015): https://doi.org/10.1063/1.4921265
- Alekseev et al. (2021): https://doi.org/10.1134/S1064562421050021
- John and Parthasarathy (2021): https://doi.org/10.1063/5.0019413
- Middelkamp (2024): https://essay.utwente.nl/essays/104793
- Sarkar (2026): https://arxiv.org/abs/2502.15183v4
- Applebaum and van Neerven, full v2: https://www.researchgate.net/publication/262108763_Second_quantisation_for_skew_convolution_products_of_infinitely_divisible_measures
- Nishiyama and Fukumizu (2016): https://www.jmlr.org/papers/v17/14-132.html
- Fornaro et al. (2021): https://doi.org/10.1016/j.jfa.2020.108807

## 8. Revision addendum (4 November 2026)

This addendum records changes made in the revision round of 4 November 2026. Theorem numbers below refer to the revised manuscript.

**Public prior posting.** A GitHub issue search found the-omega-institute/trureturing issue #23376, opened 28 October 2026 by the account `loning` and still open with no comments when read on 4 November 2026. It preregisters the Philipp et al. necessity question, quotes Remarks 2.2(c) and 4.2 of arXiv:2405.14429v1, and gives a "proposed manual route" with the witness \(A=\begin{pmatrix}-1&5\\0&-1\end{pmatrix}\), \(B=C=I_2\), and the two-noise Gram identity \(\det(I+4Q_t)^{-1/2}\exp[-(x-y)^\top M_t^\top(I+4Q_t)^{-1}M_t(x-y)]\). The issue states that the route is uncompiled and that it supplies no proof, refutation, priority claim or resolution credit. It does not state the general criterion \(AP+PA^\top\preceq4BB^\top\), the rectangular or state-dependent classification, or the Lévy and diffusion-limit results. The manuscript now cites it neutrally: the separating witness was publicly proposed there, without proof, before this work. Whether the issue and this work share an upstream source has not been established. GitHub issue search is now part of the recorded search protocol.

**Reframing.** The manuscript now leads with covariance rigidity (Theorem 5), additive-noise rigidity (Theorem 9), the Gaussian-component noise boundary (Theorems 8 and 11) and the diffusion-limit result (Theorem 12). The OU answer (Theorem 6) is presented as an application obtained through the classical Fock criterion and an elementary semigroup argument.

**New result: additive-noise rigidity (Theorem 9).** For \(Tf(x)=\mathbb E f(F(x)+Z)\) with Borel \(F\) and noise satisfying \(|\varphi(\eta)|\ge ce^{-\gamma|\eta|^2}\), which includes every infinitely divisible law with or without a Gaussian part, boundedness \(\mathcal H_P\to\mathcal H_R\) forces \(F\) affine with full column rank; for infinitely divisible noise the criterion is \(MRM^\top\preceq P+4Q\) with \(Q\) the Gaussian component, including rectangular \(M\). The proof works through Fourier translates and characters, not through the exp-quadratic form of Theorem 5. No prior statement was found in the bounded search; this is not evidence of priority. Open: noise whose characteristic function vanishes on an open set or decays faster than every Gaussian, and state-dependent non-Gaussian noise.

**New application: admissible bandwidths (Section 8).** The admissible set \(\{P\succ0:AP+PA^\top\preceq4BB^\top\}\) is convex, equals twice the set certified by the earlier sufficient condition, and has an exact isotropic threshold. Corollary 18 verifies the invariance hypothesis of the kEDMD bound in Philipp et al. (2025b), Theorem 4.2 (arXiv:2312.10460v1 numbering), for multivariate OU processes. This only checks a hypothesis of an existing theorem; it does not change its constants.

**Forward-citation check.** The domain review of 4 November 2026 reported that Semantic Scholar indexed no papers citing the PAMM article. Hertel et al. (2026) concern Sobolev-space invariance on bounded domains, not Gaussian RKHSs.
