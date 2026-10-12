# HW3 - how to run this

For TA: Quick guide on how to run the code:

## Setup (if on a MAC / if not it's slightly different)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run (from this folder)

```bash
python problem5.py        # Problem 5: orbital elements, T, p, h, energy, impact check
python problem6.py        # Problem 6: back to position & velocity
python problems7to10.py   # Problems 7-10: position & velocity + orbit plot
```

`problem1.py` and `problem2.py` only hold the functions used by the scripts above.
Problems 3 and 4 are derivations only (see the report).
