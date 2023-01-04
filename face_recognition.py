def face_recognizer():
    import cv2
    import pyttsx3
    from home_page import login
    import sqlite3

    engine=pyttsx3.init('sapi5')
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 2.0)    
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def call_by_name():
        connection = sqlite3.connect('Users/users.db')  # Creating a database connection
        cursor = connection.cursor()  # Creating a cursor
        names = cursor.execute("SELECT name FROM users")
        for name in names:
            say = "Welcome to our system" + " " + str(name)
            speak(say) 
            
        connection.commit()  # Commit changes
        connection.close()  # Closing the connection

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 2

    names = ['', 'deepak']

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 350)
    cam.set(4, 350)

    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:
        ret, img = cam.read()

        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            converted_image, 
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])

            if (accuracy < 100):
                call_by_name()
                cam.release()
                login()

            else:
                speak("Unknown User, Please Register First.")

        cv2.imshow('Camera', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
    