import sys
import os
sys.path.append(os.getcwd() + '/../src')
import unittest
import utils

class TestUtils(unittest.TestCase):

    def test_createTabulaRecta(self):
        tabulaRecta = utils.createTabulaRecta()
        table = ''
        for l in tabulaRecta:
            table += ' '.join(l) + "\n"
        self.assertEqual(tabulaRecta[25][25], 'y', "tabulaRecta not created correctly:\n" + table)

    def lookUpTabulaRecta():
        pass

if __name__ == '__main__':
    unittest.main()
