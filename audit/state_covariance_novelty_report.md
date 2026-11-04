# Novelty gate rerun: state-dependent Gaussian transition rigidity

Search and proof date: 1 November 2026.
This detailed report is incorporated into consolidated_novelty_report.md; the older novelty_report.md is retained only under provenance/superseded_audits/. The original fixed-affine statement has since been identified as a special case of classical Olshanski/Neretin Gaussian operator theory. It must be credited as such. The strengthened target is frozen separately in target_state_covariance.yaml and proved in manuscript.md, Theorem 5 (the working source manuscript_core.md is retained under provenance/working_sections/).

## 1. Exact strengthened claim

For arbitrary Borel maps F:R^d->R^m and Q:R^d->S_+^m, the Markov transition

\[
Tf(x)=\int f(u)\,N(F(x),Q(x))(du)
\]

maps the global Gaussian RKHS H_P(R^m) into H_R(R^d) if and only if Q is constant, F(x)=Mx+b with M full column rank, and MRM^T<=P+4Q. It has exact range H_E and norm

\[
E=(M^T(P+4Q)^{-1}M)^{-1},\qquad
\|T\|=\left(\frac{\det P}{\det(P+4Q)}\right)^{1/4}
\left(\frac{\det E}{\det R}\right)^{1/4}.
\]

The proposed additional contribution is covariance constancy and the complete transition-law classification under an RKHS mapping hypothesis. The affine boundedness subcase, deterministic composition rigidity, Gaussian integrals and range-RKHS machinery are prior art.

## 2. Structural fingerprint and proof

The proof uses the complexified Gaussian sections
kappa_y(u)=exp[-(u-y)^TP^{-1}(u-y)], with norm one for real centers y. Along a complexified real state line, boundedness gives a jointly entire family Phi(z,y) whose magnitude is bounded uniformly in real y for every fixed complex z.

On the real line Gaussian integration gives

\[
\Phi(t,y)=a(t)\exp[-(F(t)-y)^TC(t)(F(t)-y)],
\quad C(t)=(P+2Q(t))^{-1}.
\]

Logarithmic derivatives in y recover a meromorphic coefficient matrix mathcal C(z) on the complex line. Analytic continuation makes the real-center Gaussian expression hold off the discrete zero set of Phi(z,0). Uniform boundedness in real y forces Re(u^T mathcal C(z)u)>=0 for every real u. The Cayley transform

\[
\frac{u^T\mathcal C(z)u-1}{u^T\mathcal C(z)u+1}
\]

is bounded, extends across the discrete omitted points, and is constant by Liouville's theorem. Therefore Q is constant along every real line, hence globally.

The mean coefficients have only meromorphic poles. Once mathcal C is constant, the identity Phi(z,e_i)=g(z)exp(2L_i(z)-C_ii) excludes any pole: its exponential would have an essential singularity which a finite-order zero of g cannot cancel. The mean therefore extends entirely. Optimizing over real centers gives

\[
a\exp[(\operatorname{Im}F(z))^TC(\operatorname{Im}F(z))]
\le \|T\|\exp[2(\operatorname{Im}z)^2v^TR^{-1}v].
\]

Entire harmonic functions with this linear growth are affine, so F is affine on lines and globally. This direct proof does not invoke deterministic rigidity as a black box, but that known special case is explicitly attributed.

## 3. Exact prior-art collisions and distinct hypotheses

### 3.1 Fixed affine Gaussian operators: verified collision

The optimisation/prior-art agent verified the Olshanski criterion in:

- Yu. A. Neretin, *Lectures on Gaussian Integral Operators and Classical Groups*, EMS,2011, Chapter5, Proposition1.3 and Theorem1.4, printed p288 (PDF page300), https://www.mat.univie.ac.at/~neretin/lectures/ems.pdf .
- Yu. A. Neretin, *A semigroup of operators in the boson Fock space*, Functional Analysis and Its Applications24(2)(1990),135–144, https://doi.org/10.1007/BF01077706 .

