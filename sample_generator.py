def sampleGenerator():
    import cv2
    import tkinter
    import pyttsx3 
    from tkinter import messagebox
    from trainer_model import model_trainer

    engine=pyttsx3.init('sapi5')
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 2.0)    
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 350)
    cam.set(4, 350)

    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    face_id = input("Enter a numeric user ID here:")
    speak("We are ready to take your samples.")
    count = 0

    while True:
        ret, img = cam.read()
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(converted_image, 1.3, 5)

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            count += 1

            cv2.imwrite("samples/face." + str(face_id) + '.' + str(count) + ".jpg", converted_image[y:y+h,x:x+w])
            cv2.imshow('image', img)

        k = cv2.waitKey(60) & 0xff

        if k == 27:
            break
        elif count >= 10:
            break

    response = messagebox.askokcancel("Samples","Your samples are taken successfully!!!")
    if response == 1:
        speak("Your samples are taken, now we are going to train the model for you.")
        model_trainer()
    cam.release()
    cv2.destroyAllWindows()