from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk



#------------------importing pages--------------------------
import homepage as HomePage
import registration as Reg
import scanImage as scan

title="Number Plate Recognition"

def raised_frame(frame):
    frame.tkraise()




root =Tk()
root.wm_minsize(500,400)
root.wm_maxsize(500,500)
root.configure(background="#282935")


f1= Frame(root,width=500, height=500,background="#282935")
f2= Frame(root,width=500, height=500,background="#282935")
f3= Frame(root,width=500, height=500,background="#282935")

for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky='news')

HomePage.HomePage(f1, raised_frame,f2,f3)
Reg.RegistrationPage(f2, raised_frame, f1)
scan.ScanPage(f3, raised_frame, f1)

raised_frame(f1)
root.mainloop()

