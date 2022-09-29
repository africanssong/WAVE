import tkinter
import tkinter.font
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

import WAVESocket
import WAVELogUtill
import time
import atexit
import socket


def loginForParticipant(host, port, userID):
    mylist = window.grid_slaves()
    for i in mylist:
        i.destroy()

    window.geometry("2500x1500+0+0")  # width x height + x coor + y coor

    # window.attributes('-alpha',0.5)   # 투명도 조절. 0~1
    window.wm_attributes("-transparent", True)
    window.wm_attributes("-topmost", 1)  # 창을 항상 상단에 배치 / 0 외 모든 인자 True
    window.configure(bg='systemTransparent')
    # window.attributes('-fullscreen',True)

    print("Logged IN Successfully")
    clock_width.grid()

    atexit.register(handleClientExit, host, port, userID)
    clock()
    WAVESocket.clientOpen(host, port, userID)


def handleClientExit(host, port, userID):
    now = time.localtime()
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((host, port))
    clientSocket.send(
        f'[{now.tm_year:4d}-{now.tm_mon:02d}-{now.tm_mday:02d}/{now.tm_hour:02d}:{now.tm_min:02d}:{now.tm_sec:02d}] {userID}: exit'.encode())
    exit()


# pyinstaller -i=./wave.ico -F -w main.py     # i : 아이콘 모양, f: 하나의 파일, w : 콘솔실행없음.
# pip install pillow
# pyinstaller -i=./wave.ico -n wave -F -w main.py  wave 이름 설정.

textstr = "FDL@kookmin.ac.kr %Y-%m-%d %H:%M:%S "
FDL = ""
for i in range(120):
    FDL += textstr
    if ((i+1) % 4 == 0):
        FDL += "\n\n"


def clock():  # 현재 시간 표시 / 반복
    live_T = time.strftime(FDL)  # Real Time
    clock_width.config(text=live_T)
    clock_width.after(200, clock)  # .after(지연시간{ms}, 실행함수)


def check_data():
    if user_id.get() == "1" and password.get() == "1":

        mylist = window.grid_slaves()
        for i in mylist:
            i.destroy()

        window.geometry("2500x1500+0+0")  # width x height + x coor + y coor

        # window.attributes('-alpha',0.5)   # 투명도 조절. 0~1
        window.wm_attributes("-transparent", True)
        window.wm_attributes("-topmost", 1)  # 창을 항상 상단에 배치 / 0 외 모든 인자 True
        window.configure(bg='systemTransparent')
        # window.attributes('-fullscreen',True)

        print("Logged IN Successfully")
        clock_width.grid()
        clock()

        WAVESocket.serverOpen('127.0.0.1', 12319)

    elif user_id.get() == "2" and password.get() == "2":
        loginForParticipant('127.0.0.1',  12319, user_id.get())
    elif user_id.get() == "3" and password.get() == "3":
        loginForParticipant('127.0.0.1',  12319, user_id.get())
    elif user_id.get() == "4" and password.get() == "4":
        loginForParticipant('127.0.0.1',  12319, user_id.get())
    elif user_id.get() == "5" and password.get() == "5":
        loginForParticipant('127.0.0.1',  12319, user_id.get())

    else:
        # 로그인 정보가 유효하지 않음을 나타내는 팝업창 띄우기
        messagebox.showinfo("로그인 정보", "Check your Username/Password")
        print("Check your Usernam/Password")


''' main '''
window = tkinter.Tk()
font = tkinter.font.Font(family="Consolas", size=40)
window.title("practic")


# window.attributes('-alpha',1)   # 투명도 조절. 0~1
window.wm_attributes("-transparent", True)
window.wm_attributes("-topmost", 1)  # 창을 항상 상단에 배치 / 0 외 모든 인자 True
# window size
window.geometry("800x500+20+20")  # width x height + x coor + y coor
# window.attributes('-fullscreen',True)
window.resizable(True, True)           # width, height   size var

''' 버튼 이벤트 '''
user_id, password = StringVar(), StringVar()
id = Label(window, text="Username : ").grid(row=0, column=0, padx=100, pady=20)
id_in = Entry(window, textvariable=user_id).grid(
    row=0, column=1, padx=100, pady=20)

pw = Label(window, text="Password : ").grid(row=1, column=0, padx=100, pady=20)
pw_in = Entry(window, textvariable=password).grid(
    row=1, column=1, padx=100, pady=20)

btn = Button(window, text="Login", command=check_data).grid(
    row=2, column=1, padx=10, pady=10)

''' 메뉴 옵션 '''
mainMenu = Menu(window)
window.config(menu=mainMenu)

WAVEMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=WAVEMenu)

WAVEMenu.add_command(label="로그 기록 확인", command=WAVELogUtill.genLogEvent)
WAVEMenu.add_separator()  # 구분선 추가
WAVEMenu.add_command(label="종료", command=window.destroy)

''' 워터마크 시간 '''
clock_width = tkinter.Label(window, fg="black", font=font)
clock_width.configure(bg='systemTransparent')


window.mainloop()
