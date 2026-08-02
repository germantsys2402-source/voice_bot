from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow


import subprocess
import webbrowser
import speech_recognition as sr

from ai import*


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

app=QApplication([]) 
ex=Widget()
recognizer = sr.Recognizer()
def capture_voice_input():
    with sr.Microphone() as micro:
        print("Слухаю...")
        audio = recognizer.listen(micro)
    return audio    

def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("Ви сказали: " + text)
    except:
        text = " "
        print("I dont understand.")
    return text    
def process_voice_command(text):
    if "hello" in text.lower():
        print("How can I help you?")
    if "calculator" in text.lower():
        subprocess.call(['calc'])
    if "scratch" in text.lower():
        subprocess.call(["C:/Users/1/AppData/Local/Programs/Scratch 3/Scratch 3.exe"])
    elif "youtube" in text.lower():
        webbrowser.open("https://www.youtube.com/?app=desktop&gl=UA&hl=uk")
    elif "gemini" in text.lower():
        webbrowser.open("https://gemini.google.com/app?hl=uk")
    elif "canva" in text.lower():
        webbrowser.open("https://www.canva.com/")
    elif "pinterest" in text.lower():
        webbrowser.open("https://ru.pinterest.com/#top")
    elif "rozetka" in text.lower():
        webbrowser.open("https://rozetka.com.ua/?gad_source=1&gad_campaignid=23862418707&gbraid=0AAAAAq0EKAOd32a8Jrbyq50QHIUuf2MFC&gclid=Cj0KCQjwjIPSBhCCARIsABGyK7v1ApmuQ-P8KnncfbdfbxEzBPFiz5x_IUjqooQ5n43ozL30chHeH4IaAu_6EALw_wcB")
    elif "kahoot" in text.lower():
        webbrowser.open("https://kahoot.it/")
    if "micro" in text.lower():
        result = generate(text[5:])
        ex.ui.textEdit.append(result)  
        ex.ui.textEdit.append("\n")
        
def main():
    audio = capture_voice_input()
    a = convert_voice_to_text(audio)
    process_voice_command(a)



def text_ai():
    line = ex.ui.lineEdit.text()
    if line != "":
        result = generate(line)
        ex.ui.textEdit.append(result) 
        ex.ui.textEdit.append("\n")
        ex.ui.lineEdit.clear()



ex.ui.start_zapis.clicked.connect(main)
ex.ui.pushButton.clicked.connect(text_ai)
ex.ui.textEdit.setReadOnly(True)
ex.show()
app.exec_()       




