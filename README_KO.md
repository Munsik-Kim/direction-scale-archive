# Shared-Scale Attention의 교정 지연 — 연구 종료 기록

Attention이 잘못된 정보에 계속 집중하는 조건을 제한 모형의 정리와 비교 실험으로 분석했습니다. 증명, 실험 코드, 저장 결과와 실제 Swin·Qwen에서 확인한 한계를 함께 공개합니다.

**저자: Munsik Kim** · v0.6-archive · CLOSED / ARCHIVED_RESEARCH_RECORD · STEP18에서 종료

[보고서 PDF](manuscript/main.pdf) · [코드와 재현 안내](REPRODUCE.md) · [English](README.md)

정보의 순위를 고르는 과정과 그 순위에 강하게 집중하는 정도를 구분했습니다. 제한 모형에서는 공유 scale을 학습할 때 순위 교정이 늦어지는 결과를 얻었지만, 손실·초기조건·학습 경로에 따라 효과가 달랐습니다. 실제 사전학습 Swin·Qwen에서는 scale 고정의 반복 가능한 학습 이점을 입증하지 못했습니다. 확보한 결과와 반대 근거를 보존하고 연구를 종료했습니다.

| 실험군 | 비교와 실제 결과 | 해석의 한계 |
| --- | --- | --- |
| 초기 Recall / DSR | 기본 검색 학습 gate 미확보 | Scale 기제를 판정할 수 없었음 |
| 제한 이론 / GD | 명시 초기조건·직접 beta·Copy-MSE의 지연 및 별도 유한예산 결과 | 일반 Transformer·AdamW 정리가 아님 |
| 학습 가능한 QK Bridge | Joint의 순위 교정은 늦지만 최종 raw risk는 낮음 | 시간·누적 손실·최종 손실을 구분 |
| Swin common clipping | Seed 1103 +37/25760, Seed 1104 −99/51520 | HOLD의 Training 이점 부호 미재현 |
| Qwen 근거 선택 / 두 개입 | 당시 HELDOUT decoy N 10 / C 22; P14=−1/128; STEP15 N/C 손실 동반 감소 | 입력 혼동 효과와 Scale 기제는 별개 |
| STEP16R 통제 비교 | 손실·좌표·기하·Q 공유·추가 raw Key–Value 경로에 따라 상충 | 별도 우회 경로를 일반 V/O로 부르지 않음 |
| STEP17–18 Attention-only V/O | P17=0; 목표 계수 norm 약2964.68, 실제 약0.992; 누적 분해 18건 미해결 | 표현 가능성이 학습 도달·영구 고착을 뜻하지 않음 |

[실험 목적·규모·반대 결과](docs/EXPERIMENTS.md), [주장 범위](docs/SCOPE_AND_LIMITATIONS.md), [수치표](results/summary.csv), [근거 연결표](results/evidence_index.csv)를 함께 보세요. 원고는 [영문 종료판 TeX](manuscript/main.tex)이며 기존 [완전 증명 부록](manuscript/supplement/PROOF_SUPPLEMENT_EN.md)을 보존했습니다.

**영문 종료판 PDF 10쪽과 기존 부록 15쪽·4쪽을 실제 조판하고 페이지를 확인했습니다.** [빌드·화면 검토 기록](manuscript/PDF_BUILD.md)에 원고와 PDF의 해시를 남겼습니다. 수식·증명·실험 결과는 보존했습니다.

저장자료 재현은 다음 명령으로 합니다.

~~~bash
python scripts/reproduce_summaries.py --input results --out reproduced
python scripts/reproduce_figures.py --input results --out reproduced/figures
python scripts/verify_public_bundle.py --root .
~~~

명령은 모델 추론·학습·ODE 적분·최소-norm 재최적화를 호출하지 않습니다. Swin은 집단 정답 수, Qwen은 count·층별 집계표 수준의 재현입니다. 통제 모형은 작은 W/beta/v/o 배열에서 손실과 등록 지표를 재계산합니다. [재현 범위](REPRODUCE.md)에 세 수준을 구분했습니다.

## 인용 안내

저자는 **Munsik Kim**입니다. [CITATION.cff](CITATION.cff)에서 인용 메타데이터를 제공합니다.

> Kim, Munsik. (2026). *Correction Delays in Shared-Scale Attention*. 연구 아카이브, **v0.6-archive**. 공개일 **2026-10-08**. [저장소](https://github.com/Munsik-Kim/direction-scale-archive); [고정 기록: 커밋 e6b1b5aad87b48d9775ef4136a018ded277cfa81](https://github.com/Munsik-Kim/direction-scale-archive/tree/e6b1b5aad87b48d9775ef4136a018ded277cfa81).

`v0.6-archive`는 문서 버전이며 Git 태그나 GitHub Release를 뜻하지 않습니다. 재사용과 출처 표시 조건은 [라이선스 범위](LICENSE_SCOPE.md)에 정리했습니다.

Waterbirds 이미지, SQuAD/QED 문항·근거·답변·토큰 ID, 모델 Weight, 개인 경로와 비공개 배송 기록은 공개 묶음에 없습니다. QED annotation 권리는 미확인 상태를 유지합니다. 원본 코드는 [Apache-2.0](LICENSE), 논문·증명·그림·공개 수치 자료는 [CC BY 4.0](LICENSE-PAPER)을 적용합니다. 각 라이선스의 고지·출처 표시 조건에 따라 수정·재배포·상업적 이용이 가능합니다. [데이터와 공개 범위](docs/DATA_AND_LICENSES.md)를 확인하세요.

새 실험·학습·ODE 적분·자동 후속은 없습니다. 이 표시는 이 연구의 종료 상태이며, GitHub 저장소를 읽기 전용으로 바꾸거나 다른 연구자의 독립적인 후속 연구를 금지한다는 뜻은 아닙니다.
