#!/usr/bin/env python3
'''
  /************************/
  /*  enc_dec_tests.py    */
  /*     Version 1.0      */
  /*     2024/03/14       */
  /************************/
'''
from pathlib import Path
import sys
import unittest


base_path = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(base_path))

from mod_enc_dec import decode, encode  # noqa: E402


class decode_test(unittest.TestCase):
    def test_01(self):
        INPUT = "ENC3T10506S271132184132287"
        COMPUTED = decode(INPUT)
        EXPECTED = "\\<< T \\>>"
        self.assertEqual(COMPUTED, EXPECTED)

    def test_02(self):
        INPUT = "ENC3T11279S184204205215132205215110132197132216201215216"
        COMPUTED = decode(INPUT)
        EXPECTED = "This is\n a test"
        self.assertEqual(COMPUTED, EXPECTED)

    def test_03(self):
        COMPUTED = decode("test_dec_3_in.g48", True)
        with open("test_dec_3_res.g48", "r") as file:
            EXPECTED = file.read().rstrip('\n')
        self.assertEqual(COMPUTED, EXPECTED)


class encode_test(unittest.TestCase):
    def test_01(self):
        COMPUTED = encode("test_enc_1.g48", True)
        EXPECTED = "ENC3T29443S1581581101421321732102052162051972081322181972"\
            "0821720111015014615311014213218021721613221620420113221521719821"\
            "4211217216205210201132211210132216204201132215216197199207110139"\
            "1321581581321761651771322201321761651771322201321371421321321591"\
            "1014213216820120220521020113221620120921221121419721422113221819"\
            "7214205197198208201215110223132132176165177132220132132176165177"\
            "1321831811851651821691321322251101421321732102052162051972082052"\
            "2220113221620120921221121419721422113221819721420519719820820121"\
            "5110166173178168110158158110134168205214201199216134110176165177"\
            "1322201321761651771322201321371421101341832171982142112172162052"\
            "1020113411017616517713218318118516518216913216918616517611015911"\
            "0142132209201209211214221132199208201197210217212110165166178168"\
            "110159"
        self.assertEqual(COMPUTED, EXPECTED)

    def test_02(self):
        COMPUTED = encode("test_enc_2.g48", True)
        EXPECTED = "ENC3T12071S2711101321321321321351511481551571522041321831"\
            "89183169186165176132156132156132183185166110110132132132132287"
        self.assertEqual(COMPUTED, EXPECTED)

    def test_03(self):
        COMPUTED = encode("\\<< T \\>>")
        EXPECTED = "ENC3T10506S271132184132287"
        self.assertEqual(COMPUTED, EXPECTED)

    def test_04(self):
        COMPUTED = encode("This is\n a test")
        EXPECTED = "ENC3T11279S184204205215132205215110132197132216201215216"
        self.assertEqual(COMPUTED, EXPECTED)

    def test_05(self):
        COMPUTED = encode("(1,2)", enc_type=2)
        EXPECTED = "ENC2T10224S140149144150141"
        self.assertEqual(COMPUTED, EXPECTED)


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise 'Must be using Python 3'
    unittest.main()
