#!/usr/bin/python

import sys, os
import utils


def init():
    path = os.getcwd()
    cypherTxt = utils.openFile(path + '/' + sys.argv[1])
    if cypherTxt is not None:
        print indexOfCoincidence(cypherTxt)

def indexOfCoincidence(text):
    cypherTxt = utils.stripWhiteSpace(text)
    cypherTxtLength = len(cypherTxt)
    charFreq = characterCounts(cypherTxt)
    sumFreq = sumOfFrequencies(charFreq)
    return calcIoC(sumFreq, cypherTxtLength, charFreq)

def characterCounts(txt):
    freq = {}
    for x in txt.lower():
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    return freq

def sumOfFrequencies(charFreq):
	freqTotal = 0.0
	for char, n in charFreq.iteritems():
		freqTotal+= n * (n - 1)
	return freqTotal

def calcIoC(sumOfFreq, txtLength, charFreq):
    return sumOfFreq / ((txtLength * (txtLength - 1)) / len(charFreq))

if __name__ == "__main__":
    init()
