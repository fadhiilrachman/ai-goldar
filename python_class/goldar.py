# -*- coding: utf-8 -*-
import sys, json
from .pohonpakar import PohonPakar

class GolDar(PohonPakar):

	data = None

	def __init__(self):
		# Load data dari PohonPakar
		kriteria = PohonPakar()
		self.data = kriteria.importData()

	def pilihKriteria(self, pilihan):
		send=None
		if pilihan not in self.data:
			send={'error': 'Pilihan tidak ditemukan'}
		else:
			send=self.data[pilihan]
		send=json.dumps(send)
		return send