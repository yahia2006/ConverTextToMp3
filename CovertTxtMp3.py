#أستدعاء المكاتب

from langdetect import detect
from tkinter import *
from tkinter import filedialog
from gtts import gTTS
from PIL import Image,ImageTk
from tkinter import messagebox




#دوال البرنامج

def GetInpText():
    return text_area.get("1.0",END)

def arabicConvert():
    sound=gTTS(GetInpText(),lang="ar")
    sound.save(filedialog.asksaveasfilename())
    messagebox.showinfo("convert info","Done Converting ✔")

def englishConvert():
    sound=gTTS(GetInpText(),lang="en")
    sound.save(filedialog.asksaveasfilename())
    messagebox.showinfo("convert info","Done Converting ✔")
    

def Convert():
    if detect(GetInpText())=="ar" and GetInpText()!="":
        arabicConvert()
    if detect(GetInpText())=="en" and GetInpText()!="":
        englishConvert()
    







#واجهة المستخدم


app=Tk()
app.title("Convert Text To Mp3")
app.iconbitmap("icon.ico")
app.geometry("750x550+230+150")
app.config(background="white")
app.resizable(False,False)

logo=ImageTk.PhotoImage(Image.open("img.png"))
lab=Label(image=logo,bg="white")
lab.pack()

lab2=Label(text="Enter Text Here ",fg="#111",bg="white",font=(14,14))
lab2.place(x=315,y=170)



text_area = Text(app, wrap='word', height=15, width=50,bd=7)
text_area.pack(side=LEFT, expand=True)



btn=Button(text="Convert To Mp3",bg="green",fg="white",width=70,font=(14,14),justify='center',command=Convert)
btn.place(x=0,y=511)


app.mainloop()

