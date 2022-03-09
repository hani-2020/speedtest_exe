from cProfile import label
from tkinter import *
import speedtest
def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/((1024**2)*8), 2))+" MB/sec"
    up=str(round(sp.upload()/((1024**2)*8), 2))+" MB/sec"
    lab_down.config(text=down)
    lab_up.config(text=up)
sp=Tk()
sp.title("Speed Test By Oola")
sp.geometry("500x300")
sp.config(bg="#143f5c")
lab=Label(sp, text="Speed Test By Oola", font=("MS Serif", 20, "bold"), bg="#143f5c", fg="white")
lab.place(x=120, y=25)
lab=Label(sp, text="Download Speed", font=("MS Serif", 14, "bold"), bg="#143f5c", fg="white")
lab.place(x=10, y=125)
lab_down=Label(sp, text="00", font=("MS Serif", 14, "bold"), bg="#143f5c", fg="white")
lab_down.place(x=50, y=150)
lab=Label(sp, text="Upload Speed", font=("MS Serif", 14, "bold"), bg="#143f5c", fg="white")
lab.place(x=350, y=125)
lab_up=Label(sp, text="00", font=("MS Serif", 14, "bold"), bg="#143f5c", fg="white")
lab_up.place(x=350, y=150)
button=Button(sp, text="Start Test", font=("MS Serif", 14, "bold"), relief=RAISED, bg="#ffffff", command=speedcheck)
button.place(x=200, y=200, height=50, width=115)
sp.mainloop()