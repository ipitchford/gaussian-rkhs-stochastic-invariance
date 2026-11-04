# When Gaussian kernel spaces are invariant under stochastic dynamics

*Transition rigidity, a Gaussian-component noise boundary and a discontinuous diffusion limit*

Author: Anonymous. Text CC0-1.0; code MIT (see `LICENSE.md`). Version 0.1.0-candidate, an unrefereed research candidate. Its review was internal and AI-assisted, not human peer review.

- Version DOI: [10.5281/zenodo.23937400](https://doi.org/10.5281/zenodo.23937400); concept DOI (all versions): [10.5281/zenodo.23937399](https://doi.org/10.5281/zenodo.23937399)
- Release page: <https://evidencepress.org/releases/gaussian-rkhs-stochastic-invariance/>

## The question in one paragraph

Kernel methods such as kernel EDMD learn how a random system evolves by working inside a space of smooth test functions, typically the reproducing kernel Hilbert space (RKHS) of a Gaussian kernel $k_P(x,y)=\exp[-(x-y)^\top P^{-1}(x-y)]$. Their error analysis often assumes the space is *invariant*: averaging any observable in the space over one step of the dynamics gives another member of the space. Philipp et al. (2025, PAMM) proved invariance for linear SDEs $dX=AX\,dt+B\,dW$ (Ornstein–Uhlenbeck processes) when $AP+PA^\top\preceq2BB^\top$, and left open whether this is necessary. **It is not: the exact condition is $AP+PA^\top\preceq4BB^\top$.** The factor 4 arises because the RKHS norm involves two independent copies of the noise, whose difference has twice the covariance.

## Main results

- **Rigidity.** If a Markov transition with Gaussian conditional laws $N(F(x),Q(x))$ (arbitrary Borel fields) maps one global Gaussian RKHS boundedly into another, then $Q$ is constant, $F$ is affine with full-column-rank matrix $M$, and $MRM^\top\preceq P+4Q$ exactly (Theorem 5). For transitions "deterministic map plus fixed noise" whose noise characteristic function has a Gaussian lower bound (every infinitely divisible law, pure jumps included), the map must be affine (Theorem 9). So Euler-type steps of nonlinear SDEs never preserve a global Gaussian RKHS.
- **Noise boundary.** For affine maps with infinitely divisible noise only the Gaussian covariance component enters the matrix boundary (Theorems 8 and 11).
- **Discontinuous diffusion limit.** A compound-Poisson approximation with jumps $\pm\varepsilon$ of a stable linear diffusion converges to it at sharp order $\varepsilon^2$ in the norm from the RKHS to bounded continuous functions, yet at $t=1/10$ every approximant sends the fixed observable $e^{-8|x|^2/5}$ outside the RKHS while the Brownian limit keeps it inside (Theorem 12, Proposition 13).
- **OU answer and bandwidth rule.** All-time invariance holds exactly when $AP+PA^\top\preceq4BB^\top$ (Theorem 6). The stable controllable shear $A=\begin{pmatrix}-1&5\\0&-1\end{pmatrix}$, $B=P=I$ satisfies it but not the factor-2 condition. For an isotropic width $P=\sigma^2I$ the admissible range is $\sigma^2\le4/\lambda_{\max}\big((BB^\top)^{-1/2}(A+A^\top)(BB^\top)^{-1/2}\big)$, twice the earlier range (shear: $4/3$, not $2/3$). The invariance hypothesis of the kEDMD error bound of Philipp et al. (2025b, Theorem 4.2) then holds for multivariate OU processes (Corollary 18).

## What is prior work, and what is not claimed

The fixed affine criterion is a specialisation of classical Gaussian-Fock operator theory (Neretin 1990, 2011): the OU answer is a translation, not a new operator theorem. The shear witness and a proposed derivation were posted first, explicitly unproven, in GitHub issue [the-omega-institute/trureturing #23376](https://github.com/the-omega-institute/trureturing/issues/23376) (28 October 2026). All statements concern the global RKHS norm, not pointwise prediction or finite-data learning. State-dependent non-Gaussian transitions remain open. Novelty is asserted only within a bounded, dated search (see `audit/`).

## Files

| File | Contents |
| --- | --- |
| `manuscript.pdf`, `manuscript.md` | The paper with all proofs (PDF built by `code/build.py`: Pandoc with a XeTeX engine). |
| `code/verify.py` | Exact rational and numerical checks of the constants, thresholds and Table 1; explicit failures (valid under `python -O`); also draws the figure. |
| `audit/verification_results.json` | Output of the final run. |
| `figures/invariance_and_norm.{pdf,png}` | Figure 1. |
| `requirements.txt` | Pinned packages (numpy 2.3.5, scipy 1.17.0, matplotlib 3.10.8). |
| `audit/*.md`, `audit/target_*.yaml` | Dated, bounded prior-art audits and machine-readable targets. |
| `AI_INDEX.md`, `RESEARCH_GATES.json`, `MANIFEST.sha256` | Package index, gate record, checksums. |
| `refs.bib`, `refs/records.jsonl` | Bibliography and the Crossref/arXiv/GitHub records it was copied from. |
| `CITATION.cff`, `.zenodo.json`, `LICENSE.md` | Citation, archive metadata, licences. |
| `.github/workflows/replay.yml` | CI replay (with and without `-O`). |

## Reproduce

```bash
python -m pip install -r requirements.txt
python3 -I -B code/verify.py --output-dir OUT
python3 -I -B -O code/verify.py --output-dir OUT_O
```

Each run takes about 15 seconds and writes only inside the chosen directory; compare `OUT/verification_results.json` with `audit/verification_results.json` (last-digit float differences across platforms are expected). **The theorems rest on the written proofs, not on these finite checks.**

## How to cite

Anonymous (2026). *When Gaussian kernel spaces are invariant under stochastic dynamics: transition rigidity, a Gaussian-component noise boundary and a discontinuous diffusion limit*. Version 0.1.0-candidate. Evidence Press, unrefereed candidate. https://doi.org/10.5281/zenodo.23937400
