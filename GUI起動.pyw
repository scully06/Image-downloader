from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.filedialog
import 画像抽出
import sys
import urllib.request, urllib.error
root =Tk()
root.title("URLから画像抽出")
#関数の作成
def URL_input():
    direct = tkinter.filedialog.askdirectory(initialdir = dir)
    print(direct)
    if direct == "" or t.get() =="":
        return
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-Agent", "Mozilla/5.0")]
    urllib.request.install_opener(opener)
    try:
        url_temp = urllib.request.urlopen(t.get())
        url_temp.close()
    except:
        messagebox.showwarning("エラー","正しいURLを入力してください。")
        return
    else:
        画像抽出.get_URL(t.get(),direct)
#ウィジェットの作成
try:
    frame1 = ttk.Frame(root,padding=16)
    label1 = ttk.Label(frame1,text ="URLを入力してください。")
    t = StringVar()
    entry1 = ttk.Entry(frame1,textvariable=t)
    button1 = ttk.Button(
        frame1,text="OK",
        command=URL_input
    )
    direct = StringVar()
except Exception as e:
    print("2")
    print(e)
#レイアウト
frame1.pack()
label1.grid(row = 0, column = 0)
entry1.grid(row = 0, column = 1)
button1.grid(row = 0, column = 2)
root.mainloop()