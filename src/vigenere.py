#!/usr/bin/python

import sys
import os
import utils
from ioc import indexOfCoincidence


def init():
    path = os.getcwd()
    cypherTxt = utils.openFile(path + '/' + sys.argv[1])
    cypherTxt = utils.stripWhiteSpace(cypherTxt)
    iocTable = calculateIoCTable(cypherTxt)
    print iocTable


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

if __name__ == '__main__':
    init()
