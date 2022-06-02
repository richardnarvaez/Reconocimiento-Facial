import cv2
import socketClient
import getImagePaths, recognizeFaces

if __name__ == "__main__":
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('C:\\Users\\wromero\\Desktop\\rec\\reconocimiento-test\\src\\reconocimiento2\\modeloLBPHFace.xml')
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    socketClient.conectarse()
    print("hola usuario")
    recognizeFaces.recognize(face_recognizer, cap, faceClassif, socketClient, getImagePaths.getImagePaths())
    cap.release()
    cv2.destroyAllWindows()