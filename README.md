# 우리 사이, 그 이상

캠퍼스의 협력 프로젝트에서 만난 다섯 인물과 관계를 쌓는 **한국어 미연시**입니다. 대화와 선택이 호감·신뢰, 개인 루트와 결말에 이어집니다. 공개 소스는 **0.6.11-test**입니다.

## 주요 기능

- **공통 스토리와 개별 루트** — CH01부터 CH07까지의 공통 이야기와 다섯 인물의 개별 루트를 제공합니다.
- **호감·신뢰와 엔딩** — 선택에 따라 관계와 분기가 달라지고, 해금한 엔딩을 엔딩 다이어리에서 확인합니다.
- **게임 속 스마트폰** — 단체방과 개인 메시지가 장면에 맞춰 열리고 일부 대화에서는 직접 답장을 고릅니다.
- **인물 스크랩북·갤러리** — 만난 인물의 프로필, 선택으로 해금한 메모와 장면 일러스트를 모아 봅니다.

## 기술 스택

| 영역 | 사용 기술 |
| --- | --- |
| 게임 엔진 | Ren’Py 8.5.3 · Python · Ren’Py 스크린 언어 |
| 연출·데이터 | `.rpy` 대본 · JSON 관계 및 이미지 등록 자료 · PNG/WebP · OGG |
| 검증 | Ren’Py 네이티브 테스트와 Lint |

## 실행 방법

1. 이 저장소를 클론하거나 ZIP으로 내려받아 압축을 풉니다.
2. **Ren’Py 8.5.3 SDK**를 설치하고 런처 설정의 **프로젝트 디렉터리**를 이 저장소 루트로 지정합니다. [Ren’Py 8.5.3 SDK](https://www.renpy.org/release/8.5.3)
3. 프로젝트 목록에서 `renpy_project`를 선택하고 **Launch Project**를 누릅니다. [Ren’Py 런처 안내](https://www.renpy.org/doc/html/quickstart.html#the-ren-py-launcher)

게임 소스와 실행에 필요한 리소스는 [renpy_project](renpy_project)에 있습니다. 일부 루트의 특수 표정과 일러스트 구간은 제작 중입니다.

## 자료

- [0.6.11 업데이트와 작업 범위](docs/CH07_PRIVATE_STANDING_RELEASE_0.6.11.md)
- [관계와 분기 시스템](docs/RELATIONSHIP_SYSTEM_0.6.md)
- [스마트폰 연출](docs/PHONE_TIMELINE_0.5.md) · [UI 설계](DESIGN.md)
- [이전 UI 작업 기록](https://github.com/hacho1/campus-romance-vn/blob/22d62799b10190f23c22589a5456b3543b3fa8ec/README.md)
