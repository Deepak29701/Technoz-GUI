from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time
import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import webbrowser
import os
import wikipedia
from englisttohindi.englisttohindi import EngtoHindi



engine=pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
engine.setProperty('volume', 2.0)    
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def login():
    
    window2 = Toplevel()
    window2.title("Technoz AI | Login")
    width = window2.winfo_screenwidth()
    height = window2.winfo_screenheight()
    window2.geometry("%dx%d" % (width, height))
    window2.iconbitmap("favicon/favicon_image.ico")
    window2.config(bg="black")

    def give_weather_report(city):
        import requests
        import json

        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        api = "db446ae8aa63bad08186118b1b7a0648"
        url = base_url  + "q=" + city + "&appid=" + api
        res = requests.get(url)

        x = res.json()

        if res.status_code == 200:

            y = x["main"]       # store the value of "main" key in variable y
            current_temperature = y["temp"]   # store the value corresponding to the "temp" key of y
            
            current_pressure = y["pressure"]    # store the value corresponding to the "pressure" key of y
            
            current_humidity = y["humidity"]    # store the value corresponding to the "humidity" key of y
            
            z = x["weather"]    # store the value of "weather" key in variable z
            
            weather_description = z[0]["description"]       # store the value corresponding to the "description" key at the 0th index of z
            

            temperature_text = "Sophie: The temperature is " + str(current_temperature) + "Degree Kelvin"
            label = Label(chat_box, text=temperature_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
            label.pack()
            speak(f"Temperature is {current_temperature} degree Kelvin")
            pressure_text = "Sophie: The atmospheric pressure is " + str(current_pressure) + "hPa"
            label = Label(chat_box, text=pressure_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
            label.pack()
            speak(f"Atmospheric pressure is {current_pressure} hPa")
            humidity_text = "Sophie: The Humidity is " + str(current_humidity) + "%"
            label = Label(chat_box, text=humidity_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
            label.pack()
            speak(f"Humidity is {current_humidity} percent")
            weather_text = "Sophie: The weather report is " + str(weather_description)
            label = Label(chat_box, text=weather_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
            label.pack()
            speak(f"The weather report is {weather_description}")

        else:
            print(" City Not Found ")


    def speechRecognition():
        
        def takeCommand():
            global chat_box
            r = sr.Recognizer()
            with sr.Microphone(sample_rate=48000) as source:
                l_text = "Listening..."
                label = Label(chat_box, text=l_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                label.pack()
                label.dontloseit = l_text
                r.pause_threshold = 10
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, phrase_time_limit=5)
            
            try:
                r_text = "Recognizing....."
                label = Label(chat_box, text=r_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                label.pack()
                label.dontloseit = r_text
                query = r.recognize_google(audio,language='en-us')
                query_var = f'You: {query}'
                label = Label(chat_box, text=query_var, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                label.pack()
                label.dontloseit = query_var
                
            except Exception as e:
                #print(e) 
                cu_text = "Sophie: I cannot understand what you have said, so say that again please....."
                label = Label(chat_box, text=cu_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                label.pack()
                label.dontloseit = cu_text
                return "None"

            query = query.lower()
            return query

        def wishMe():
            global chat_box
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                time_greet = 'Sophie: Good Morning'
                label = Label(chat_box, text=time_greet, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                label.pack()
                label.dontloseit = time_greet
                speak("Good Morning")
            elif hour>=12 and hour<18:
                time_greet = 'Sophie: Good Afternoon!!!'
                label = Label(chat_box, text=time_greet, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                label.pack()
                label.dontloseit = time_greet
                speak("Good Afternoon")
            elif hour>=18 and hour<21:
                time_greet = 'Sophie: Good Evening!!!'
                label = Label(chat_box, text=time_greet, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                label.pack()
                label.dontloseit = time_greet
                speak("Good Evening")
            else:
                time_greet = 'Sophie: Good Night!!!'
                label = Label(chat_box, text=time_greet, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                label.pack()
                label.dontloseit = time_greet
                speak("Good Night")
            
            h_text = "Sophie: I am Sophie, Please tell me how can I help you?"
            label = Label(chat_box, text=h_text, fg="#00D7FF", bg="black", 
                        font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
            label.pack()
            label.dontloseit = h_text
            speak("I am Sophie,Please tell me how can I help you")


        #The Main Body of the Project.

        def main():
            global position
            wishMe()
            while True:
                global chat_box
                query = takeCommand()
                user_response = f'You: {query}' 
                label = Label(chat_box, text=user_response, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                label.pack()
                label.dontloseit = user_response
        
                if 'hello' in query:
                    greet = 'Sophie: Hello '
                    label = Label(chat_box, text=greet, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = greet
                    speak("Hello Sir")

                elif 'open youtube' in query:
                    oy_text = "Sophie: Opening YouTube..."
                    label = Label(chat_box, text=oy_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = oy_text
                    speak("Opening Youtube...")
                    webbrowser.open("youtube.com")       
                
                elif 'tell me about' in query:
                    speak("Searching Wikipedia.....")
                    query = query.replace("wikipedia"," ")
                    results = wikipedia.summary(query,sentences=2) + ""
                    speak("According to Wikipedia")
                    label = Label(chat_box, text=results, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = results
                    speak(results)

                elif 'open google' in query:
                    og_text = "Sophie: Opening Google..."
                    label = Label(chat_box, text=og_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = og_text
                    speak("Opening Google...")
                    webbrowser.open("google.com")

                elif 'open mail' in query:
                    om_text = "Sophie: Opening Mail..."
                    label = Label(chat_box, text=om_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = om_text
                    speak("Opening Mail...")
                    webbrowser.open("mail.google.com")

                elif 'open amazon' in query:
                    oa_text = "Sophie: Opening Amazon..."
                    label = Label(chat_box, text=oa_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = oa_text
                    speak("Opening Amazon...")
                    webbrowser.open("amazon.in")
                    
                elif 'open project' in query:
                    project_dir='F:\Deepak\B.Tech_Work\FUTURE_PROJECT\Python'
                    folder = os.listdir(project_dir)
                    op_text = "Sophie: You have different files to open in it,So I am opening the most preferable one..."
                    label = Label(chat_box, text=op_text, 
                                fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = op_text
                    speak("You have different files to open in it,So I am opening the most preferable one...")
                    label = Label(chat_box, text=folder, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = folder
                    speak("Opening the file you want me to open...")
                    os.startfile(os.path.join(project_dir,folder[7]))

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    Time = f'Sophie: Sir,the time is {strTime}. '
                    label = Label(chat_box, text=Time, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = Time
                    speak(f"Sir,the time is {strTime}")

                elif 'open code' in query:
                    oc_text = "Sophie: Opening Visual Studio Code..."
                    label = Label(chat_box, text=oc_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = oc_text
                    speak("Opening Visual Studio Code...")
                    code_Path = "F:\Deepak\B.Tech_Work\Software\Visual Studio Code.lnk"
                    os.startfile(code_Path)
                
                elif 'open file' in query:
                    of_text = "Sophie: Opening Project PPT..."
                    label = Label(chat_box, text=of_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = of_text
                    speak("Opening Project PPT...")
                    file_Path = "F:\Deepak\B.Tech_Work\FUTURE_PROJECT\Project Analysis.pptx"
                    os.startfile(file_Path)
                
                elif 'open teams' in query:
                    ot_text = "Sophie: Opening Microsoft Teams..."
                    label = Label(chat_box, text=ot_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = ot_text
                    speak("Opening Microsoft Teams...")
                    class_Path = "C:\\Users\\hp\\Downloads\\Teams_windows_x64.exe"
                    os.startfile(class_Path)

                elif 'give me the weather report' in query:
                    speak("Please tell me the name of the city")
                    city = takeCommand()
                    give_weather_report(city)
                
                elif 'sleep' in query:
                    s_text = "Sophie: Ok Sir, Have a nice day."
                    label = Label(chat_box, text=s_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = s_text
                    speak("Ok Sir, Have a nice day.")
                    speechRecognition.quit()

                elif 'about yourself' in query:
                    y1_text = "I am Voice Assistant for Technoz AI System"
                    y2_text = "I was created to assist the user to get their task done easily"
                    y3_text = "I can perform various tasks."
                    label = Label(chat_box, text=y1_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = y1_text
                    speak("I am Voice Assistant for Technoz AI System")
                    label = Label(chat_box, text=y2_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = y2_text
                    speak("I was created to assist the user to get their task done easily")
                    label = Label(chat_box, text=y3_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = y3_text
                    speak("I can perform various tasks.")

                elif 'thank you' in query:
                    label_text = "Sophie: Your Welcome Sir, do you want me to do something else for you no."
                    label = Label(chat_box, text=label_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = label_text
                    speak("Your Welcome Sir, do you want me to do something else now")
                    cm = takeCommand()
                    if(cm == 'no'):
                        s_text = "Sophie: Ok Sir, I am going to sleep now."
                        label = Label(chat_box, text=s_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                        label.pack()
                        label.dontloseit = s_text
                        speak("Ok Sir, I am going to sleep now")
                        window2.destroy()
                        
                else:
                    w_text = "I am waiting for your next order."
                    label = Label(chat_box, text=w_text, fg="#00D7FF", bg="black", font=("Times Roman", 11, "bold"), justify=LEFT, wraplength=30)
                    label.pack()
                    label.dontloseit = w_text
                    speak("I am waiting for your next order.")

        
    main()


    menu_bar = Menu(window2, background="#00D7FF", fg="green", bd=0)
    window2.config(menu=menu_bar)
    File = Menu(menu_bar, tearoff=False, background="#00D7FF", fg="black") 
    menu_bar.add_cascade(label="File", menu=File)
    File.add_command(label="Exit", command=window2.destroy)

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

    image = ImageTk.PhotoImage(Image.open("images/image1.png"))
    my_image1 = Label(window2, image=image, bg="black")
    my_image1.place(x=0, y=0)

    start_button = Button(window2, text="Start", fg="white", bg="green", font=("Arial", 18, "bold"), 
                        padx=10, pady=3, bd=0, activebackground="white", activeforeground="black", command=speechRecognition)
    start_button.place(x=450, y=90)

    clock_frame = LabelFrame(window2, text="", bg="black", bd=0)
    clock_frame.place(x=1028, y=70)

    clocktime = Label(clock_frame, text="", fg="#72FFFF", font=("Helvetica", 30), bg='black')
    clocktime.pack()
    time_zone_label = Label(clock_frame, text="", fg='#72FFFF', font=('Helvetica', 15), bg='black')
    time_zone_label.pack()
    date_label = Label(clock_frame, text="", fg='#72FFFF', font=('Helvetica', 15), bg='black')
    date_label.pack()

    clock()

    box_label = Label(window2, text="Chatbox", fg="white", bg="#00D7FF", font=('Comic Sans MS', 13), padx=2, pady=2)
    box_label.place(x=955, y=205)
    
    global chat_box
    chat_box = Frame(window2, padx=2, pady=10, background="black", width=315, height=390, highlightbackground="#00D7FF", highlightthickness=2)
    chat_box.place(x=955, y=238)
    
    
    robo_image = ImageTk.PhotoImage(Image.open("images/robo-image.png"))
    robo_label = Label(window2, image=robo_image, bg="black", width=80, height=100)
    robo_label.place(x=1180, y=520)
    robo_label.dontloseit = robo_image
    
    end_label = Label(window2, text="Copyright  ©  2022 | Technoz AI System | Designed by Deepak, Virendra & Yash", 
                    font=("Arial", 13, "bold"), fg="white", bg="black")
    end_label.place(x=250, y=600)


    window2.mainloop()