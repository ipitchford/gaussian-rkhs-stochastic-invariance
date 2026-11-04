# AI index: Gaussian RKHS invariance under stochastic dynamics (v0.1.0-candidate)

Machine-oriented map of claims, evidence and limits. Human readers should start with [README.md](README.md) and the paper [manuscript.pdf](manuscript.pdf) (source [manuscript.md](manuscript.md)).
Version DOI 10.5281/zenodo.23937400; concept DOI 10.5281/zenodo.23937399.

## Notation

k_P(x,y) = exp[-(x-y)^T P^{-1} (x-y)], H_P its RKHS on all of R^d. Transition Tf(x) = E f(X') with X' ~ N(F(x),Q(x)) or X' = F(x)+Z. Affine: F(x)=Mx+b. OU: dX = AX dt + B dW, D = BB^T. Loewner order <=.
PSWPN25a = Philipp, Schaller, Worthmann, Peitz, Nuske, PAMM 25(1) (2025) e202400127, arXiv:2405.14429v1 (sufficient condition AP+PA^T <= 2BB^T; necessity left open).

## Claims and where they are proved

| ID | Claim | Location in [manuscript.md](manuscript.md) | Evidence type |
|---|---|---|---|
| C1 | Theorem 5: Gaussian transitions bounded H_P(R^m) -> H_R(R^d) have constant Q, affine F, full-column-rank M, and MRM^T <= P+4Q | Section 2.5 | proof (arbitrary Borel fields) |
| C2 | Proposition 3: exact range and norm of affine Gaussian transitions; boundedness iff MRM^T <= P+4Q | Section 2.3 | proof; specialisation of Neretin's Gaussian-Fock theory (Section 3) |
| C3 | Theorem 6: OU all-time invariance iff AP+PA^T <= 4BB^T; norm grows like exp(-t tr A/2) | Section 4 | proof (no stability or controllability assumption) |
| C4 | Shear A=[[-1,5],[0,-1]], B=P=I satisfies factor 4 but not factor 2 | Section 4.1 | proof + exact rational check |
| C5 | Theorems 8, 11: for affine infinitely divisible noise only the Gaussian component Q (rate D) enters the boundary | Sections 5.1, 5.4 | proof |
| C6 | Theorem 9: additive noise with a Gaussian lower bound on its characteristic function forces affine drift | Section 5.2 | proof; Cauchy-noise numerical illustration |
| C7 | Theorem 12, Prop. 13: compound-Poisson approximants converge at sharp order eps^2 (H_I -> C_b), yet each sends exp(-8|x|^2/5) outside H_I at t=1/10 | Section 6 | proof + quadrature of constants (Gamma ~ 0.0993) |
| C8 | Props. 14-17, Cor. 18: sampling thresholds, isotropic rule sigma^2 <= 4/lambda_max, kEDMD hypothesis for multivariate OU | Sections 7-8 | proof; Table 1 reproduced |
| C9 | Theorems 19-20: isometry to a classical OU semigroup, spectrum, growth, finite-rank barrier | Section 9 | proof (imported spectral theorem attributed) |

## Verification artefacts

- [code/verify.py](code/verify.py) -> [audit/verification_results.json](audit/verification_results.json) and [figures/invariance_and_norm.png](figures/invariance_and_norm.png): exact rational checks (sections A, B, H) and quadrature checks (C-G) of constants and normalisations; explicit check() failures, valid under python -O. Scope: finite checks only, not the theorems.
- Pinned packages: [requirements.txt](requirements.txt). CI: [.github/workflows/replay.yml](.github/workflows/replay.yml). PDF build: [code/build.py](code/build.py).

## Sources and novelty record

- [refs.bib](refs.bib), [refs/records.jsonl](refs/records.jsonl): bibliography and registry records.
- [audit/consolidated_novelty_report.md](audit/consolidated_novelty_report.md), [audit/state_covariance_novelty_report.md](audit/state_covariance_novelty_report.md), [audit/levy_novelty.md](audit/levy_novelty.md), [audit/fock_prior_art_and_asymptotic.md](audit/fock_prior_art_and_asymptotic.md); targets [audit/target_state_covariance.yaml](audit/target_state_covariance.yaml), [audit/target_levy.yaml](audit/target_levy.yaml).
- [RESEARCH_GATES.json](RESEARCH_GATES.json); [MANIFEST.sha256](MANIFEST.sha256); [LICENSE.md](LICENSE.md); [CITATION.cff](CITATION.cff); [.zenodo.json](.zenodo.json).

## Limits

Unrefereed candidate: internal AI-assisted review only; no human peer review, independent reproduction or proof-assistant formalisation. The fixed affine criterion (C2) and the OU answer (C3) are a translation of classical Gaussian-Fock theory; the witness (C4) and a proposed derivation appeared first, explicitly unproven, in GitHub issue the-omega-institute/trureturing #23376 (28 October 2026). Statements concern the global RKHS norm, not pointwise prediction or finite-data learning. State-dependent non-Gaussian transitions are open. Priority only within a bounded search.
