# AMCOS Conference booklet files

## What?

This is a LaTeX template for conference booklets, sometimes called booklets of abstracts. It includes an additional python script to automatise the management and inclusion of abstracts. The template also has an option to compile a short and a long version of the booklet, for print and online use, for example. The template is ready to use as is, but also easily customisable for willing users.

This template was originally created in 2018 for the AMCOS conference, a 5-day physics international conference about complex oscillatory systems: [https://amcosconference.com/](https://amcosconference.com/).

### Features

- Ready templates for the following sections: About, Timetable, List of Abstracts (for talks), List of Abstracts (for posters), List of Participants, Useful Information, Partner Institutions and Sponsors.

- LaTeX environments to display the timetable, and a (long and short version of) list of abstracts, of posters, and of participants.

- Automated management of abstracts via additional python script.

- Automated creation of a short or long version of the booklet via a one-word option in the template. Creation of both via an additional bash script.

## Workflow

1. Create abstracts database: copy paste each abstract text from source (.pdf, .txt, .tex, ...) to a different .txt file
2. Make basic formatting changes to the .txt
3. Run the python script (.txt -> .tex)
4. Input each abstract .tex files into the main .tex file via \input command
5. Compile the .tex project manually or with ./compile.sh to get both versions at once

## Formatting ot the .txt file for each abstract

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
- after keys like "TITLE" no white space
- if no references, do not write the REFS key at the end


## TODO

- [x] deal with two version of abstract (online without references)
- [x] deal with figures
- [x] deal with (underline) corresponding/speaking author
- [ ] add links in online version?
- [x] check presenting author

## Credits

This template and all accompanying scripts were developped by Maxime Lucas and Pau Clusella.  
For any comments or questions, please contact ml.maximelucas@gmail.com.  
Please acknowledge any use of this template and link to this page.  

