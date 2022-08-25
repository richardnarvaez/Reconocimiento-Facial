from email import message
import cv2
import os
import socketClient
import socketio

def getImagePaths():
    dato = os.path.dirname(__file__)
    if dato is None:
        print("Data is null")
    else:
        rutaimagenes = os.path.join(dato,'img')
        dataPath = rutaimagenes
        imagePaths = os.listdir(dataPath)
        return imagePaths


def recognize(face_recognizer, cap, faceClassif,socketClient,imagePaths):
    while True:
        ret,frame = cap.read()
        if ret == False: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)
            cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
            if result[1] < 70:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                socketClient.sendEvent("Persona detectada")
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                socketClient.sendEvent("No es la persona registrada")           
        cv2.imshow('frame',frame)
        k = cv2.waitKey(1)
        if k == 27:
            break

if __name__ == "__main__":
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('C:\\Users\\wromero\\Desktop\\rec\\reconocimiento-test\\src\\reconocimiento2\\modeloLBPHFace.xml')
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    socketClient.conectarse()
    print("hola usuario")
    recognize(face_recognizer, cap, faceClassif, socketClient, getImagePaths())
    cap.release()
    cv2.destroyAllWindows()