For a symmetric Gaussian Fock block kernel Gamma=[[K,L],[L^T,N]], boundedness is equivalent to ||Gamma||<=1 and ||K||,||N||<1. The exact Gaussian-RKHS affine parameter translation was independently derived by that agent and is saved in gaussian_rkhs_prior_art_and_asymptotic.md. It yields the sharp covariance inequality after a Schur complement. Thus the fixed affine boundedness statement is mathematically classical, even though the specific2025 OU necessity question does not recognize the sharp condition.

The Olshanski criterion begins with an already quadratic Gaussian integral kernel. It does not itself derive covariance constancy or affine mean from arbitrary Borel conditional Gaussian parameters. A broader preserver theorem could nevertheless subsume the strengthened result; the search below is not exhaustive.

### 3.2 Deterministic rigidity: verified collision

Ikeda–Ishikawa–Sawano2022, Theorems1.1 and1.2, https://arxiv.org/html/1911.11992v4 , covers arbitrary-map bounded composition in Gaussian RKHSs. The state-covariance proof recovers its Gaussian deterministic special case Q=0. No priority claim is made for that part.

Ohnishi et al.2024, Remark3.1, https://arxiv.org/html/2106.15775v2 , already asserts affine restrictions in a stochastic Koopman discussion. It does not state covariance-field constancy or the present complete quantitative criterion in the inspected passage.

### 3.3 Gaussian-to-Gaussian superoperators: primary full theorem inspected, different premise

G. De Palma, A. Mari, V. Giovannetti and A. S. Holevo, *Normal form decomposition for Gaussian-to-Gaussian superoperators*, Journal of Mathematical Physics56,052202(2015), https://doi.org/10.1063/1.4921265 ; full PDF https://arxiv.org/pdf/1502.01870v4 .

TheoremIII.1, pp8–12, assumes a bounded linear map on the Hilbert space of Hilbert–Schmidt operators sends all Gaussian quantum states to Gaussian quantum states. It derives linear mean and affine covariance transformations. TheoremIII.2, p13, is its classical analogue: a bounded linear Feller map on finite signed measures must preserve the whole set of Gaussian probability laws, and is then an affine Gaussian Markov map. The proof uses variation of the Gaussian input covariance and a heat-equation identity.

Our hypothesis is different: the transition law is Gaussian conditional on each state, and its expectation operator is bounded between Gaussian RKHSs. We do not assume that every Gaussian distribution of the input state produces a Gaussian output distribution. The inspected theorems therefore cannot simply be cited to prove the strengthened classification. This is a verified hypothesis distinction, not proof of historical novelty.

### 3.4 Holevo2017: abstract inspected, full theorem unavailable

A. S. Holevo, *On a Characterization of Gaussian Transition Operators*, Theory of Probability and Its Applications61(4)(2017),712–718, https://doi.org/10.1137/S0040585X97T988435 .

The publisher abstract says the paper characterizes Markov operators preserving Gaussian probability measures and integral operators preserving unnormalized Gaussian measures. The full paper is behind a purchase/sign-in page in the available web interface. Its exact variants were not inspected. It remains an unresolved possible preserver-theory overlap; no strong exclusion should be claimed from its abstract alone.

### 3.5 Alekseev–Afonin–Bogachev2021: primary full theorem inspected, different premise

G. A. Alekseev, K. A. Afonin and V. I. Bogachev, *On Gaussian transition operators*, Doklady Mathematics104(2)(2021),229–233, https://doi.org/10.1134/S1064562421050021 . Russian primary record: https://www.mathnet.ru/eng/danma196 ; Russian DOI https://doi.org/10.31857/S2686954321050027 .

Initial attempts to access the Math-Net PDF and English publisher text failed. A later Russian-language search located the complete primary Russian HTML article at https://sciencejournals.ru/view-article/?a=DANMIUp2105002Alekseev&j=danmiup&n=1&v=500&y=2021 . The introduction, Theorems1–3 and their proof were inspected.

