

import unittest
import cv2
import os
import imutils

dato = os.path.dirname(__file__)
rutaimagenes = os.path.join(dato,'img')


def Ingresarnombre():
	print(" Face Recognition  ")
	print(" Please enter your name")
	nombre= input()
	return nombre

def Crearcarpeta(personName):
	dato = os.path.dirname(__file__)
	rutaimagenes = os.path.join(dato,'img')
	dataPath = rutaimagenes #Cambia a la ruta donde hayas almacenado Data
	personPath = dataPath + '/' + personName
	
	if not os.path.exists(personPath):
		print('Carpeta creada: ',personPath)
		os.makedirs(personPath)
		return personPath
	else:
		print(" CARPETA YA EXITE  ")
		return personPath

	personName.assertTrue(personPath)


class testCrearCarpteta(unittest.TestCase):
	def	testCrearCarpte (selft):
		selft.assertEqual(Crearcarpeta('Inge Rosero'),os.path.join(dato,'img')+'/Inge Rosero')
		selft.assertEqual(Crearcarpeta('Daniel Molina'),os.path.join(dato,'img')+'/Daniel Molina')
		
if __name__ == '__main__': 
	unittest.main()
    
