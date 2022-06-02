import cv2
import socketio
import recognizeFaces
recognizer = recognizeFaces
socket = socketio.Client()

if __name__ == "__main__":
    #face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    #face_recognizer.read('modeloLBPHFace.xml')
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    socket.connect("http://localhost:3000/")
    print("hola usuario")
    recognizer.recognize(30, cap, faceClassif, socket,"willy")
    cap.release()
    cv2.destroyAllWindows()