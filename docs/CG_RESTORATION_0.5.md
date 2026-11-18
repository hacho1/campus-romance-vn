# 로만 시크릿 CG · 0.5 보정본

원본 `renpy_project/game/images/cg/endings/roman_secret.png`는 교체하지 않고 보관했습니다. SHA256은 `fcd225e18a9bcb1aaba55de2aff2d5ebc2c12a24fed5f62a9d6f626d3eea65b1`, 원래 크기는 1344×768입니다.

이번 사용 파일은 `renpy_project/game/images/cg/endings/roman_secret_hd.png`입니다. built-in imagegen으로 원본을 참조해 선명도·선 복원 보정을 요청했고, 생성된 1672×941 파일을 Lanczos 방식으로 3840×2160에 맞췄습니다. 생성 원본은 `design_docs/artwork/refresh_20261108/roman_secret_restored_native.png`에 따로 있습니다. 출력 크기 표준화가 원본에 없던 실제 4K 세부 정보를 보장하는 것은 아니며, 생성 보정이므로 선과 미세한 디테일은 원본과 다를 수 있습니다.

## 최종 프롬프트

> High-fidelity restoration/upscale of this exact existing anime visual-novel CG, NOT a new illustration or a redesigned scene. The character is an adult university student age 20. Preserve the exact identity, adult facial proportions, expression, eyes, silver-lavender hair, cat ears, hairpins, bell and black bows, cream dog-print pajamas, red gift ribbon, fully clothed pose, hands, anatomy, bed folds, lighting, camera angle, composition and original pastel rendering. Do not change or invent any object, expression, clothing, pose or body shape. Only remove softness/compression artifacts and clean the original drawn line edges and very fine fabric/hair details without over-sharpening or changing the watercolor-like colors. Produce the highest-resolution wide landscape version possible for a 3840x2160 visual novel frame. Keep all original important content visible, no zoom, no crop, no added text, no border, no watermark. The result should look like the same original file at better resolution.

## 게임과 앨범

`data/cg_registry.json`의 동일 ID `ending/roman_secret`를 사용합니다. `image`는 보정본, `screen_fit`은 `contain`이고 추가 화면 crop은 없습니다. 본편과 갤러리에서 같은 전체 프레임을 사용합니다. ROMAN과 ENDING 탭에서 같은 해금 상태를 공유하며 각 탭 안에 중복 타일을 만들지 않습니다.

시크릿 완료 기록이 있는 이전 저장은 CG 전용 수집 키가 없더라도 열립니다. 해피 엔딩만 봤거나 시크릿을 완료하지 않은 경우에는 일반 갤러리에서 잠금을 유지합니다. 테스트 챕터 재생의 임시 해금은 실제 앨범에 반영하지 않습니다.

원본으로 되돌리려면 해당 항목의 `image`만 `images/cg/endings/roman_secret.png`로 바꿉니다. 재등록 도구 `tools/register_roman_release.py`는 보정본 파일이 존재하면 보정 경로를 선택하므로 경로 정책도 함께 바꿉니다.
