#!/usr/bin/python

import sys, os
import utils


def init():
    path = os.getcwd()
    cypherTxt = utils.openFile(path + '/' + sys.argv[1])
    if cypherTxt is not None:
        cypherTxt = utils.stripWhiteSpace(cypherTxt)
        cypherTxtLength = len(cypherTxt)
        charFreq = characterCounts(cypherTxt)
        print charFreq


def characterCounts(txt):
    freq = [0] * 26
    for x in txt.lower():
        freq[ord(x) - 97] += 1
    return freq

if __name__ == "__main__":
    init()
