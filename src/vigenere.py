#!/usr/bin/python

import sys
import os
import utils
from operator import itemgetter
import ioc


def init():
    '''Handles command line calls'''
    path = os.getcwd()
    cypherTxt = utils.openFile(path + '/' + sys.argv[1])
    cypherTxt = utils.stripWhiteSpace(cypherTxt)
    # cypherText = ''.join(reversed(cypherTxt))
    keyLength = ioc.estimateKeyLength(cypherTxt)
    key = findKey(cypherTxt, keyLength)
    print "Final Key: %s of length %d" % (key, keyLength)
    plainText = decryptText(cypherTxt, key)
    utils.writeFile(path + '/vigenere_plain.txt', plainText)


def findKey(text, keyLength):
    '''Work through potential keys looking for best option'''
    keys = []
    for x in xrange(int(keyLength - 1), int(keyLength + 1)):
        parentKey = ['a'] * x
        keys.append(getBestKey(text, ''.join(parentKey)))
    return max(keys, key=itemgetter(1))[0]


def getBestKey(text, parentKey, parentScore=0, index=0, bestKeys=0):
    '''Recurse through key possibilities until the best fit is found. Text is the
    cryptoText string to test the key against, parentKey is a string key,
    parentScore is the ngram score of that key, and index is the current
    column of the key to be tested'''
    scores = {}
    childKey = parentKey
    # Reset the index if we reach the end of the key
    if index == len(childKey):
        index = 0
    nPeriodText = utils.getNPeriodCharacters(len(childKey), text, index + 1)

    # Get the ngram scores of all the child keys (aaaa -> zaaa)
    for x in xrange(0,25):
        plainText = decryptText(nPeriodText, childKey[:index + 1])
        scores[childKey] = utils.getNgramScore(plainText)
        childKey = incrementKey(childKey, index)
    # for k,s in scores.iteritems():
    #     print "%s => %f\n" % (k,s)
    # Find the highest scoring child key
    bestChild = max(scores.iteritems(), key=itemgetter(1))
    print "\nBest Key: %s\tScore: %f\n" % bestChild
    # print "Parent Key: %s\tScore: %d" % (parentKey, scores[parentKey])
    # If this is better then the parent, set the parent equal to the child
    if bestChild[1] > scores[parentKey]:
        parentKey = bestChild[0]
        parentScore = bestChild[1]
    else:
        # This was the best key for this column index
        bestKeys += 1

    if bestKeys < len(parentKey):
        bestKey = getBestKey(text, parentKey, parentScore, index + 1, bestKeys)
    else:
        bestKey = (parentKey, scores[parentKey])
    return bestKey


# def getNgramScore(text):
#     '''Score the similarity of the text to English using ngrams'''
#     global biGramScore
#     if biGramScore is None:
#         biGramScore = ngram_score.ngram_score(os.getcwd() + '/data/english_bigrams.txt')
#     biScore = biGramScore.score(text.upper())
#     global triGramScore
#     if triGramScore is None:
#         triGramScore = ngram_score.ngram_score(os.getcwd() + '/data/english_trigrams.txt')
#     triScore = triGramScore.score(text.upper())
#     global quadGramScore
#     if quadGramScore is None:
#         quadGramScore = ngram_score.ngram_score(os.getcwd() + '/data/english_quadgrams.txt')
#     quadScore = quadGramScore.score(text.upper())
#     # return quadScore
#     # return triScore
#     # return biScore
#     # return (triScore + quadScore) / 2
#     return (biScore + triScore + quadScore) / 3


def incrementKey(key, index):
    '''Change the character at index position in key to the next alphabetic character.
    If the character is "z" return the key unchanged'''
    key = list(key)
    keyChar = ord(key[index]) - 97
    if keyChar == 25:
        key[index] = 'a'
    else:
        key[index] = chr(keyChar + 98)
    return ''.join(key)


def decryptText(text, key):
    '''Use the key and a Tabula Recta to decrypt the text string'''
    keyLength = len(key)
    plainText = []
    for i, c in enumerate(text):
        plainText.append(utils.lookUpTabulaRecta(c, key[i % keyLength]))
    return ''.join(plainText)


if __name__ == '__main__':
    init()
