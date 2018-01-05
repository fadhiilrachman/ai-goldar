# -*- coding: utf-8 -*-
import sys
from python_class import *

if len(sys.argv) > 1:
	pilihan = sys.argv[1]
	goldar = GolDar()
	data = goldar.pilihKriteria(pilihan)
	print(data)
else:
	print("Pilihan tidak ditemukan")