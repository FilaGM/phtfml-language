import tkinter as tk
#formspace project
#==formspace window1==
window1 = tk.Tk()
window1.geometry("500x500")
window1.title("Window")
Title = tk.Label(window1,text="Title")
Title.pack()
#~script source~ START
for a in range(0,10):
    print("Hello world")
#~script source~ END
#<looping forms>
window1.mainloop()
#formspace end