# 시아 S03–S06·시크릿 원고 적용

확정 원고의 실제 대사·선택·조건 분기를 변환했다. 스탠딩·새 SD/LD 제작은 하지 않는다.
제공된 시크릿 그림만 원고 CG MAIN 위치에서 기존 CG 시스템으로 표시한다.
숫자1/2 원고 예시는 점수로 실행하지 않는다. 실제 5/10 정책은 sia_relationship_choices.json에서 관리한다.
메뉴 ID는 파일 내 발생 순서다. S05 원고의 CHOICE01 중복 표기는 choice01(창작), choice02(발표 연락), choice03(관계)으로 구분한다.
S05 L991의 이미 화해한 경로는 원문에서 참석을 약속하므로 무보상 attend 기록을 남긴다. ELSE 경로에만 지원 선택 메뉴가 있다.
작성 중이다가 지운 주인공의 초안은 발송하지 않고 원문 그대로 일반 대사창에 표시한다. 전화 분기의 합류 상태를 보존해 다음 전환에서 폰이 남지 않게 한다.
S06 해피/배드의 마무리 서사4문장과 시크릿 마무리4문장은 실제 대사창에 출력한다. COMPLETE/다음 챕터 표제는 제작 메타로 보존한다.
재생성은 tools/import_sia_later.py --write 후 tools/import_roman_first.py --phone-cues를 실행한다. 후자는 대사를 다시 만들지 않고 최종 시간·시점 조회만 삽입한다.

## S03

- 원본 SHA256: `6c68264dcfad8314a6489855aca77871b0884aecbcc4619d82e6720ab358d708`
- 실제 대사/서술: 896, 씬: 8, 메뉴: 2, 조건: 0
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\sia_s03.rpy`

### 미제작 그림·표정·연출 콘티

- L1506: [CG 후보] 시아가 처음으로 장난기 없는 눈빛으로 주인공을 바라보는 클로즈업. 평소의 장난스러운 미소가 사라지고 옅은 홍조와 진지한 표정이 나타난다. 주인공 외형은 표시하지 않는다.
- L1895: [연출] 시아의 손이 화면 아래쪽으로 뻗어 오는 1인칭 구도 또는 일반 LD 유지.

## S04

- 원본 SHA256: `d443976ee20d6eeb174c79fea468ec130e4d1d1d974e4507965da7a35d135280`
- 실제 대사/서술: 761, 씬: 8, 메뉴: 3, 조건: 6
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\sia_s04.rpy`

### 미제작 그림·표정·연출 콘티

- L157: [LD] 시아 · 장난스러운 미소
- L201: [표정] 시아 · 당황
- L736: [LD] 시아 · 기본
- L1442: [LD] 시아 · 기본
- L1754: [LD] 시아 · 기본

## S05

- 원본 SHA256: `2dfb897380525e319bd84fc9e5ed48b974e54edd16438b5de844582519ecf1f9`
- 실제 대사/서술: 852, 씬: 8, 메뉴: 3, 조건: 13
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\sia_s05.rpy`

### 미제작 그림·표정·연출 콘티

- L1296: [LD 또는 CG 후보] 시아가 발표장 무대 위에 서 있는 장면.

## S06

- 원본 SHA256: `8612aecd2b65cb1a136e5a35c0f7c3de9d3aee332e2c61b5c0e49c1f0852f0da`
- 실제 대사/서술: 885, 씬: 12, 메뉴: 1, 조건: 3
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\sia_s06.rpy`

### 미제작 그림·표정·연출 콘티

- L496: [LD] 시아 · 기본
- L1416: [표정] 시아 · 홍조
- L1760: [CG 후보] 노을이 지는 공원에서 장난기 없이 환하게 웃는 시아의 근접 구도. 주인공 외형은 화면에 표시하지 않는다.

## SSECRET

- 원본 SHA256: `114493a3a4869a47fc11dcc0488c2f654b0969dd11789b1a7f7805dc0a7de920`
- 실제 대사/서술: 359, 씬: 5, 메뉴: 1, 조건: 0
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\sia_secret.rpy`

### 미제작 그림·표정·연출 콘티

- L366: [CG MAIN] `sia_secret_summer_low_angle`
- L368: [연출]
- L380: [표정 차분 01] 당황
- L457: [CG] `sia_secret_summer_low_angle` 유지 · 표정 차분
- L490: [표정 차분 02] 장난스러운 미소와 옅은 홍조
- L704: [LD] 시아 · 기본 미소 또는 편안한 표정
- L864: [연출] 기존 시아 홍조 LD 또는 짧은 화면 페이드. 포옹 자체를 신규 CG로 제작할 필요는 없다.

