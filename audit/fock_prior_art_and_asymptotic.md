# Supplementary audit: classical Fock overlap and exact long-time growth

Date: 1 November 2026. Intermediate research note for the parent agent.

## 1. Material prior-art finding

The complete boundedness criterion for an **already affine, additive Gaussian** transition is a special case of classical bounded Gaussian integral operators on bosonic Fock space. It should not be represented as a historically new general Gaussian-operator classification.

The primary article inspected is:

- Yu. A. Neretin, *A semigroup of operators in the boson Fock space*, Functional Analysis and Its Applications 24 (1990), 135–144, DOI https://doi.org/10.1007/BF01077706 . Author-uploaded full manuscript: https://www.researchgate.net/publication/238843064_A_semigroup_of_operators_in_the_boson_fock_space . The introduction states the finite-dimensional criterion, attributed to Olshanski; the body reproves it.

For a particularly legible complete statement, I inspected and visually checked Neretin's 2011 author PDF, *Lectures on Gaussian Integral Operators and Classical Groups*, Chapter 5, Proposition 1.3 and Theorem 1.4, printed p.288 (PDF p.300): https://www.mat.univie.ac.at/~neretin/lectures/ems.pdf . In the book's numbering these are Proposition 5.1.3 and Theorem 5.1.4. A Fock Gaussian integral operator with symmetric block matrix

\[
\Gamma=\begin{pmatrix}K&L\\L^T&N\end{pmatrix}
\]

is bounded exactly when \(\|\Gamma\|\le1\), \(\|K\|<1\), and \(\|N\|<1\).

I also inspected Hilgert's 1989 primary paper, *A note on Howe's oscillator semigroup*, https://www.numdam.org/article/AIF_1989__39_3_663_0.pdf , and Dereziński–Karczmarczyk's *Quantization of Gaussians*, https://www.fuw.edu.pl/~derezins/semigroup-pavlov.pdf . These confirm the broad established Gaussian-operator framework; the exact reduction below uses the transparent Olshanski criterion.

### Explicit reduction of our criterion to Olshanski's theorem

First whiten the kernel to \(P=I\). Put

\[
L=P^{-1/2}MP^{1/2},\qquad Q_0=P^{-1/2}QP^{-1/2}.
\]

Translation of the input is unitary, so the affine shift can be suppressed for boundedness. The real Gaussian RKHS is unitarily identified with standard complex Fock space by

\[
f(x)=e^{-|x|^2}F(\sqrt2x).
\]

This follows directly from the Fock reproducing kernel \(e^{z\cdot\bar w}\). Under this identification the transition \(Tf(x)=\mathbb E f(Lx+Z)\), \(Z\sim N(0,Q_0)\), has Fock integral kernel

\[
\det(I+2Q_0)^{-1/2}
\exp\left[\frac12z^TKz+z^TL^TS\bar w+\frac12\bar w^TN\bar w\right],
\]

where

\[
S=(I+2Q_0)^{-1},\quad K=I-L^TSL,\quad N=I-S,
\quad
\Gamma=\begin{pmatrix}I-L^TSL&L^TS\\SL&I-S\end{pmatrix}.
\]

The matrix \(\Gamma\) is real symmetric. Moreover,

\[
I-\Gamma=\begin{pmatrix}L^T\\-I\end{pmatrix}S\begin{pmatrix}L&-I\end{pmatrix}\succeq0.
\]

Taking the Schur complement of the positive definite block \(2I-S\) in \(I+\Gamma\) shows that

\[
I+\Gamma\succeq0
\iff L^T S(2I-S)^{-1}L\preceq I
\iff L^T(I+4Q_0)^{-1}L\preceq I
\iff LL^T\preceq I+4Q_0.
\]

When \(L\) is invertible, this inequality automatically ensures the two strict diagonal-block norm conditions. Indeed, \(0\prec L^TSL\prec2I\); the upper strict inequality follows from
\(S^{1/2}(I+4Q_0)S^{1/2}\prec2I\). Also \(0\preceq I-S\prec I\). Consequently Olshanski's theorem gives exactly

\[
MPM^T\preceq P+4Q.
\]

The derivation is a genuine formula-level overlap, not merely a shared use of Fourier analysis. The new mathematical content should therefore be located in the stated OU/RKHS open-question resolution, any genuinely new rigidity theorem for state-dependent transitions, and consequences not already in the general theory. The exact affine criterion by itself has a significant originality limitation.

### Very recent related paper

Sang and Zhao, *Boundedness and compactness of Gaussian integral operators between Fock spaces*, arXiv:2610.28279v1, submitted 20 October 2026 (the arXiv listing title is shorter), studies one complex variable and Gaussian integral kernels with fixed parameters across \(F^p\to F^q\). The full paper was read on 9 November 2026. Theorem 1.1 at \(p=q=2\), with the parameters of manuscript (24) at \(d=1\), reduces to criterion (26); its compactness criterion (Theorem 1.2) never holds for these operators, in agreement with Theorem 20 of the manuscript. It contains no rigidity result. The older multidimensional Olshanski criterion remains the more decisive overlap. Source: https://arxiv.org/abs/2610.28279 .

## 2. Exact Gaussian range and a basic alternative derivation

For invertible \(M\), the exact set-theoretic range of an additive Gaussian transition from \(H_P\) is \(H_R\), where

\[
R=M^{-1}(P+4Q)M^{-T}.
\]

The norm relation is

