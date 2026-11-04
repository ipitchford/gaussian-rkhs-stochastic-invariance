#!/usr/bin/env python3
"""Reproducible algebraic and numerical checks for
"When Gaussian kernel spaces are invariant under stochastic dynamics".

Usage:
    python3 -I -B code/verify.py --output-dir OUT

Every check is made with an explicit check() call that raises RuntimeError, so the
checks still run under `python -O`.  Nothing is written outside OUT; the figure is
written to OUT/figures and the results to OUT/verification_results.json.

No Monte Carlo simulation is used.  Quantities reported as "derived" are computed
here from the entered matrices and parameters, not typed in.  Numerical checks
test constants, normalisations and implementation; the proofs in the manuscript
establish the theorems.

Sections (manuscript numbering):
  A  Separating shear example, Section 4, eqs. (29), (31)-(33)    exact rationals
  B  One-step Gaussian witness, Section 2.4, eq. (13)             exact rationals
  C  Shear sampling boundary, Proposition 15; P+2Q vs P+4Q        quadrature
  D  Effective covariance identity, Theorem 19(a), eq. (65)       quadrature
  E  Norm sharpness by Gaussian frequency packets, Corollary 4    closed form
  F  Diffusion approximation, Theorem 12 / Proposition 13         quadrature
     (H_t, moment integral, bound coefficient (52), witness, Brownian
      membership, limit constant Gamma ~ 0.0993 from (57), exact
      epsilon-norms from (56) with an independent Cartesian check)
  G  Additive-noise rigidity checks, Theorem 9: Cauchy and exponential
     (asymmetric) noise, and the rectangular (m > d) Gaussian marginal
  H  Admissible bandwidths and the kEDMD hypothesis, Section 8, Table 1
  I  Figure 1
"""
from __future__ import annotations

import argparse
import json
import math
import os
import platform
import sys
import tempfile
from fractions import Fraction as Fr
from pathlib import Path


def check(cond, msg):
    """Explicit check that is not removed by python -O."""
    if not bool(cond):
        raise RuntimeError("check failed: " + msg)


def parse_args():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--output-dir", required=True,
                    help="directory for verification_results.json and figures/")
    ap.add_argument("--no-figure", action="store_true", help="skip the figure")
    return ap.parse_args()


ARGS = parse_args()
OUT = Path(ARGS.output_dir).resolve()
(OUT / "figures").mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", tempfile.mkdtemp(prefix="gk_mpl_"))

import numpy as np  # noqa: E402
import scipy  # noqa: E402
from scipy.integrate import quad, quad_vec  # noqa: E402
from scipy.linalg import expm, solve_continuous_lyapunov  # noqa: E402
from scipy.optimize import brentq  # noqa: E402

results: dict = {}


# ---------------------------------------------------------------------------
# Exact rational helpers (2x2 symmetric matrices)
# ---------------------------------------------------------------------------
def rmat(rows):
    return [[Fr(x) for x in r] for r in rows]


def radd(X, Y, a=1, b=1):
    return [[a * X[i][j] + b * Y[i][j] for j in range(2)] for i in range(2)]


def rmul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def rT(X):
    return [[X[j][i] for j in range(2)] for i in range(2)]


def rsqrt_exact(q: Fr):
    """Exact square root of a nonnegative rational, or None if irrational."""
    n, d = q.numerator, q.denominator
    rn, rd = math.isqrt(n), math.isqrt(d)
    return Fr(rn, rd) if rn * rn == n and rd * rd == d else None


def sym_eigs_exact(X):
    """Exact eigenvalues of a symmetric 2x2 rational matrix (must be rational)."""
    check(X[0][1] == X[1][0], "matrix is symmetric")
    tr = X[0][0] + X[1][1]
    det = X[0][0] * X[1][1] - X[0][1] * X[1][0]
    disc = tr * tr - 4 * det
    r = rsqrt_exact(disc)
    check(r is not None, "rational eigenvalues")
    return sorted([(tr - r) / 2, (tr + r) / 2])


def fstr(v):
    return [str(x) for x in v]


