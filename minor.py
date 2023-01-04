from tkinter import *
from tkinter import ttk
import time
import pyttsx3
import sqlite3

#Setting Engine For Speech 

engine=pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)    
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def speakOnStart():
    speak("Hello Everyone, Welcome to our AI Project")
    speak("I am Sophie, I will help you to use this system")
    speak("Hope you enjoy your time.")
    speak("So, let's get started.")

splash_window = Tk()
splash_window.geometry("600x300+400+200")
splash_window.config(background="black")
splash_window.overrideredirect(True)
splash_label1 = Label(splash_window, text="Technoz AI Starter", font=("Helvetica", 40, "bold"), fg="white", bg="black")
splash_label1.pack(padx=10, pady=20)
splash_label2 = Label(splash_window, text="Welcome to Technoz AI System", font=("Helvetica", 25, "bold"), fg="green", bg="black")
splash_label2.pack(padx=15)

def progress_move():
    progress_bar.start()
    splash_window.update_idletasks()

def get_started():
    global progress_bar
    loading = Label(splash_window, text="Loading...", bg="black", fg="white", font=('Comic Sans MS', 12))
    loading.place(x=50, y=220)
    progress_bar = ttk.Progressbar(splash_window, orient=HORIZONTAL, length=500, mode='indeterminate')
    progress_bar.place(x=50, y=250)
    progress_move()
    splash_window.after(3500, main_window)

def main_window():
    splash_window.destroy()
    from PIL import Image, ImageTk
    from register_page import register
    from about import about_developers
    from face_recognition import face_recognizer
    
    window = Tk()
    window.title("Technoz AI")
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry("%dx%d" % (width, height))
    window.iconbitmap("favicon/favicon_image.ico")
    window.config(bg="black")

    def command_over():
        pass

    def open_about():
        about_developers()

    menu_bar = Menu(window,bd= 1, background="#00D7FF", fg="green")
    window.config(menu=menu_bar)

    file_menu = Menu(menu_bar, tearoff=False, background="#00D7FF", fg="black")
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=command_over)
    file_menu.add_command(label="About", command=open_about)
    file_menu.add_command(label="Exit", command=window.destroy)

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
        
    about_frame = LabelFrame(window, text="About", padx=40, pady=30, font=('Comic Sans MS', 17), fg="#00D7FF", 
                            bg="black", borderwidth=1)
    about_frame.place(x=70, y=200)
    about_label1 = Message(about_frame, text="Welcome to our AI environment.", fg="#00D7FF", bg="black", font=('Comic Sans MS', 12), 
                        justify=LEFT, aspect=800)
    about_label1.pack(padx=5, pady=3)
    about_label2 = Message(about_frame, text="It is a General-Purpose Artificial Intelligence System", fg="#00D7FF", 
                        bg="black", font=('Comic Sans MS', 12), justify=LEFT, aspect=800)
    about_label2.pack(padx=5, pady=3)
    about_label3 = Message(about_frame, text="Created by Deepak Sarangi, Raja Virendra Mohan and Yash Sharma", 
                        fg="#00D7FF", bg="black", font=('Comic Sans MS', 12), justify=LEFT, aspect=800)
    about_label3.pack(padx=5, pady=3)

    title_label = Label(window, text="Technoz AI", fg='white', font=('Comic Sans MS', 50), bg='black')
    title_label.place(x=140, y=50)
    tag_line = Label(window, text="Where the future is being ready...", fg='blue', bg='black', font=('Cursive', 15))
    tag_line.place(x=430, y=140)

    clocktime = Label(window, text="", fg="#72FFFF", font=("Helvetica", 40), bg='black')
    clocktime.place(x=850, y=60)
    time_zone_label = Label(window, text="", fg='#72FFFF', font=('Helvetica', 20), bg='black')
    time_zone_label.place(x=875, y=120)
    date_label = Label(window, text="", fg='#72FFFF', font=('Helvetica', 20), bg='black')
    date_label.place(x=865, y=150)

    clock()

    label1 = Label(window, text="New User?", fg="white", font=('Comic Sans MS', 12), bg="black")
    label1.place(x=180, y=480)
    register_button = Button(window, text="Register", fg='red', bg='black', font=('Arial', 15), padx=8, pady=7, activebackground="green", activeforeground="white", command=lambda:[register()])
    register_button.place(x=170, y=520)
    label2 = Label(window, text="Already Registered?", fg="white", font=('Comic Sans MS', 12), bg="black")
    label2.place(x=330, y=480)
    login_button = Button(window, text="Login", fg='red', bg='black', font=('Arial', 15), padx=8, pady=7, activebackground="green", activeforeground="white", command=face_recognizer())
    login_button.place(x=360, y=520)
    
    img = ImageTk.PhotoImage(Image.open("images/image2.png"))
    image_label = Label(window, image=img, bg="white", highlightbackground="black", highlightthickness=1)
    image_label.place(x=700, y=230)
    image_label.dontloseit = img

    end_label = Label(window, text="Copyright  ©  2022 | Technoz AI System | Designed by Deepak, Virendra & Yash", font=("Arial", 13, "bold"), fg="white", bg="black")
    end_label.place(x=300, y=600)

    window.update()
    speakOnStart()
    
splash_button = Button(splash_window, text="Get Started...", fg="white", bg="green", font=("Arial", 12, "bold"), padx=5, pady=2, command=get_started)
splash_button.place(x=50, y=180)

mainloop()
