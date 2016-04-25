#!/usr/bin/python

import sys
import os
import utils
import operator
from ioc import indexOfCoincidence
import ngram_score

ngramScore = None


def init():
    path = os.getcwd()
    cypherTxt = utils.openFile(path + '/' + sys.argv[1])
    cypherTxt = utils.stripWhiteSpace(cypherTxt)
    iocTable = calculateIoCTable(cypherTxt)
    keyLength = estimateKeyLength(iocTable)
    print keyLength


def calculateIoCTable(text, maxPeriod=20):
    '''Create a dictionary with the Index of Coincidence for
    each key length up to max of the second parameter (default 20)'''
    iocTable = {}
    for n in xrange(2, maxPeriod):
        iocSum = 0
        # Get mean ioc for all n period characters up to current key length (n)
        for offset in xrange(0, n-1):
            nChars = getNPeriodCharacters(n, text, 1, offset)
            iocSum += indexOfCoincidence(nChars)
        iocTable[n] = iocSum / n
    return iocTable


# def getNPeriodCharacters(n, offset, text, length=1):
#     '''Create list of nth characters (with a given offset) from the text'''
#     textLength = len(text)
#     index = offset
#     nthCharacters = []
#     while index < textLength:
#         nthCharacters.append(text[index:index+length-1])
#         index += n
#     return nthCharacters

def getNPeriodCharacters(period, text, length=1, offset=0):
    '''Create list of nth characters (with a given offset) from the text'''
    if length >= period:
        raise ValueError('The length should be less than the period')

    textLength = len(text)
    index = offset
    nthCharacters = []
    while index < textLength:
        nthCharacters.append(text[index:index+length])
        index += period
    return ''.join(nthCharacters)


def estimateKeyLength(iocTable):
    '''Return the most likely key length from the Index of Coincidence dictionary.
    Key lengths are scored on their Index of Coincidence, with additional points
    for being a factor of one of the top 3 key length candidates'''
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
                candidates[x] += 1
    # Return the highest scoring
    return max(candidates.iteritems(), key=operator.itemgetter(1))[0]


def getBestKey(text, keyLength):
    '''Work through potential keys looking for best option'''



def testKey(parentKey, index, text):
    '''Recursive function to work through key possibilities until the best fit is found'''
    global ngramScore
    if ngramScore is None:
        ngramScore = ngram_score.ngram_score(os.getcwd() + '/../data/english_quadgrams.txt')
        childKey = parentKey
        for n in xrange(0,25):
            pass
    newKey = incrementKey(parent, index)


def incrementKey(key, index):
    '''Change the character at index position in key to the next alphabetic character.
    If the character is "z" return the key unchanged'''
    key = list(key)
    keyChar = ord(key[index]) - 97
    if keyChar < 25:
        key[index] = chr(keyChar + 98)
    return ''.join(key)


if __name__ == '__main__':
    init()
