import cv2
import os
import numpy as np
import unittest 

def obtencionImagenes(datos):
 dato = os.path.dirname(datos)
 if dato is None:
  print("Error.... Data is Null")
  return None
 else:
  rutaimagenes = os.path.join(dato,'img')
  dataPath = rutaimagenes
  
  if not os.path.exists(dataPath):
    print("No existe ruta")
    return None
  else:
   peopleList = os.listdir(dataPath)
  print("Data correcta") 
  return dataPath



class test_comrpobar_direccion(unittest.TestCase):
  def entrada_dato_none(self):
   selft.assertEqual(obtencionImagenes(None),None)
   selft.assertEqual(obtencionImagenes(__file__),os.path.join(dato,'img'))       
    
  

if __name__ == '__main__':
   unittest.main()
