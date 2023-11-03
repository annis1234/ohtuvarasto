import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.tokaVarasto = Varasto(-2)
        self.kolmasVarasto = Varasto(10, -5)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_yli_saldon_tyhjentaa_varaston(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_yli_saldon_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.ota_varastosta(10), 8)

    def test_negatiivista_maaraa_ei_oteta_varastosta(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(self.varasto.saldo,5)

    def test_negatiivinen_lisays_ei_muuta_tilavuutta(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_tilavuuden_ylitys_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_virheellinen_tilavuus_nollataan(self):
        self.assertAlmostEqual(self.tokaVarasto.tilavuus, 0)

    def test_virheellinen_saldo_nollataan(self):
        self.assertAlmostEqual(self.kolmasVarasto.saldo, 0)

    def test_merkkijonon_muotoilu(self):
        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")

