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
            text = text[:(int(sys.argv[2]) - 1)]
        text2 = text[1:]
        textLength = len(text2)
        doubles = 0
        for i, c in enumerate(text2):
            if text[i] == c:
                doubles += 1
        twinIndex = float(doubles) / float(textLength) * 26.0
        print "Double Count: %s\nText Length: %s\nTwin Index: %s" % (doubles, textLength, twinIndex)


if __name__ == "__main__":
    init()
