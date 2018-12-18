"""
Maxime Lucas
Jan 2018

Directory structure:
- booklet.py
    |- abstracts/
        |- txt/
            |- figures/
        |- tex/

Run the code in command line to process:
- the file ./abstracts/txt/t_name.txt only (verbose or silent mode)
booklet.py t_name.txt verbose
booklet.py t_name.txt
- all ./abstracts/txt/*.txt abstracts:
booklet.py 
booklet.py all
"""

import numpy as np
import csv
import glob, os, sys

tex_dir = 'abstracts/tex/'
txt_dir = 'abstracts/txt/'

if not os.path.isdir(tex_dir):
    os.mkdir(tex_dir)
if not os.path.isdir(txt_dir):
    os.mkdir(txt_dir)

def format_num_affs(string) : #---------------------------------------------
    """
    Format substring for affiliation numbers
    Input: string "{1,2}"
    Output: string "$^{1,2}$" 
    """
    
    if string == None:
        out = ''
    else :
        out = r'$^{}$' .format(string)
    return out
    
def format_authors(authors): #----------------------------------------------
    """
    Format authors names into the uniform format F. LastName
    
    Input: single string containing all author names, e.g.
            "First1 Last1, First2 Last2"
    Output: single string formatted as e.g. 
            "F1. Last1, F2. Last2"
    """

    n_auth = len(authors)
    
    for i in range(n_auth):
        if  ',' in authors[i]:
            subnames = authors[i].split(', ')
        else :
            subnames = authors[i].split(' ')
        subnames = filter(None, subnames) #remove empty strings
        if len(subnames) > 2:
            print 'long name'
        if ',' in authors[i]: # if comma, assume Last, F.
            first = subnames[-1]
            last = subnames[0]
        else: # if no comma
            if subnames[-1][-1] == '.' or len(subnames[-1]) == 1:# if Last F.
                last = subnames[0]
                firsts = subnames[1:]
            else : # assume First Last or F. Last
                last = subnames[-1]
                firsts = subnames[:-1]
            for j in range(len(firsts)): # shorten First to F. 
                if firsts[j][-1] != '.':
                    firsts[j] = firsts[j][0] + '.'
            first = ' '.join(firsts)
            
        # /!\ the case Last First will be detected as First Last
        # /!\ assumed that the Last name is always one word (no space)
            
        authors[i] = first + ' ' + last
    
    return authors
    
def fix_abstract(abs_pieces): #----------------------------------------

    # fix end of lines without space (otherwise end and start line words get glued)
    
    abstract = []
    for i in range(len(abs_pieces)):
        if abs_pieces[i][-1] != ' ' and abs_pieces[i][-1] != '-' :
            abs_pieces[i] += ' '
            abs_piece = abs_pieces[i] + ' '
            if abs_pieces[i][-1] != ' ' :
                pass
#                print 'not fixed!!!----------'
#                print "'{}'". format(abs_pieces[i])
        else: 
            abs_piece = abs_pieces[i]
        abstract.append(abs_piece)
    
    abstract = ''.join(abstract)
    
    return abstract

    
# MAIN FUNCTION ----------------------------------------------------

