#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#
__author__ = 'diego'
# plantilla clase

class NombreClase(herencia):
	"""Esto es una clase que realiza metodos a partir de unos atributos"""

	def __init__(self, atributo1, atributo2, atributoN):
		"""Esto es el contructor y es opcional, el el inicializador """
		self.atributo1 = atributo1
		self.atributo2 = atributo2
		self.atributoN = atributoN

	def metodo1(self):
		print "accion del método1 "

	def metodo2(self):
		print "accion del método2"

	def metodoN(self):
		print "acción del método3"
