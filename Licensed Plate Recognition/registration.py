from tkinter import *
from tkinter import messagebox
#from tkinter import ttk
from ttkthemes import themed_tk as tk
import database as database


title = "Number Plate Recognition"


def RegistrationPage(frame, raised_frame, homePage):
    def addValuesToDatabase():
        plateNoText = plateNoTextField.get()
        nameText = nameTextField.get()
        carNameText = carNameTextField.get()

        if(plateNoText and nameText and carNameText):
            plateNoTextField.delete(0,END)
            nameTextField.delete(0,END)
            carNameTextField.delete(0,END)


            report = database.create(plateNoText, nameText, carNameText)
            messagebox.showinfo('Message', report)
        else:
            messagebox.showinfo('Message', 'Fill in all the fields')

    heading = Label(frame, text=title, bg="#fff", fg="#282935", width=25, height=3, font=('arial', 25, 'bold'), )
    heading.place(x=0, y=0)

    plateNoLabel = Label(frame,text="Plate Number:", bg="#282935", fg="#fff", height=2, font=('arial', 13, 'bold'))
    plateNoLabel.place(x=150, y=150)

    plateNoTextField = Entry(frame, width=25)
    plateNoTextField.place(x=160, y=180)

    nameLabel = Label(frame,text="Name:", bg="#282935", fg="#fff", height=2, font=('arial', 13, 'bold'))
    nameLabel.place(x=150, y=200)

    nameTextField = Entry(frame, width=25)
    nameTextField.place(x=160, y=230)

    carNameLabel = Label(frame,text="Car Name:", bg="#282935", fg="#fff", height=2, font=('arial', 13, 'bold'))
    carNameLabel.place(x=150, y=250)

    carNameTextField = Entry(frame, width=25)
    carNameTextField.place(x=160, y=280)

    backButton = Button(frame, text="Back", bg="#fff", fg="#282935", width=5, font=('arial', 12, 'bold'), command=lambda:raised_frame(homePage))
    backButton.place(x=100, y=360)

    submitButton = Button(frame, text="Submit", bg="#fff", fg="#282935", width=5,
                          command=addValuesToDatabase,
                          font=('arial', 12, 'bold'), )
    submitButton.place(x=330, y=360)

    # frame.mainloop()