Theorem1 extends the Gaussian-measure-preserver result to locally convex spaces, assuming preservation of Gaussian laws supported on affine lines. Theorem2 weakens the continuity hypothesis and Theorem3 treats the one-dimensional case. These hypotheses still quantify over all nondegenerate one-dimensional Gaussian INPUT distributions, rather than conditional laws alone. The introduction explicitly explains that Gaussian images of Dirac masses are insufficient and gives the pushforward x->x^3 as a counterexample. The proof varies Gaussian input variance and uses the heat equation to identify constant conditional variance and affine mean. Thus its assumption is genuinely distinct from the present Gaussian RKHS boundedness hypothesis; it is not a direct theorem-level collision.

### 3.6 Coherent and squeezed-state preservers

Searches also used the Fock-space translation: T* maps real-labelled coherent sections to Gaussian vectors with potentially varying squeeze. No exact bounded-preserver theorem for this family was located in the retrieved sources. Quantum Gaussian operations, Gaussian symmetries, and Gaussian-to-Gaussian density-state maps are adjacent topics; most retrieved theorems assume unitarity, complete positivity or preservation of all Gaussian density states. The search was bounded, and this alias is an active historical-novelty risk.

### 3.7 John–Parthasarathy2021: generating-function parametrisation, different premise

T. C. John and K. R. Parthasarathy, *A common parametrization for finite mode Gaussian states, their symmetries, and associated contractions with some applications*, Journal of Mathematical Physics62(2),022102(2021), https://doi.org/10.1063/5.0019413 ; primary full PDF https://arxiv.org/pdf/1911.06555v4 .

The introduction and structural SectionsIV–V were inspected, especially pp28–34. DefinitionV.1 defines E2 by an already quadratic-exponential coherent generating function. TheoremV.6 proves that this class is a weakly closed semigroup; TheoremV.7 characterizes Gaussian density operators within E2. CorollaryV.8 starts with Z in E2 to derive preservation of Gaussian density states. PropositionV.10 treats unitaries and finite-rank projections; the Gaussian symmetry results require unitarity and preservation of all Gaussian density states under conjugation. No arbitrary bounded coherent-vector-to-Gaussian-vector preserver characterization was found in these structural sections. The result therefore does not directly establish covariance rigidity from the hypotheses of our theorem.

## 4. Search log after the structural extension

All queries below were run on1November2026. Engine1 was used for primary-source and stronger-coverage searches; engine2 for routine narrowing.

| Query group | Primary material inspected or result | Consequence |
|---|---|---|
| "Gaussian" "RKHS" "state-dependent" covariance Koopman; "Gaussian" "composition operator" covariance "constant"; "heteroscedastic" "Koopman" "Gaussian" | Originating2025 OU paper and current Koopman material | No state-covariance theorem found in these results |
| "Gaussian transition" "reproducing kernel" bounded operator; "Gaussian" "Markov" "RKHS" "constant covariance"; "Gaussian" "covariance" "Liouville" "composition"; "Gaussian kernel" "heteroscedastic" "bounded" operator | Mainly unrelated Gaussian processes and probability material | No exact analytic-rigidity argument identified |
| "On Gaussian Transition Operators"; "Gaussian" "kernel" "covariance rigidity"; "Gaussian" "Markov kernels" "affine" characterization bounded operator | Holevo2017 and Alekseev–Afonin–Bogachev2021 identified | Close alias requires explicit source inspection |
| "Holevo" "On a Characterization of Gaussian Transition Operators" pdf; "On Gaussian Transition Operators" Alekseev Afonin Bogachev pdf | Holevo publisher abstract; Math-Net primary record; inaccessible full texts | Precise missingness retained |
| "bounded" "operators" "coherent states" "Gaussian" preservation | De Palma et al.2015; Gaussian symmetries/parametrisations | Triggered full primary PDF inspection |
| "bounded operator" "maps" "coherent states" "squeezed"; "Gaussian-preserving" "bounded" operators pure; "Gaussian states" "linear operators" "pure" "classification" | Quantum Gaussian operation/symmetry literature | No exact real-labelled Gaussian-vector preserver theorem located |
| "linear operators" "Gaussian functions" "preserve"; "bounded" "Gaussian functions" "maps" "characterization"; "coherent states" "Gaussian states" "preserving" "operator" theorem; "Gaussian transition operators" "translations" | Adjacent Gaussian-function and quantum-operation literature | No theorem-level collision verified |
| Gaussian function preservers linear operator characterization; bounded operators coherent states squeezed states characterization Fock | Giedke–Cirac2002 abstract, Neretin-related quantum Gaussian work | General Gaussian-state-preserver aliases remain to be reviewed comprehensively |
| Alekseev Afonin Bogachev Gaussian transition operators theorem covariance; "О гауссовских операторах перехода" pdf; "Холево" "характеризации гауссовских операторов перехода" pdf | Complete primary Russian HTML of Alekseev–Afonin–Bogachev2021 found and inspected | Closed the earlier full-text access gap; verified Gaussian-input-preservation distinction |
| Direct primary PDF1911.06555v4; find DefinitionV.1, TheoremV.6, TheoremV.7, Gaussian symmetry, preservation | John–Parthasarathy2021 structural SectionsIV–V and overview | Quadratic-exponential kernel is assumed for E2; no arbitrary coherent-image rigidity theorem in inspected sections |

