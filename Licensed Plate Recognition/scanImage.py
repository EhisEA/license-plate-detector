from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import themed_tk as tk

from PIL import ImageTk, Image

import scanForPlateNumber as scanPlate
import database as database
title="Number Plate Recognition"


def ScanPage(frame, raised_frame, homePage):

    heading = Label(frame, text=title, bg="#fff", fg="#282935", width=25, height=3, font=('arial', 25, 'bold'), )
    heading.place(x=0, y=0)

    backButton = Button(frame, text="Back", bg="#fff", fg="#282935", width=5, font=('arial', 12, 'bold'),
                        command=lambda: raised_frame(homePage))
    backButton.place(x=50, y=460)

    WIDTH = 300
    HEIGHT = 300

    imageLabel = Label(frame)
    imageLabel.place(x=10, y=140)

    def displayImage(filename):
       if(filename):
           IM = Image.open(filename).resize((WIDTH, HEIGHT), Image.ANTIALIAS)
           # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
           img = ImageTk.PhotoImage(IM)
           imageLabel.image = img  # <== this is were we anchor the img object
           imageLabel.configure(image=img)
           dirLabel['text'] = filename
           scanImageButton["state"]="normal"



    def scanImage():
        path = dirLabel['text']
        print(scanPlate.main(path))
        plateNumber = scanPlate.main(path)
        plateLabel['text'] = plateNumber
        seacrchDatabaseButton["state"] = "normal"


    def fileDialog():
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
        displayImage(filename)

    def searchDatabase():
        report, dates = database.search(plateLabel['text'])
        if(report):

            newWindow = Tk()
            date_frame = Frame(newWindow, width=300, height=200, background="#282935")
            date_frame.place(x=330, y=60)
            newWindow.wm_minsize(500, 300)
            newWindow.wm_maxsize(500, 300)
            newWindow.configure(background="#282935", )

            scroll = Scrollbar(date_frame)
            scroll.pack(side="right", fill="y")

            list = Listbox(date_frame, )
            list.pack(side="left", fill="y")
            newPlateLabel = Label(newWindow, text="LICENSE NUMBER:", bg="#282935", fg="#fff",
                                  font=('arial', 15, 'bold'))
            newPlateLabel.place(x=20, y=10)
            newPlateLabel = Label(newWindow, text="OWNER NAME:", bg="#282935", fg="#fff", font=('arial', 15, 'bold'))
            newPlateLabel.place(x=20, y=70)
            newPlateLabel = Label(newWindow, text="CAR NAME:", bg="#282935", fg="#fff", font=('arial', 15, 'bold'))
            newPlateLabel.place(x=20, y=130)
            newPlateLabel = Label(newWindow, text="DATE CREATED:", bg="#282935", fg="#fff", font=('arial', 15, 'bold'))
            newPlateLabel.place(x=20, y=190)
            newPlateLabel = Label(newWindow, text="VIEWED DATE:", bg="#282935", fg="#fff", font=('arial', 15, 'bold'))
            newPlateLabel.place(x=300, y=30)

            newPlateLabelValue = Label(newWindow, text=report[0][0], bg="#282935", fg="#aaa",
                                       font=('arial', 15, 'bold'))
            newPlateLabelValue.place(x=40, y=40)
            newPlateLabelValue = Label(newWindow, text=report[0][1], bg="#282935", fg="#aaa",
                                       font=('arial', 15, 'bold'))
            newPlateLabelValue.place(x=40, y=100)
            newPlateLabelValue = Label(newWindow, text=report[0][2], bg="#282935", fg="#aaa",
                                       font=('arial', 15, 'bold'))
            newPlateLabelValue.place(x=40, y=160)
            newPlateLabelValue = Label(newWindow, text=report[0][3], bg="#282935", fg="#aaa",
                                       font=('arial', 15, 'bold'))
            newPlateLabelValue.place(x=40, y=220)
            a = 1
            for data in dates:
                list.insert(a, str(a) + "). " + data[0] + "  ")
                a = 1 + a

            scroll.config(command=list.yview)
            list.config(yscrollcommand=scroll.set)
            newWindow.mainloop()

            # messagebox.showinfo('Message', "Lincense number exist in database")
        else:
            messagebox.showinfo('Message', "Lincense number is not in database")


        return


    browseButton = Button(frame, text="Browse file", bg="#fff", fg="#282935", font=('arial', 12, 'bold'),
                        command=fileDialog)
    browseButton.place(x=320, y=160)

    scanImageButton = Button(frame, text="Scan Image For Plate", state=DISABLED, bg="#fff", fg="#282935", font=('arial', 12, 'bold'),
                          command=scanImage)
    scanImageButton.place(x=320, y=200)

    scanHeading = Label(frame, text="Plate Number:", bg="#282935", fg="#fff", font=('arial', 15, 'bold'))
    scanHeading.place(x=320, y=250)

    plateLabel = Label(frame, text="", bg="#282935", fg="#fff", font=('arial', 15, 'bold'))
    plateLabel.place(x=320, y=280)

    seacrchDatabaseButton = Button(frame, text="Search Database", state=DISABLED,  bg="#fff", fg="#282935", font=('arial', 12, 'bold'),
                       command=searchDatabase)
    seacrchDatabaseButton.place(x=320, y=360)


    dirLabel = Label(frame, text="", fg="#fff", font=('arial', 15, 'bold'))


