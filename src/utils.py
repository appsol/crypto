import re
import string

tabulaRecta = None

def openFile(fileName):
    '''Open and read the passed text file'''
    try:
        txtFile = open(fileName, 'r')
    except IOError as (eNum, eStr):
        print "Cannot open %s for reading: %s" % (fileName, eStr)
        return None
    txt = txtFile.read()
    txtFile.close()
    return txt


def writeFile(fileName, text):
    '''Open a file for writing and write the text to it'''
    try:
        txtFile = open(fileName, 'w')
    except IOError as (eNum, eStr):
        print "Cannot open %s for writing: %s" % (fileName, eStr)
        return None
    txtFile.write(str(text))
    txtFile.close()
    return fileName


def stripWhiteSpace(txt):
    '''Change to lower case then strip all characters except a-z'''
    return re.sub('[^a-zA-Z]', '', txt)


def createTabulaRecta():
    '''Create and store the lookup table for the Vigenere cypher'''
    global tabulaRecta
    if tabulaRecta is None:
        doubleAlphabet = string.lowercase + string.lowercase
        tabulaRecta = [None] * 26
        for n in xrange(0, 26):
            tabulaRecta[n] = doubleAlphabet[n:n+26]
    return tabulaRecta


def lookUpTabulaRecta(textChar, keyChar, decrypt=True):
    '''Look up a character in the Tabula Recta either to encrypt or decrypt'''
    tabulaRecta = createTabulaRecta()
    if decrypt:
        i = 0
        for c in tabulaRecta:
            if c[ord(keyChar.lower()) - 97] == textChar.lower():
                return chr(i + 97)
            i += 1
    else:
        for c in tabulaRecta:
            if c[0] == textChar.lower():
                return c[ord(keyChar.lower()) - 97]


def getNPeriodCharacters(period, text, length=1, offset=0):
    '''Create list of nth characters (with a given offset) from the text'''
    if length > period:
        raise ValueError('The length %d should be less than the period %d' % (length, period))

    textLength = len(text)
    index = offset
    nthCharacters = []
    while index < textLength:
        nthCharacters.append(text[index:index+length])
        index += period
    return ''.join(nthCharacters)