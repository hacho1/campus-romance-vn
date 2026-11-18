# 0.5 배경·음악·효과음 제작 기록

작성일: 2026-11-08. 작업 루트: `D:\CampusRomance_VN`. 기존 배경과 음악은 보존했다. 스탠딩, 히로인 LD/SD는 이 작업에서 생성하지 않았다.

## 배경 4장

완성 이미지 경로는 모두 `renpy_project/game/images/backgrounds/refresh_20261108/` 아래다. GPT 내장 이미지 생성 도구로 각각 제작했다. 인물, UI, 의도한 읽을 수 있는 글자를 넣지 않았으며 기존 캠퍼스 배경의 봄빛·크림·하늘색·분홍색·라벤더 계열에 맞췄다.

| 파일 | 적용 장소 | 화면 구성 |
| --- | --- | --- |
| `bookshop.png` | 원고의 소규모 서점 | 햇살이 드는 독립서점. 왼쪽 계산대, 책 진열대, 중앙 빈 공간. |
| `garden.png` | 저녁 정원·연못·작은 공원 | 노을과 작은 연못, 오른쪽 벤치, 전경 산책로. 낮·밤 장면은 기존 배경을 유지. |
| `gamebooth.png` | 다림의 게임 체험 공간 | 축제 천막, 퍼즐 화면과 컨트롤러, 왼쪽 체험 테이블, 중앙·오른쪽 빈 공간. |
| `roman_room.png` | 로만의 방·책상 | 따뜻한 스탠드 조명과 창밖 밤하늘. 책상·서가·침대와 작은 강아지 인형. |

네 장의 생성 원본은 1672×941이며 `artwork/refresh_20261108/raw/`에 그대로 보관했다. 사용자 지시에 따라 FFmpeg Lanczos 보간으로 최종 1920×1080 PNG를 만들었다. 이는 규격 통일이며 원본에 없는 세부를 새로 복원한 처리가 아니다. 생성 도구 기본 저장 위치에 있던 결과를 D드라이브로 복사했으며 재생성하지 않았다.

전체 영어 프롬프트, 최초 도구 출력 경로, D 원본·최종 경로는 `artwork/refresh_20261108/image_generation.json`에 기록했다. 최종 네 장을 직접 열어 인물 없는 구성, 미래 스탠딩을 위한 여백, 하단 대사창 공간을 확인했다.

`systems/story_draft_runtime.rpy`의 장소 해석만 확장했다. `story_draft_scene()`은 계속 `standing=False`를 사용한다. 로만의 방은 이미 밤빛으로 그려져 있어 조명 레지스트리에 야간 원본 경로를 지정하여 이중 푸른 틴트를 막았다. 낭독·문학 행사장 내부는 이미 존재하는 `presentation` 배경을 재사용하고 행사장 앞·옆·복도는 해당 장소 규칙을 유지했다.

## BGM 2곡: 원본 작곡·악기 합성

외부 음악 서비스의 최신 사용 가능 모델과 가격을 조회했다. 요청당 90초·기악곡 1개 비용 견적은 13.08크레딧, 두 곡 합계 26.16크레딧이었다. 첫 요청은 `Out of credits on pro (monthly) plan in Private workspace.`로 거절되어 접수된 작업은 0건이었다. 두 번째 생성 요청은 제출하지 않았다. 완성 음악을 외부 AI 음악 서비스가 만들었다고 표기하지 않는다.

부모 작업자의 승인에 따라 로컬에서 새로운 악보와 악기 합성으로 제작했다. 외부 녹음·샘플·기존 곡·soundfont를 사용하지 않았다. `tools/create_refresh_audio.cjs`에 악보, 시드, 모델 악기, 믹싱 및 내보내기 과정을 남겼다. 망치로 울리는 현의 비정수 배음과 미세한 디튠, 나일론 현의 Karplus–Strong 발현, 부드러운 패드, 작은 종, 브러시 질감을 조합했다. 단위 악구마다 멜로디·악기·벨로시티·발음 시차가 변한다.

| 등록 키 / 최종 OGG | 악보 | 길이 | 용도 |
| --- | --- | --- | --- |
| `dark` / `dark_pages_loop.ogg` | D단조, 72BPM, 24마디, 185음 | 80초 | 불안·집착·낮고 느린 피아노·Uneasy Silence·희미한 피아노. |
| `meta` / `warm_pages_loop.ogg` | G장조, 84BPM, 32마디, 580음 | 약 91.43초 | Warm Memories, Quiet Reflection 등 축제 이후의 회상. |

최종 파일은 `renpy_project/game/audio/generated_refresh/`에 있다. `data/audio.json`의 기존 `dark`·`meta` 두 등록 항목 첫 경로에 연결했고 이전 대체 파일 목록도 남겼다. 그 외 18개 등록 항목은 백업과 내용이 같다. 두 곡 모두 48kHz 스테레오 Vorbis q5다.

