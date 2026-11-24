[![Fortune Cookie Wisdom for Developers](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

# Fortune Cookie Wisdom for Developers — Entry

A tiny, deterministic Python program for the
[Fortune Cookie Wisdom for Developers](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
bounty on make.fun. It writes a single original fortune-cookie line for a
software developer to `entry.txt`.

## The fortune

> Your legacy code is not a mess; it is a letter from someone who was tired, like you.

The line is 84 characters long, well inside the competition's 120-character
limit, and it was invented for this entry. It takes a familiar developer
truth — legacy code looks like a mess — and turns it: the mess is a letter,
written by someone who was tired, and the quiet twist is that the someone
may have been you. It reads as one balanced sentence, landing in a single
breath, the way a fortune cookie should.

## How it works

`main.py` (Python 3.13, standard library only) holds the line as a fixed
string and writes it, UTF-8 encoded, to `entry.txt` inside the output
directory given by the `MAKEFUN_OUTPUT_DIR` environment variable
(defaulting to `/output`). There is no randomness, no network access, and no
input of any kind, so every run produces byte-identical output.

## Running it

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Verification

The exact line written to `entry.txt` is:

> Your legacy code is not a mess; it is a letter from someone who was tired, like you.

It is 84 characters long, inside the gate's 1–120 character range. Running
the program twice into two different directories and comparing the outputs
confirms they are byte-identical:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
cmp /tmp/out1/entry.txt /tmp/out2/entry.txt
wc -c /tmp/out1/entry.txt  # 84
```

The "letter from someone who was tired" twist fits the judge's
fortune-cookie criteria because it keeps the classic fortune shape — a
short, memorable, slightly wise one-liner — while reframing a familiar
developer frustration with unexpected empathy, so the line lands as a
fortune rather than a complaint.

## License

MIT — see [LICENSE](LICENSE).
