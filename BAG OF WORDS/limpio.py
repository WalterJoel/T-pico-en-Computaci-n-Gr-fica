#!/usr/bin/env python
# -*- coding: utf-8 -*-
#con los comentarios puedo utilizar ñ y tildes
import nltk
import csv
import sys 
import os
from time import time
reload(sys) 
sys.setdefaultencoding("utf-8")
from nltk.tokenize import sent_tokenize, word_tokenize  #Para tokenizar las palabras
from nltk.corpus import stopwords  						#Para las palabras vacias
import unicodedata 	

def elimina_tildes(input_str):
	nkfd_form = unicodedata.normalize('NFKD', unicode(input_str))
	return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

class ProcesarTexto:
	# La libreria ofrece palabras en español para (STOPWORDS)
	english_words    = set(stopwords.words('english'))
	list_news        = []  
	total_new        = 0
	def __init__(self):
		self.total_new = 0
	def abrir_carpeta():
		for filename in os.listdir(os.getcwd()):
			print "hello"
def main():
	objetoProcesar = ProcesarTexto()
	objetoProcesar.abrir_carpeta()
main()
