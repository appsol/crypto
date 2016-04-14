#!/usr/bin/python

import sys, os
import utils


def init():
    path = os.getcwd()
    cypherTxt = utils.openFile(path + '/' + sys.argv[1])
    if cypherTxt is not None:
        cypherTxt = utils.stripWhiteSpace(cypherTxt)
        cypherTxtLength = len(cypherTxt)
        print cypherTxtLength
        charFreq = characterCounts(cypherTxt)
        print charFreq
        sumFreq = sumOfFrequencies(charFreq)
        print sumFreq
        ci = sumFreq / (cypherTxtLength * (cypherTxtLength - 1))
        print ci


def characterCounts(txt):
    freq = [0] * 26
    for x in txt.lower():
        freq[ord(x) - 97] += 1
    return freq

def sumOfFrequencies(charFreq):
	freqTotal = 0.0
	for n in charFreq:
		freqTotal+= n * (n - 1)
	return freqTotal

if __name__ == "__main__":
    init()
