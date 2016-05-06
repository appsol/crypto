import sys
import os
sys.path.append(os.getcwd() + '/src')
import unittest
import caesar

plainText = "thereseemedtobenouseinwaitingbythelittledoorsoshewentbacktothetablehalfhopingshemightfindanotherkeyonit"
shift1CipherText = "uifsftffnfeupcfopvtfjoxbjujohczuifmjuumfeppstptifxfoucbdlupuifubcmfibmgipqjohtifnjhiugjoebopuifslfzpoju"
shift5CipherText = "ymjwjxjjrjiytgjstzxjnsbfnynslgdymjqnyyqjittwxtxmjbjsygfhpytymjyfgqjmfqkmtunslxmjrnlmyknsifstymjwpjdtsny"
shift25CipherText = "sgdqdrddldcsnadmntrdhmvzhshmfaxsgdkhsskdcnnqrnrgdvdmsazbjsnsgdszakdgzkegnohmfrgdlhfgsehmczmnsgdqjdxnmhs"


class TestCaesar(unittest.TestCase):

    def test_decryptText(self):
        global plainText
        global shift1CipherText
        global shift5CipherText
        global shift25CipherText
        shift1Text = caesar.decryptText(shift1CipherText, 1)
        self.assertEqual(plainText, shift1Text, "Failed to decrypt cipher text with shift of 1\nExpected: %s\nGot: %s" % (plainText, shift1Text))
        shift5Text = caesar.decryptText(shift5CipherText, 5)
        self.assertEqual(plainText, shift1Text, "Failed to decrypt cipher text with shift of 5\nExpected: %s\nGot: %s" % (plainText, shift5Text))
        shift25Text = caesar.decryptText(shift1CipherText, 25)
        self.assertEqual(plainText, shift1Text, "Failed to decrypt cipher text with shift of 25\nExpected: %s\nGot: %s" % (plainText, shift25Text))
        shift0Text = caesar.decryptText(plainText, 0)
        self.assertEqual(plainText, shift0Text, "Failed to decrypt cipher text with shift of 0\nExpected: %s\nGot: %s" % (plainText, shift0Text))

    def test_getKey(self):
        global plainText
        global shift1CipherText
        global shift5CipherText
        global shift25CipherText

        shift1Key = caesar.getKey(shift1CipherText)
        self.assertEqual(1, shift1Key, "Failed to return correct key for 1 shifted cipher text\nExpected: 1 Got: %d" % shift1Key)
        shift5Key = caesar.getKey(shift5CipherText)
        self.assertEqual(5, shift5Key, "Failed to return correct key for 5 shifted cipher text\nExpected: 5 Got: %d" % shift5Key)
        shift25Key = caesar.getKey(shift25CipherText)
        self.assertEqual(25, shift25Key, "Failed to return correct key for 25 shifted cipher text\nExpected: 25 Got: %d" % shift25Key)
        shift0Key = caesar.getKey(plainText)
        self.assertEqual(0, shift0Key, "Failed to return correct key for 0 shifted cipher text\nExpected: 0 Got: %d" % shift0Key)

if __name__ == '__main__':
    unittest.main()
