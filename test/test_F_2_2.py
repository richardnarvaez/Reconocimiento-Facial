
import os
import cv2
import numpy as np
#import pytest




#dataPath = ''
#F2.2

def readImages(dataPath):
    label = 0
    labels = []
    facesData =[]
    try:
        peopleList = os.listdir(dataPath)
        if peopleList:
            for nameDir in peopleList:
                personPath = dataPath + '/' + nameDir
                print('Reading images...')
                for fileName in os.listdir(personPath):
                    print('Faces: ', nameDir + '/' + fileName)
                    labels.append(label)
                    facesData.append(cv2.imread(personPath+'/'+fileName,0))
                label = label + 1
            
            face_recognizer = cv2.face.LBPHFaceRecognizer_create()
            print("Training...")
            face_recognizer.train(facesData, np.array(labels))
            face_recognizer.write('modeloLBPHFace.xml')
            print("Model save...")
            return True
        else:
            print("There're not persons registered yet")
            return False
    except:
        print("There was a problem with datapath :/")
        return False

#readImages(dataPath)

#CP2.2.1(dataPath == Invalid_Route)
def test_answer1():
    dataPath = 'C:/Some/invalid/route' #Some avoid route
    print(bool(dataPath))
    assert readImages(dataPath) == False

#CP2.2.2(dataPath == Valid_Route)
"""def test_answer2():
    dato = os.path.dirname(__file__)
    dataPath = os.path.join(dato,'img') #Some correct route
    print(bool(dataPath))
    assert readImages(dataPath) == True"""

#CP2.2.3(dataPath==’’)
def test_answer3():
    dataPath = '' #Some avoid route
    print(bool(dataPath))
    assert readImages(dataPath) == False

#CP2.2.4(dataPath==None)
def test_answer4():
    dataPath = None
    assert readImages(dataPath) == False

#CP2.2.5(dataPath==Any_numerical_value)
def test_answer5():
    rangeNumbers = 234.54
    dataPath = rangeNumbers
    assert readImages(dataPath) == False

#CP2.2.6(dataPath=={})
def test_answer6():
    dataPath = {}
    assert readImages(dataPath) == False

#CP2.2.7(dataPath==[])
def test_answer7():
    dataPath = []
    assert readImages(dataPath) == False

#CP2.2.8(dataPath==Any_Emoji)
def test_answer8():
    dataPath = '😁'
    assert readImages(dataPath) == False

#CP2.2.9(dataPath == Some_Route_with_invalid_character(Ñ))
"""def test_answer9():
    dato = os.path.dirname(__file__)
    dataPath = os.path.join(dato,'img2')
    assert readImages(dataPath) == True"""






