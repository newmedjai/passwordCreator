import random
import tkinter
from tkinter import *



pencere = Tk()
pencere.title("ŞİFRE ÜRETİCİ PROGRAMI")
pencere.geometry('1024x768')
pencere.iconbitmap("sifre.ico")
#pencere.configure(background="red")


buyukHarf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "Q", "P", "R", "S", "T",
             "U", "V", "Y", "Z"]
kucukHarf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "q", "p", "r", "s", "t",
             "u", "v", "y", "z"]
sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


yazis1=tkinter.Label(pencere,text="1-Sadece küçük harflerden oluştur",font="3",fg="black")
yazis1.pack()
yazis2=tkinter.Label(pencere,text="2-Büyük ve küçük harflerden oluştur",font="3",fg="black")
yazis2.pack()
yazis3=tkinter.Label(pencere,text="3-Büyük, küçük harfler ve sayılardan oluştur",font="3",fg="black")
yazis3.pack()

yazib=tkinter.Label(pencere,text="",font="5")
yazib.pack()

#yazi9=tkinter.Label(pencere,text="DİKKAT!!!",font="10",fg="red")
#yazi9.pack()

#yazi3=tkinter.Label(pencere,text="En fazla 24 hane girebilirsiniz",font="3",fg="red")
#yazi3.pack()
yazi4=tkinter.Label(pencere,text="Hane sayısı",font="3",fg="black")
yazi4.pack()

giris=tkinter.Entry(width=20)
giris.pack()

yazi5=tkinter.Label(pencere,text="",font="3",fg="blue")
yazi5.pack()

yazi6=tkinter.Label(pencere,text="Seçenek",font="3",fg="black")
yazi6.pack()

giris2=tkinter.Entry(width=20)
giris2.pack()



def uret():
    veri=int(giris.get())
    secenek =int(giris2.get())

    if secenek==3:
        liste=buyukHarf+kucukHarf+sayilar
        sifre = random.sample(liste, veri)
        yazi2.config(text="Oluşturulan şifreniz:")
        yazi1.config(text=sifre,fg="blue")
    elif secenek==2:
        liste=buyukHarf+kucukHarf
        sifre = random.sample(liste, veri)
        yazi2.config(text="Oluşturulan şifreniz:")
        yazi1.config(text=sifre,fg="blue")
    elif secenek==1:
        liste=kucukHarf
        sifre = random.sample(liste, veri)
        yazi2.config(text="Oluşturulan şifreniz:")
        yazi1.config(text=sifre,fg="blue")

def temizle():
    giris.delete(0,tkinter.END)
    giris2.delete(0,tkinter.END)
    yazi1.config(text="")
    yazi2.config(text="")
def exit():
    pencere.destroy()

buton1 = Button(pencere)
buton1.pack()
buton1.config(text="Üret", bg="blue", fg="yellow",font="5", command=uret)

butonTemizle=Button(pencere)
butonTemizle.config(text="Temizle",font="5", command=temizle)
butonTemizle.pack()


yazi2=tkinter.Label(pencere,text="Şifre üretmek için hane sayısını ve seçenek girip 'Üret' tuşuna basınız",font="5")
yazi2.pack()

butonExit=Button(pencere)
butonExit.config(text="Çıkış",font="5",fg="red",command=exit)
butonExit.pack()

etiket2=tkinter.Label(pencere,text="                 ")
etiket2.pack()


yazi2=tkinter.Label(pencere,text="",font="5")
yazi2.pack()
yazi1=tkinter.Label(pencere,text="",font="5")
yazi1.pack()

mainloop()





