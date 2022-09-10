import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import 画像抽出
import urllib.request, urllib.error
import os.path
import time
def show_pop():
    error_message = QMessageBox()   
    error_message.setWindowTitle("エラー")
    error_message.setText("正しいURLを入れてください。")
    error_message.setStandardButtons(QMessageBox.Ok)
    error_message.buttonClicked.connect(popup)
    sys.exec_()
def popup(i):
    print(i.text())
def URL_input():
    try:
        rootpath = os.path.abspath(os.path.dirname("__file__"))
        direct = QFileDialog.getExistingDirectory(None,"rootpath", rootpath)
        urlo = url.toPlainText()
        print(urlo)
        if direct == "" or urlo =="":
            print("1")
            return
    except Exception as t:
        print(t)
        return
    else:
        opener = urllib.request.build_opener()
        opener.addheaders = [("User-Agent", "Mozilla/5.0")]
        urllib.request.install_opener(opener)
        try:
            url_temp = urllib.request.urlopen(urlo)
            url_temp.close()
        except Exception as y:
            print(y)
            return
        else:
            #print(urlo)
            #print(direct)
            print("3")
            画像抽出.get_URL(urlo,direct)
app = QApplication(sys.argv)
root = QWidget()
root.resize(300,250)
root.setWindowTitle("画像ダウンローダー")
#ここから入力フォーム
url = QTextEdit(root)
url.setPlaceholderText("URLを入力してください。")
#ここからボタン
button = QPushButton(root)
button.setText("OK")
button.clicked.connect(URL_input)
button.move(100,200)

root.show()
sys.exit(app.exec_())