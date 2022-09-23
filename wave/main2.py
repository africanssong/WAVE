import tkinter
import tkinter.font
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

import WAVESocket
import WAVELogUtill
import time
from webbrowser import get
import atexit
import socket

import pymysql
import datetime

import smtplib
from email.mime.text import MIMEText

import random

# pyinstaller -i=./wave.ico -n wave -F -w main.py

def loginForParticipant(host, port, userID):
    mylist = window.grid_slaves()
    for i in mylist:
        i.destroy()

    window.geometry("2500x1500+0+0")  # width x height + x coor + y coor

    # window.attributes('-alpha',0.5)   # 투명도 조절. 0~1
    window.wm_attributes("-transparent", True)
    #window.wm_attributes("-topmost", 1)  # 창을 항상 상단에 배치 / 0 외 모든 인자 True
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

FDL = " %Y-%m-%d %H:%M:%S   "

def clock():  # 현재 시간 표시 / 반복
    live_T = time.strftime(FDL)  # Real Time
    multiFDL = " "

    for i in range(90):
        multiFDL += user_id.get()+live_T
        if ((i+1) % 6 == 0):
            multiFDL += "\n\n"
    
    clock_width.config(text= multiFDL)
    clock_width.after(200, clock)  # .after(지연시간{ms}, 실행함수)


''' main '''
window = tkinter.Tk()
font = tkinter.font.Font(family="Consolas", size=40)
window.title("WAVE")

# Remove the Title bar of the window
#window.overrideredirect(True)

window.resizable(False, False)

# window.attributes('-alpha',1)   # 투명도 조절. 0~1
window.wm_attributes("-transparent", True)
#window.wm_attributes("-topmost", 1)  # 창을 항상 상단에 배치 / 0 외 모든 인자 True
# window size
window.geometry("800x500+20+20")  # width x height + x coor + y coor
# window.attributes('-fullscreen',True)
#window.resizable(True, True)           # width, height   size var

''' 버튼 이벤트 '''
user_id, password = StringVar(), StringVar()
id = Label(window, text="Username : ").grid(row=0, column=0, padx=100, pady=20)
id_in = Entry(window, textvariable=user_id).grid(
    row=0, column=1, padx=100, pady=20)

pw = Label(window, text="Password : ").grid(row=1, column=0, padx=100, pady=20)
pw_in = Entry(window, textvariable=password).grid(
    row=1, column=1, padx=100, pady=20)

clock_width = tkinter.Label(window, fg="black", font=font)
clock_width.configure(bg='systemTransparent')

# Sign up window
def signupmain():
    signup = Toplevel(window)
    #signup.attributes("-topmost", 1)
    signup.title("Sign up")
    signup.grid()
    signup.geometry("850x550+20+20")  # width x height + x coor + y coor
    signup.resizable(True, True)

    # 회원가입 id/pw 입력 칸 생성
    usid, uspw , uspwcheck, usname, usbir, usem, usvar = StringVar(), StringVar() , StringVar() , StringVar(), StringVar(), StringVar(), StringVar()
    Label(signup, text="ID : ").grid(row=0, column=0, padx=80, pady=20)
    Entry(signup, textvariable=usid).grid(row=0, column=1, padx=100, pady=20)

    Label(signup, text="비밀번호 : ").grid(row=1, column=0, padx=80, pady=20)
    Entry(signup, textvariable=uspw).grid(row=1, column=1, padx=100, pady=20)

    Label(signup, text="비밀번호 확인 : ").grid(row=2, column=0, padx=80, pady=20)
    Entry(signup, textvariable=uspwcheck).grid(row=2, column=1, padx=100, pady=20)


    Label(signup, text="이름 : ").grid(row=3, column=0, padx=80, pady=20)
    Entry(signup, textvariable=usname).grid(row=3, column=1, padx=100, pady=20)

    Label(signup, text="생년월일(YYYYMMDD) : ").grid(row=4, column=0, padx=80, pady=20)
    Entry(signup, textvariable=usbir).grid(row=4, column=1, padx=100, pady=20)

    Label(signup, text="email : ").grid(row=5, column=0, padx=80, pady=20)
    Entry(signup, textvariable=usem).grid(row=5, column=1, padx=100, pady=20)

    Label(signup, text="인증번호 : ").grid(row=6, column=0, padx=80, pady=20)
    Entry(signup, textvariable=usvar).grid(row=6, column=1, padx=100, pady=20)


    # 중복 체크 함수
    def check_id():
        db = pymysql.connect(host = 'localhost', user = 'root', password = '1111', charset='utf8mb4')  #db 연결
        cursor=db.cursor(pymysql.cursors.DictCursor)
        cursor.execute('USE Wave;');                    #Wave db 사용. (사용하던 Db가 있는 상황에서 진행.)

        flag = True
        #f = open("/Users/chang/Downloads/WAVE-main/wave/id_pw.txt", "r")
        #lines = f.readlines();   

        uid =usid.get()
        checkIdRe = "select ID from user_list where ID = '"+uid+"';"
        #print(usid.get())
        #print(checkIdRe)
        cursor.execute(checkIdRe);
        idlist = cursor.fetchall()
        if (idlist!=()):        #비어있지 않으면. 
            messagebox.showinfo("회원가입", "이미 존재하는 아이디 입니다")
                # print("이미 존재하는 아이디 입니다")
            flag = False
        else:
            messagebox.showinfo("회원가입", "사용할 수 있는 아이디 입니다")
            Button(signup, text="Sign up", command=signUp, state=NORMAL).grid(row=7, column=1, padx=10, pady=10)

        db.commit()
        db.close()

        # for item in lines:
        #     # 아이디 중복 확인
        #     idItem = item.split("//")
        #     if(idItem[0] == usid.get()) : 
        #         messagebox.showinfo("회원가입", "이미 존재하는 아이디 입니다")
        #         # print("이미 존재하는 아이디 입니다")
        #         flag = False
        # f.close()
        # if(flag):
        #     messagebox.showinfo("회원가입", "사용할 수 있는 아이디 입니다")
        #     Button(signup, text="Sign up", command=signUp, state=NORMAL).grid(row=4, column=1, padx=10, pady=10)

    def validate_date(date_text):
        try:
            datetime.datetime.strptime(date_text,"%Y%m%d")
            return True
        except ValueError:
            return False

    def sendmail():
        global idenNum
        idenNum=""
        for i in range(6):
            a=str(random.randrange(0,10))
            idenNum += a

        print(idenNum)

        uem = usem.get()
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()      # say Hello
        smtp.starttls()  # TLS 사용시 필요
        smtp.login('chjeon96@gmail.com', 'rfyejfdufjjzpfxq')
        
        msg = MIMEText('인증번호 : '+ idenNum)
        msg['Subject'] = 'Wave 인증번호 메일'

        msg['To'] = uem
        smtp.sendmail('chjeon96@gmail.com', uem, msg.as_string())
 
        smtp.quit()


    # 회원가입 함수
    def signUp():
        # 'a' : 쓰기모드이며 파일에 내용을 이어 쓸 때 사용하는 옵션입니다.
        # f = open("/Users/chang/Downloads/WAVE-main/wave/id_pw.txt", "a")
        # # print("sign_up:" + usid + ":" + uspw)
        # f.write(usid.get())
        # f.write("//")
        # f.write(uspw.get())
        # f.write("\n")
        # f.close()
        uid =usid.get()
        upw =uspw.get()
        upwch = uspwcheck.get()
        uname = usname.get()
        ubir = usbir.get()
        uem = usem.get()
        uvar = usvar.get()

        if(upw!=upwch):
            messagebox.showinfo("비밀번호", "비밀번호와 확인이 다릅니다.")
        elif(validate_date(ubir)==False):
            messagebox.showinfo("날짜", "생일 형식이 올바르지 않습니다 YYYYMMDD")
        elif(idenNum!=uvar):
            messagebox.showinfo("인증번호", "인증번호가 틀렸습니다.")
        else:    
            db = pymysql.connect(host = 'localhost', user = 'root', password = '1111', charset='utf8mb4')  #db 연결
            cursor=db.cursor(pymysql.cursors.DictCursor)
            cursor.execute('USE Wave;');  
            
            cursor.execute("INSERT into user_list values ("+"'"+uid + "','"+upw + "','"+ uname +"','"+ ubir+ "','"+ uem + "');");
            db.commit()
            db.close()

            signup.destroy()


    # 아이디 중복 체크 버튼
    Button(signup, text="ID check", command=check_id).grid(row=0, column=3, padx=10, pady=10)
    
    Button(signup, text="mail check", command=sendmail).grid(row=5, column=3, padx=10, pady=10)

    # 회원가입 버튼
    # 아이디 중복 체크 해야만 버튼 활성화
    Button(signup, text="Sign up", command=signUp, state=DISABLED).grid(row=7, column=1, padx=10, pady=10)


