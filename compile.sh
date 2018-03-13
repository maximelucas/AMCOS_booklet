#!/bin/bash

# need two compilations each, if not the vertical side color lines get messed up
# todo: check if can be made cleaner with latexmk

# compile for online version
pdflatex -synctex=1 -interaction=nonstopmode "\newif\ifOnline \Onlinetrue \input{main.tex}"
pdflatex -synctex=1 -interaction=nonstopmode "\newif\ifOnline \Onlinetrue \input{main.tex}"
mv main.pdf booklet_online.pdf

# compile for printed version
pdflatex -synctex=1 -interaction=nonstopmode "\newif\ifOnline \Onlinefalse \input{main.tex}"
pdflatex -synctex=1 -interaction=nonstopmode "\newif\ifOnline \Onlinefalse \input{main.tex}"
# extract timetable pages
#pdftk main.pdf cat 5-9 output timetable.pdf
#pdftk main.pdf cat 32-36 output list_posters.pdf
mv main.pdf booklet_printed.pdf
