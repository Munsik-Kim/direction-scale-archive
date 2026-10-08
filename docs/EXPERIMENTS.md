# Experiments: questions, comparisons, outcomes

The experiments are grouped by scientific purpose. Stage IDs connect to evidence files; they are not independent replications. “Read” and “saved-data reaggregated” refer to this closeout, not a new historical run.

## 1. Was basic recall learnable before testing scale?

**Why:** a retrieval model must first learn the basic task before failures can diagnose scale mediation. **Comparison:** early Recall/DSR and frozen-routing diagnosis. **Actual scope:** bounded preliminary runs, preserved as initial attempts; full raw training reconstruction is not part of this public closeout. **Result:** E05/D5 shortfalls and original_full_G0_passed=false remain in the existing proof/source summaries. **Limit:** scale mechanism unjudged, rather than a proof that retrieval cannot be learned. This entry is report-only; old_DSR_confirmations=NOT_RUN.

## 2. Can shared scale delay correction under explicit assumptions?

**Why:** isolate ranking from concentration with a tractable population model. **Comparison:** direct beta joint versus fixed-scale Copy-MSE, an explicit initialization box; GF versus actual Cartesian GD at separately specified budgets. **Scale:** 27 prescribed GF paths across nine initializations; 36 stored Cartesian GD paths; separate exact-real finite-budget arguments. **Result:** sharp GF leading log-time coefficient, fixed-scale polynomial correction and conditional population-risk separation. The reference c≈0.51261834895 belongs to the reference initialization. Common evaluation-scale risk and raw-scale risk disagree: 54/72 stored raw contrasts favor Joint. **Limit:** exact stated key/readout/population/coordinate assumptions; no arbitrary-query, sharp GD-escape or Adam transfer theorem. Existing complete English proofs are preserved, not newly reviewed.

Sources: [uniform GF records](../results/selected/restricted_uniform_gf.csv), [GD summaries](../results/selected/restricted_gd_summary.csv), [risk contrasts](../results/selected/restricted_gd_risk_contrasts.csv), [proof supplement](../manuscript/supplement/PROOF_SUPPLEMENT_EN.md).

## 3. Does the ordering/risk distinction survive learnable Q and K?

**Why:** move beyond independently parameterized scalar query angles. **Comparison:** learned Q/K matrices, joint versus fixed scale, two prescribed finite-query runs. **Scale:** separate small four-dimensional matrix bridge; its matrix learning rates are not the theorem's rho. **Result:** fixed reached 99% correct ranking at 8,250 updates, joint at 10,000 and 9,750, while joint had lower final raw risk. Stored hard-risk area contrasts are positive in both development runs. **Limit:** final risk and correction time differ; two chosen models do not establish a seed-population effect or sharp law for free Q/K.

Source: [stored bridge comparison](../results/selected/learnable_qk_bridge_areas.json); event/update details remain historical manuscript evidence, not recomputed from complete raw histories here.

## 4. Does scale freezing improve actual Swin training?

**Why:** test native pretrained attention in a practical classification task. **Comparison:** the first pilot had six runs (two seeds, Native/Hold/Balanced); the later natural-sampling NCC/HCC comparison used common clipping and two training seeds. **Scale:** Swin V2 Tiny, Waterbirds Train 4,795 / Val 1,199. Each later seed has two 1,000-update runs, batch 64, evaluation at 11 registered nodes, full Hard census 240 plus fixed Easy probe 96.

**Result:** pilot integrated validation Hard CE favored Hold (Native−Hold≈+.058145,+.469775), but final WGA favored Native in both seeds. In the later common-clipping policy, exact training Hard error-area contrasts are +37/25760 and −99/51520. Hold's training benefit does not replicate. At k1000, HCC has better validation WGA in both seeds; NCC has better actual validation-frequency accuracy. Group changes and confidence must be separated from training fit.

**Limit:** first-pilot and common-clipping policies/evaluation sets differ; data conflict is not negative attention gap; native capped log-scale, relative bias, CE, AdamW and learned readout differ from the theorem. No p-value, equivalence, step-saving percentage or “benign theory regime” is inferred.

Sources: [pilot groups](../results/selected/swin_pilot_validation_groups.csv), [1103 counts](../results/selected/swin_1103_train_hard_counts.csv), [1104 counts](../results/selected/swin_1104_train_hard_counts.csv), [summary](../results/summary.csv).

## 5. Can Qwen follow evidence, and do the specified gain tests reduce confusion?

**Why:** establish interpretable wrong-evidence behavior, then distinguish an input effect from scale effects. **Comparison:** EO/N/C/QO/CF; layer0 score multipliers .8/1/1.25; one all-layer common-radial direction from DEV-N gradient. **Scale:** frozen Qwen3-0.6B revision c1899de289a04d12100db370d81485cdf75e47ca. Final 256 unique questions/doc clusters: SQuAD 164 / QED 92. Original DEV 128 / HELDOUT 128, five variants; later partitions explicitly reused. The gradient study uses 28 layers / 56 gain tensors / 7,168 coordinates, not 7,168 independent experiments.