# ---------------------------------------------------------------------------
# A. Separating example
# ---------------------------------------------------------------------------
A_r = rmat([[-1, 5], [0, -1]])
B_r = rmat([[1, 0], [0, 1]])
P_r = rmat([[1, 0], [0, 1]])
I_r = rmat([[1, 0], [0, 1]])
BBt = rmul(B_r, rT(B_r))
LA = radd(rmul(A_r, P_r), rmul(P_r, rT(A_r)))          # AP + PA^T
old_slack = radd(BBt, LA, 2, -1)                        # 2BB^T - (AP+PA^T)
sharp_slack = radd(BBt, LA, 4, -1)                      # 4BB^T - (AP+PA^T)
old_e, sharp_e = sym_eigs_exact(old_slack), sym_eigs_exact(sharp_slack)
check(old_e[0] < 0, "published sufficient condition (31) fails")
check(sharp_e[0] > 0, "sharp condition (29) holds strictly")
D_eff = radd(BBt, LA, 1, Fr(-1, 4))                     # BB^T - (AP+PA^T)/4
D_eff_e = sym_eigs_exact(D_eff)
check(D_eff_e[0] > 0, "effective diffusion positive definite")
# Hurwitz: triangular, eigenvalues are the diagonal entries. Controllable: B invertible.
check(A_r[1][0] == 0 and A_r[0][0] < 0 and A_r[1][1] < 0, "A Hurwitz")
check(B_r[0][0] * B_r[1][1] - B_r[0][1] * B_r[1][0] != 0, "(A,B) controllable")
trA = A_r[0][0] + A_r[1][1]
# Isotropic thresholds: 4 / lambda_max(A + A^T) (B = I), and the published half.
sym_e = sym_eigs_exact(radd(A_r, rT(A_r)))
sig_sharp = Fr(4) / sym_e[1]
sig_old = Fr(2) / sym_e[1]
check(sig_sharp == Fr(4, 3) and sig_old == Fr(2, 3), "isotropic thresholds 4/3 and 2/3")
results["A_separating_example"] = {
    "A": [[-1, 5], [0, -1]], "B": "I_2", "P": "I_2",
    "derived_old_slack_eigenvalues": fstr(old_e),
    "derived_sharp_slack_eigenvalues": fstr(sharp_e),
    "derived_effective_diffusion": [fstr(r) for r in D_eff],
    "derived_effective_diffusion_eigenvalues": fstr(D_eff_e),
    "derived_operator_norm": f"exp({-trA / 2}*t)",
    "derived_eigenvalues_A_plus_AT": fstr(sym_e),
    "derived_isotropic_threshold_sharp": str(sig_sharp),
    "derived_isotropic_threshold_published": str(sig_old),
}
# Shear-family thresholds |s| <= 2+4q (sharp) and |s| <= 2q' style (published) at q=1.
s_sharp = max(s for s in range(0, 50) if sym_eigs_exact(radd(radd(I_r, I_r, 4, 0), radd(rmat([[-1, s], [0, -1]]), rT(rmat([[-1, s], [0, -1]]))), 1, -1))[0] >= 0)
s_old = max(s for s in range(0, 50) if sym_eigs_exact(radd(radd(I_r, I_r, 2, 0), radd(rmat([[-1, s], [0, -1]]), rT(rmat([[-1, s], [0, -1]]))), 1, -1))[0] >= 0)
check((s_old, s_sharp) == (4, 6), "integer shear thresholds 4 and 6 at q = 1")
results["A_separating_example"]["derived_integer_shear_thresholds"] = {"published": s_old, "sharp": s_sharp}

# ---------------------------------------------------------------------------
# B. One-step Gaussian witness (scalar), Section 2.4: M=3, Q=1, P=R=1.
# Input k_G with G=1 is in H_1 because 2G-P=1>0.  Output matrix (G+2Q)/M^2.
# ---------------------------------------------------------------------------
Mw, Qw, Pw, Gw = Fr(3), Fr(1), Fr(1), Fr(1)
out_width = (Gw + 2 * Qw) / (Mw * Mw)
check(2 * Gw - Pw > 0, "witness input belongs to H_P (19)")
check(2 * out_width - Pw <= 0, "witness output not in H_R (13)")
check(Mw * Pw * Mw - Pw - 4 * Qw > 0, "matrix condition violated")
in_norm2 = Gw / rsqrt_exact(Pw * (2 * Gw - Pw))
results["B_one_step_witness"] = {
    "M": 3, "Q": 1, "P": 1, "input": "exp(-x^2)",
    "derived_output_width": str(out_width),
    "derived_matrix_slack_MRM^T-P-4Q": str(Mw * Pw * Mw - Pw - 4 * Qw),
    "derived_input_norm_squared_(13)": str(in_norm2),
}


# ---------------------------------------------------------------------------
# C. Shear sampling boundary (Proposition 15)
# ---------------------------------------------------------------------------
def gramian(A, D, t):
    return quad_vec(lambda u: expm(A * u) @ D @ expm(A.T * u), 0, t,
                    epsabs=1e-11, epsrel=1e-11)[0]


def shear_slack(s, t, q=1.0):
    e = math.exp(-2 * t)
    h = 1 + 2 * q
    a = h * (1 - e) + s * s * (q * (1 - e * (1 + 2 * t)) - h * t * t * e)
    b = s * (q * (1 - e) - h * t * e)
    return np.array([[a, b], [b, h * (1 - e)]])


def shear_det(s, t, q=1.0):
    e = math.exp(-2 * t)
    h = 1 + 2 * q
    return (h * h + s * s * q * (1 + q)) * (1 - e) ** 2 - s * s * h * h * t * t * e


