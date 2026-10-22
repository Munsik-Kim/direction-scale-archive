# Data, provenance and redistribution boundaries

This public payload is a selected research record. Permission to publish it does not establish permission to redistribute every third-party dataset or implementation used in historical experiments.

| Material | Historical source / recorded rights status | Public payload | Excluded |
| --- | --- | --- | --- |
| Waterbirds | waterbird_complete95_forest2water2; CUB bird photos composited with Places backgrounds; source-specific rights not newly investigated | Group counts, aggregate CE/error curves, recipe description | All images, filenames/IDs, source photo/background corpus, checkpoints |
| Evidence diagnostic | SQuAD 1.1 train and QED train; historical card records SQuAD CC-BY-SA-4.0 attribution; QED Wikipedia source and annotation rights are distinct, annotation license UNVERIFIED | Counts, condition/placement methodology, model revision, layer-level numeric sums | Questions, excerpts, answers, aliases, completions, offsets and reconstructable token IDs |
| Qwen / Swin | Official pretrained checkpoints; unchanged recorded identity | Aggregate measurements and parameterization description | Model weights, tokenizer cache, original implementation copies, optimizer states |
| Controlled population | Authored two-query mathematical law with independent sign Values | Specification, small synthetic W/beta/v/o states, numerical summaries, selected authored functions | Dense solver cache, full original handoff bundles |
| Existing proofs / editorial prose | Supplied approved manuscript and authored proof/scope supplements | Public-copy sources and existing assumptions | Private review history, internal locators, delivery receipts |
| Figures | Regenerated from selected numerical tables/arrays | Six PNG charts; standard installed fonts used to render | Standalone font files |

## Dataset meaning and scale

**Waterbirds.** Input is an RGB image; target y is bird type (0 landbird, 1 waterbird), while a is background (0 land, 1 water). Aligned groups have y=a; conflicting groups have y!=a. These are metadata groups, not posterior difficulty labels or certified attention gaps.

| (y,a) | Training | Validation |
| --- | ---: | ---: |
| 00 | 3498 | 467 |
| 01 | 184 | 466 |
| 10 | 56 | 133 |
| 11 | 1057 | 133 |
| Total | 4795 | 1199 |

Common-clipping training evaluated all 240 Hard images and only a fixed 96-image Easy probe. That 336-image union is a training subset. Each paired seed had two 1000-update runs with effective batch 64, or 128,000 main image exposures in total. Its 33,770 main evaluation image-forwards are repeated computation, not that many unique images. Training fit, group macro, WGA and actual validation-frequency accuracy have different denominators. Official Test was not evaluated.

**Evidence selection.** The final cohort contains 256 unique question/document-cluster pairs: SQuAD-derived 164 and QED-derived 92. DEV 128 and then HELDOUT 128 were the initial operational partitions; STEP14/15 reuse them as observed data. Five variants per question yield 1280 paired inputs, not 1280 independent questions. The original SQuAD-only 128-documents-by-two-questions proposal was changed to the final mixed 256-by-one construction. Static-trial compliance remained false. Contamination in model pretraining is UNKNOWN.

**Controlled task.** Two Queries have masses 19/20 and 1/20. Each has two opposite keys and independent sign Values. Enumerating four Value combinations and two candidate orders produces 16 rows per law, with 24 unique raw inputs across STRONG/WEAK. This is an exact population average, not 16 randomly sampled subjects. STEP18 analyzed six existing H3 paths × 401 states; it created no new trajectory.

## Rights and attribution

The method references preserved in the manuscript credit the original Waterbirds, SQuAD/QED, Transformer and distractor work. Dataset-specific source licenses and annotation permissions are not replaced by a project license. Uncertain QED/SQuAD-derived text is conservatively omitted, including token IDs from which it could be recovered.

The research report and original project material are authored by **Munsik Kim**. Original code is licensed under [Apache-2.0](../LICENSE). The report, proofs, figures, documentation, and original selection/arrangement of public tables and synthetic saved states are licensed under [CC BY 4.0](../LICENSE-PAPER). [LICENSE_SCOPE.md](../LICENSE_SCOPE.md) maps these categories, and [CITATION.cff](../CITATION.cff) supplies citation metadata.

Both licenses permit use, copying, modification and redistribution, including commercial use, subject to their notice and attribution terms. Reuse within these grants does not require separate author permission. Cite Munsik Kim and the report, retain the relevant notices, and identify changes as required.

These project grants do not relicense third-party source text, images, annotations, implementation copies or pretrained weights. Dataset-specific terms remain separate. QED annotation redistribution rights remain **UNVERIFIED**, and the excluded assets listed above are still omitted. No exclusive rights are claimed in unprotected ideas, mathematical methods or facts; applicable legal exceptions and GitHub Terms rights are unaffected.

### Scope inquiries

Use [repository Issues](https://github.com/Munsik-Kim/direction-scale-archive/issues) for questions about the report or license scope. Questions are optional for uses already permitted by the published licenses. Do not post private data; third-party uses must follow the relevant source terms.

The selected model-free aggregates and authored synthetic specifications support the documented reproduction levels. Complete native reruns need separately and legitimately obtained local assets and the original larger records; no download or account access is performed by this payload.
