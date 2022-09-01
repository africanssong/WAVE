#tcpserver.py

from base64 import decode
from socket import *

host = "10.30.46.82"
port = 10051        

serverSocket = socket(AF_INET, SOCK_STREAM)             # 소켓 생성
serverSocket.bind((host,port))                          # 생성한 소켓에 설정한 HOST와 PORT 맵핑
serverSocket.listen(1)                                  # 맵핑된 소켓을 연결 요청 대기 상태로 전환
print("대기")

connectionSocket,addr = serverSocket.accept()           # 실제 소켓 연결 시 반환되는 실제 통신용 연결된 소켓과 연결주소 할당

print(str(addr),"에서 접속되었습니다.")                     # 연결 완료했다고 알림

while True :
    data = connectionSocket.recv(1024)                      # 데이터 수신, 최대 1024
    decodedData = data.decode("utf-8")
    
    if decodedData == "q":
        connectionSocket.send("exit".encode("utf-8"))  # 데이터 송신
        print("server: 연결 종료")
        break

    print("받은 데이터 :", decodedData)             # 받은 데이터 UTF-8
    connectionSocket.send("메시지 수신 완료".encode("utf-8"))  # 데이터 송신
    print("server: ", "Success!")
    
serverSocket.close()                                    # 서버 닫기