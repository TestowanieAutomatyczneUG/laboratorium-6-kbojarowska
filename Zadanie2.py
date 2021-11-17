import unittest

class RomanNumerals:
    def roman(self, num):
        romanDict={1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC',
                400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M', 2000: 'MM', 3000: 'MMM'}
        if num in romanDict:
            return romanDict[num]

roman = RomanNumerals().roman

class RomanNumeralsTest(unittest.TestCase):

    def test_1_is_a_single_i(self):
        self.assertEqual(roman(1), "I")

    def test_2_is_two_i_s(self):
        self.assertEqual(roman(2), "II")

    def test_3_is_three_i_s(self):
        self.assertEqual(roman(3), "III")

    def test_4_being_5_1_is_iv(self):
        self.assertEqual(roman(4), "IV")

    def test_5_is_a_single_v(self):
        self.assertEqual(roman(5), "V")

    def test_6_being_5_1_is_vi(self):
        self.assertEqual(roman(6), "VI")

    def test_9_being_10_1_is_ix(self):
        self.assertEqual(roman(9), "IX")

    @unittest.skip("not done yet")
    def test_20_is_two_x_s(self):
        self.assertEqual(roman(27), "XXVII")

    @unittest.skip("not done yet")
    def test_48_is_not_50_2_but_rather_40_8(self):
        self.assertEqual(roman(48), "XLVIII")

    @unittest.skip("not done yet")
    def test_49_is_not_40_5_4_but_rather_50_10_10_1(self):
        self.assertEqual(roman(49), "XLIX")

    @unittest.skip("not done yet")
    def test_50_is_a_single_l(self):
        self.assertEqual(roman(59), "LIX")

    @unittest.skip("not done yet")
    def test_90_being_100_10_is_xc(self):
        self.assertEqual(roman(93), "XCIII")

    @unittest.skip("not done yet")
    def test_100_is_a_single_c(self):
        self.assertEqual(roman(141), "CXLI")

    @unittest.skip("not done yet")
    def test_60_being_50_10_is_lx(self):
        self.assertEqual(roman(163), "CLXIII")

    @unittest.skip("not done yet")
    def test_400_being_500_100_is_cd(self):
        self.assertEqual(roman(402), "CDII")

    @unittest.skip("not done yet")
    def test_500_is_a_single_d(self):
        self.assertEqual(roman(575), "DLXXV")

    @unittest.skip("not done yet")
    def test_900_being_1000_100_is_cm(self):
        self.assertEqual(roman(911), "CMXI")

    @unittest.skip("not done yet")
    def test_1000_is_a_single_m(self):
        self.assertEqual(roman(1024), "MXXIV")

    @unittest.skip("not done yet")
    def test_3000_is_three_m_s(self):
        self.assertEqual(roman(3000), "MMM")