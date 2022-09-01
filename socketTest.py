'''
2022 컴퓨터네트워크 과제 1
정보보안암호수학과 20172258 이제원
'''

from encodings import utf_8
import socket
import argparse
from time import sleep


def my_info(ID, name):  # 학번, 이름을 입력받아 출력하는 함수
    print("Student ID:", ID)
    print("Name:", name)


def rqst_error(a):  # 404, 301 오류 검출 함수
    if (a.find('Not Found') == 15):
        print('404 Not Found')
        exit(0)
    if (a.find('Moved Permanently') == 15):
        print('301 Moved Permanently')
        exit(0)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('hostname', type=str)
    parser.add_argument('portnum', type=int)
    parser.add_argument('filename', type=str)

    args = parser.parse_args()
    host = args.hostname
    port = args.portnum
    filename = args.filename

    my_info('20172258', 'Jewon Lee')

    try:
        client_sock = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)  # 소켓 생성
        client_sock.connect((host, port))  # 소켓 연결
    except OSError:  # 예외 처리, 잘못된 host가 입력되었을 경우 아래를 출력하며 프로그램 종료
        print("{}: unknown host".format(host))
        exit(1)

    # http 요청 메시지
    rqst_msg = 'GET ' + filename + ' HTTP/1.0\r\nHost: ' + host + \
        '\r\nUser-agent: HW1/1.0\r\nConnection: close\r\n\r\n'

    client_sock.send(rqst_msg.encode('utf-8'))  # 요청메시지 전송

    content_len = 0
    if(filename == '/member/palladio.JPG'):
        data = client_sock.recv(254)  # 헤더파일
        # print(data.decode()) # 헤더 내용 확인

        rqst_error(str(data))

        # Content-Length 구하기
        t = str(data)[str(data).find('Content-Length') +
                      16:str(data).find('Connection')-4]

        content_length = int(t)

        print("Total Size {:} bytes".format(content_length))

        name = 'palladio.JPG'
        f = open(name, 'wb')
        while (1):

            if(len(data) < 1):
                print(
                    'Download Complete: {:}, {:}/{:}'.format(name, content_len, content_length))
                break

            data = client_sock.recv(50000)
            f.write(data)
            content_len += len(data)

            tt = int((content_len/content_length)*100)
            print(
                'Current Downloading {:}/{:} (bytes) {:}%'.format(content_len, content_length, int((content_len/content_length)*100)))

    else:  # html 파일
        data = client_sock.recv(273)  # 헤더 분리
        # print(data.decode()) # 헤더 내용 확인

        rqst_error(str(data))

        f = open('index.html', 'wb')
        while (1):

            if(len(data) < 1):
                break

            data = client_sock.recv(50000)
            f.write(data)
            content_len += len(data)

    f.close()
    client_sock.close()


if __name__ == "__main__":
    main()

'''
output

jewon@ijewon-ui-MacBookAir hw1test-5 % bash testall.sh 20172258.py 
20172258.py
20172258.py
20172258.py
HTTP/1.1 404 Not Found
<title>404 Not Found</title>
404 Not Found
aaa.cs.kookmin.ac.kr: unknown host

Binary File Compare

Text File Compare
Result:  31 20172258.py
'''