def txt2tex(file_name, verbose=False) :

    """
    From a properly formatted .txt abstract file, make two 
    (printed and online version) .tex files with the right 
    format to be used in the main booklet .tex file.
    
    Input: string with name of source .txt file
           e.g.: t_name.txt (abstract for a talk), 
                 p_name.txt (abstract for a poster)

    Output: - to_name.tex file (online version)
            - tp_name.txt file (printed version)
           ("t" stands for talk, is replaced by "p" for poster) 
           
    Options: boolean "verbose"
             if true, print info including 
             final text for the .tex files
    """

    print file_name # format: t_name.txt or p_name.txt

    file_type = file_name[0] # either talk 't' or poster 'p'
    file_id = file_name[2:-4] # 'name'

    # READ .TXT FILE
    with open(txt_dir + file_name, 'rbU') as inputfile:
        reader = csv.reader(inputfile, delimiter='\n')
        data = [i[0] for i in reader]

    # EXTRACT INDICES
    idx_title = data.index("TITLE")
    idx_author = data.index("AUTHOR")
    idx_affshort = data.index("AFFSHORT")
    idcs_aff =[i for i,j in enumerate(data) if j == 'AFF']
    idx_abs = data.index("ABS")
    absshort = False
    if "ABSSHORT" in data:
        absshort = True
        idx_absshort = data.index("ABSSHORT")
    # idx_refs = data.index("REFS")

    n_aff = len(idcs_aff)
    data = np.array(data)

    # EXTRACT DATA AS TEXT
    title = data[idx_title+1] # title 
    if title[-1] == '.':
        title = title[:-1]
    authors = data[idx_author+1:idx_affshort]
    aff_short = data[idx_affshort+1]
    affs = [None]*n_aff # list of affiliations
    for i in range(n_aff) :
        start = idcs_aff[i]+1
        if i == n_aff - 1 :
            end = idx_abs
        else :
            end = idcs_aff[i+1]
        affi = data[start:end]
        affi = "".join(affi)
        affs[i] = affi
    if 'REFS' not in data:
        refs = []
        idx_refs = len(data)
        if absshort:
            idx_abs_end = idx_absshort
        else:
            idx_abs_end = len(data)
        
    else:
        idx_refs = list(data).index("REFS")
        refs = data[idx_refs+1:]
        idx_abs_end = idx_refs

    # fix end of lines without space (otherwise end and start line words get glued)
    
    abs_pieces = data[idx_abs+1:idx_abs_end]
    abstract = fix_abstract(abs_pieces)
    
    if absshort: 
        absshort_pieces = data[idx_absshort+1:]
        abstract_short = fix_abstract(absshort_pieces)
        
    n_auth = len(authors) # number of authors
    n_refs = len(refs)

    if verbose:
        print '----RAW DATA'
        print title
        print authors
        print aff_short
        print affs
        print refs
        print

    i_speaker = 0
    affs_auth = [None]*n_auth # list of affiliations for each author

    # PROCESS AFFILIATIONS AND PRESENTING AUTHOR
    abs_type = ' '
    tag = ''
    for i,author in enumerate(authors):
        if author[-1] == '*' : # if presenting author
            authors[i] = author[:-2]
            i_speaker = i
        if author[-1] == 'x' : # if invited talk (assume one author)
            authors[i] = author[:-2]
            abs_type = 'IS'
            tag = r'\IStag'
        elif author[-1] == '+' : # if keynote lecture (assume one author)
            authors[i] = author[:-2] 
            abs_type = 'KL'
            tag = r'\KLtag'
        elif author[-1] == '/' : # if special lecture (assume one author)
            authors[i] = author[:-2] 
            abs_type = 'IT'
            tag = r'\ITtag'
                       
        if '{' in author: # if affiliations
            i_i = author.index('{')
            i_f = author.index('}')
            affs_auth[i] = author[i_i:i_f+1]
            authors[i] = author[:i_i-1]

    if verbose:
        print "PROCESSED DATA"
        print title
        print authors
        print affs_auth

    authors = format_authors(authors)

    # FORMAT DATA INTO INPUT TEXT FOR LATEX
    auths_final = ''
    for i in range(n_auth):
        if i == i_speaker:
            if n_auth > 1: # if more than one author, underline speaker
                auths_final += r'\underline{' + authors[i] + r'}'
            elif n_auth == 1:
                auths_final += authors[i]
        else: 
            auths_final += authors[i]
        auths_final += format_num_affs(affs_auth[i])
        if i < n_auth-1 :
            auths_final += ', '

    if n_aff == 1 :
        affs_final = affs[0]
    else :
        affs_final = r'\newline{}'.join([r'$^{}$ {}' .format(i+1,aff) for i,aff in enumerate(affs)])
    # refs_final = ' \\ '.join(refs)
    if n_refs == 0:
        refs_final = ''
    else:
        refs_final = r"""
        \textbf{{References}} \newline{{}}{}""" .format(r'\newline{}'.join(refs))

    if abs_type == ' ':
        talk_type = ''
    else:
        talk_type = r' \hfill ' + abs_type

    # PUT ALL TOGETHER FOR DIFFERENT FORMATS: PRINTED/ONLINE AND TALK/POSTER 
    if not absshort:
        abstract_short = abstract
    
    if file_type == 't' : # talk printed

        printed = r"""
        \begin{{abstract}}{{{}}}{{%
            {}}}{{%
            {}}}{{%
            {}}}
        {}
        \end{{abstract}}
        """ .format(title, authors[i_speaker], aff_short, tag, abstract_short)

        with open(tex_dir + 'tp_' + file_id + '.tex', "w") as text_file:
            text_file.write(printed)
            
        if verbose:
            print
            print 'Talk, printed:'
            print printed

    elif file_type == 'p' : # poster printed


        printed = r"""\poster{{{}}}{{%
        {}}}{{%
        {}}}""" .format(title, authors[i_speaker], aff_short)

        with open(tex_dir + 'pp_' + file_id + '.tex', "w") as text_file:
            text_file.write(printed)
            
        if verbose:
            print
            print 'Poster, printed:'
            print printed

    # poster and talk online
    online = r"""
    \begin{{abstract_online}}{{{}}}{{%
        {}}}{{%
        {}}}{{%
        {}}}
    {}
    {}
    \end{{abstract_online}}
    """ .format(title, auths_final, tag, affs_final, abstract, refs_final)

    with open(tex_dir + file_type + 'o_' + file_id + '.tex', "w") as text_file:
        text_file.write(online)

    if verbose:
        print 'Online'
        print online
        
        print auths_final

    return online, printed
    
    
#=======================================================================
if __name__ == "__main__":

    verb = False
    if len(sys.argv) > 2 and sys.argv[2] == 'verbose':
        verb = True
    if len(sys.argv) == 1 or sys.argv[1] == 'all': # process all .txt files
    
        for file_name in glob.glob(txt_dir + "*.txt"):
            #print file_name.split('/')[-1]
            online, talkp = txt2tex(file_name.split('/')[-1])
            
    elif '.txt' in sys.argv[1]: # process single specified .txt file
    
        online, talkp = txt2tex(sys.argv[1], verbose=verb)
        
            
        

    
