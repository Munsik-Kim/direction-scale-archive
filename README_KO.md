# Shared-Scale Attention의 교정 지연 — 연구 종료 기록

**v0.6-archive · CLOSED / ARCHIVED_RESEARCH_RECORD · STEP18에서 종료**

이 연구는 Attention이 유용한 정보를 **올바른 순위로 고르는 과정**과 현재 순위에 **더 강하게 집중하는 과정**을 구분했습니다. 명시된 제한 모형에서는 공유 Scale을 학습할 때 순위 교정이 늦어지는 정리와 수치 결과를 확보했습니다. 그러나 손실, Scale 좌표, 초기 Key 기하, 학습 가능한 정보 경로가 달라지면 도움과 손해도 달라졌습니다.

실제 사전학습 Swin·Qwen에서는 Scale 고정의 반복 가능한 학습 이점이나 범용적인 Scale 매개 병목을 입증하지 못했습니다. 모든 Transformer에서 불가능하다는 증명도 아닙니다. 연구를 더 확대하지 않고 확보한 결과와 반대 근거를 보존합니다.

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

**새 종료판 PDF는 만들지 못했습니다(PDF_NOT_BUILT).** 현재 환경에 TeX 컴파일러가 없습니다. 과거 PDF를 이름만 바꿔 제공하지 않았으며 새 원고의 페이지 조판은 미검증입니다. 여섯 핵심 PNG 그림은 저장 수치로 재생성하고 열어 확인했습니다.

저장자료 재현은 다음 명령으로 합니다.

~~~bash
python scripts/reproduce_summaries.py --input results --out reproduced
python scripts/reproduce_figures.py --input results --out reproduced/figures
python scripts/verify_public_bundle.py --root .
~~~

명령은 모델 추론·학습·ODE 적분·최소-norm 재최적화를 호출하지 않습니다. Swin은 집단 정답 수, Qwen은 count·층별 집계표 수준의 재현입니다. 통제 모형은 작은 W/beta/v/o 배열에서 손실과 등록 지표를 재계산합니다. [재현 범위](REPRODUCE.md)에 세 수준을 구분했습니다.

Waterbirds 이미지, SQuAD/QED 문항·근거·답변·토큰 ID, 모델 Weight, 개인 경로와 비공개 배송 기록은 공개 묶음에 없습니다. QED annotation 권리는 미확인 상태를 유지합니다. 프로젝트 라이선스·저자 정보도 임의로 부여하지 않았습니다. [데이터와 공개 범위](docs/DATA_AND_LICENSES.md)를 확인하세요.

새 실험·학습·ODE 적분·자동 후속은 없습니다. 이 표시는 연구 종료 상태이며 GitHub 저장소의 archive 설정을 변경했다는 뜻은 아닙니다.
