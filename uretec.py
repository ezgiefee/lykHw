import random

class Generator:
	"""
	Generates random news entries
	"""

	def generate_name(self):
		names = [
			"Ezgi"
			"Ali"
			"Osman"
			"Derya"
			"Batu"
			"Eren"
			"Eser"
			"Fatih"
			"Cemile"
			"Zümrüt"
		]
		return random.choice(names)

	def generate_surname(self):
		surnames = [
			"Efe"
			"Aslan"
			"Gedik"
			"Dayı"
			"Turan"
			"Erik"
			"Güzel"
			"Gül"
			"Derman"
			"Çiçek"
		]
		return random.choice(surnames)

	def generate(self):
		olaylar = [
			"{} {}'in 3 Gün Yatmadan Yaptığı Proje'de Bug Bulan {} Developer Kayıp.",
            "{} {}'ında içinde oldugu Python'mu Ruby mi Kavgasında {} kişi Gıdıklanrak Öldü.",
            "Şarkı dinlemesine izin verilmeyen {} {} Adlı Ergen Cinnet Geçirdi {} ölü",
            "Kahve'yi Çok Seven Lyk Eğitmeni {} {}, Abanat Kahvecisi Kapanınca Cinnet Geçirdi {} Yaralı",
            "Hava Alanı Olmayan Bolu'da {} {}'nın Kontrolunde Olan Boeing 747 Kazası {} Ölü.",
            "{} {} 'ında içinde bulunduğu Apple'mı Android'mi Kavgasında {} ölü Microsft Phone'cular Halinden Memnun.",
			"{2} Yıllık Profosyonel Öğrenci Olan {0} {1} Universte Şeref Madalyası Aldı",
		]

		return random.choice(olaylar).format(
			self.generate_name(),
			self.generate_surname(),
			random.randint(0,100)
			)