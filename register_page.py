from tkinter import *
from PIL import Image, ImageTk
import pyttsx3
import time
from tkinter import messagebox
from sample_generator import sampleGenerator

def register():
    import sqlite3

    window3 = Toplevel()
    window3.title("Technoz AI | Registration")
    width = window3.winfo_screenwidth()
    height = window3.winfo_screenheight()
    window3.geometry("%dx%d" % (width, height))
    window3.iconbitmap("favicon/favicon_image.ico")
    window3.config(bg="black")

    def face_recognition():
        engine=pyttsx3.init('sapi5')
        engine.setProperty('rate', 190)
        engine.setProperty('volume', 1.0)    
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        engine.say("Your face recognition process is being ready.")
        engine.say("Please look into your camera.")
        sampleGenerator()
        engine.runAndWait()


    def create_database():
        global Id 
        connection = sqlite3.connect('Users/users.db')  # Creating a database connection
        cursor = connection.cursor()  # Creating a cursor
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                        id INT,
                        name TEXT,
                        age INT,
                        email TEXT
                    )""")
        
        Id = 0 
         
        connection.commit()  # Commit changes
        connection.close()  # Closing the connection

    def data_collection():
        create_database()
        global Id
        connection = sqlite3.connect('Users/users.db')  # Creating a database connection
        cursor = connection.cursor()  # Creating a cursor
        Id += 1
        cursor.execute("INSERT INTO users VALUES (:Id, :name, :age, :email)",
                        {
                            'Id': Id,
                            'name': name.get(),
                            'age': age.get(),
                            'email': email.get()
                        })    
        connection.commit()  # Commit changes
        connection.close()  # Closing the connection

        name.delete(0,END)
        age.delete(0,END)
        email.delete(0,END)


    def popup():
        data_collection()
        response = messagebox.askokcancel("Successful Registration", "Thank You for registering successfully")
        if response == 1:
            window3.destroy()  

    def clock():
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        am_pm = time.strftime("%p")
        day = time.strftime("%A")
        weekday = time.strftime("%d")
        month = time.strftime("%m")
        year = time.strftime("%Y")
        time_zone = time.strftime("%Z")
        clocktime.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
        clocktime.after(1000, clock)
        time_zone_label.config(text=time_zone)
        date_label.config(text=weekday + "-" + month + "-" + year + ", " + day)


    title_label = Label(window3, text="User Registration", fg="white", font=('Comic Sans MS', 45),bg="black")
    title_label.place(x=150, y=60)

    form_frame = LabelFrame(window3, text="Registration Form", font=('Comic Sans MS', 20), fg="blue", padx=60, pady=15, bg="#BCCEF8", borderwidth=1)
    form_frame.place(x=100, y=200)

    name_label = Label(form_frame, text="Name", fg="white", font=('Comic Sans MS', 20),bg="#BCCEF8")
    name_label.grid(row=3, column=0)
    name = Entry(form_frame, fg="black", bg="#EDEDED", font=('Helvetica', 16))
    name.grid(row=3, column=1, sticky="ew", padx=8)

    age_label = Label(form_frame, text="Age", fg="white", font=('Comic Sans MS', 20),bg="#BCCEF8")
    age_label.grid(row=4, column=0)
    age = Entry(form_frame, fg="black", bg="#EDEDED", font=('Helvetica', 16))
    age.grid(row=4, column=1, sticky="ew", padx=8)

    email_label = Label(form_frame, text="Email ID", fg="white", font=('Comic Sans MS', 20),bg="#BCCEF8")
    email_label.grid(row=5, column=0)
    email = Entry(form_frame, fg="black", bg="#EDEDED", font=('Helvetica', 16))
    email.grid(row=5, column=1, sticky="ew", padx=8)

    terms_button = Checkbutton(form_frame,text="I Agree to Terms & Conditions", bg="#BCCEF8" , onvalue=1, offvalue=0, font=('Helvetica', 16), activebackground="#BCCEF8")
    terms_button.grid(row=6, column=0, pady=10)

    fr_button = Button(form_frame, text="Ready for Face Recognition", fg='black', bg='grey', font=('Arial', 15), padx=8, pady=7, activebackground="green",
                             activeforeground="white", highlightbackground="black", highlightthickness=2, bd=0, command=face_recognition)
    fr_button.grid(row=7, column=0, padx=5, pady=20)

    register_button = Button(form_frame, text="Register", fg='black', bg='grey', font=('Arial', 15), padx=8, pady=7, activebackground="green",
                             activeforeground="white", highlightbackground="black", highlightthickness=2, bd=0, command=popup)
    register_button.grid(row=7, column=1, pady=20)

    clocktime = Label(window3, text="", fg="#72FFFF", font=("Helvetica", 40), bg='black')
    clocktime.place(x=850, y=60)
    time_zone_label = Label(window3, text="", fg='#72FFFF', font=('Helvetica', 20), bg='black')
    time_zone_label.place(x=875, y=120)
    date_label = Label(window3, text="", fg='#72FFFF', font=('Helvetica', 20), bg='black')
    date_label.place(x=865, y=150)

    clock()

    end_label = Label(window3, text="Copyright  ©  2022 | Technoz AI System | Designed by Deepak, Virendra & Yash", font=("Arial", 13, "bold"), fg="white", bg="black")
    end_label.place(x=300, y=600)

    window3.mainloop()