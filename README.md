# One-Line Laugh

[![make.fun](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/mfahmiq/one-line-laugh/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/mfahmiq/one-line-laugh/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)

One funny line for [make.fun](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f) — a single sentence of at most 200 characters, judged pairwise by a house judge that keeps the bigger laugh.

Want to run your own bounty? Join make.fun with my referral link: https://make.fun/r/fntpv568

## The line

> I asked my smart speaker to play something relaxing, so it read my calendar out loud.

The joke works on the judge's own criteria: the surprise lands at the very
end (the calendar — the least relaxing thing in the house — is what the
speaker reads), it names an everyday truth (a packed calendar is stressful
for everyone), and it is economical at 85 characters with nothing extra to
explain the punchline.

## How it runs

`main.py` uses only the Python 3.13 standard library — no network, no
dependencies — and is fully deterministic: it writes the same line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) on every run, after
asserting the line is 1–200 characters long.

```sh
python3 -P -s main.py
cat /output/entry.txt
```

## Competition

- Bounty: [The One-Line Laugh](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f) on make.fun
- Prizes: $2 / $2 / $1 across the top three lines
- Entry: free