\[
\|Tf\|_{H_R}^2
=\left(\frac{\det P}{\det(P+4Q)}\right)^{1/2}\|f\|_{H_P}^2.
\]

This is also the standard image-RKHS construction applied to the feature map
\(x\mapsto\mathbb E[k_P(\cdot,Mx+b+Z)]\). Its kernel is

\[
\mathbb E_{Z,Z'}k_P(Mx+b+Z,My+b+Z')
=\left(\frac{\det P}{\det(P+4Q)}\right)^{1/2}k_R(x,y).
\]

Thus the factor four comes from comparing two independent noises, whose difference has covariance \(2Q\), inside the Gaussian kernel with spectral covariance \(P/2\). This range calculation is an application of basic image-RKHS and Gaussian convolution identities; it should not be promoted as novel machinery.

The general differing-space statement is: \(T:H_P\to H_S\) is bounded iff \(MSM^T\preceq P+4Q\), with norm

\[
\|T\|=|\det M|^{-1/2}(\det P/\det S)^{1/4}.
\]

## 3. Requested norm asymptotic: verified

Assume \(A\) Hurwitz and \(AP+PA^T\preceq4D\). Set

\[
M_t=e^{tA},\quad Q_t=\int_0^te^{sA}De^{sA^T}\,ds,
\quad\Sigma=\int_0^\infty e^{sA}De^{sA^T}\,ds,
\quad c_P=\pi^{-d/2}(\det P)^{-1/2}.
\]

The exact Fourier identity gives

\[
e^{t\operatorname{tr}A}\|K^tf\|_P^2
=c_P\int|\widehat f(\xi)|^2
\exp\left[\frac14\xi^TM_tPM_t^T\xi-\xi^TQ_t\xi\right]\,d\xi.
\]

Because \(P+4Q_t-M_tPM_t^T\succeq0\), the integrand is bounded by
\(|\widehat f(\xi)|^2e^{\xi^TP\xi/4}\), which is integrable. Hurwitz stability gives \(M_t\to0\), \(Q_t\to\Sigma\). Dominated convergence yields

\[
\boxed{
e^{t\operatorname{tr}A}\|K^tf\|_P^2
\longrightarrow c_P\int|\widehat f(\xi)|^2e^{-\xi^T\Sigma\xi}\,d\xi.
}
\]

For every nonzero \(f\), the limit is strictly positive and finite, since its Fourier transform is nonzero on a set of positive measure and the Gaussian factor is positive everywhere. Therefore

\[
\lim_{t\to\infty}\frac1t\log\|K^tf\|_P=-\frac12\operatorname{tr}A.
\]

This applies even when \(f\) has zero invariant-measure mean. It describes a global function-space norm and does not contradict pointwise mixing.

The normalised squared norm is nonincreasing, since

\[
\frac{d}{dt}[P+4Q_t-M_tPM_t^T]
=e^{tA}(4D-AP-PA^T)e^{tA^T}\succeq0.
\]

### A self-contained absence-of-eigenvectors proof

For Hurwitz \(A\), the effective covariance rate \(D_e=D-(AP+PA^T)/4\) has stationary Gramian \(\Sigma+P/4\succ0\), so its finite-time Gramian is positive definite for every \(t>0\). Thus

\[
\|K^tf\|_P<e^{-t\operatorname{tr}A/2}\|f\|_P\quad(f\ne0,t>0).
\]

If \(K^tf=\mu f\), iteration and the asymptotic force \(|\mu|=e^{-t\operatorname{tr}A/2}\), contradicting this strict inequality. Zero cannot be an eigenvalue because Gaussian convolution and invertible composition are injective. Therefore each \(K^t\), \(t>0\), has empty point spectrum. The generator has no eigenvectors as a consequence. This proof does not require importing the classical point-spectrum theorem.

## 4. Restricted-domain qualification

For a Gaussian RKHS restricted to any set with nonempty interior, the restriction map is isometric and onto: analytic continuation makes its nullspace zero. This is stated explicitly in Philipp et al., *Error Analysis of Kernel EDMD for Prediction and Control in the Koopman Framework*, Appendix D, equation (D.1), published 16 July 2025, https://doi.org/10.1007/s00332-025-10182-3 .

Consequently one should not say that merely restricting the Gaussian RKHS to a bounded open region eliminates the RKHS-to-RKHS operator-norm obstruction. Weaker target norms, such as uniform or invariant-measure \(L^2\) norms, do eliminate that particular logical implication and are the correct qualification.

## 5. Search scope

The targeted search covered real/complex Fock spaces, Segal–Bargmann transforms, Gaussian integral operators, Gaussian averaging, expected Gaussian kernels, conditional-mean embeddings, heat/OU intertwining, and Gaussian RKHS range formulas. It found the exact classical Fock reduction above. It did not locate a previous explicit statement of the factor-four OU/RKHS answer, but absence of a located statement is not proof of historical priority.

## Revision addendum (4 November 2026)

The Fock-space specialisation is now Section 3 of the revised manuscript, placed directly after the Gaussian transition results, and the matrix \((I+2Q_0)^{-1}\) is renamed \(W\) there to avoid a clash with \(S=P+4Q\). The asymptotic growth and point-spectrum results of this note are Theorem 19(c). The fixed affine criterion, and hence the OU answer, remains a specialisation of the Olshanski criterion; in addition, the separating witness was publicly proposed without proof in GitHub issue the-omega-institute/trureturing #23376 on 28 October 2026.
