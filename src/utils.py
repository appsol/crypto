import re

def openFile(fileName):
    '''Open and read the passed text file'''
    try:
        txtFile = open(fileName, 'r')
    except IOError as (eNum, eStr):
        print "Cannot open %s for reading: %s" % (fileName, eStr)
        return None
    txt = txtFile.read()
    return txt

def stripWhiteSpace(txt):
    '''Change to lower case then strip all characters except a-z'''
    return re.sub('[^a-zA-Z]', '', txt)