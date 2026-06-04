import tkinter as tk
from tkinter import ttk


window=tk.Tk()
window.title("tk")
window.geometry("350x125")
label1=tk.Label(window, width=10, text="Principal")
label2=tk.Label(width=10, text="Interest Rate")
label3=tk.Label(width=10, text="Years")
entry1=tk.Entry(width=12)
entry2=tk.Entry(width=12)
combo = ttk.Combobox(window,values=["1","2","3"], width=10)
label4=tk.Label(width=10, text="Amount")
entry3=tk.Entry(width=10)


label1.place(x=25)
label2.place(x=135)
label3.place(x=250)
entry1.place(x=25, y=25)
entry2.place(x=135, y=25)
combo.place(x=250, y=25)
label4.place(x=75, y=100)
entry3.place(x=135,y=100)
window.mainloop()