def threshold(s, q=1.0):
    h = 1 + 2 * q
    if abs(s) <= 2 * h:
        return 0.0
    r = abs(s) * h / (2 * math.sqrt(h * h + s * s * q * (1 + q)))
    return brentq(lambda t: math.sinh(t) / t - r, 1e-6, 20, xtol=1e-14)


max_slack_err = max_det_err = 0.0
for s in [0.0, 4.0, 5.0, 6.0, 7.0, 10.0, 25.0]:
    for q in [0.0, 0.25, 1.0, 2.0]:
        A = np.array([[-1.0, s], [0.0, -1.0]])
        for t in [0.01, 0.1, 0.35, 0.7, 1.5]:
            M = expm(A * t)
            direct = np.eye(2) + 4 * gramian(A, q * np.eye(2), t) - M @ M.T
            max_slack_err = max(max_slack_err, float(np.max(np.abs(direct - shear_slack(s, t, q)))))
            max_det_err = max(max_det_err, abs(float(np.linalg.det(direct)) - shear_det(s, t, q)))
check(max_slack_err < 2e-10, "closed shear slack matches quadrature")
check(max_det_err < 2e-8, "closed shear determinant (59) matches quadrature")
thr = {str(s): threshold(s) for s in [4, 5, 6, 7, 10, 25, 100]}
check(abs(thr["7"] - 0.3000561741) < 1e-9, "threshold s=7")
check(abs(thr["10"] - 0.4721567642) < 1e-9, "threshold s=10")
lim = brentq(lambda t: math.sinh(t) / t - 3 / (2 * math.sqrt(2)), 1e-6, 2, xtol=1e-14)
check(abs(lim - 0.5979259925) < 1e-9, "large-shear limit")
# The minimum eigenvalue of the slack changes sign at T_{7,1}.
A7 = np.array([[-1.0, 7.0], [0.0, -1.0]])
for tt, sign in [(thr["7"] - 1e-3, -1), (thr["7"] + 1e-3, 1)]:
    M = expm(A7 * tt)
    lm = np.linalg.eigvalsh(np.eye(2) + 4 * gramian(A7, np.eye(2), tt) - M @ M.T)[0]
    check(sign * lm > 0, "slack changes sign at T_{7,1}")
# Kernel-section route versus space route (P+2Q vs P+4Q): for the shear s=5,
# I+2Q_t-M_tM_t^T is indefinite at small t while I+4Q_t-M_tM_t^T is positive.
A5 = np.array([[-1.0, 5.0], [0.0, -1.0]])
sec_vs_space = []
for tt in [0.05, 0.1, 1.0]:
    M = expm(A5 * tt)
    Qt = gramian(A5, np.eye(2), tt)
    sec_vs_space.append({"t": tt,
                         "min_eig_I+2Q-MM^T": float(np.linalg.eigvalsh(np.eye(2) + 2 * Qt - M @ M.T)[0]),
                         "min_eig_I+4Q-MM^T": float(np.linalg.eigvalsh(np.eye(2) + 4 * Qt - M @ M.T)[0])})
check(sec_vs_space[0]["min_eig_I+2Q-MM^T"] < 0 < sec_vs_space[0]["min_eig_I+4Q-MM^T"], "2Q route fails, 4Q holds at t=0.05")
results["C_shear_sampling"] = {"cases": 140, "max_entry_error": max_slack_err,
                               "max_determinant_error": max_det_err,
                               "sampling_thresholds_q1": thr, "large_shear_limit": lim,
                               "section_route_vs_space_route_s5": sec_vs_space}

# ---------------------------------------------------------------------------
# D. Effective covariance identity (Theorem 16), noncommuting instances
# ---------------------------------------------------------------------------
rng = np.random.default_rng(193705)
max_cov_err = 0.0
for i in range(24):
    d = 2 + i % 3
    X = rng.normal(size=(d, d))
    P = X @ X.T + 0.3 * np.eye(d)
    A = rng.normal(size=(d, d)) - 2 * np.eye(d)
    S = (A @ P + P @ A.T) / 4
    D = (max(np.linalg.eigvalsh(S).max(), 0) + 0.3) * np.eye(d)
    t = 0.03 + 0.01 * i
    M = expm(A * t)
    closed = gramian(A, D, t) + (P - M @ P @ M.T) / 4
    max_cov_err = max(max_cov_err, float(np.max(np.abs(gramian(A, D - S, t) - closed))))
check(max_cov_err < 1e-9, "effective covariance identity (65)")
results["D_effective_covariance"] = {"cases": 24, "max_entry_error": max_cov_err}

# ---------------------------------------------------------------------------
# E. Norm sharpness: Gaussian frequency packets attain ||T|| in the limit.
# ---------------------------------------------------------------------------
ratios = []
for w in [1.0, 0.5, 0.2, 0.1, 0.05, 0.01]:
    ratios.append({"frequency_width": w,
                   "ratio_to_exact_norm": float(np.linalg.det(np.eye(2) + w * w * shear_slack(5, 0.4) / 4) ** (-0.25))})
