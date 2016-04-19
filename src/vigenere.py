#!/usr/bin/python

import sys
import os
import utils
import operator
from ioc import indexOfCoincidence


def init():
    path = os.getcwd()
    cypherTxt = utils.openFile(path + '/' + sys.argv[1])
    cypherTxt = utils.stripWhiteSpace(cypherTxt)
    iocTable = calculateIoCTable(cypherTxt)
    keyLength = estimateKeyLength(iocTable)
    print keyLength


def calculateIoCTable(text, maxPeriod=20):
    iocTable = {}
    for n in xrange(2, maxPeriod):
        iocSum = 0
        for offset in xrange(0, n-1):
            nChars = getNPeriodCharacters(n, offset, text)
            iocSum += indexOfCoincidence(''.join(nChars))
        iocTable[n] = iocSum / n
    return iocTable


def getNPeriodCharacters(n, offset, text):
    textLength = len(text)
    index = offset
    nthCharacters = []
    while index < textLength:
        nthCharacters.append(text[index])
        index += n
    return nthCharacters


def estimateKeyLength(iocTable):
    sortedIoC = sorted(iocTable.iteritems(), key=operator.itemgetter(1), reverse=True)
    keys = [x for x, y in sortedIoC]
    candidates = {}
    score = 3
    for x in keys[:3]:
        candidates[x] = score
        score -= 1
        for y in keys[:3]:
            if x == y:
                continue
            if y % x == 0:
                candidates[x] += 1
    return max(candidates.iteritems(), key=operator.itemgetter(1))[0]


if __name__ == '__main__':
    init()
