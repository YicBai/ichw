#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "YicBai"
__pkuid__  = "1800011840"
__email__  = "1800011840@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import string


def lower(r):
    return r.lower()

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    for i in """!#$%&()*+,-."/:;<=>?@[\]^_`{|}~""":
        lines=lines.replace(i," ")
    words=lines.split()

    words=list(map(lower,words))

    word_s={}
    for wd in words:
        if wd in word_s:
            word_s[wd]+=1
        else:
            word_s[wd]=1

    sortwds=list(word_s.items())
    sortwds.sort(key=lambda x:x[1],reverse=True)

    if topn<len(sortwds):
        for i in range(topn):
            print(sortwds[i])
    else:
        for i in range(len(sortwds)):
            print(sortwds[i])
    

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    else:    
        try:
            doc = urlopen(sys.argv[1])
            docstr = doc.read()
            doc.close()
            docstr=docstr.decode('utf-8')
            if len(sys.argv) == 2:
                wcount(docstr)
            else:
                wcount(docstr,sys.argv[2])
        except Exception:
            print("there's an error.")
