PY ?= python3

all: main.pdf

main.pdf: main.tex sections/*.tex figures/*.tex figures/*.png outputs/*.txt ../*.py
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	pdflatex -interaction=nonstopmode -halt-on-error main.tex

# re-run the scripts (from the repo root) to refresh program output and figures
outputs:
	cd .. && $(PY) problem5.py > report/outputs/problem5.txt
	cd .. && $(PY) problem6.py > report/outputs/problem6.txt
	cd .. && MPLBACKEND=Agg $(PY) problems7to10.py > report/outputs/problems7to10.txt

clean:
	rm -f main.aux main.log main.out main.pdf

.PHONY: all outputs clean
