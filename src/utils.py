import re

def openFile(fileName):
    try:
        txtFile = open(fileName, 'r')
    except IOError as (eNum, eStr):
        print "Cannot open %s for reading: %s" % (fileName, eStr)
        return None
    txt = txtFile.read()
    return txt

def stripWhiteSpace(txt):
    return re.sub('[^a-zA-Z]', '', txt)