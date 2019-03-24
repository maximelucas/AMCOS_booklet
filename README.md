# AMCOS Conference booklet files

## What?

This is AMCOS_booklet, a LaTeX template for conference booklets, sometimes called book of abstracts. It includes an additional python script to automatise the management and inclusion of abstracts. The template also has an option to compile a short and a long version of the booklet, for print and online use, for example. The template is ready to use as is, but also easily customisable for willing users.

This template was originally created in 2018 for the AMCOS conference, a 5-day physics international conference about complex oscillatory systems: [https://amcosconference.com/](https://amcosconference.com/). 

Example conferences booklets using the AMCOS booklet template:
- AMCOS: [pdf](https://amcos.files.wordpress.com/2018/07/booklet_updated_july.pdf) of long version, conference [website](https://amcosconference.com/)
- COMPENG 2018: [pdf](http://compeng2018.ieeesezioneitalia.it/wp-content/uploads/2018/10/booklet_corretto3.pdf) of long version, conference [website](http://compeng2018.ieeesezioneitalia.it/)
- WiN COSTNET: [pdf](https://github.com/luisacutillo78/WiN-Workshop/blob/master/main.pdf) of long version, conference [website](https://win.leeds.ac.uk/)


### Features

- Templates for the following sections: About, Timetable, List of Abstracts (for talks), List of Abstracts (for posters), List of Participants, Useful Information, Partner Institutions and Sponsors.

- LaTeX environments to display the timetable, and a (long and short version of) list of abstracts, of posters, and of participants.

- Automated management of abstracts via additional python script.

- Automated creation of a short or long version of the booklet via a one-word option in the template. Creation of both via an additional bash script.

- Easily customisable in terms of layout, colours, and content.

Disclaimer: the documentation is work in progress.

## How?

### Workflow

1. Create abstracts database: copy paste each abstract text from source (.pdf, .txt, .tex, ...) to a different .txt file
2. Make basic formatting changes to the .txt files
3. Run the python script (.txt -> .tex)
4. Input each abstract .tex files into the main .tex file via \input command
5. Compile the .tex project manually, or with ./compile.sh to get short and long versions at once

### Directory structure

```
-- main.tex
-- other .tex files
-- booklet.py
-- compile.sh
-- abstracts/
    |-- txt/
        |-- .txt files of abstracts created by user
    |-- tex/
        |-- .tex files for abstracts created by booklet.py
-- images/
    |-- image files for abstracts
```

### Formatting ot the .txt file for each abstract

Each abstract should be saved as `p_name.txt` (`t_name.txt`) for a poster (talk). The name cannot contain any white space or underscore character.

```
TITLE
Title of the abstract
AUTHOR
Author1 name {1,2} * +
Author2 name {2}
AFFSHORT
University, City, Country, of 1st affiliation of presenting author (with *)
AFF
University1, City, Country
AFF
University2, City, Country
ABS
Some abstract long text.
REFS (optional)
[1] Ref1
[2] Ref2
ABSHORT (optional)
Abstract version without references or figures.
```

- "*" indicates the presenting author
- to indicate the type of talk, use after the presenting "+" for keynote lecture, "x" for invited talk, "/" for special talk
- check to LaTeX-format the math
- get rid of "artificial" dashes from end of lines
- if only one affiliation, do NOT specify {1} after the author names
- get rid of non ascii characters (accents in author names, quotes, weird dashes)
- format exotic characters and accents as you would in LaTeX
- after keys like "TITLE" no white space
- if no references, do not write the REFS key at the end
- figures can be included as in LaTeX files via the \includegraphics command

## Cite

Please acknowledge any use of this template and explicitly link to this page.  

`The open LaTeX template used to generate this booklet is available at https://github.com/maximelucas/AMCOS_booklet.`  

We'd be happy to hear about your booklet, and to include it in our list above!

## Contact

For any comments, suggestions, or questions, please contact us at ml.maximelucas [at] gmail.com.  

## Credits 

This template and all accompanying scripts were developped by Maxime Lucas and Pau Clusella.  
Thanks to Thomas Kreuz for useful feedback and advice.  

