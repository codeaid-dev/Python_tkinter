import tkinter
import time

root = tkinter.Tk()
root.title('Clock')

time_info = tkinter.Label(root, text='00:00:00', font=('Helvetica',48), fg='green', bg='black')
time_info.pack(pady=20)
date_info = tkinter.Label(root, text='', font=('Helvetica',16))
date_info.pack(pady=10)

def clock():
    global time_info,date_info
    fmt = '%I:%M:%S %p'
    fmd = '%Y年%m月%d日 %A\n%Z'
    t = time.localtime()
    str_time = time.strftime(fmt, t)
    str_date = time.strftime(fmd, t)
    time_info.config(text=str_time)
    date_info.config(text=str_date)
    root.after(1000, clock)

clock()

root.mainloop()
