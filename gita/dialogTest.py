import tkinter as tk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd

tk.Tk().withdraw()

mb.showinfo("프로젝트", "프로젝트 설문조사")

yesno = mb.askyesno('질문', '프로젝트는 잘 진행되고 있으신가요?')

if yesno:
    mb.showinfo('예를 선택', '참 잘 했어요.')
else:
    mb.showinfo('아니요를 선택', '이런. 화이팅')
    trouble = sd.askstring(
        '문제 입력', '진행에 어려운 점을 입력해주세요.\n(미입력 시 종료)',
        initialvalue='문제점')
    if trouble =='' or trouble ==None: quit()
    mb.showinfo('문제해결', trouble + '을 해결하세요.')
