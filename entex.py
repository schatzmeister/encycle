#! python3
# -*- coding: utf-8 -*-
"""Entex.

Usage:
    entex.py <infile> <outfile> [--comp]
    entex.py (-h | --help)
    entex.py (-v | --version)
    
Options:
    -h --help       Show this screen.
    -v --version    Show version.
    --comp          Compile TeX document into pdf.
"""

import sys
import data
import codecs
from collections import OrderedDict
from subprocess import run
from docopt import docopt
   
def write_preamble(outfile, preamble='preamble.tex'):
    """Write the contents of preamble.tex to outfile."""
    with codecs.open(outfile, 'w', encoding = 'utf8') as out:
        with codecs.open(preamble, 'r', encoding = 'utf8') as pre:
            for line in pre:
                out.write(line)

def write_begin(outfile):
    """Write \begin{document} into outfile."""
    with codecs.open(outfile, 'a', encoding = 'utf8') as out:
        out.write('\n\n\\begin{document}\n')
        
def write_end(outfile):
    """Write \end{document} into outfile."""
    with codecs.open(outfile, 'a', encoding = 'utf8') as out:
        out.write('\n\\end{document}\n')

def write_entry(outfile, lemma, description):
    """Write an entry off a lemma-description-pair."""
    with codecs.open(outfile, 'ab', encoding = 'utf8') as out:
        out.write("\n\\begin{entry}")
        out.write("{{{0}}}\n".format(lemma))
        if description is None:
            description = ""
        out.write(description)
        out.write("\n\\end{entry}\n")
        
def write_entries(outfile, dict):
    """Write entries off a lemma-decription-dictionary."""
    with codecs.open(outfile, 'a', encoding = 'utf8') as out:
        for key, value in dict.items():
            write_entry(outfile, key, value)
   
def write_tex(inf, outf):
    entries = data.read_sheet(inf)
    write_preamble(outf)
    write_begin(outf)
    write_entries(outf, entries)
    write_end(outf)

def entex(file):
    try:
        run(['xelatex', file])
    except OSError as err:
        sys.stderr('Execution failed: ', err)    
    
def main():
    args = docopt(__doc__, version='Encycle enTeX 1.0')
    write_tex(args['<infile>'], args['<outfile>'])
    if args['--comp']:
        entex(args['<outfile>'])
    
if __name__ == '__main__':
    main()
