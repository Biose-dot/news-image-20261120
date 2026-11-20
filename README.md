# The World Today — Friday 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Biose-dot/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Biose-dot/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A one-page newspaper front page summing up the world news of
Friday 20 November 2026, for the make.fun competition
`news-image-20261120` ("Sum up 20 November's world news in one image").

## Stories covered

1. **The Hague — UN court: Myanmar committed genocide.** The
   International Court of Justice ruled Myanmar committed genocide
   against the Rohingya in its 2017 campaign — the court's first
   such finding against a state. (Sources: NYT, BBC, Reuters via
   news wires, 20 Nov 2026.)
2. **Shenzhen — Trump, Xi and Putin meet.** The first three-way
   summit of the US, Chinese and Russian leaders ended with a
   four-point peace declaration, including nuclear disarmament
   talks. (Sources: BBC, SimpleLife.news, 20 Nov 2026.)
3. **Riyadh — Missile hits Riyadh's tallest tower.** A suspected
   Houthi missile damaged the PIF Tower, headquarters of Saudi
   Arabia's $900bn sovereign wealth fund; windows blown out across
   seven to eight floors, no injuries reported. (Sources: Reuters
   via The Edge / Devdiscourse / Sowetan, 19–20 Nov 2026.)
4. **Odisha, India — Cyclone Akvan strikes the east coast.**
   Landfall near Gopalpur on the morning of 20 November with gusts
   to 90 km/h and heavy rain; more than 300,000 people evacuated.
   (Sources: India Meteorological Department bulletin, The Hindu /
   Sambad English, 20 Nov 2026.)
5. **Wall Street — Anthropic's record IPO soars 17%.** The AI
   firm's $81.3bn listing — the largest IPO on record — closed
   about 17% above its $83 offer price, valuing it at roughly
   $1.8 trillion. (Sources: NEXA / news wires, 20 Nov 2026.)
6. **Also today:** S&P 500 falls 2%, a fifth straight loss;
   Europe says it is ready for talks with Russia on Ukraine; COP31
   climate talks enter their final days in Antalya; 13,000 protest
   in Tokyo against the Takaichi government.

## How it was made

The image is drawn from scratch by `build_image.py` (Python + PIL,
DejaVu fonts, no network, fully deterministic): a masthead naming
the date, one lead story with a scales-of-justice illustration, four
story panels with simple shape-drawn illustrations (flags, tower,
cyclone, chart), and an "Also today" strip. No downloaded or
photographic images are used.

## Running

```sh
python3 build_image.py   # regenerate entry.png (1024x1024, < 1 MiB)
node main.ts             # copies entry.png to /output/entry.png
                         # (or $MAKEFUN_OUTPUT_DIR when set)
```

## License

MIT — see `LICENSE`.
