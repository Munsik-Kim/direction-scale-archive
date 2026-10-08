#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
command -v xelatex >/dev/null || { echo 'PDF_NOT_BUILT: XeLaTeX unavailable. No installation or experiment is performed.' >&2; exit 2; }
mkdir -p checks
for n in 1 2; do
  xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex > "checks/main_$n.log" 2>&1
done
(
  cd supplement
  for stem in TYPESET_PROOF_SUPPLEMENT_EN Scope_Addendum_EN; do
    for n in 1 2; do
      xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error "$stem.tex" > "../checks/$stem-$n.log" 2>&1
    done
  done
)
echo 'Built source documents only; no scientific computation was launched.'
