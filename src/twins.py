#!/usr/bin/python

import sys
import os
import utils


def init():
    path = os.getcwd()
    text = utils.openFile(path + '/' + sys.argv[1])
    if text is not None:
        text = utils.stripWhiteSpace(text)
        if len(sys.argv) > 2:
            subLength = int(sys.argv[2])
        else:
            subLength = None
        result = getTwinIndex(text, subLength)
        print "Double Count: %s\nText Length: %s\nTwin Index: %s" % (result['dbl'], result['len'], result['ti'])


def getTwinIndex(text, subLength=None):
    '''Calculate the Twin Index by counting double letters in the text.
    pass a length integer as the second parameter to work only with a substring
    '''
    if subLength is not None:
        text = text[:subLength]
    # Copy the text string and shift forward by 1
    text2 = text[1:]
    textLength = len(text2)
    doubles = 0
    # Compare the copies at the same index to find doubles
    for i, c in enumerate(text2):
        if text[i] == c:
            doubles += 1
    # Cast all results to floats
    twinIndex = float(doubles) / float(textLength) * 26.0
    return {'len': textLength, 'dbl': doubles, 'ti': twinIndex}


if __name__ == "__main__":
    init()