박자에 맞춘 전체 악구 길이를 기준으로 잔향·리버브 꼬리를 처음으로 순환시켰다. 끝 무음을 넣거나 매 반복마다 볼륨을 떨어뜨리지 않는다. 게임의 기존 BGM 재생 함수가 곡 전환 시 fade-in/out을 처리한다. 파일을 두 번 연속 재생해도 음표 잔향이 이어질 수 있도록 원본 신호를 순환 렌더했다.

측정 결과는 두 곡 모두 -21.99 LUFS, 샘플 클리핑 0이다. 인코딩 후 true peak는 각각 -8.80/-10.79dBTP이며, 파일 끝→처음의 최대 채널 샘플 차이는 0.004511/0.002561이다. 이 값은 디코드와 신호 경계 확인 결과이며 사람의 청취로 음악적 이음새를 승인한 결과는 아니다. 실제 청취는 수행하지 않았다. 기악곡임은 사용한 합성 악기 구성상 확정되며 음성·가사 소스를 넣지 않았다.

수정 가능한 원본 악보 JSON, MIDI, 무손실 16비트 PCM 마스터는 `artwork/refresh_20261108/audio/`에 있다. 초기 외부 서비스 요청 프롬프트는 같은 폴더의 `generation_requests.json`, 측정과 파일 SHA는 `audio_render_report.json`에 있다.

## 효과음 4개

`systems/refresh_audio.rpy`의 `refresh_sfx(key, volume=None)`로 한 번 재생한다. 현재 효과음 채널을 사용하고, 누락되거나 알 수 없는 키이면 오류 없이 `False`를 반환한다. 기본 볼륨은 게임 효과 0.70, 심장 소리 0.58이다.

| 키 / WAV | 길이 | 소리 | 제안한 원고 연결점 |
| --- | --- | --- | --- |
| `game_start` / `game_start.wav` | 1.15초 | 작은 C–E–G 종의 시작음 | CH06_DARIM SOURCE L48 시작, L81 재시작 |
| `game_fail` / `game_fail.wav` | 0.85초 | 짧게 내려가는 E–E♭–C 음형 | CH06_DARIM L59 실패 |
| `game_clear` / `game_clear.wav` | 1.65초 | C–E–G–C의 가벼운 완료음 | CH06_DARIM L89 클리어 |
| `heartbeat` / `heartbeat.wav` | 2.25초 | 두 차례 낮고 부드러운 심장 박동 | R06 L689의 첫 roman_obsess_01, L1813의 첫 roman_obsess_02 |

심장 소리는 한 호출 안에 두 번의 박동이 포함되어 있다. 부모 작업자가 `tools/apply_presentation_cues.py`로 위 Darim 네 cue와 R06 두 cue를 실제 연결했다. L689는 원고 위험 누적 D가4 이상일 때만, 배드 장면 L1813은 해당 장면에서 한 번만 재생한다. 음악·효과음 연결을 위해 대사와 선택 문구를 바꾸지 않았다.

WAV는 모두 48kHz 스테레오 16비트 PCM, 처음 5ms와 끝 40ms에 짧은 페이드를 적용했다. 게임 효과 peak 약 -5.04dBFS, 심장 소리 약 -7.96dBFS이며 시작·끝 신호 차이는 0이다. 악기 합성 코드로 만든 원본 효과음이고 외부 파일을 가져오지 않았다.

## 재현과 검증

- 생성·렌더: `node D:\CampusRomance_VN\tools\create_refresh_audio.cjs <기존 ffmpeg.exe 절대 경로>`
- 읽기 전용 자산 점검: `node D:\CampusRomance_VN\tools\audit_refresh_assets.cjs <기존 ffmpeg.exe 절대 경로>`
- 최종 자산 10개의 크기·SHA·PNG 해상도·디코드·음악 등록·기존 음악 항목 보존: `artwork/refresh_20261108/asset_manifest.json`
- 원본 백업: `backups/refresh_0_5_20261108/assets/audio.json`, `story_draft_runtime.rpy`

추가로 `tests/ui_refresh_050/assets_native/README.md`의 격리 SDK 자산 실행 검사를 완료했다. 1case/11 assertions PASS. 네 배경의 실제 PNG 디코드·map/light/tint와 두 BGM·네 효과음의 SDK PCM 디코드 및 재생 위치를 확인했다. 음원은 비활성화하지 않고 SDL dummy 오디오 장치에만 출력했으며 실제 스피커나 사용자 전경 앱을 사용하지 않았다. 관련15개 생산 파일과 fixture의 SHA도 일치한다. 정원·게임부스의 엔진 스크린샷을 저장하고 직접 확인했다.

도구 설치는 추가로 하지 않았다. 생성·최종 이미지, 음악 마스터·악보·효과음, 도구 및 점검 결과는 모두 D드라이브에 보관했다. 이 문서의 자산 검사와 별도로 실제 Ren'Py 전체 실행·저장·폰 UI 회귀 검사는 부모 작업자의 통합 QA에서 진행한다.
