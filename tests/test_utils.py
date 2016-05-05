import sys
import os
sys.path.append(os.getcwd() + '/src')
import unittest
import utils

class TestUtils(unittest.TestCase):

    def test_createTabulaRecta(self):
        tabulaRecta = utils.createTabulaRecta()
        table = ''
        for l in tabulaRecta:
            table += ' '.join(l) + "\n"
        print table
        self.assertEqual(tabulaRecta[25][25], 'y', "tabulaRecta not created correctly:\n" + table)

    def test_lookUpTabulaRecta(self):
        encryptChar = utils.lookUpTabulaRecta('J', 'Q', False)
        self.assertEqual(encryptChar, 'z', 'Mis-encrypted J as %s using key character Q' % encryptChar)
        decryptChar = utils.lookUpTabulaRecta('Z', 'Q', True)
        self.assertEqual(decryptChar, 'j', 'Mis-decrypted Z as %s using key character Q' % decryptChar)

    def test_getNPeriodCharacters(self):
        text = 'vptnvffuntshtarptymjwzirappljmhhqvsubwlzzygvtyitarptyiougxiuydtgzhhvvmum'
        n4l2 = 'vpvfnttatywzapjmqvbwzytyaryigxydzhvm'
        n2l1 = 'vtvfnstrtmwiapjhqsblzgtiapyogiytzhvu'
        n3l2o4 = 'vfunshartyjwirppjmhqsuwlzyvtitrpyiugiudtzhvvum'
        result = utils.getNPeriodCharacters(4, text, 2)
        self.assertEqual(result, n4l2, "Failed with period of 4 and length of 2.\nExpected:\n%s\nGot:\n%s" % (n4l2, result))
        result = utils.getNPeriodCharacters(2, text, 1)
        self.assertEqual(result, n2l1, "Failed with period of 2 and length of 1.\nExpected:\n%s\nGot:\n%s" % (n2l1, result))
        result = utils.getNPeriodCharacters(3, text, 2, 4)
        self.assertEqual(result, n3l2o4, "Failed with period of 3 a length of 2 and an offset of 4.\nExpected:\n%s\nGot:\n%s" % (n3l2o4, result))

if __name__ == '__main__':
    unittest.main()
