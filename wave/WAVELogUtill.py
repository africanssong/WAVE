from tkinter import *
import tkinter.ttk as ttk


''' WAVE LOG 기록창 생성 함수 
- 서버에게만 이벤트가 활성화됨(클라이언트는 로그기록 확인 불가)
- 여러명의 클라이언트(참가자)가 서버와 연결되면 로그창에 해당 로그가 찍힘 
'''


def genLogEvent():
    ''' 외부 이벤트 생성(WAVE LOG 기록창) '''
    window = Toplevel()

    ''' 타이틀 설정 '''
    window.title('WAVE LOG 기록창')

    ''' 이벤트 크기 설정 '''
    window.geometry("500x500")

    WAVELogChat(window)


def WAVELogChat(window):
    WAVELogChatFrame = Frame(window)

    ''' 스크롤바 생성 '''
    scrollbar = Scrollbar(WAVELogChatFrame)

    ''' 스크롤바 위치 설정 '''
    scrollbar.pack(side='right', fill='y')
    global chatLog
    chatLog = Text(WAVELogChatFrame, width=62, height=24,
                    state='disabled', yscrollcommand=scrollbar.set)
    chatLog.pack(side='left')  # place(x=20, y=60)
    scrollbar['command'] = chatLog.yview

    chatLog = Text(window, width=65, height=29, state='disabled', spacing2=2)
    chatLog.place(x=20, y=60)

    ''' 닫기 버튼 생성(해당 버튼 클릭 시 이벤트 종료)'''
    logButton = Button(window, text="닫기", command=window.destroy)

    ''' 닫기 버튼을 이벤트의 중앙 하단에 위치시킴'''
    logButton.pack(side='bottom', pady="5")



def testMenu():

    app = Tk()

    app.title('WAVELog')
    app.geometry("300x500")

    mainMenu = Menu(app)
    app.config(menu=mainMenu)

    WAVEMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="파일", menu=WAVEMenu)

    WAVEMenu.add_command(label="로그 기록 확인", command=genLogEvent)
    WAVEMenu.add_separator()  # 구분선 추가
    WAVEMenu.add_command(label="종료", command=app.destroy)

    app.mainloop()


# main()
