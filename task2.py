import tkinter as tk 
from tkinter import *

window=tk.Tk()
window.title("Pokemon Adventure")
window.geometry("550x650")

mainphoto=PhotoImage(file="main.png")
minimapphoto=PhotoImage(file="minimap.png")
logophoto=PhotoImage(file="logo.png")
compassphoto=PhotoImage(file="compass.png")

label1=tk.Label(window, width=100, text="mini map", image=minimapphoto, compound="bottom")
button1=tk.Button(width=10, text="Map")
button2=tk.Button(width=10,text="Inventory")
button3=tk.Button(width=10,text="Pokedex")
button4=tk.Button(width=10,text="Roster")
button5=tk.Button(width=10,text="Journal")
button6=tk.Button(width=10,text="Help")
button7=tk.Button(width=10,text="Shop")
label2=tk.Label(width=425, image=mainphoto, compound="bottom")
label3=tk.Label(width=120, image=logophoto, compound="bottom")
label4=tk.Label(width=100, image=compassphoto, compound="bottom")

label1.place(x=445,y=50)
button1.place(x=460,y=160)
button2.place(x=460,y=185)
button3.place(x=460,y=205)
button4.place(x=460,y=230)
button5.place(x=460,y=255)
button6.place(x=460,y=280)
button7.place(x=460,y=305)
label2.place(x=10,y=50)
label3.place(x=265, y=525)
label4.place(x=25, y=500)


window.mainloop()


