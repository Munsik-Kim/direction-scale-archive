# Reproduction boundaries

The default workflow uses only this public payload. Run from its root:

~~~bash
python scripts/reproduce_summaries.py --input results --out reproduced
python scripts/reproduce_figures.py --input results --out reproduced/figures
python scripts/verify_public_bundle.py --root .
python -m unittest discover -s tests -v
~~~

The scripts accept the shown arguments; input and output paths may be absolute. Output goes to a new directory, not the immutable selected records. Python 3.11.15, NumPy 1.26.4 and Matplotlib 3.10.9 were used. [requirements-reproduce.txt](requirements-reproduce.txt) records those package versions; installing or upgrading an environment was not part of closeout. The summary and verification commands need NumPy, while figure generation also needs Matplotlib. Pandas, SciPy, PyTorch, Transformers, a GPU and network access are unnecessary.

## Three different levels

| Level | Provided material / computation | Valid claim |
| --- | --- | --- |
| 1. Stored aggregate tables | Native group counts/CE, Qwen condition counts and layer contributions, controlled run summaries | Tables/figures and contrasts can be rebuilt; this does not recover native per-image logits or rerun strict scoring |
| 2. Small synthetic numerical arrays | Six H3 trajectories, 401 stored nodes each, W/beta/v/o packing | Recalculate gaps, population MSE, c, P17 on the registered grid; inspect original readout witnesses and LS representation |
| 3. Historical complete learning / inference | External datasets, model weights, large native gradients, original private inputs and full drivers are omitted | Not performed or validated in this closeout; not a default command, test, build, or CI job |

Levels 1–2 use the published project code and material under [Apache-2.0 / CC BY 4.0](LICENSE_SCOPE.md). Follow the relevant notices and attribution terms. Level 3 assets remain omitted and subject to their separate source terms.

The minimal mathematical STEP17 functions in [experiments/step17/model.py](experiments/step17/model.py) preserve their original formulas with an import-path change. They have no integration driver. The public summary script is a separate arithmetic implementation and does not import that historical model. Training, generation and ODE solvers are intentionally absent from Quickstart.

## What is actually recalculated

- Swin 1103/1104: correct/n → equal-group error → exact Fraction trapezoid over k=0,100,…,1000 → NCC−HCC. Endpoint WGA is re-minimized over four groups; frequency accuracy uses the observed split counts.
- Pilot 1101/1102: saved group CE → full-horizon validation Hard CE contrast; final WGA from correct counts. These policies differ from the later common-clipping recipe.
- Qwen STEP13/14: saved condition counts → integer paired contrast with the fixed denominator 128. Question/answer text is not public, so strict EM token/text scoring is not advertised as raw-reproducible.
- Qwen STEP15: sum all 28 stored layer contributions for each split/condition; finite-displacement plots use original saved means. No backward or new finite probe is run.
- Controlled STEP16R: count status labels and display stored matched-event ratios. A horizon censor is not a correction event or infinite time.
- STEP17/18: evaluate the six grid-state arrays, check 12 first/end states against a separate raw 16-row formula, recompute P17 as a Fraction, and evaluate the old endpoint feasible coefficient. The lower norm bracket is a historical static-solver record, not a newly solved optimum. An SVD LS coefficient is representation, not trained performance.
- The 18 unresolved cumulative quadratures are carried as recorded. They are not recomputed at a new resolution or “fixed”.

NPZ loading uses allow_pickle=False. Arrays contain only numerical synthetic states; no pretrained tensors, sentence token IDs, or optimizer objects.

## Figures and manuscript

The six fixed-topic PNG files are under [manuscript/figures](manuscript/figures). The figure script writes new copies, without selecting favorable cells, seeds, or heads.

The [English report PDF](manuscript/main.pdf), [proof supplement PDF](manuscript/supplement/TYPESET_PROOF_SUPPLEMENT_EN.pdf) and [scope addendum PDF](manuscript/supplement/Scope_Addendum_EN.pdf) were built on 2026-10-22. Sources and checksums are in the [build record](manuscript/PDF_BUILD.md). With XeLaTeX or Tectonic already installed, rebuild into a new directory:

~~~bash
bash manuscript/build.sh /tmp/direction-scale-pdf-NEW_ID
~~~

The script uses XeLaTeX with -no-shell-escape or Tectonic with --untrusted. Tectonic may fetch TeX resource files on first use. The command only typesets the report and preserved supplements; it does not install an engine or launch a scientific experiment. The original closeout's PDF_NOT_BUILT status is retained as history in [STATUS.md](STATUS.md), alongside the completed build.

The closeout tested Quickstart in a disposable directory containing only this payload. Privacy/source transformations and internal absolute-path provenance remain outside the public archive.
