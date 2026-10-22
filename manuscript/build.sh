#!/usr/bin/env bash
set -euo pipefail

if (( $# > 1 )); then
  echo "Usage: bash manuscript/build.sh [OUTPUT_DIRECTORY]" >&2
  exit 2
fi
source_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
output_dir="${1:-$source_dir}"

if command -v xelatex >/dev/null; then
  engine=xelatex
elif command -v tectonic >/dev/null; then
  engine=tectonic
else
  echo 'PDF_NOT_BUILT: XeLaTeX or Tectonic is required. No installation or experiment is performed.' >&2
  exit 2
fi
mkdir -p -- "$output_dir"
output_dir="$(cd -- "$output_dir" && pwd)"
mkdir -p -- "$output_dir/checks" "$output_dir/supplement"

build_document() {
  local directory="$1" stem="$2" destination="$3"
  (
    cd -- "$directory"
    if [[ "$engine" == xelatex ]]; then
      for pass in 1 2; do
        xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error \
          -output-directory="$destination" "$stem.tex" \
          > "$output_dir/checks/$stem-$pass.log" 2>&1
      done
    else
      tectonic --untrusted --keep-logs --outdir "$destination" "$stem.tex" \
        > "$output_dir/checks/$stem-tectonic.log" 2>&1
    fi
  )
}
build_document "$source_dir" main "$output_dir"
build_document "$source_dir/supplement" TYPESET_PROOF_SUPPLEMENT_EN "$output_dir/supplement"
build_document "$source_dir/supplement" Scope_Addendum_EN "$output_dir/supplement"
echo "Built report and preserved supplements with $engine in $output_dir."
echo 'Typesetting only; no scientific computation was launched.'
