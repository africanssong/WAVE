import tkinter
import tkinter.font
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

import time
from webbrowser import get
# pyinstaller -i=./wave.ico -F -w main.py     # i : 아이콘 모양, f: 하나의 파일, w : 콘솔실행없음.
# pip install pillow
# pyinstaller -i=./wave.ico -n wave -F -w main.py  wave 이름 설정.

window = tkinter.Tk()
#  sdafsdf
font = tkinter.font.Font(family="Consolas", size=40)

window.title("practic")

# window.attributes('-alpha',1)   # 투명도 조절. 0~1
window.wm_attributes("-transparent", True)
window.wm_attributes("-topmost", 1)  # 창을 항상 상단에 배치 / 0 외 모든 인자 True
# window size
window.geometry("800x500+20+20")  # width x height + x coor + y coor
# window.attributes('-fullscreen',True)
window.resizable(True, True)           # width, height   size var

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
    signup.attributes("-topmost", 1)
    signup.title("Sign up")
    signup.grid()
    signup.geometry("800x300+20+20")  # width x height + x coor + y coor
    signup.resizable(True, True)

    # 회원가입 id/pw 입력 칸 생성
    usid, uspw = StringVar(), StringVar()
    Label(signup, text="Username : ").grid(row=0, column=0, padx=100, pady=20)
    Entry(signup, textvariable=usid).grid(row=0, column=1, padx=100, pady=20)

    Label(signup, text="Password : ").grid(row=1, column=0, padx=100, pady=20)
    Entry(signup, textvariable=uspw).grid(row=1, column=1, padx=100, pady=20)

    # signUp()
    
    # 아이디 중복 체크 버튼 (근데 아직 안 되는)
    # UnboundLocalError: local variable 'check_id' referenced before assignment
    Button(signup, text="ID check", command=check_id).grid(row=2, column=1, padx=10, pady=10)

    # 회원 가입 버튼 만들어야 함
    Button(signup, text="Sign up", command=signUp).grid(row=4, column=1, padx=10, pady=10)

    # 중복 체크 함수
    def check_id():
        f = open("id_pw.txt", "r")
        # print("sign_up:" + usid + ":" + uspw)
        # 한줄씩 배열로 읽어옴
        lines = f.readlines();      
        print(lines)
        for item in lines:
            if(item == usid.get()) : 
                messagebox.showinfo("회원가입", "이미 존재하는 아이디 입니다")
                print("이미 존재하는 아이디 입니다")
        f.close()


    # 회원가입 함수
    def signUp():
        # 'a' : 쓰기모드이며 파일에 내용을 이어 쓸 때 사용하는 옵션입니다.
        f = open("id_pw.txt", "a")
        # print("sign_up:" + usid + ":" + uspw)
        f.write(usid.get(), uspw.get())
        uu = "id.."
        vv = "pw.."
        f.write(uu, vv)
        f.close()
        
        


def check_data():
    user_id_str = user_id.get()
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

    else:
        # 로그인 정보가 유효하지 않음을 나타내는 팝업창 띄우기
        messagebox.showinfo("로그인 정보", "Check your Username/Password")
        print("Check your Usernam/Password")

btn = Button(window, text="Login", command=check_data).grid(
    row=2, column=1, padx=10, pady=10)

btn_signup_start = Button(window, text="Sign Up", command=signupmain).grid(
    row=3, column=1, padx=10, pady=10)


FDL = " @kookmin.ac.kr %Y-%m-%d %H:%M:%S   "

def clock():  # 현재 시간 표시 / 반복
    live_T = time.strftime(FDL)  # Real Time
    multiFDL = " "

    for i in range(20):
        multiFDL += user_id.get()+live_T
        if ((i+1) % 4 == 0):
            multiFDL += "\n\n"
    
    clock_width.config(text= multiFDL)
    clock_width.after(200, clock)  # .after(지연시간{ms}, 실행함수)

# signupmain()
# signUp()


# FDL = " FDL@kookmin.ac.kr %Y-%m-%d %H:%M:%S "


# def clock():  # 현재 시간 표시 / 반복
    
#     live_T = time.strftime(FDL)  # Real Time

#     multiFDL = ""
#     for i in range(20):
#         multiFDL += user_id.get()+FDL
#         if ((i+1) % 4 == 0):
#             multiFDL += "\n\n"

#     clock_width.config(text= multiFDL)
#     clock_width.after(200, clock)  # .after(지연시간{ms}, 실행함수)







# #button
# count=0
# def countUP():
#     global count
#     count +=1
#     label.config(text=str(count))

# button = tkinter.Button(window, overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
# button.pack()

# #entry
# def calc(event):
#     label.config(text="결과="+str(eval(entry.get())))

# entry=tkinter.Entry(window)
# entry.bind("<Return>", calc)
# entry.pack()

# #list box

# listbox = tkinter.Listbox(window, selectmode='extended', height=0)
# listbox.insert(0, "1번")
# listbox.insert(1, "2번")
# listbox.insert(2, "2번")
# listbox.insert(3, "2번")
# listbox.insert(4, "3번")
# #listbox.delete(1, 2)
# listbox.activate(3)
# listbox.pack()


#text= Text(window)
#
# text.insert(INSERT,"FDL\n")
# text.insert(END,"—")
# text.pack()
 
window.mainloop()
