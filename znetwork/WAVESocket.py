from _thread import *
from tkinter import *
import time
import socket


def receivedData(socket):
    first = True

    while True:
        try:
            data = socket.recv(1024)
            print(data.decode('utf-8'))
            if first:
                first = False

        except ConnectionAbortedError as e:
            exit()


def connectClient(host, port, userID):
    now = time.localtime()
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((host, port))
    clientSocket.send(
        f'[{now.tm_year:4d}-{now.tm_mon:02d}-{now.tm_mday:02d}/{now.tm_hour:02d}:{now.tm_min:02d}:{now.tm_sec:02d}] {userID}: connected'.encode())
    exit()


def clientOpen(host, port, userID):
    start_new_thread(connectClient, (host, port, userID))


def threaded(clientSocket, addr):
    for c in clientList:
        c.sendall(('[System] ' + str(addr[1]) + ' 님이 접속하였습니다.').encode())
    while True:
        try:
            data = clientSocket.recv(1024)
            print(data.decode('utf-8'))
        except ConnectionResetError as e:
            clientList.remove(clientSocket)
            for c in clientList:
                c.sendall(('[System] ' + str(addr[1]) + ' 님이 나갔습니다.').encode())
            break
    clientSocket.close()


def serverOpen(host, port):
    start_new_thread(makeServer, (host, port))


def makeServer(HOST, PORT):
    global serverSocket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    serverSocket.bind((HOST, PORT))
    serverSocket.listen()
    print("클라이언트 접속 대기 중")

    while True:
        clientSocket, addr = serverSocket.accept()
        clientList.append(clientSocket)
        start_new_thread(threaded, (clientList[-1], addr))


clientList = []
