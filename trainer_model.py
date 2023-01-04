def model_trainer():
    import cv2
    import numpy as np
    from PIL import Image
    import os
    import pyttsx3
    import tkinter
    from tkinter import messagebox

    engine=pyttsx3.init('sapi5')
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 2.0)    
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    path = 'samples'

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def Images_And_Labels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []

        for imagePath in imagePaths:
            gray_img = Image.open(imagePath).convert('L')
            img_arr = np.array(gray_img, 'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_arr)

            for (x,y,w,h) in faces:
                faceSamples.append(img_arr[y:y+h,x:x+w])
                ids.append(id)

        return faceSamples,ids

    speak("Training faces, It will take a few seconds so please wait...")

    faces,ids = Images_And_Labels(path)
    recognizer.train(faces, np.array(ids))

    recognizer.write('trainer/trainer.yml')

    response = messagebox.askokcancel("Model Trainer","AI Model is trained successfully!!!")
    if response == 1:
        speak("Your Model is trained successfully, now you can login.")
        