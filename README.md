# The World on Wednesday — 55 Sourced Stories from 25 November 2026 in One Image

[![Competition](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/c/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![Rank](https://make.fun/badge/news-image-20261125/Hagai17/world-on-wednesday/rank.svg)](https://make.fun/c/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![Reward](https://make.fun/badge/news-image-20261125/Hagai17/world-on-wednesday/reward.svg)](https://make.fun/c/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-page broadsheet summing up **Wednesday 25 November 2026**: 55 sourced
stories in 8 sections, every item reported on the day and labelled
**CONFIRMED** or **REPORTED** with its source named.

## What's on the page

- **Three leads with graphics** — two tankers mined in the Strait of Hormuz
  (schematic map), nine dead and 17 trapped in the flooded Bogor gold mine
  (stat strip: 9 dead · 17 trapped · 325 rescuers · 100 m shaft · 11 escaped),
  and the Asia chip rout (index bars: Kospi −6.2%, Taiex −5.0%, Nikkei −2.8%,
  Shanghai −2.0%).
- **A UTC timeline strip** (00–24) across the top and a numbered
  "Where it happened" atlas strip tying all 18 numbered stories to regions.
- **18 numbered stories** with factual blurbs and per-story sources
  (AP, Reuters, BBC News, Ofgem, Egypt's Health Ministry, Emergency Lawyers,
  Ukrainian officials, Gaza medics, Indonesian officials).
- **Regional one-liner columns** — Europe, Africa, Middle East, Asia-Pacific,
  Science & Tech, Business, Americas, Sport & Culture, plus a wire column.
- **A DATE CHECK box** that names the day's most tempting older stories
  (the Abu Dhabi talks, the 12 Nov oilseed halt) and excludes them, and a
  **markets ticker** footer.

## How it runs

`main.py` (Python 3, standard library only, no network) copies the shipped
`entry.png` to `/output/entry.png` byte for byte and verifies the copy size,
so two runs produce identical output. The image is 1024×1024, 349,310 bytes,
JPEG-encoded under a `.png` name as the rules allow (the gate reads the
first bytes).

The front page itself was researched from the day's wire reporting and
typeset as a static HTML broadsheet, rendered to the final image offline;
the shipped program is the deterministic copy step.

## License

MIT — see `LICENSE`.
