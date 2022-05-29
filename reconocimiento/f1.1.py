
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


if __name__ == '__main__': 

    print("CASO DE PRUEBA 1:")
    personName = "Inge Raul"
    print("CASO DE PRUEBA 2:")
    personName= "Inge Raul"
    Crearcarpeta()