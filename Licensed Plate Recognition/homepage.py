from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk



title="Number Plate Recognition"


def HomePage(f1, raised_frame, reg, scan):

    heading = Label(f1, text=title, bg="#fff", fg="#282935",width=25, height= 3, font=('arial', 25, 'bold'),)
    heading.place(x=0,y=0)

    registrationButton = Button(f1, text="Register", bg="#fff", fg="#282935", width=20, font=('arial', 15, 'bold'), command=lambda:raised_frame(reg))
    registrationButton.place(x=130, y=250)

    scanButton = Button(f1, text="Scan", bg="#fff", fg="#282935", width=20, font=('arial', 15, 'bold'), command=lambda:raised_frame(scan))
    scanButton.place(x=130, y=300)


    # root.mainloop()



'''
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root = Tk()
# root.get_themes()
# root.set_themes("radiance")
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()

'''