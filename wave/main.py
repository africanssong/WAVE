import tkinter
import tkinter.font
from tkinter import *
import time
# pyinstaller -i=./wave.ico -F -w main.py     # i : 아이콘 모양, f: 하나의 파일, w : 콘솔실행없음.
# pip install pillow
# pyinstaller -i=./wave.ico -n wave -F -w main.py  wave 이름 설정. 

window=tkinter.Tk()

font = tkinter.font.Font(family="Consolas",size=60)

window.title("practic")

window.attributes('-alpha',0.1)   # 투명도 조절. 0~1
window.wm_attributes("-topmost", 1) # 창을 항상 상단에 배치 / 0 외 모든 인자 True
#window size
window.geometry("2500x1500+0+0")   #width x height + x coor + y coor
#window.attributes('-fullscreen',True)
window.resizable(True, True)           # width, height   size var

#label
##textstr = "FDLFDL \n" 
#FDL =""
#for i in range(3):
#    FDL += textstr

#label=tkinter.Label(window, text=FDL, fg="black",font=font)

#label.pack()

textstr = "FDL@kookmin.ac.kr %Y-%m-%d %H:%M:%S "
FDL =""
for i in range(120):
    FDL += textstr
    if ((i+1)%4==0):
        FDL+="\n"

def clock(): # 현재 시간 표시 / 반복
   live_T = time.strftime(FDL) # Real Time
   clock_width.config(text=live_T)
   clock_width.after(200, clock) # .after(지연시간{ms}, 실행함수)


#clock_frame = Frame(window)
#clock_frame.pack()

clock_width = tkinter.Label(window, fg="black",font=font)
clock_width.grid()
clock()

# clock_width = tkinter.Label(window, fg="black",font=font)
# clock_width.pack()
# clock()



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