check(all(r["ratio_to_exact_norm"] < 1 for r in ratios), "packets below the norm")
check(ratios[-1]["ratio_to_exact_norm"] > 0.9999, "packets approach the norm")
results["E_norm_sharpness_packets"] = ratios

# ---------------------------------------------------------------------------
# F. Diffusion approximation (Theorem 12, Proposition 13), d = 2, P = I, t = 1/10
# ---------------------------------------------------------------------------
A = np.array([[-1.0, 5.0], [0.0, -1.0]])
t_star = 0.1
c_I = 1 / math.pi                                   # c_P for P = I_2
# H_t = int_0^t ||e^{sA}||^4 ds and its bound (e^{6t}-1)/6.
H_t = quad(lambda s: np.linalg.norm(expm(A * s), 2) ** 4, 0, t_star, epsabs=1e-13)[0]
H_bound = (math.exp(6 * t_star) - 1) / 6
check(H_t <= H_bound, "H_t below its bound")
check(max(np.linalg.eigvalsh((A + A.T) / 2)) == 1.5, "lambda_max of symmetric part is 3/2")
# Moment integral int |xi|^8 e^{-|xi|^2/4} = 24576 pi (polar quadrature).
mom = 2 * math.pi * quad(lambda r: r ** 9 * math.exp(-r * r / 4), 0, np.inf)[0]
check(abs(mom / (24576 * math.pi) - 1) < 1e-12, "moment integral 24576 pi")
pref = (2 * math.pi) ** -1 * c_I ** -0.5 * math.sqrt(mom)
check(abs(pref - 32 * math.sqrt(6)) < 1e-9, "prefactor 32 sqrt 6")
coef_bound = 2 * math.sqrt(6) / 9 * (math.exp(6 * t_star) - 1)
check(abs(coef_bound - pref * H_bound / 24) < 1e-12, "bound coefficient (2 sqrt6/9)(e^{6t}-1)")
check(coef_bound < 0.448, "bound coefficient < 0.448 at t = 1/10")
coef_true_H = pref * H_t / 24
# Witness (53): M = e^{t A^T}-type matrix used in the proof.
Mw = expm(A.T * t_star).T  # e^{tA}
Mm = math.exp(-0.1) * np.array([[1.0, 0.5], [0.0, 1.0]])
check(np.max(np.abs(Mw - Mm)) < 1e-14, "closed form of e^{A/10}")
v = np.array([1.0, 1.0]) / math.sqrt(2)
ray = float(v @ Mm @ Mm.T @ v)
check(abs(ray - 13 / 8 * math.exp(-0.2)) < 1e-14, "v^T M M^T v = (13/8) e^{-1/5}")
check(ray > 1.25, "ray variance exceeds 5/4")
eig_w = np.linalg.eigvalsh(Mm @ Mm.T - 1.25 * np.eye(2))
check(eig_w[1] > 0 > eig_w[0], "MM^T - 5/4 I indefinite")
# Witness f = exp(-8|x|^2/5) = k_G with G = (5/8) I: norm^2 = det G / sqrt(det P det(2G-P)).
G = Fr(5, 8)
wit_norm2 = (G * G) / rsqrt_exact((2 * G - 1) ** 2)
check(wit_norm2 == Fr(25, 16), "witness norm squared 25/16")
# Brownian output membership (Theorem 12): (5/4)I + 4Q_t - M M^T >= I/4 > 0.
Qt = gramian(A, np.eye(2), t_star)
brown = np.linalg.eigvalsh(1.25 * np.eye(2) + 4 * Qt - Mm @ Mm.T)[0]
check(brown >= 0.25 - 1e-12, "Brownian output stays in H_I")
# Limit constant Gamma_{I,t} from (57) by exact radial integration:
# a_t(r theta) = r^4 a(theta), j_0(r theta) = r^2 j(theta), so
# int a^2 e^{-2 j_0 - |xi|^2/4} = int_theta a(theta)^2 Gamma(5) / (2 (2 j(theta) + 1/4)^5).
s_nodes, s_w = np.polynomial.legendre.leggauss(60)
s_nodes = 0.5 * t_star * (s_nodes + 1)
s_w = 0.5 * t_star * s_w
E_s = np.array([expm(A.T * s) for s in s_nodes])     # e^{s A^T}


def a_and_j(theta):
    xi = np.array([math.cos(theta), math.sin(theta)])
    z = E_s @ xi
    return float(s_w @ np.sum(z ** 4, axis=1)), float(s_w @ (0.5 * np.sum(z ** 2, axis=1)))


def gamma_integrand(theta):
    a, j = a_and_j(theta)
    return a * a * 24.0 / (2 * (2 * j + 0.25) ** 5)


ang = quad(gamma_integrand, 0, 2 * math.pi, limit=400, epsabs=1e-14, epsrel=1e-12)[0]
Gamma = (2 * math.pi) ** -1 / (24 * math.sqrt(c_I)) * math.sqrt(ang)
check(0.0990 < Gamma < 0.0995, "limit constant Gamma_{I,1/10} ~ 0.0993")


