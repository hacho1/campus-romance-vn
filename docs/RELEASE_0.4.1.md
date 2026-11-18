# 0.4.1 — CH07 시아 메시지 중복 수정

공개 버전은 0.4.1 / build 2026110804입니다. 게임을 종료한 뒤 기존 바탕화면 런처에서 **업데이트 확인 → 설치·업데이트**로 받습니다. 기존 저장을 다시 불러오면 해당 중복 말풍선도 정리됩니다.

## 수정 내용

CH07 SC01 끝과 SC02 시작에서 시아의 「야 / 다들 살아 있냐?」가 각각 전송되어 네 말풍선이 되던 문제를 수정했습니다. 앞 장면에서 한 번만 보내고 다음 장면은 오므의 답장으로 이어집니다.

이미 중복된 상태의 저장을 불러오면 이 장면의 연속 중복 말풍선만 정리합니다. 두 번째 「야」까지만 나온 저장도 처리하며, 읽지 않은 수와 마지막 메시지 키를 함께 맞춥니다. 다른 장면·개인방·발신자의 정상 반복 메시지와 선택·호감도·신뢰도는 건드리지 않습니다.

원고는 보존하고 생성기의 `scene_echoes` 예외를 함께 수정했으므로 재생성해도 중복이 되살아나지 않습니다. 신규 그림은 없습니다.

## 수정 파일

기준 경로: `D:\CampusRomance_VN`.

- `renpy_project/game/routes/chapter07_official.rpy`: SC02의 반복 발송 두 줄 제외.
- `renpy_project/game/systems/phone_system.rpy`: 기존 저장의 해당 중복 이력 복구.
- `renpy_project/game/options.rpy`: 0.4.1 버전.
- `tools/import_ch06_ch07.py`: 반복 장면 생성 예외 및 audit.
- `launcher_publish/prepare_payload.py`: SDK 아이콘 처리 뒤 남은 파일 핸들을 회수해 Windows의 snapshot EXE 교체 잠금 해제. 아이콘·실행 코드 결과는 기존과 동일합니다.
- `docs/CH06_CH07_STORYBOARD_AUDIT.json`, `CH06_CH07_STORYBOARD.md`: 수정 근거·가이드.

변경 전 백업: `backups/phone_scene_echo_20261108`.

## 검증·게시 결과

네이티브 수정 검사 **4개 사례 / 9 SDK assertion PASS**: 새 진행, 격리된 실제 0.4.0 중복/부분 중복 저장 불러오기·재저장·재로드, 정상 반복 보존, unread/마지막 키/수치/선택/플래그/재적용 검증. Lint PASS, fixture와 원본 437개 파일 SHA 대조 일치. 원고·기존 이미지는 바꾸지 않았습니다.

실제 사용자 게임이 별도로 실행 중이어서 자동 저장과 persistent는 작업 시작 해시에서 달라졌습니다. QA는 격리 savedir를 사용했으며 사용자 파일은 복원·덮어쓰기하지 않았습니다. 실제 사용자의 진행 기록을 검사 fixture로 사용하지 않았습니다.

온라인 업로드·활성화 PASS. 기존 1,759조각을 재사용하고 53조각/2,129,408바이트를 새로 올렸습니다. manifest SHA256은 `a1af095b25a6d4c689bbc4250bf24d3c6281a3e1dea5994f27bb5383578d1c8a`입니다. 개인 저장·개인키는 배포하지 않습니다.

공개 HTTPS 사후 검증 **PASS**. production CLI(QA override 없음)가 0.4.1/2026110804와 1,814파일을 확인했습니다. raw manifest 812,917바이트·고정 SHA 서명 RSA 검증, CH07/phone_system RPYC 실제 청크 다운로드·조립 SHA, 공지 두 개의 내용·개수가 일치합니다. 전체 게임 신규 설치는 수행하지 않았습니다.

[통합 QA 보고서](../tests/phone_scene_echo_20261108/README.md) · [공개 검증](../tests/phone_scene_echo_20261108/public-1794123092362/RESULT.json)

게임 파일·공지의 증분 업데이트이며 사이트 코드·런처 EXE 변경은 없습니다. 게시 후 같은 [공개 주소](https://campus-romance-playtest.naiski.chatgpt.site/)에서 새 버전을 확인할 수 있습니다.
