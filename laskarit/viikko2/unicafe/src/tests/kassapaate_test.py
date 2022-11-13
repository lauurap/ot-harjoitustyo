import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
	def setUp(self):
		self.kassapaate = Kassapaate()
		self.kassassa_rahaa = 100000
		self.edulliset = 0
		self.maukkaat = 0
		self.maksukortti = Maksukortti(1000)

	def test_luotu_kassapaate_on_olemassa(self):
		self.assertNotEqual(self.kassapaate, None)



#Luodun kassapäätteen rahamäärä ja myytyjen lounaiden 
#määrä on oikea (rahaa 1000 euroa, lounaita myyty 0)
	def test_konstruktori_asettaa_rahan_oikein(self):
        	self.assertEqual(self.kassassa_rahaa, 100000)

	def test_konstruktori_asettaa_edulliset_oikein(self):
        	self.assertEqual(self.edulliset, 0)

	def test_konstruktori_asettaa_maukkaat_oikein(self):
        	self.assertEqual(self.maukkaat, 0)

#Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta
	def test_käteisosto_edullinen_muuttaa_saldoa_oikein(self):
		self.kassapaate.syo_edullisesti_kateisella(300)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

	def test_käteisosto_edullinen_muuttaa_edullisia_oikein(self):
		self.kassapaate.syo_edullisesti_kateisella(300)
		self.assertEqual(self.kassapaate.edulliset, 1)

	def test_käteisosto_edullinen_ei_muuta_saldoa_jos_maksu_pieni(self):
		self.kassapaate.syo_edullisesti_kateisella(200)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


	def test_käteisosto_edullinen_ei_muuta_edullisia_jos_maksu_pieni(self):
		self.kassapaate.syo_edullisesti_kateisella(200)
		self.assertEqual(self.kassapaate.edulliset, 0)


	def test_käteisosto_maukas_muuttaa_saldoa_oikein(self):
		self.kassapaate.syo_maukkaasti_kateisella(500)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

	def test_käteisosto_maukas_muuttaa_maukkaita_oikein(self):
		self.kassapaate.syo_maukkaasti_kateisella(500)
		self.assertEqual(self.kassapaate.maukkaat, 1)

	def test_käteisosto_maukas_ei_muuta_saldoa_jos_maksu_pieni(self):
		self.kassapaate.syo_maukkaasti_kateisella(200)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


	def test_käteisosto_maukas_ei_muuta_maukkaita_jos_maksu_pieni(self):
		self.kassapaate.syo_maukkaasti_kateisella(200)
		self.assertEqual(self.kassapaate.maukkaat, 0)

#Jos maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla 
#ja vaihtorahan suuruus on oikea
#Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
#Jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu, 
#kaikki rahat palautetaan vaihtorahana ja myytyjen lounaiden määrässä 
#ei muutosta


	def test_korttiosto_edullinen_muuttaa_saldoa_oikein(self):
		self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")



	def test_korttiosto_edullinen_muuttaa_edullisia_oikein(self):
		self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
		self.assertEqual(self.kassapaate.edulliset, 1)

	def test_korttiosto_edullinen_ei_muuta_saldoa_jos_saldo_pieni(self):
		maksukortti = Maksukortti(200)
		self.kassapaate.syo_edullisesti_kortilla(maksukortti)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


	def test_korttiosto_edullinen_ei_muuta_edullisia_jos_saldo_pieni(self):
		maksukortti = Maksukortti(200)
		self.kassapaate.syo_edullisesti_kortilla(maksukortti)
		self.assertEqual(self.kassapaate.edulliset, 0)


	def test_korttiosto_maukas_muuttaa_saldoa_oikein(self):
		self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")

	def test_korttiosto_maukas_muuttaa_maukkaita_oikein(self):
		self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
		self.assertEqual(self.kassapaate.maukkaat, 1)

	def test_korttiosto_maukas_ei_muuta_saldoa_jos_saldo_pieni(self):
		maksukortti = Maksukortti(200)
		self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


	def test_korttiosto_maukas_ei_muuta_maukkaita_jos_saldo_pieni(self):
		maksukortti = Maksukortti(200)
		self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
		self.assertEqual(self.kassapaate.maukkaat, 0)

#seuraavissa tarvitaan Maksukorttia:
#Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta
#Jos maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla 
#ja vaihtorahan suuruus on oikea
#Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
#Jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu, 
#kaikki rahat palautetaan vaihtorahana ja myytyjen lounaiden määrässä 
#ei muutosta

	def test_kortille_voi_ladata_rahaa(self):
		self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

	def test_kortille_ei_voi_ladata_negatiivista_rahaa(self):
		self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)