# Exact epsilon-norms from the MMD identity (56), by polar quadrature.
def g_rem(u):
    """u^2/2 - (1 - cos u), cancellation-free."""
    u2 = u * u
    small = np.abs(u) < 0.05
    series = u2 * u2 / 24 - u2 ** 3 / 720 + u2 ** 4 / 40320
    return np.where(small, series, u2 / 2 - 2 * np.sin(u / 2) ** 2)


th = np.linspace(0, 2 * math.pi, 512, endpoint=False)
r_nodes, r_w = np.polynomial.legendre.leggauss(240)
r_nodes = 12.0 * (r_nodes + 1)
r_w = 12.0 * r_w
XI = np.stack([np.cos(th), np.sin(th)], axis=1)            # (n_th, 2)
Z = np.einsum("sij,tj->sti", E_s, XI)                      # (n_s, n_th, 2)
j0_dir = np.einsum("s,sti->t", s_w, 0.5 * Z ** 2)          # j_0 on unit circle


def eps_norm(eps):
    total = 0.0
    for k, r in enumerate(r_nodes):
        u = eps * r * Z
        diff = np.einsum("s,sti->t", s_w, g_rem(u)) / (eps * eps)  # j_0 - j_eps >= 0
        j0 = r * r * j0_dir
        val = (np.exp(-j0) * np.expm1(diff)) ** 2 * math.exp(-r * r / 4)  # (e^{-j_eps} - e^{-j_0})^2
        total += r_w[k] * r * val.mean() * 2 * math.pi
    return (2 * math.pi) ** -1 / math.sqrt(c_I) * math.sqrt(total)


eps_rows = []
for eps in [0.4, 0.2, 0.1, 0.05]:
    nrm = eps_norm(eps)
    eps_rows.append({"epsilon": eps, "norm": nrm, "norm_over_eps2": nrm / eps ** 2})
    check(nrm <= coef_bound * eps ** 2, "exact norm below the uniform bound (52)")
check(all(abs(r["norm_over_eps2"] - Gamma) < 5e-5 for r in eps_rows if r["epsilon"] <= 0.1),
      "norm/eps^2 converges to Gamma")
# Independent Cartesian-grid evaluation of (56) at eps = 0.2, without the remainder trick.
hc = 0.05
gc = np.arange(-14, 14 + hc / 2, hc)
XC, YC = np.meshgrid(gc, gc)
XIc = np.stack([XC.ravel(), YC.ravel()], axis=1)
Zc = np.einsum("sij,nj->sni", E_s, XIc)
j0c = np.einsum("s,sni->n", s_w, 0.5 * Zc ** 2)
jec = np.einsum("s,sni->n", s_w, 1 - np.cos(0.2 * Zc)) / 0.04
cart = (2 * math.pi) ** -1 / math.sqrt(c_I) * math.sqrt(
    float(((np.exp(-jec) - np.exp(-j0c)) ** 2 * np.exp(-(XIc ** 2).sum(1) / 4)).sum()) * hc * hc)
polar02 = next(r["norm"] for r in eps_rows if r["epsilon"] == 0.2)
check(abs(cart / polar02 - 1) < 1e-6, "polar and Cartesian (56) agree at eps = 0.2")
del Zc
# Taylor bound 0 <= j_0 - j_eps <= eps^2 H_t |xi|^4 / 24 at sample frequencies.
max_ratio = 0.0
for eps in [0.03, 0.1, 0.5, 1.0]:
    for scale in [0.1, 1.0, 4.0, 12.0]:
        xi = scale * np.array([1.0, -0.7])
        z = E_s @ xi
        diff = float(s_w @ np.sum(g_rem(eps * z), axis=1)) / eps ** 2
        bnd = eps ** 2 * float(s_w @ np.sum(z ** 4, axis=1)) / 24
        check(-1e-12 <= diff <= bnd * (1 + 1e-9) + 1e-15, "Taylor remainder bound")
        max_ratio = max(max_ratio, diff / bnd)
results["F_diffusion_approximation"] = {
    "t": "1/10", "witness": "exp(-8|x|^2/5)", "derived_witness_norm_squared": str(wit_norm2),
    "ray_variance_(13/8)e^(-1/5)": ray, "eigs_MM^T-5/4I": eig_w.tolist(),
    "brownian_output_min_eig_(5/4)I+4Q-MM^T": float(brown),
    "H_t": H_t, "H_t_bound_(e^(6t)-1)/6": H_bound,
    "moment_integral_over_pi": mom / math.pi, "prefactor_32sqrt6": pref,
    "bound_coefficient_(52)": coef_bound, "coefficient_with_exact_H_t": coef_true_H,
    "limit_constant_Gamma": Gamma, "bound_over_Gamma": coef_bound / Gamma,
    "exact_eps_norms_(56)": eps_rows, "cartesian_check_eps_0.2": cart, "taylor_bound_max_ratio": max_ratio,
}

