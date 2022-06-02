from email import message
import cv2
import os
import socketClient

def recognize(face_recognizer, cap, faceClassif,socketClient,imagePaths):
    while True:
        ret,frame = cap.read()
        if ret == False: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            result = predecirRostro(face_recognizer, detectarRostro(auxFrame,x,y,w,h))
            cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
            if result[1] < 70:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                emitirMensajeSocket("Persona detectada")
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                emitirMensajeSocket("No es la persona registrada")           
        cv2.imshow('frame',frame)
        k = cv2.waitKey(1)
        if k == 27:
            break

def obtenerRutaFotos():
    dato = os.path.dirname(__file__)
    if dato is None:
        print("Data is null")
    else:
        rutaimagenes = os.path.join(dato,'img')
        dataPath = rutaimagenes
        imagePaths = os.listdir(dataPath)
        return imagePaths

def emitirMensajeSocket(mensaje):
    socketClient.sendEvent(mensaje)

def detectarRostro(frame, a, b, c, d):
    rostro = frame[b:b+d,a:a+c]
    rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
    return rostro

def predecirRostro(fr, rostro):
    return fr.predict(rostro)

def leerModeloMatematico():
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('modeloLBPHFace.xml')
    return face_recognizer

def conectarSocket():
    socketClient.conectarse()

def driver():    
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    conectarSocket()
    recognize(leerModeloMatematico(), cap, faceClassif, socketClient, obtenerRutaFotos())
    cap.release()
    cv2.destroyAllWindows()

driver()