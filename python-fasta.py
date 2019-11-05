#!/usr/bin/env python
#fun!

import sys

def read_fasta(filename):
    """
    Read a FASTA format sequence from the named file
    """
    seq = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        # we do not want to include the fasta identifier line
        if not '>' in line:
            seq = seq + line
    f.close()
    return seq
print(read_fasta(sys.argv[1]))

