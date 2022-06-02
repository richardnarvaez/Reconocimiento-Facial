import cv2
import pytest
import recognizeFaceTest
import recognizeFaceTest2
import recognizeFaceTest3
import socketio

socket = socketio.Client()

def test_testCase1():
    cap = cv2.VideoCapture()
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    # socket.connect("http://localhost:3000/")
    # socket.disconnect()
    
    assert recognizeFaceTest.recognize(70, cap, faceClassif, socket,"willy") == "cp1"

def test_testCase2():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    # socket.connect("http://localhost:3000/")
    # socket.disconnect()
    valid = recognizeFaceTest2.recognize(70, cap, faceClassif, socket,"willy")
    assert  valid == "cp2" or valid == "cp"

def test_testCase3():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    # socket.connect("http://localhost:3000/")
    # socket.disconnect()
    valid = recognizeFaceTest2.recognize(60, cap, faceClassif, socket,"willy")
    assert valid  == "cp3" or valid == "cp"

def test_testCase4():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    # socket.connect("http://localhost:3000/")
    # socket.disconnect()
    valid = recognizeFaceTest3.recognize(70, cap, faceClassif, socket,"willy")
    assert valid == "cp4" or valid == "cp"

def test_testCase5():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    # socket.connect("http://localhost:3000/")
    # socket.disconnect()
    valid = recognizeFaceTest3.recognize(60, cap, faceClassif, socket,"willy")
    assert valid == "cp5" or valid == "cp"