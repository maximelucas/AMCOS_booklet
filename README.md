# AMCOS Conference booklet files

For more information about the AMCOS conference, go to [https://amcosconference.com/](https://amcosconference.com/).



## Workflow

1. copy paste abstract text from source (.pdf, .txt, .tex, ...) to a .txt file
2. make basic formatting changes to the .txt
3. run the python script (.txt -> .tex)
4. compile the .tex project manually or with ./compile.sh to get all versions at once
## Formatting ot the .txt file

```
TITLE
Title of the abstract
AUTHOR
Author1 name {1,2} * +
Author2 name {2}
AFFSHORT
University, City, Country, of 1st affiliation of presenting authour (with *)
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
- check to latex-format the math
- get rid of "artificial" dashes from end of lines
- if only one affiliation, do NOT specify {1} after the author names
- get rid of non ascii characters (accents in author names, quotes, weird dashes)
- after keys like "TITLE" no white space!
- if no references, do not write the REFS key at the end


## TODO

- [x] deal with two version of abstract (online without references)
- [x] deal with figures
- [x] deal with (underline) corresponding/speaking author
- [ ] add links in online version?
- [x] check presenting author
