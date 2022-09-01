# tcpclient.py

from socket import *

ip = "10.30.46.82"
port = 10051

clientSocket = socket(AF_INET, SOCK_STREAM)			# 소켓 생성
clientSocket.connect((ip,port))					# 서버와 연결

print("연결 완료")

while True:
    sendData = input()
    clientSocket.send(sendData.encode("utf-8"))		# 데이터 송신

    print("client: 메시지 전송", sendData)
    receivedData = clientSocket.recv(1024)					# 데이터 수신
    
    if receivedData.decode("utf-8") == "exit":
        print("client: 연결 종료", receivedData.decode("utf-8"))
        break
        
    print("server : ",receivedData.decode("utf-8"))
    
clientSocket.close()						# 연결 종료
    