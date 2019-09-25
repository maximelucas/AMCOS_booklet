#!/bin/bash

#======================================================
# This file is part of
# "AMCOS_booklet"
# Version 1.1 (04/07/2019)
# A LaTeX template for conference books of abstracts
#
# This template is available at:
# https://github.com/maximelucas/AMCOS_booklet
#
# License: GNU General Public License v3.0
#
# Authors:
# Maxime Lucas (ml.maximelucas@gmail.com)
# Pau Clusella
#=======================================================

# need two compilations each: if not, the vertical side color lines get messed up
# todo: check if can be made cleaner with latexmk

# compile for online version
pdflatex -synctex=1 -interaction=nonstopmode "\newif\ifOnline \Onlinetrue \input{MAIN.tex}"
pdflatex -synctex=1 -interaction=nonstopmode "\newif\ifOnline \Onlinetrue \input{MAIN.tex}"
mv MAIN.pdf booklet_online.pdf

# compile for printed version
pdflatex -synctex=1 -interaction=nonstopmode "\newif\ifOnline \Onlinefalse \input{MAIN.tex}"
pdflatex -synctex=1 -interaction=nonstopmode "\newif\ifOnline \Onlinefalse \input{MAIN.tex}"
# extract timetable pages
#pdftk main.pdf cat 5-9 output timetable.pdf
#pdftk main.pdf cat 32-36 output list_posters.pdf
mv MAIN.pdf booklet_printed.pdf
