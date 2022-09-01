import tkinter
import tkinter.font
from tkinter import ttk
from tkinter import *
import time
# pyinstaller -i=./wave.ico -F -w main.py     # i : 아이콘 모양, f: 하나의 파일, w : 콘솔실행없음.
# pip install pillow
# pyinstaller -i=./wave.ico -n wave -F -w main.py  wave 이름 설정. 

window=tkinter.Tk()
#  sdafsdf
font = tkinter.font.Font(family="Consolas",size=40)

window.title("practic")

#window.attributes('-alpha',1)   # 투명도 조절. 0~1
window.wm_attributes("-transparent", True)
window.wm_attributes("-topmost", 1) # 창을 항상 상단에 배치 / 0 외 모든 인자 True
#window size
window.geometry("800x500+20+20")   #width x height + x coor + y coor
#window.attributes('-fullscreen',True)
window.resizable(True, True)           # width, height   size var



textstr = "FDL@kookmin.ac.kr %Y-%m-%d %H:%M:%S "
FDL =""
for i in range(120):
    FDL += textstr
    if ((i+1)%4==0):
        FDL+="\n\n"

def clock(): # 현재 시간 표시 / 반복
   live_T = time.strftime(FDL) # Real Time
   clock_width.config(text=live_T)
   clock_width.after(200, clock) # .after(지연시간{ms}, 실행함수)

clock_width = tkinter.Label(window, fg="black",font=font)
clock_width.configure(bg='systemTransparent')



def check_data():
    if user_id.get() == "1" and password.get() == "1":
        window2 = Toplevel(window)
        window2.geometry("2500x1500+0+0")   #width x height + x coor + y coor
        
        #window.attributes('-alpha',0.5)   # 투명도 조절. 0~1
        window2.wm_attributes("-transparent", True)
        window2.wm_attributes("-topmost", 1) # 창을 항상 상단에 배치 / 0 외 모든 인자 True
        window2.configure(bg='systemTransparent')
        #window.attributes('-fullscreen',True)

        print("Logged IN Successfully")
        clock_width.grid()
        clock()

    else:
        print("Check your Usernam/Password")

user_id, password = StringVar(), StringVar()
id =  Label(window, text = "Username : ").grid(row = 0, column = 0, padx = 100, pady = 20)
id_in =   Entry(window, textvariable = user_id).grid(row = 0, column = 1, padx = 100, pady = 20)

pw = Label(window, text = "Password : ").grid(row = 1, column = 0, padx = 100, pady = 20)
pw_in =  Entry(window, textvariable = password).grid(row = 1, column = 1, padx = 100, pady = 20)

btn= Button(window, text = "Login", command = check_data).grid(row = 2, column = 1, padx = 10, pady = 10)











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
#text.insert(INSERT,"FDL\n")
#text.insert(END,"—")
#text.pack()

window.mainloop()