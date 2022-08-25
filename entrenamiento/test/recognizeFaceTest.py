import cv2
resp = "cp"

def recognize(face_recognizer, cap, faceClassif, socket,imagePaths):
    global resp
    while True:
        ret,frame = cap.read()
        if ret == False: 
            resp = "cp1"
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()

        faces = faceClassif.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
            result = face_recognizer

            cv2.putText(frame,'0, '+'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
            
            if result < 70:
                cv2.putText(frame,imagePaths,(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                #socket send
                print("message received with    Persona detectada")

            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                #socket sned
                print("message received with    No es la persona registrada")

        cv2.imshow('frame',frame)
        # k = cv2.waitKey(1)
        k=27
        if k == 27: #esc key
            break
    cv2.destroyAllWindows()
    return resp