# ---------------------------------------------------------------------------
# G. Additive-noise rigidity sanity check (Theorem 9), 1-D Cauchy noise
# (pure jump, no Gaussian part, no moments): Fourier identity (42), the mass
# mu(R) = ||G~||_P^2, and the Gaussian lower bound used in the growth step.
# ---------------------------------------------------------------------------
Pc, sc, Lc = 1.7, 0.6, 400.0


def Gt(y):
    return quad(lambda z: math.exp(-(y - z) ** 2 / Pc) * sc / math.pi / (sc * sc + z * z),
                y - 12, y + 12, limit=200)[0]


ft_rows = []
for eta in [0.0, 0.7, 1.9]:
    if eta == 0:
        val = quad(Gt, -Lc, Lc, limit=800)[0] + 2 * math.sqrt(math.pi * Pc) * sc / (math.pi * Lc)
    else:
        val = 2 * quad(Gt, 0, Lc, weight="cos", wvar=eta, limit=800)[0]
    val /= math.sqrt(2 * math.pi)
    pred = 2 ** -0.5 * math.sqrt(Pc) * math.exp(-Pc * eta ** 2 / 4) * math.exp(-sc * abs(eta))
    ft_rows.append({"eta": eta, "numeric": val, "predicted": pred})
    check(abs(val - pred) < 5e-5, "Fourier identity (42) for Cauchy noise")
mu = lambda e: math.pi ** -0.5 * 0.5 * math.sqrt(Pc) * math.exp(-Pc * e * e / 4) * math.exp(-2 * sc * abs(e))
muR = quad(mu, -40, 40, points=[0])[0]
normG = (math.pi ** -0.5 * Pc ** -0.5) * quad(lambda e: 0.5 * Pc * math.exp(-Pc * e * e / 4) * math.exp(-2 * sc * abs(e)), -40, 40, points=[0])[0]
check(abs(muR - normG) < 1e-10, "mu(R) = ||G~||_P^2")
lb_rows = []
gam = 1.0  # 2 s |e| <= gam e^2 + s^2/gam, so |phi|^2 >= e^{-s^2/gam} e^{-gam e^2}
for bb in [1.0, 3.0, 4.5]:
    lhs = quad(lambda e: math.exp(2 * e * bb) * mu(e), -30, 60, limit=400, points=[0])[0]
    Bq = Pc / 4 + gam
    lb = math.pi ** -0.5 * 0.5 * math.sqrt(Pc) * math.exp(-sc * sc / gam) * math.sqrt(math.pi / Bq) * math.exp(bb * bb / Bq)
    lb_rows.append({"b": bb, "integral": lhs, "lower_bound": lb})
    check(lhs >= lb, "Gaussian lower bound (45)")
# Asymmetric noise: Z ~ Exp(1), phi(eta) = 1/(1 - i eta). The sign convention
# G~ = k_P(.,0) * law(Z) requires FT(G~) = 2^{-1/2} sqrt(P) e^{-P eta^2/4} conj(phi(eta)).
def Gexp(y):
    return quad(lambda z: math.exp(-(y - z) ** 2 / Pc) * math.exp(-z), 0, max(0.0, y) + 14, limit=200)[0]


asym_rows = []
for eta in [0.4, 1.3]:
    re_ = quad(lambda y: Gexp(y) * math.cos(eta * y), -14, 60, limit=400)[0] / math.sqrt(2 * math.pi)
    im_ = -quad(lambda y: Gexp(y) * math.sin(eta * y), -14, 60, limit=400)[0] / math.sqrt(2 * math.pi)
    pred = 2 ** -0.5 * math.sqrt(Pc) * math.exp(-Pc * eta ** 2 / 4) / complex(1, eta)  # conj(1/(1-i eta))
    wrong = 2 ** -0.5 * math.sqrt(Pc) * math.exp(-Pc * eta ** 2 / 4) / complex(1, -eta)
    asym_rows.append({"eta": eta, "numeric": [re_, im_], "predicted": [pred.real, pred.imag]})
    check(abs(complex(re_, im_) - pred) < 1e-6, "Fourier identity (42) for asymmetric (exponential) noise")
    check(abs(complex(re_, im_) - wrong) > 1e-2, "law(-Z) convention is excluded")
