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

No new MIT, Apache, Creative Commons, or other blanket license is assigned. No verified project license or approved author/affiliation metadata was supplied for this public closeout; therefore LICENSE and CITATION.cff are not fabricated. Access to this record does not itself grant a blanket reuse license. A future placement under an existing repository license would need its scope checked before posting.

Public access and separate permission to copy, modify, redistribute, or use material commercially are distinct. This clarification assigns no license to the project or any individual file. Reproduction commands describe technical capability, not blanket reuse permission. This guidance does not restrict lawful citation, applicable copyright limitations or exceptions, unprotected ideas, mathematical methods or facts, or rights provided by [GitHub's Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#d-user-generated-content), including viewing and forking public repositories.

Code, manuscript/proof expression, figures, aggregate numerical data, and synthetic saved states are separate material categories. These documents do not establish all rights-holders or rights for every file. Neither project guidance nor any future permission for authored material replaces third-party rights in source text, images, annotations, implementation copies or weights.

For proposed manuscript republication, translation or adaptation, figure republication, code/data-bundle redistribution or product incorporation, identify the relevant rights-holder and intended scope wherever separate permission is needed. No such permission is granted here.

### Scope inquiries

Use [repository Issues](https://github.com/Munsik-Kim/direction-scale-archive/issues) for public scope inquiries. This is an intake route, not a verified rights-holder contact or licensing authority. State the files/version, purpose, modification/redistribution plans, and public/commercial scope. Do not post private data or personal information. An inquiry or response alone is not authorization.

The selected model-free aggregates and authored synthetic specifications support the documented reproduction levels. Complete native reruns need separately and legitimately obtained local assets and the original larger records; no download or account access is performed by this payload.
