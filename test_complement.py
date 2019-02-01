from unittest import TestCase
from DNA_complement import main


class TestComplement(TestCase):
    def test_complement_general_case(self):
        dna = "ACTAG"
        complementary_dna = "TGATC"
        self.assertEqual(complementary_dna, main.complement(dna))

    def test_complement_A(self):
        dna = "A"
        complementary_dna = "T"
        self.assertEqual(complementary_dna, main.complement(dna))

    def test_complement_T(self):
        dna = "T"
        complementary_dna = "A"
        self.assertEqual(complementary_dna, main.complement(dna))

    def test_complement_G(self):
        dna = "G"
        complementary_dna = "C"
        self.assertEqual(complementary_dna, main.complement(dna))

    def test_complement_C(self):
        dna = "C"
        complementary_dna = "G"
        self.assertEqual(complementary_dna, main.complement(dna))
