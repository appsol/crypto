import sys
import os
sys.path.append(os.getcwd() + '/src')
import unittest
import utils
import vigenere

cryptoText = """vptnvffuntshtarptymjwzirappljmhhqvsubwlzzygvtyitarptyiougxiuydtgzhhvvmum
shwkzgstfmekvmpkswdgbilvjljmglmjfqwioiivknulvvfemioiemojtywdsajtwmtcgluy
sdsumfbieugmvalvxkjduetukatymvkqzhvqvgvptytjwwldyeevquhlulwpkt"""

class TestVigenere(unittest.TestCase):

    def Key(self):
        global cryptoText
        parent = 'BBBBAAA'
        index = 4
        text = utils.stripWhiteSpace(cryptoText)
        bestKey = vigenere.testKey(parent, index, text)

    def test_incrementKey(self):
        keys = [
            ('aaaaaa', 0),
            ('aaaaaz', 5),
            ('zaaaaa', 0),
            ('zzzbaa', 3),
            ('zzzzzz', 5)
        ]
        newKeys = [
            'baaaaa',
            'aaaaaa',
            'aaaaaa',
            'zzzcaa',
            'zzzzza'
        ]
        results = []
        for k, i in keys:
            results.append(vigenere.incrementKey(k, i))
        self.assertEqual(results, newKeys, 'Expected %s\nReturned %s' % ('|'.join(newKeys), '|'.join(results)))

    def test_getBestKey(self):
        key1 = vigenere.getBestKey(utils.stripWhiteSpace(cryptoText), 'aaaaaaa')
        self.assertEqual(key1[0], 'ciphers', "Failed to find key.\nExpected: 'ciphers'\nGot: %s Score: %f" % key1)



if __name__ == '__main__':
    unittest.main()