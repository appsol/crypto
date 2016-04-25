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

if __name__ == '__main__':
    unittest.main()
