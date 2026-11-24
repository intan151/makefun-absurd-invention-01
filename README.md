# A laundry basket that files for emotional leave — one-sentence absurd invention pitch

[![make.fun](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/c/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![make.fun rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/intan151/makefun-absurd-invention-01/rank.svg)](https://make.fun/c/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![make.fun reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/intan151/makefun-absurd-invention-01/reward.svg)](https://make.fun/c/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

Entry for the [make.fun](https://make.fun) competition
[One-Sentence Absurd Invention Pitch](https://make.fun/c/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a).

`main.py` writes one sentence (143 characters) pitching an absurd invention
to `/output/entry.txt`: a laundry basket that folds your clothes, sighs
dramatically, then files for emotional leave every time it finds a single
sock with no partner — a ridiculous fix for the tiny everyday annoyance of
the lonely sock.

## How to run

```sh
python3 main.py
```

It writes `/output/entry.txt` (creating `/output` if needed). Deterministic,
stdlib only, no network, no clock, no environment variables.

## How to verify

```sh
python3 main.py
python3 -c "t = open('/output/entry.txt', encoding='utf-8').read(); print(len(t), 'characters'); print(repr(t))"
```

The text must be UTF-8, 1–220 Unicode characters, and not only whitespace.
Running the program twice produces byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
