import sys
import os
sys.path.append(os.getcwd() + '/src')
import unittest
import utils
import ioc

class TestIoc(unittest.TestCase):

    def test_characterCounts(self):
        text = """The opposite wall of this entry was hung all over with a heathenish
         array of monstrous clubs and spears. Some were thickly set with glittering
         teeth resembling ivory saws; others were tufted with knots of human hair;
         and one was sickle-shaped, with a vast handle sweeping round like the segment
         made in the new-mown grass by a long-armed mower. You shuddered as you gazed,
         and wondered what monstrous cannibal and savage could ever have gone a
         death-harvesting with such a hacking, horrifying implement. Mixed with these
         were rusty old whaling lances and harpoons all broken and deformed. Some were
         storied weapons. With this once long lance, now wildly elbowed, fifty years
         ago did Nathan Swain kill fifteen whales between a sunrise and a sunset. And
         that harpoon-so like a corkscrew now-was flung in Javan seas, and run away
         with by a whale, years afterwards slain off the Cape of Blanco. The original
         iron entered nigh the tail, and, like a restless needle sojourning in the
         body of a man, travelled full forty feet, and at last was found imbedded in
         the hump."""
        freq = {'e': 103,
                'a': 84,
                'n': 72,
                's': 60,
                't': 58,
                'o': 54,
                'i': 51,
                'r': 47,
                'h': 47,
                'd': 43,
                'l': 43,
                'w': 37,
                'g': 21,
                'u': 21,
                'f': 20,
                'm': 18,
                'y': 17,
                'c': 14,
                'p': 11,
                'b': 11,
                'k': 10,
                'v': 9,
                'j': 2,
                'x': 1,
                'z': 1}
        counts = ioc.characterCounts(utils.stripWhiteSpace(text))
        self.assertEqual(counts, freq, 'Mis-counted character frequency.\nExpected:\n%s\nGot:\n%s' % (freq, counts))

    def test_indexOfCoincidence(self):
        text1 = "RSTCS JLSLR SLFEL GWLFI ISIKR MGL"
        ioc1 = round(ioc.indexOfCoincidence(text1), 6)
        self.assertEqual(ioc1, 0.087302, 'IOC Test 1 failed. Expected: %f\tGot: %f' % (0.087302, ioc1))

        text2 = """VVQGY TVVVK ALURW FHQAC MMVLE HUCAT WFHHI PLXHV UWSCI GINCM
        UHNHQ RMSUI MHWZO DXTNA EKVVQ GYTVV QPHXI NWCAB ASYYM TKSZR
        CXWRP RFWYH XYGFI PSBWK QAMZY BXJQQ ABJEM TCHQS NAEKV VQGYT
        VVPCA QPBSL URQUC VMVPQ UTMML VHWDH NFIKJ CPXMY EIOCD TXBJW
        KQGAN"""
        ioc2 = round(ioc.indexOfCoincidence(text2), 6)
        self.assertEqual(ioc2, 0.041989, 'IOC Test 2 failed. Expected: %f\tGot: %f' % (0.041989, ioc2))

        text3 = """TYWUR USHPO SLJNQ AYJLI FTMJY YZFPV EUZTS GAHTU WNSFW EEEVA
        MYFFD CZTMJ WSQEJ VWXTU QNANT MTIAW AOOJS HPPIN TYDDM VKQUF
        LGMLB XIXJU BQWXJ YQZJZ YMMZH DMFNQ VIAYE FLVZI ZQCSS AEEXV
        SFRDS DLBQT YDTFQ NIVKU ZPJFJ HUSLK LUBQV JULAB XYWCD IEOWH
        FTMXZ MMZHC AATFX YWGMF XYWZU QVPYF AIAFJ GEQCV KNATE MWGKX
        SMWNA NIUSH PFSRJ CEQEE VJXGG BLBQI MEYMR DSDHU UZXVV VGFXV
        JZXUI JLIRM RKZYY ASETY MYWWJ IYTMJ KFQQT ZFAQK IJFIP FSYAG
        QXZVK UZPHF ZCYOS LJNQE MVK"""
        ioc3 = round(ioc.indexOfCoincidence(text3), 6)
        self.assertEqual(ioc3, 0.041180, 'IOC Test 3 failed. Expected: %f\tGot: %f' % (0.041180, ioc3))

        text4 = """WQXYM REOBP VWHTH QYEQV EDEXR BGSIZ SILGR TAJFZ OAMAV VXGRF
        QGKCP IOZIJ BCBLU WYRWS TUGVQ PSUDI UWOES FMTBT ANCYZ TKTYB
        VFDKD ERSIB JECAQ DWPDE RIEKG PRAQF BGTHQ KVVGR AXAVT HARQE
        ELUEC GVVBJ EBXIJ AKNGE SWTKB EDXPB QOUDW VTXES MRUWW RPAWK
        MTITK HFWTD AURRV FESFE STKSH FLZAE ONEXZ BWTIA RWWTT HQYEQ
        VEDEX RBGSO REDMT ICM"""
        ioc4 = round(ioc.indexOfCoincidence(text4), 6)
        self.assertEqual(ioc4, 0.043351, 'IOC Test 4 failed. Expected: %f\tGot: %f' % (0.043351, ioc4))

if __name__ == '__main__':
    unittest.main()