# Rectangular marginal (m = 3 > d = 2): push-forward of e^{-eta^T S eta/4} under M^T
# has density proportional to e^{-zeta^T E zeta/4}, E = (M^T S^{-1} M)^{-1}.
Mr = np.array([[1.0, 0.2], [0.3, -1.1], [0.5, 0.7]])
Xr = np.array([[1.2, 0.1, 0.0], [0.1, 0.9, 0.2], [0.0, 0.2, 1.5]])
Sr = Xr @ Xr.T + 0.5 * np.eye(3)
Er = np.linalg.inv(Mr.T @ np.linalg.inv(Sr) @ Mr)
nvec = np.linalg.svd(Mr.T)[2][-1]
pinv = Mr @ np.linalg.inv(Mr.T @ Mr)
marg = []
for zeta in [np.array([0.0, 0.0]), np.array([1.0, -0.5]), np.array([-0.7, 1.9]), np.array([2.0, 1.0])]:
    e0 = pinv @ zeta
    dens = quad(lambda t: math.exp(-float((e0 + t * nvec) @ Sr @ (e0 + t * nvec)) / 4), -np.inf, np.inf)[0]
    marg.append(dens / math.exp(-float(zeta @ Er @ zeta) / 4))
check(max(marg) / min(marg) - 1 < 1e-9, "rectangular push-forward marginal has exponent zeta^T E zeta / 4")
results["G_additive_noise_rigidity_cauchy"] = {"asymmetric_exponential_noise": asym_rows, "rectangular_marginal_ratio_spread": max(marg) / min(marg) - 1, "fourier_identity": ft_rows, "mu_R": muR,
                                              "norm_squared": normG, "lower_bound": lb_rows}


# ---------------------------------------------------------------------------
# H. Admissible bandwidths and the kEDMD hypothesis (Section 7)
# ---------------------------------------------------------------------------
def min_eig(X):
    return float(np.linalg.eigvalsh(0.5 * (X + X.T))[0])


def iso_threshold(A, G, factor):
    """sup{s >= 0 : s (A + A^T) <= factor * G}, by bisection (concave constraint)."""
    S = A + A.T
    if np.linalg.eigvalsh(S)[-1] <= 0:
        return float("inf")
    lo, hi = 0.0, 1.0
    while min_eig(factor * G - hi * S) >= -1e-14:
        hi *= 2
        check(hi < 1e12, "threshold finite")
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if min_eig(factor * G - mid * S) >= -1e-14:
            lo = mid
        else:
            hi = mid
    return lo


I2 = np.eye(2)
s4, s2 = iso_threshold(A, I2, 4.0), iso_threshold(A, I2, 2.0)
check(abs(s4 - 4 / 3) < 1e-10 and abs(s2 - 2 / 3) < 1e-10, "isotropic thresholds 4/3, 2/3")
lam_closed = 4 / np.linalg.eigvalsh(A + A.T)[-1]                 # (63) with G = I
check(abs(s4 - lam_closed) < 1e-10, "closed form (63)")
Bs = np.array([[0.0], [1.0]])
s4s, s2s = iso_threshold(A, Bs @ Bs.T, 4.0), iso_threshold(A, Bs @ Bs.T, 2.0)
check(abs(s4s - 8 / 21) < 1e-10 and abs(s4s / s2s - 2) < 1e-9, "singular-noise threshold 8/21")
# Scalar OU: dX = a X dt + b dW. Threshold 2 b^2 / a for a > 0, none for a <= 0.
check(iso_threshold(np.array([[-0.7]]), np.array([[1.0]]), 4.0) == float("inf"), "stable scalar OU never binds")
check(abs(iso_threshold(np.array([[0.5]]), np.array([[0.3 ** 2]]), 4.0) - 2 * 0.09 / 0.5) < 1e-10, "unstable scalar 2b^2/a")
Sig = solve_continuous_lyapunov(A, -I2)
ray_rows = []
for c in [0.01, 1.0, 4.0, 100.0, 1e4]:
    sl = min_eig(4 * I2 - (A @ (c * Sig) + (c * Sig) @ A.T))
    ray_rows.append({"c": c, "min_eig_sharp_slack": sl})
    check(sl > 0, "Lyapunov ray admissible")
# Unstable-mode cap (61): A = diag(0.5, -1), B = I; w = e1, Re lambda = 0.5.
Au = np.diag([0.5, -1.0])
for p11 in [1.0, 4.0, 4.0 + 1e-6, 5.0]:
    P = np.diag([p11, 1.0])
    ok = min_eig(4 * I2 - (Au @ P + P @ Au.T)) >= -1e-12
    check(ok == (p11 <= 2 * 1.0 / 0.5 + 1e-12), "unstable-mode cap w^*Pw <= 2|B^T w|^2/Re lambda")
ts = [0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 3.0]
Qs = {t: 0.5 * (gramian(A, I2, t) + gramian(A, I2, t).T) for t in ts}


def exact_norm(P, M, Q):
    S = P + 4 * Q
    E = np.linalg.inv(M.T @ np.linalg.inv(S) @ M)
    return (np.linalg.det(P) / np.linalg.det(S)) ** 0.25 * (np.linalg.det(E) / np.linalg.det(P)) ** 0.25


