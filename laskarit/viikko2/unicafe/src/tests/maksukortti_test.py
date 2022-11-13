import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

#kortin saldo alussa oikein
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

#rahan lataaminen kasvattaa saldoa oikein
    def test_kortille_voi_ladata_rahaa(self):
    	self.maksukortti.lataa_rahaa(2500)

    	self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")


#rahan ottaminen toimii: saldo vähenee oikein, jos rahaa on tarpeeksi
# ja saldo ei muutu, jos rahaa ei ole tarpeeksi
#metodi palauttaa True, jos rahat riittivät ja muuten False

    def test_kortilta_voi_ottaa_rahaa(self):
    	self.maksukortti.ota_rahaa(200)

    	self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")

    def test_kortilta_ei_voi_ottaa_liikaa_rahaa(self):
    	self.maksukortti.ota_rahaa(2000)

    	self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")	