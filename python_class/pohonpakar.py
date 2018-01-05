# -*- coding: utf-8 -*-

class PohonPakar():

	dataPohonPakar = {
		# 1
		'1': {
			'type': 'kriteria',
			'text': 'Apakah anda suka mengungkapkan rasa kesal anda secara langsung terhadap seseorang ketika marah?',
			'if_yes': '22',
			'if_no': '21'
		},
		# 2
		'21': {
			'type': 'kriteria',
			'text': 'Apakah anda suka membuat daftar belanjaan ketika akan pergi ke supermarket?',
			'if_yes': '33',
			'if_no': '34'
		},
		'22': {
			'type': 'kriteria',
			'text': 'Apakah anda suka membuat daftar belanjaan ketika akan pergi ke supermarket?',
			'if_yes': '32',
			'if_no': '31'
		},
		# 3
		'31': {
			'type': 'kriteria',
			'text': 'Apakah anda suka lama-lama ketika mengambil uang di ATM meskipun ada orang yang mengantri dibelakang anda?',
			'if_yes': '41',
			'if_no': '42'
		},
		'32': {
			'type': 'kriteria',
			'text': 'Apakah anda tipe orang yang tidak mau menerima saran orang lain ketika saran itu tidak sesuai dengan yang anda harapkan?',
			'if_yes': '43',
			'if_no': '44'
		},
		'33': {
			'type': 'kriteria',
			'text': 'Apakah anda sering membicarakan orang lain ketika sedang bersama teman-teman anda?',
			'if_yes': '45',
			'if_no': '46'
		},
		'34': {
			'type': 'kriteria',
			'text': 'Apakah anda suka merasa kebingungan ketika akan membeli sesuatu di tempat belanja?',
			'if_yes': '48',
			'if_no': '47'
		},
		# 4
		'41': {
			'type': 'kriteria',
			'text': 'Apakah anda suka memikirkan suatu masalah ketika sedang mandi?',
			'if_yes': '52',
			'if_no': '51'
		},
		'42': {
			'type': 'kriteria',
			'text': 'Apakah Anda suka merasa kebingungan ketika memilih menu makanan?',
			'if_yes': '63',
			'if_no': '64'
		},
		'43': {
			'type': 'kriteria',
			'text': 'Apakah anda suka mengomentari mengenai rasa dari makanan yang anda pesan?',
			'if_yes': '53',
			'if_no': '511'
		},
		'44': {
			'type': 'kriteria',
			'text': 'Apakah anda suka mempelajari mata pelajaran yang disukai saja?',
			'if_yes': '611',
			'if_no': '621'
		},
		'45': {
			'type': 'kriteria',
			'text': 'Apakah Anda suka menawarkan teman untuk memesan makanan sesuai dengan yang anda pesan?',
			'if_yes': '54',
			'if_no': '55'
		},
		'46': {
			'type': 'kriteria',
			'text': 'Apakah Anda suka memilih untuk diam ketika berselisih faham dengan orang lain?',
			'if_yes': '68',
			'if_no': '67'
		},
		'47': {
			'type': 'kriteria',
			'text': 'Apakah Anda tipe orang yang selalu percaya diri dalam melakukan suatu hal?',
			'if_yes': '56',
			'if_no': '57'
		},
		'48': {
			'type': 'kriteria',
			'text': 'Apakah anda orang yang suka menunda-nunda pekerjaan dan akhirnya tidak jadi dilakukan?',
			'if_yes': '42',
			'if_no': '43'
		},
		# 5
		'51': {
			'type': 'kriteria',
			'text': 'Apakah anda suka mempelajari mata pelajaran yang disukai saja?',
			'if_yes': '612',
			'if_no': '622'
		},
		'511': {
			'type': 'kriteria',
			'text': 'Apakah anda suka mempelajari mata pelajaran yang disukai saja?',
			'if_yes': '61',
			'if_no': '62'
		},
		'52': {
			'type': 'kriteria',
			'text': 'Apakah Anda suka merasa kebingungan ketika memilih menu makanan?',
			'if_yes': '632',
			'if_no': '642'
		},
		'53': {
			'type': 'kriteria',
			'text': 'Apakah Anda suka merasa kebingungan ketika memilih menu makanan?',
			'if_yes': '631',
			'if_no': '641'
		},
		'54': {
			'type': 'kriteria',
			'text': 'Apakah anda orang yang suka menunda-nunda pekerjaan dan akhirnya tidak jadi dilakukan?',
			'if_yes': '65',
			'if_no': '66'
		},
		'55': {
			'type': 'kriteria',
			'text': 'Apakah anda sering menangis dikamar mandi ketika ada masalah?',
			'if_yes': '70',
			'if_no': '69'
		},
		'56': {
			'type': 'kriteria',
			'text': 'Apakah Anda lebih memilih untuk diam ketika berselisih paham dengan orang lain?',
			'if_yes': '671',
			'if_no': '681'
		},
		'57': {
			'type': 'kriteria',
			'text': 'Apakah anda sering menangis dikamar mandi ketika ada masalah?',
			'if_yes': '703',
			'if_no': '693'
		},
		# 6
		'6': {
			'type': 'hasil',
			'goldar': 'O',
			'kriteria': [
				'Memiliki jiwa Pemimpin, berani',
				'Memiliki karakter yang terbuka, energik dan sosial',
				'Orang tipe ini suka menjadi pusat perhatian. Mengatakan apa yang ada dalam pikirannya secara jujur',
				'Emosinya bersifat stabil, sederhana sehingga apa yang telah terjadi tidak pernah meninggalkan efek yang lama'
			]
		},
		'61': {
			'type': 'kriteria',
			'text': 'Apakah anda orang yang selektif dalam memilih teman?',
			'if_yes': '72',
			'if_no': '71'
		},
		'611': {
			'type': 'kriteria',
			'text': 'Apakah anda orang yang selektif dalam memilih teman?',
			'if_yes': '6',
			'if_no': '71'
		},
		'612': {
			'type': 'kriteria',
			'text': 'Apakah anda suka mempelajari mata pelajaran yang disukai saja?',
			'if_yes': '6',
			'if_no': '72'
		},
		'62': {
			'type': 'kriteria',
			'text': 'Apakah Anda tipe orang yang terbuka terhadap siapa saja?',
			'if_yes': '72',
			'if_no': '71'
		},
		'621': {
			'type': 'kriteria',
			'text': 'Apakah Anda tipe orang yang terbuka terhadap siapa saja?',
			'if_yes': '6',
			'if_no': '72'
		},
		'622': {
			'type': 'kriteria',
			'text': 'Apakah Anda tipe orang yang terbuka terhadap siapa saja?',
			'if_yes': '6',
			'if_no': '72'
		},
		'63': {
			'type': 'kriteria',
			'text': 'Apakah Anda orang yang peka terhadap perasaan orang lain?',
			'if_yes': '6',
			'if_no': '72'
		},
		'631': {
			'type': 'kriteria',
			'text': 'Apakah Anda orang yang peka terhadap perasaan orang lain?',
			'if_yes': '6',
			'if_no': '72'
		},
		'632': {
			'type': 'kriteria',
			'text': 'Apakah Anda orang yang peka terhadap perasaan orang lain?',
			'if_yes': '6',
			'if_no': '6'
		},
		'64': {
			'type': 'kriteria',
			'text': 'Apakah anda orang yang selektif dalam memilih teman?',
			'if_yes': '6',
			'if_no': '72'
		},
		'641': {
			'type': 'kriteria',
			'text': 'Apakah anda orang yang selektif dalam memilih teman?',
			'if_yes': '6',
			'if_no': '6'
		},
		'642': {
			'type': 'kriteria',
			'text': 'Apakah anda orang yang selektif dalam memilih teman?',
			'if_yes': '72',
			'if_no': '72'
		},
		'65': {
			'type': 'kriteria',
			'text': 'Apakah Anda sering mencari kambing hitam ketika menghadapi masalah?',
			'if_yes': '75',
			'if_no': '76'
		},
		'66': {
			'type': 'kriteria',
			'text': 'Apakah anda suka mengomentari mengenai rasa dari makanan yang anda pesan?',
			'if_yes': '80',
			'if_no': '761'
		},
		'661': {
			'type': 'kriteria',
			'text': 'Apakah Anda sering mencari kambing hitam ketika menghadapi masalah?',
			'if_yes': '751',
			'if_no': '762'
		},
		'651': {
			'type': 'kriteria',
			'text': 'Apakah Anda sering mencari kambing hitam ketika menghadapi masalah?',
			'if_yes': '753',
			'if_no': '76'
		},
		'67': {
			'type': 'kriteria',
			'text': 'Apakah anda tipe orang yang suka membicarakan orang lain, tetapi takut jika orang tersebut mengetahuinya?',
			'if_yes': '77',
			'if_no': '78'
		},
		'671': {
			'type': 'kriteria',
			'text': 'Apakah anda tipe orang yang suka membicarakan orang lain, tetapi takut jika orang tersebut mengetahuinya?',
			'if_yes': '771',
			'if_no': '781'
		},
		'681': {
			'type': 'kriteria',
			'text': 'Apakah anda tipe orang yang suka membicarakan orang lain, tetapi takut jika orang tersebut mengetahuinya?',
			'if_yes': '771',
			'if_no': '781'
		},
		'68': {
			'type': 'kriteria',
			'text': 'Apakah anda tipe orang yang suka membicarakan orang lain, tetapi takut jika orang tersebut mengetahuinya?',
			'if_yes': '72',
			'if_no': '6'
		},
		'69': {
			'type': 'kriteria',
			'text': 'Apakah anda tipe orang yang serius dalam mempersiapkan segala sesuatu?',
			'if_yes': '72',
			'if_no': '762'
		},
		'693': {
			'type': 'kriteria',
			'text': 'Apakah anda tipe orang yang serius dalam mempersiapkan segala sesuatu?',
			'if_yes': '794',
			'if_no': '804'
		},
		# 7
		'70': {
			'type': 'kriteria',
			'text': 'Apakah anda suka mengomentari mengenai rasa dari makanan yang anda pesan?',
			'if_yes': '7',
			'if_no': '6'
		},
		'71': {
			'type': 'hasil',
			'goldar': 'B',
			'kriteria': [
				'Mereka memiliki empati, mudah memahami pemikiran orang lain',
				'Mereka adalah spesialis di bidang yang digelutinya',
				'Jika mengerjakan sesuatu, mereka selalu fokus kepada apa yang tengah dikerjakan',
				'Tidak peduli dengan keadaan sekitar, mengharapkan banyak kebebasan',
				'Memiliki gejolak emosi yang besar, temperamental',
			]
		},
		'72': {
			'type': 'hasil',
			'goldar': 'B',
			'kriteria': [
				'Mereka memiliki empati, mudah memahami pemikiran orang lain',
				'Mereka adalah spesialis di bidang yang digelutinya',
				'Jika mengerjakan sesuatu, mereka selalu fokus kepada apa yang tengah dikerjakan',
				'Tidak peduli dengan keadaan sekitar, mengharapkan banyak kebebasan',
				'Memiliki gejolak emosi yang besar, temperamental',
			]
		},
		'703': {
			'type': 'kriteria',
			'text': 'Apakah anda suka mengomentari mengenai rasa dari makanan yang anda pesan?',
			'if_yes': '795',
			'if_no': '805'
		},
		'75': {
			'type': 'hasil',
			'goldar': 'A',
			'kriteria': [
				'Orang dengan golongan darah ini dapat menahan emosi sampai akhirnya meledak',
				'Menekan perasaan diri sendiri, itulah yang kerap dilakukan Tipe Darah A',
				'Benar-benar perhatian terhadap sekitar dan hal-hal yang kecil sekalipun',
				'Selalu melakukan segala sesuatu dengan sangat teliti, sangat berhati-hati, perfeksionis',
			]
		},
		'76': {
			'type': 'hasil',
			'goldar': 'A',
			'kriteria': [
				'Orang dengan golongan darah ini dapat menahan emosi sampai akhirnya meledak',
				'Menekan perasaan diri sendiri, itulah yang kerap dilakukan Tipe Darah A',
				'Benar-benar perhatian terhadap sekitar dan hal-hal yang kecil sekalipun',
				'Selalu melakukan segala sesuatu dengan sangat teliti, sangat berhati-hati, perfeksionis',
			]
		},
		'751': {
			'type': 'hasil',
			'goldar': 'A',
			'kriteria': [
				'Orang dengan golongan darah ini dapat menahan emosi sampai akhirnya meledak',
				'Menekan perasaan diri sendiri, itulah yang kerap dilakukan Tipe Darah A',
				'Benar-benar perhatian terhadap sekitar dan hal-hal yang kecil sekalipun',
				'Selalu melakukan segala sesuatu dengan sangat teliti, sangat berhati-hati, perfeksionis',
			]
		},
		'761': {
			'type': 'hasil',
			'goldar': 'A',
			'kriteria': [
				'Orang dengan golongan darah ini dapat menahan emosi sampai akhirnya meledak',
				'Menekan perasaan diri sendiri, itulah yang kerap dilakukan Tipe Darah A',
				'Benar-benar perhatian terhadap sekitar dan hal-hal yang kecil sekalipun',
				'Selalu melakukan segala sesuatu dengan sangat teliti, sangat berhati-hati, perfeksionis',
			]
		},
		'762': {
			'type': 'hasil',
			'goldar': 'AB',
			'kriteria': [
				'Mereka tidak memusingkan hal-hal kecil dan terlihat sebagai orang yang religious',
				'Mereka tidak suka dibatasi. jika merasa sangat dikekang, mereka akan keluar jalur dan melakukan hal-hal dengan cara mereka sendiri',
				'Karakter orang ini mudah berubah-ubah tergantung mood',
				'Pecinta kedamaian, paling tidak suka terlibat pertikaian individual',
			]
		},
		'79': {
			'type': 'hasil',
			'goldar': 'A',
			'kriteria': [
				'Orang dengan golongan darah ini dapat menahan emosi sampai akhirnya meledak',
				'Menekan perasaan diri sendiri, itulah yang kerap dilakukan Tipe Darah A',
				'Benar-benar perhatian terhadap sekitar dan hal-hal yang kecil sekalipun',
				'Selalu melakukan segala sesuatu dengan sangat teliti, sangat berhati-hati, perfeksionis',
			]
		},
		'78': {
			'type': 'hasil',
			'goldar': 'A',
			'kriteria': [
				'Orang dengan golongan darah ini dapat menahan emosi sampai akhirnya meledak',
				'Menekan perasaan diri sendiri, itulah yang kerap dilakukan Tipe Darah A',
				'Benar-benar perhatian terhadap sekitar dan hal-hal yang kecil sekalipun',
				'Selalu melakukan segala sesuatu dengan sangat teliti, sangat berhati-hati, perfeksionis',
			]
		},
		'77': {
			'type': 'hasil',
			'goldar': 'A',
			'kriteria': [
				'Orang dengan golongan darah ini dapat menahan emosi sampai akhirnya meledak',
				'Menekan perasaan diri sendiri, itulah yang kerap dilakukan Tipe Darah A',
				'Benar-benar perhatian terhadap sekitar dan hal-hal yang kecil sekalipun',
				'Selalu melakukan segala sesuatu dengan sangat teliti, sangat berhati-hati, perfeksionis',
			]
		},
		'771': {
			'type': 'hasil',
			'goldar': 'AB',
			'kriteria': [
				'Mereka tidak memusingkan hal-hal kecil dan terlihat sebagai orang yang religious',
				'Mereka tidak suka dibatasi. jika merasa sangat dikekang, mereka akan keluar jalur dan melakukan hal-hal dengan cara mereka sendiri',
				'Karakter orang ini mudah berubah-ubah tergantung mood',
				'Pecinta kedamaian, paling tidak suka terlibat pertikaian individual',
			]
		},
		'781': {
			'type': 'hasil',
			'goldar': 'AB',
			'kriteria': [
				'Mereka tidak memusingkan hal-hal kecil dan terlihat sebagai orang yang religious',
				'Mereka tidak suka dibatasi. jika merasa sangat dikekang, mereka akan keluar jalur dan melakukan hal-hal dengan cara mereka sendiri',
				'Karakter orang ini mudah berubah-ubah tergantung mood',
				'Pecinta kedamaian, paling tidak suka terlibat pertikaian individual',
			]
		},
		'791': {
			'type': 'hasil',
			'goldar': 'A',
			'kriteria': [
				'Orang dengan golongan darah ini dapat menahan emosi sampai akhirnya meledak',
				'Menekan perasaan diri sendiri, itulah yang kerap dilakukan Tipe Darah A',
				'Benar-benar perhatian terhadap sekitar dan hal-hal yang kecil sekalipun',
				'Selalu melakukan segala sesuatu dengan sangat teliti, sangat berhati-hati, perfeksionis',
			]
		},
		'752': {
			'type': 'hasil',
			'goldar': 'AB',
			'kriteria': [
				'Mereka tidak memusingkan hal-hal kecil dan terlihat sebagai orang yang religious',
				'Mereka tidak suka dibatasi. jika merasa sangat dikekang, mereka akan keluar jalur dan melakukan hal-hal dengan cara mereka sendiri',
				'Karakter orang ini mudah berubah-ubah tergantung mood',
				'Pecinta kedamaian, paling tidak suka terlibat pertikaian individual',
			]
		},
		'753': {
			'type': 'hasil',
			'goldar': 'AB',
			'kriteria': [
				'Mereka tidak memusingkan hal-hal kecil dan terlihat sebagai orang yang religious',
				'Mereka tidak suka dibatasi. jika merasa sangat dikekang, mereka akan keluar jalur dan melakukan hal-hal dengan cara mereka sendiri',
				'Karakter orang ini mudah berubah-ubah tergantung mood',
				'Pecinta kedamaian, paling tidak suka terlibat pertikaian individual',
			]
		},
		'795': {
			'type': 'hasil',
			'goldar': 'A',
			'kriteria': [
				'Orang dengan golongan darah ini dapat menahan emosi sampai akhirnya meledak',
				'Menekan perasaan diri sendiri, itulah yang kerap dilakukan Tipe Darah A',
				'Benar-benar perhatian terhadap sekitar dan hal-hal yang kecil sekalipun',
				'Selalu melakukan segala sesuatu dengan sangat teliti, sangat berhati-hati, perfeksionis',
			]
		},
		'794': {
			'type': 'hasil',
			'goldar': 'A',
			'kriteria': [
				'Orang dengan golongan darah ini dapat menahan emosi sampai akhirnya meledak',
				'Menekan perasaan diri sendiri, itulah yang kerap dilakukan Tipe Darah A',
				'Benar-benar perhatian terhadap sekitar dan hal-hal yang kecil sekalipun',
				'Selalu melakukan segala sesuatu dengan sangat teliti, sangat berhati-hati, perfeksionis',
			]
		},
		'7': {
			'type': 'hasil',
			'goldar': 'A',
			'kriteria': [
				'Orang dengan golongan darah ini dapat menahan emosi sampai akhirnya meledak',
				'Menekan perasaan diri sendiri, itulah yang kerap dilakukan Tipe Darah A',
				'Benar-benar perhatian terhadap sekitar dan hal-hal yang kecil sekalipun',
				'Selalu melakukan segala sesuatu dengan sangat teliti, sangat berhati-hati, perfeksionis',
			]
		},
		# 8
		'8': {
			'type': 'hasil',
			'goldar': 'A',
			'kriteria': [
				'Orang dengan golongan darah ini dapat menahan emosi sampai akhirnya meledak',
				'Menekan perasaan diri sendiri, itulah yang kerap dilakukan Tipe Darah A',
				'Benar-benar perhatian terhadap sekitar dan hal-hal yang kecil sekalipun',
				'Selalu melakukan segala sesuatu dengan sangat teliti, sangat berhati-hati, perfeksionis',
			]
		},
		'80': {
			'type': 'hasil',
			'goldar': 'A',
			'kriteria': [
				'Orang dengan golongan darah ini dapat menahan emosi sampai akhirnya meledak',
				'Menekan perasaan diri sendiri, itulah yang kerap dilakukan Tipe Darah A',
				'Benar-benar perhatian terhadap sekitar dan hal-hal yang kecil sekalipun',
				'Selalu melakukan segala sesuatu dengan sangat teliti, sangat berhati-hati, perfeksionis',
			]
		},
		'801': {
			'type': 'hasil',
			'goldar': 'AB',
			'kriteria': [
				'Mereka tidak memusingkan hal-hal kecil dan terlihat sebagai orang yang religious',
				'Mereka tidak suka dibatasi. jika merasa sangat dikekang, mereka akan keluar jalur dan melakukan hal-hal dengan cara mereka sendiri',
				'Karakter orang ini mudah berubah-ubah tergantung mood',
				'Pecinta kedamaian, paling tidak suka terlibat pertikaian individual',
			]
		},
		'804': {
			'type': 'hasil',
			'goldar': 'AB',
			'kriteria': [
				'Mereka tidak memusingkan hal-hal kecil dan terlihat sebagai orang yang religious',
				'Mereka tidak suka dibatasi. jika merasa sangat dikekang, mereka akan keluar jalur dan melakukan hal-hal dengan cara mereka sendiri',
				'Karakter orang ini mudah berubah-ubah tergantung mood',
				'Pecinta kedamaian, paling tidak suka terlibat pertikaian individual',
			]
		},
		'805': {
			'type': 'hasil',
			'goldar': 'AB',
			'kriteria': [
				'Mereka tidak memusingkan hal-hal kecil dan terlihat sebagai orang yang religious',
				'Mereka tidak suka dibatasi. jika merasa sangat dikekang, mereka akan keluar jalur dan melakukan hal-hal dengan cara mereka sendiri',
				'Karakter orang ini mudah berubah-ubah tergantung mood',
				'Pecinta kedamaian, paling tidak suka terlibat pertikaian individual',
			]
		}
	}

	def exportData(self, data):
		dataGoldar = self.dataPohonPakar
		dataGoldar.update(data)
		return True

	def importData(self):
		return self.dataPohonPakar