table = []
for s2v in [0.5, 2 / 3, 1.0, 4 / 3, 1.5, 2.0, 4.0]:
    P = s2v * I2
    row = {"sigma2": s2v,
           "published_rule_(31)": min_eig(2 * I2 - (A @ P + P @ A.T)) >= -1e-12,
           "sharp_rule_(29)": min_eig(4 * I2 - (A @ P + P @ A.T)) >= -1e-12,
           "invariant_at_t": []}
    for t in ts:
        M = expm(A * t)
        ok = min_eig(P + 4 * Qs[t] - M @ P @ M.T) >= -1e-12
        row["invariant_at_t"].append(ok)
        if ok:
            check(abs(exact_norm(P, M, Qs[t]) - math.exp(t)) < 1e-8 * math.exp(t), "exact norm e^t")
    if row["sharp_rule_(29)"]:
        check(all(row["invariant_at_t"]), "sharp rule implies every sampling time")
    else:
        check(not row["invariant_at_t"][0], "violation detected at the shortest step")
    table.append(row)
first_ok = {r["sigma2"]: next((t for t, ok in zip(ts, r["invariant_at_t"]) if ok), None) for r in table}
check(first_ok[1.5] == 0.5 and first_ok[2.0] == 1.0 and first_ok[4.0] == 2.0, "Table 1 sampling entries")
results["H_admissible_bandwidths"] = {
    "isotropic_threshold_sharp": s4, "isotropic_threshold_published": s2,
    "singular_noise_B=e2": {"sharp": s4s, "published": s2s},
    "lyapunov_ray": ray_rows, "sampling_times": ts, "table": table,
    "first_invariant_sampling_time": {str(k): v for k, v in first_ok.items()},
}

# ---------------------------------------------------------------------------
# I. Figure
# ---------------------------------------------------------------------------
Sigma = solve_continuous_lyapunov(A, -I2)
limit_ratio = float(np.linalg.det(I2 / 2 + Sigma) ** (-0.25) / 2)
results["I_fixed_observable_asymptotic_ratio"] = limit_ratio
if not ARGS.no_figure:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "pdf.fonttype": 42, "svg.hashsalt": "gk",
                         "path.simplify": False})
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 4.2), layout="constrained")
    ss = np.linspace(0, 24, 260)
    tsv = np.array([threshold(s) for s in ss])
    axs[0].fill_between(ss, tsv, 0.85, color="#d4d0a5", alpha=.65, label="Invariant at this sampling interval")
    axs[0].fill_between(ss, 0, tsv, color="#bc7893", alpha=.30, label="Not invariant")
    axs[0].plot(ss, tsv, color="#76456d", lw=2.2)
    axs[0].axvline(4, color="#9d642f", ls=":", lw=1.8)
    axs[0].axvline(6, color="#386d64", ls="--", lw=1.4)
    axs[0].text(4.2, 0.80, "earlier sufficient\nthreshold s = 4", color="#9d642f", fontsize=8, va="top")
    axs[0].text(6.2, 0.62, "sharp all-time\nthreshold s = 6", color="#386d64", fontsize=8, va="top")
    axs[0].set(xlabel="Shear strength s", ylabel="Sampling interval t", xlim=(0, 24), ylim=(0, .85),
               title="A. Invariance boundary (Brownian covariance rate I)")
    axs[0].legend(loc="lower right", fontsize=7.8, frameon=False)
    times = np.linspace(0, 3.0, 181)
    rat = []
    for t in times:
        M = expm(A * t)
        H = I2 / 2 + gramian(A, I2, t) - M @ M.T / 4
        rat.append(float(np.linalg.det(H) ** (-.25) / 2))
    check(abs(rat[0] - 1) < 1e-12, "figure normalisation at t = 0")
    axs[1].plot(times, rat, color="#76456d", lw=2.2, label="e⁻ᵗ ||Kᵗ f|| / ||f||")
    axs[1].axhline(limit_ratio, color="#386d64", ls="--", label=f"Exact limiting ratio ≈ {limit_ratio:.3f}")
    axs[1].set(xlabel="Time t", ylabel="Norm after removing the eᵗ growth factor", ylim=(0, 1.05),
               title="B. A fixed Gaussian observable grows at rate eᵗ")
    axs[1].legend(loc="upper right", fontsize=8, frameon=False)
    fig.savefig(OUT / "figures" / "invariance_and_norm.pdf", metadata={"CreationDate": None})
    fig.savefig(OUT / "figures" / "invariance_and_norm.png", dpi=180)
    plt.close(fig)
    results["figure"] = ["figures/invariance_and_norm.pdf", "figures/invariance_and_norm.png"]

results["environment"] = {"python": platform.python_version(), "numpy": np.__version__,
                          "scipy": scipy.__version__, "matplotlib": __import__("matplotlib").__version__,
                          "optimize_flag": sys.flags.optimize}
results["status"] = "all checks passed"
(OUT / "verification_results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: results[k] for k in ["status", "environment"]}, indent=2))
print("Gamma_{I,1/10} =", Gamma, "; bound coefficient =", coef_bound, "; ratio =", coef_bound / Gamma)
