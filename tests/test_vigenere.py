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

    def test_getNPeriodCharacters(self):
        text = 'vptnvffuntshtarptymjwzirappljmhhqvsubwlzzygvtyitarptyiougxiuydtgzhhvvmum'
        n4l2 = 'vpvfnttatywzapjmqvbwzytyaryigxydzhvm'
        n2l1 = 'vtvfnstrtmwiapjhqsblzgtiapyogiytzhvu'
        n3l2o4 = 'vfunshartyjwirppjmhqsuwlzyvtitrpyiugiudtzhvvum'
        result = vigenere.getNPeriodCharacters(4, text, 2)
        self.assertEqual(result, n4l2, "Failed with period of 4 and length of 2.\nExpected:\n%s\nGot:\n%s" % (n4l2, result))
        result = vigenere.getNPeriodCharacters(2, text, 1)
        self.assertEqual(result, n2l1, "Failed with period of 2 and length of 1.\nExpected:\n%s\nGot:\n%s" % (n2l1, result))
        result = vigenere.getNPeriodCharacters(3, text, 2, 4)
        self.assertEqual(result, n3l2o4, "Failed with period of 3 a length of 2 and an offset of 4.\nExpected:\n%s\nGot:\n%s" % (n3l2o4, result))

    def test_getBestKey(self):
        key1 = vigenere.getBestKey(utils.stripWhiteSpace(cryptoText), 'aaaaaaa')
        self.assertEqual(key1, 'ciphers', "Failed to find key.\nExpected: 'ciphers'\nGot: %s" % key1)

if __name__ == '__main__':
    unittest.main()