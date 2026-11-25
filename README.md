# Six Words to a Payday

[![make.fun](https://img.shields.io/badge/make.fun-entry-blue)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)

A make.fun entry for **Six Words to a Payday**: one line, exactly six words, 1-60 characters, written to `/output/entry.txt` by `main.py`.

## The line

> Payday arrived. My boss quit first.

(35 characters, six words, inside the 1-60 gate.)

## How it works

`main.py` writes the six-word line to `/output/entry.txt`, with a gate self-check (six words, 1-60 characters, single line, no em dash) and a verify step that re-reads the written file and asserts it matches the line byte for byte.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

- make.fun competition: `u-irvan-motion-six-words-to-a-payday-89fb591f`
- Pot: $2, top 10
- Harness: program/v1