## 5. Outcome by contribution unit

| Unit | Decision | Permitted positioning |
|---|---|---|
| Fixed affine matrix condition | COLLISION / BRIDGE | Classical Gaussian operator theory translated explicitly to the Koopman/RKHS question |
| Negative answer to necessity of the2025 condition | Exact source-question resolution | State the counterexample and sharp replacement while crediting classical affine theory |
| Arbitrary covariance-field constancy | BOUNDED UNCERTAINTY | A self-contained proven classification step; historical novelty provisional |
| Direct mean-affinity proof | Known-special-case recovery and proof synthesis | Credit deterministic rigidity; describe a common analytic proof |
| Rectangular dimensions and exact coisometric range | Standard range-RKHS consequence | Complete the classification quantitatively without standalone novelty claims |
| Whole manuscript | Mathematically substantive synthesis, priority incomplete | Any assessment must reflect uninspected variants in Holevo2017, the bounded scope of the preserver search, the classical affine overlap, and the earlier public posting of the OU witness (GitHub issue #23376) |

## 6. Decision

Proceed with the theorem and self-contained proof, while presenting originality cautiously. There is no mathematical gap presently identified in the covariance/mean rigidity argument, but the strongest statement-level novelty claim has not passed an exhaustive preserver-literature audit. Neither failed search queries nor a recent source's open-question wording can establish priority.

The next historical check is the full text of Holevo2017 for variants beyond its main Gaussian-input-preservation theorem, followed by any bounded coherent-to-Gaussian-vector preserver theorem not found in this search. Alekseev–Afonin–Bogachev2021 has now been checked at theorem level. Do not treat this proof alone as establishing historical priority.

## Revision addendum (4 November 2026)

In the revised manuscript this result is Theorem 5. It now has a companion, Theorem 9, which drops the Gaussian conditional-law assumption for additive state-independent noise: if the noise characteristic function satisfies a Gaussian lower bound (every infinitely divisible law does), boundedness between global Gaussian RKHSs forces an affine Borel drift. For constant covariance this contains the drift part of Theorem 5. Ohnishi et al. (2024), Remark 3.1, was re-read in arXiv:2106.15775v2: it states that for a Gaussian RKHS "the only dynamics inducing bounded Koopman operators are those of affine", citing Ikeda et al., for deterministic dynamics. It contains no noise, covariance-field statement or matrix criterion. The OU witness was posted without proof in GitHub issue the-omega-institute/trureturing #23376 on 28 October 2026; that issue does not state the rigidity results.
