# Common-route standing plan

CH01–CH05 retain their existing authored standing directions. CH06–CH07 now
explicitly opt present characters into the existing PixAI standing system.
No new artwork, dialogue, choices, labels, scores, phone records, CGs or SD
events are introduced by the standing postprocessor.

## Rebuild and check

Use the project Python executable (with `-B -X utf8`) to run:

```text
tools/import_ch06_ch07.py --write
tools/apply_common_staging.py --check
```

For a standing-only refresh of existing generated routes, run
`tools/apply_common_staging.py --write`. Without an option it previews the
change summary. The postprocessor is pure and idempotent and is called by
the importer after generating each chapter. It fails on missing, duplicate
or changed manuscript anchors rather than moving a cue to another scene.
The standing-only command also adds the shared helper's optional arguments.

`story_draft_scene(description, cast=None, standing=False)` keeps the
text-first default used by the Roman and Sia private routes. Only reviewed
CH06–CH07 calls specify `cast=...` and `standing=True`. Each background
resets faces/cast, so every in-person shot supplies its full present cast.
The fresh shot fades in; later arrivals use the existing slide-in API.

## Scene rules

The complete source-line-keyed table is `SCENES` in
`tools/apply_common_staging.py`. `CUES` contains sparse face changes and
arrivals. Managed blocks carry `COMMON STANDING BEGIN/END` comments; removing
those blocks and the explicit scene options exactly restores the prior
chapter content. The script verifies this projection on every run.

| Chapter and section | Standing cast |
| --- | --- |
| CH06 SC01 room / plaza establishing shot | Empty |
| CH06 SC01 booth | Darim, Roman, Harin; Sia and Omu enter at L176/L179 |
| CH06 SC02 plaza / rival booth | Both teams logically present; existing team-shot switching |
| CH06 SC03 booth / entrance / record table / centre | Roman + Darim / Omu + Sia + Harin / Darim / Harin |
| CH06 SC03 rest area | Five heroines |
| CH06 SC04 all five partner branches | Chosen heroine only, including Harin's existing morning flashback |
| CH06 SC05 own booth / rival booth / both booths | Five heroines / Sia + four rivals / both teams |
| CH06 SC06 booth / empty interior / sunset / night | Five / empty / five / five |
| CH06 SC07 room / clubroom / emptied table / walk | Empty / five, then arriving rivals / five after rivals leave / empty |
| CH07 SC01–02 | Empty; messages remain phone conversations |
| CH07 SC03–04 cafe | Five heroines |
| CH07 SC05 recollection and route choice | Empty |
| CH07 SC06 invitation benches | Empty during each private phone invitation |
| CH07 SC06 actual meeting locations | Chosen heroine only; full cast re-established after phone closes |
| CH07 SC07 room and night messages | Empty |

Nine logical cast members never create a nine-person lineup. The existing
`story_shot_members` selects the five-heroines shot or four-rivals shot by
speaker. Sia and the four rivals may share the five-person shot in SC05,
where that is the actual cast. All standings retain the engine's fixed
872-pixel width and automatic speaker brightness.

In CH06 SC07 the first Hyeophap line is spoken from outside the closed
door. `story_offscreen_actor` suppresses that line's automatic standing
addition while the five heroines remain visible. It is cleared at the
following Darim reply; all four rivals enter at the manuscript's arrival.
Chapter entry also clears this transient flag in the shared runtime.

Existing SD/CG production directions in these chapters remain comments.
The postprocessor does not execute or invent any illustrated event. Phone
mode continues to clear the cast and suppress standings, and existing
illustration boundaries remain authoritative. Existing assets provide all
faces; the registry preserves Omu's `direct` neutral base.
