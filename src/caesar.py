#!/usr/bin/python

import sys
import os
import utils
import string
from operator import itemgetter
import ngram_score


def init():
    '''Handles command line calls'''
    path = os.getcwd()
    cipherText = utils.openFile(path + '/' + sys.argv[1])
    cipherText = utils.stripWhiteSpace(cipherText)
    key = getKey(cipherText)
    plainText = decryptText(cipherText, key)
    utils.writeFile(path + '/caesar_plain.txt', plainText)

def getKey(cipherText):
    scores = {}
    for x in xrange(0,26):
        plainText = decryptText(cipherText, x)
        scores[x] = utils.getNgramScore(plainText)
        print "Key: %d Score:%f\n" % (x,scores[x])
    return max(scores.iteritems(), key=itemgetter(1))[0]

def decryptText(text, key):
    plainChars = []
    doubleAlphabet = string.lowercase + string.lowercase
    for c in text:
        plainChars.append(doubleAlphabet[ord(c) - 97 - key])
    return ''.join(plainChars)

if __name__ == '__main__':
    init()
