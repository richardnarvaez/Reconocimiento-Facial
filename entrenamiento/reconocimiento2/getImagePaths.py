import os


def getImagePaths():
    dato = os.path.dirname(__file__)
    if dato is None:
        print("Data is null")
    else:
        rutaimagenes = os.path.join(dato,'img')
        dataPath = rutaimagenes
        imagePaths = os.listdir(dataPath)
        return imagePaths