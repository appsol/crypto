#!/usr/bin/python

import sys
import os
import operator
import utils


def init():
    path = os.getcwd()
    cypherTxt = utils.openFile(path + '/' + sys.argv[1])
    if cypherTxt is not None:
        print indexOfCoincidence(cypherTxt)


def indexOfCoincidence(text):
    '''Return the Index of Coincidence for the given text'''
    cypherTxt = utils.stripWhiteSpace(text)
    cypherTxtLength = len(cypherTxt)
    charFreq = characterCounts(cypherTxt)
    sumFreq = sumOfFrequencies(charFreq)
    return calcIoC(sumFreq, cypherTxtLength, charFreq)


def characterCounts(txt):
    '''Count character frequency across the text'''
    freq = {}
    for x in txt.lower():
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    return freq


def sumOfFrequencies(charFreq):
    '''Sum the potential of character coincidence'''
    freqTotal = 0.0
    for char, n in charFreq.iteritems():
        freqTotal += n * (n - 1)
    return freqTotal


def calcIoC(sumOfFreq, txtLength, charFreq):
    '''Calculate the Index of Coincidence'''
    # return sumOfFreq / ((txtLength * (txtLength - 1)) / len(charFreq))
    return sumOfFreq / (txtLength * (txtLength - 1))


def calculateIoCTable(text, maxPeriod=20):
    '''Create a dictionary with the Index of Coincidence for
    each key length up to max of the second parameter (default 20)'''
    iocTable = {}
    for n in xrange(2, maxPeriod):
        iocSum = 0
        # Get mean ioc for all n period characters up to current key length (n)
        for offset in xrange(0, n-1):
            nChars = utils.getNPeriodCharacters(n, text, 1, offset)
            iocSum += indexOfCoincidence(nChars)
        iocTable[n] = iocSum / n
    return iocTable


def estimateKeyLength(cypherTxt):
    '''Return the most likely key length from the Index of Coincidence dictionary.
    Key lengths are scored on their Index of Coincidence, with additional points
    for being a factor of one of the top 3 key length candidates'''
    iocTable = calculateIoCTable(cypherTxt)
    # Sort the key length IOC dictionary descending
    sortedIoC = sorted(iocTable.iteritems(), key=operator.itemgetter(1), reverse=True)
    # Just need the sorted key lengths
    keys = [x for x, y in sortedIoC]
    candidates = {}
    score = 3
    # Iterate over the top 3
    for x in keys[:3]:
        # Apply reducing score
        candidates[x] = score
        score -= 1
        # If they are a factor of another candidate add to score
        for y in keys[:3]:
            if x == y:
                continue
            if y % x == 0:
                candidates[x] += 2
    # Return the highest scoring
    return max(candidates.iteritems(), key=operator.itemgetter(1))[0]

if __name__ == "__main__":
    init()
