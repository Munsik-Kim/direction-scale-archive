# PDF build and layout check

Status: **PDF_BUILT_RENDER_CHECKED**. Built on **2026-10-22** with Tectonic 0.17.0.

The original 2026-10-08 closeout recorded `PDF_NOT_BUILT` because no TeX compiler was available then. The PDFs below were newly typeset from the archived sources. Attribution and font lookup were updated; mathematical statements, proof bodies, measurements and research decisions were preserved.

| Document | Pages | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| [main.pdf](main.pdf) | 10 | 686465 | `38f7296480e0a077941e8c87467b7f055496f707f24239523f0cb196a48ef7cc` |
| [supplement/TYPESET_PROOF_SUPPLEMENT_EN.pdf](supplement/TYPESET_PROOF_SUPPLEMENT_EN.pdf) | 15 | 138746 | `34309facf4485a37f1989dcc3e1ed9c3bfe06c0cbaed6a480f2c1cae4b6f63a2` |
| [supplement/Scope_Addendum_EN.pdf](supplement/Scope_Addendum_EN.pdf) | 4 | 63328 | `6682f306340b23a2978f5f182f70deb8e8d77c55b90160660d16860bd70bb821` |

All three PDFs identify **Munsik Kim** on the cover and in PDF author metadata. The main report includes the six existing figures. All 29 pages were rendered; contact sheets were inspected for layout, with full-page checks of the report cover, mathematical notation and figures. No blank pages, off-page text, missing-glyph or overfull-box warnings were found. The proof supplement retains two underfull-box notices (loose line spacing) from the preserved typesetting.

This checks the compiled document, not the mathematical validity of its claims or external peer review. Research remains **CLOSED / ARCHIVED_RESEARCH_RECORD**; unresolved integrals and third-party annotation rights retain their recorded status.

## Rebuild

Use an already installed XeLaTeX or Tectonic engine and a new output directory:

~~~bash
bash manuscript/build.sh /tmp/direction-scale-pdf-NEW_ID
~~~

The script disables external shell commands. Tectonic may fetch TeX resource files on first use. It does not install an engine, download a model, train, run inference, integrate trajectories or optimize a readout. Font fallbacks refer to standard TeX font files rather than a private font path.

## Source identities

| Source | SHA-256 |
| --- | --- |
| [main.tex](main.tex) | `a389bc942a12820056d52ec1b9e2e9dd8b3417389be090d41c695806c598d668` |
| [TYPESET_PROOF_SUPPLEMENT_EN.tex](supplement/TYPESET_PROOF_SUPPLEMENT_EN.tex) | `f560aa24de969096731f8e5e3a60e404db4ba57266f47d652d55b02d3804a2df` |
| [Scope_Addendum_EN.tex](supplement/Scope_Addendum_EN.tex) | `4787a50669d44d697a9636c0c53fbfcd0ddfc5b7802753797c9616afce05d570` |