**Result:** initial HELDOUT N decoys 10 and C 22, EO correct 108 and CF-new correct 107. Layer0 reused HELDOUT N/C decoys: LOW 9/22, BASE 10/22, HIGH 11/23, giving P14=−1/128. The known ten-error subset did not replace the full denominator. STEP15 reused-heldout answer-loss slopes N≈−2.4693639 and C≈−2.97817005 are both negative; EO/CF also decrease. These fail the selected scale-conflict explanation.

**Limit:** greedy output, candidate margin, correct-answer CE and attention gap are different. No actual fine-tuning or free-generation benefit was measured in STEP15. Repeated Vale/London/Alex Voss, static-trial compliance=false, plan changes, contamination UNKNOWN and uncertain annotation rights persist.

Sources: [evidence counts](../results/selected/qwen_evidence_counts.csv), [layer0 counts](../results/selected/qwen_layer0_counts.csv), [all-layer contributions](../results/selected/qwen_radial_layer_contributions.csv), [finite means](../results/selected/qwen_radial_finite_means.csv). Only aggregate reproduction is public.

## 6. Which controlled assumptions change help, delay and output bypass?

**Why:** separate loss, coordinate and information-access changes. **Comparison:** STEP16R A's three losses x direct/log coordinates x nine rates; B's STRONG/WEAK geometry x shared/separate Q x raw Key–Value path on/off x scale policies and rates. **Scale:** A 54 joint cells plus three matched Fixed paths; B 32 logical / 24 unique slow-time paths. Two-query 95/5 population, 16 rows/law, 24 unique raw inputs; B horizon tau 40 and 401 nodes.

**Result:** A 42 correction events and 12 physical-log-horizon censors. In STRONG/R_OFF/rho=.003, sharing Q changes Fixed wrong-rank occupancy .40625→.12125 while Joint stays at 1. R_ON can lower risk without rank correction; other geometry/rate comparisons favor Joint. All factorial contrasts are preserved.

**Limit:** Q sharing changes constraints and cross-gradient paths; raw x^T B sum kV has information unavailable to attention-only V/O. Censor times are not first-hit events or infinite time. No general Transformer phase map or majority-mediator intervention is claimed.

Sources: [A cells](../results/selected/controlled_loss_coordinate_cells.csv), [matched events](../results/selected/controlled_loss_coordinate_ratios.csv), [B comparisons](../results/selected/controlled_geometry_paths.csv). These are stored-table reproductions; full raw A/B histories are not bundled.

## 7. Why did attention-only readout learning miss the bypass target?

**Why:** remove raw Key–Value access and separate readout expressivity from learning. **Comparison:** one fixed head, one learned V/O head, three diverse learned V/O heads, two geometries, two rates and two scale policies. **Scale:** STEP17 has 24 logical paths, twelve new unique Main integrations and six reused parent paths; three designated tight checks were historical validation. STEP18 reads the six H3 Main paths × 401 nodes, with 42 fixed target-norm cells and 14 norm-ball cells. The closeout performs no new integration or optimization.

**Result:** the one-head misranked MSE lower bound is 1/2. P17=0: no registered-grid all-head wrong-rank, both-group-MSE<=.1 bypass. Five other unique H3 paths meet targets after rank correction; STRONG Joint rho=.003 remains misranked with group 2 MSE≈1.84742. At its tau 40 attention, target-norm bracket≈2964.68383 versus actual≈.9921652 differs from zero-residual LS norm≈4342.68. A small resolved residual subspace holds 99.997769% of instantaneous residual energy; factorized gain matrix G is nonzero. Weighted J's V/O/Q/scale local contributions are nonpositive. All 18 cumulative quadratures remain unresolved.

**Limit:** oracle availability is not trained performance. Current-norm insufficiency is a static-attention result, not a future norm ceiling or GF time bound. One WEAK tau 1 case has a target solution within the actual norm ball but the learned coefficients still miss it. Instantaneous subspace share is not causal attribution. No generic Transformer impossibility or renewed toy sweep follows.

Sources: [all 24 path summaries](../results/selected/attention_vo_all_path_summaries.csv), [six numerical state files](../results/selected/states), [norm records](../results/selected/readout_target_norm_records.csv), [unresolved quadratures](../results/selected/readout_quadrature_unresolved.csv).

The final decision is **FREEZE_AND_INTEGRATE_CONTROLLED_SERIES**. See [scope](SCOPE_AND_LIMITATIONS.md) and [data/rights](DATA_AND_LICENSES.md).
