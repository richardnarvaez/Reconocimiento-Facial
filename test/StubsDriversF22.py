
import os
import cv2
import numpy as np


def readImages(dataPath):
    label = 0
    labels = []
    facesData =[]
    try:
        peopleList = getRoute()
        if peopleList:
            for nameDir in peopleList:
                personPath = dataPath + '/' + nameDir
                print('Reading images...')
                for fileName in os.listdir(personPath):
                    print('Faces: ', nameDir + '/' + fileName)
                    labels.append(label)
                    facesData.append(readImage(personPath,fileName))
                label = label + 1
            
            face_recognizer = createFaceRecognizerInstance()
            print("Training...")
            training(face_recognizer, facesData, labels)
            print("Creating model...")
            createModel(face_recognizer)
            print("Model save :)")
            return True
        else:
            print("There're not persons registered yet")
            return False
    except:
        print("There was a problem with datapath :/")
        return False

#STUBS
def getRoute():
    dato = os.path.dirname(__file__)
    dataPath = os.path.join(dato,'img')
    route = os.listdir(dataPath)
    return route

def readImage(personPath,fileName):
    facesDataItem = cv2.imread(personPath+'/'+fileName,0)
    return facesDataItem

def createFaceRecognizerInstance():
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    return face_recognizer

def training(face_recognizer, facesData, labels):
    face_recognizer.train(facesData, np.array(labels))

def createModel(face_recognizer):
    face_recognizer.write('modeloLBPHFace.xml')



#DRIVER
def learning():
    #Funcionalidad 2.1
    dato = os.path.dirname(__file__)
    dataPath = os.path.join(dato,'img')
    #Funcionalidad 2.2
    readImages(dataPath)

learning()

