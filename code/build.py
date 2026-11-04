#!/usr/bin/env python3
"""Build manuscript.pdf from manuscript.md with Pandoc and a XeTeX engine.

Uses xelatex when it is installed, otherwise tectonic (the XeTeX-based engine).
Intermediate files (LaTeX source and logs) go to --build-dir, by default a new
temporary directory; the PDF is written to --output (default: manuscript.pdf
beside manuscript.md).  The manuscript and figures are read only.

Usage: python3 code/build.py [--output PATH] [--build-dir DIR]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(args, cwd, log):
    res = subprocess.run(args, cwd=cwd, text=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    Path(log).write_text(res.stdout, encoding="utf-8")
    if res.returncode:
        raise RuntimeError(f"command failed ({res.returncode}): {args}\n{res.stdout[-8000:]}")
    return res.stdout


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--output", type=Path, default=ROOT / "manuscript.pdf")
    ap.add_argument("--build-dir", type=Path, default=None)
    args = ap.parse_args()
    if shutil.which("pandoc") is None:
        raise SystemExit("Required executable not found: pandoc")
    engine = "xelatex" if shutil.which("xelatex") else ("tectonic" if shutil.which("tectonic") else None)
    if engine is None:
        raise SystemExit("Neither xelatex nor tectonic is installed")
    build = (args.build_dir or Path(tempfile.mkdtemp(prefix="gk_build_"))).resolve()
    build.mkdir(parents=True, exist_ok=True)
    src = ROOT / "manuscript.md"
    tex = build / "manuscript.tex"
    run(["pandoc", str(src), "-f", "markdown+tex_math_single_backslash", "-s",
         "--number-sections", "-t", "latex", "--resource-path", str(ROOT),
         "-V", "graphics=true", "-o", str(tex)], ROOT, build / "pandoc.log")
    latex = tex.read_text(encoding="utf-8").replace(
        "\\begin{document}", "\\graphicspath{{" + ROOT.as_posix() + "/}}\n\\begin{document}", 1)
    tex.write_text(latex, encoding="utf-8")
    for n in (1, 2):
        if engine == "xelatex":
            run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", tex.name], build, build / f"tex-{n}.log")
        else:
            run(["tectonic", "-X", "compile", "--keep-logs", tex.name], build, build / f"tex-{n}.log")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(build / "manuscript.pdf", args.output)
    log = (build / "manuscript.log").read_text(errors="replace") if (build / "manuscript.log").exists() else ""
    record = {"engine": engine, "source_sha256": hashlib.sha256(src.read_bytes()).hexdigest(),
              "pdf": str(args.output), "pdf_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
              "build_dir": str(build),
              "warnings": [l for l in log.splitlines() if "Overfull" in l or "Missing character" in l
                           or "undefined" in l.lower()]}
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