def check_data():
    # 로그인 - 아이디 / 비밀번호 확인
    #f = open("/Users/chang/Downloads/WAVE-main/wave/id_pw.txt", "r")
    # print("sign_up:" + usid + ":" + uspw)
    # 한줄씩 배열로 읽어옴
    #lines = f.readlines()
    db = pymysql.connect(host = 'localhost', user = 'root', password = '1111', charset='utf8mb4')  #db 연결
    cursor=db.cursor(pymysql.cursors.DictCursor)
    cursor.execute('USE Wave;');                    #Wave db 사용. (사용하던 Db가 있는 상황에서 진행.)

    logInError = 0
    #for item in lines:
        #idItem = item.split("//")
        # ID 확인
    user_idget =user_id.get()
    pwget = password.get()
    checkuserId = "select ID from user_list where ID = '"+user_idget+"' and '" + pwget +"';"
    cursor.execute(checkuserId);
    idpwlist = cursor.fetchall()
    print(checkuserId)

    print(idpwlist)
    if (idpwlist!=()):        #비어있지 않으면. 
        logInError = 1

        # if(idItem[0] == user_id.get()) : 
        #     # 해당 id에 맞는 비밀번호 확인
        #     if(idItem[1].split("\n")[0] == password.get()):
        #         logInError = 1
            
    if(logInError == 1):
        if user_id.get() == "host" and password.get() == "1111":
    
            mylist = window.grid_slaves()
            for i in mylist:
                i.destroy()

            window.geometry("2500x1500+0+0")  # width x height + x coor + y coor

            # window.attributes('-alpha',0.5)   # 투명도 조절. 0~1
            window.wm_attributes("-transparent", True)
            #window.wm_attributes("-topmost", 1)  # 창을 항상 상단에 배치 / 0 외 모든 인자 True
            window.configure(bg='systemTransparent')
            # window.attributes('-fullscreen',True)

            print("Logged IN Successfully")
            clock_width.grid()
            clock()

            WAVESocket.serverOpen('127.0.0.1', 12319)

        else:
            loginForParticipant('127.0.0.1',  12319, user_id.get())

    else:
        print("wrong password")
        # 로그인 정보가 유효하지 않음을 나타내는 팝업창 띄우기
        messagebox.showinfo("로그인 정보", "Check your Username/Password")
    
    #f.close()
    db.commit()
    db.close()


btn = Button(window, text="Login", command=check_data).grid(
    row=2, column=1, padx=10, pady=10)

btn_signup_start = Button(window, text="Sign Up", command=signupmain).grid(
    row=3, column=1, padx=10, pady=10)




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
