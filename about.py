from tkinter import *
from PIL import Image, ImageTk
from tkfontawesome import icon_to_image
import webbrowser
from tkinter import messagebox

def about_developers():
    
    window4 = Toplevel()
    window4.title("Technoz AI | Developers")
    width = window4.winfo_screenwidth()
    height = window4.winfo_screenheight()
    window4.geometry("%dx%d" % (width, height))
    window4.iconbitmap("favicon/favicon_image.ico")
    window4.config(bg="#2C3333")

    def deepak_fb():
        answer_fb = messagebox.askyesno(title="Confirmation", message="Do you want to open Deepak's Facebook Account?")
        if answer_fb:
            webbrowser.open("https://facebook.com/deepaksarangi29701")
    def deepak_insta():
        answer_insta = messagebox.askyesno(title="Confirmation", message="Do you want to open Deepak's Instagram Account?")
        if answer_insta:
            webbrowser.open("https://instagram.com/deepak_sarangi")
    def deepak_mail():
        pass
    def deepak_linkedin():
        answer_linkedin = messagebox.askyesno(title="Confirmation", message="Do you want to open Deepak's Linkedin Account?")
        if answer_linkedin:
            webbrowser.open("https://www.linkedin.com/in/deepak-sarangi-4a666a1ba?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BhAT5gga8Q86ufpxIU7Q2kQ%3D%3D")

    def virendra_fb():
        answer_fb = messagebox.askyesno(title="Confirmation", message="Do you want to open Virendra's Facebook Account?")
        if answer_fb:
            webbrowser.open("https://www.facebook.com/profile.php?id=100014784036198")
    def virendra_insta():
        answer_insta = messagebox.askyesno(title="Confirmation", message="Do you want to open Virendra's Instagram Account?")
        if answer_insta:
            webbrowser.open("https://instagram.com/vir.endra201")
    def virendra_mail():
        pass
    def virendra_linkedin():
        answer_linkedin = messagebox.askyesno(title="Confirmation", message="Do you want to open Virendra's Linkedin Account?")
        if answer_linkedin:
            webbrowser.open("https://www.linkedin.com/in/virendra-mohan")

    def yash_fb():
        answer_fb = messagebox.askyesno(title="Confirmation", message="Do you want to open Yash's Facebook Account?")
        if answer_fb:
            webbrowser.open("https://www.facebook.com/yash.sharma.9862")
    def yash_insta():
        answer_insta = messagebox.askyesno(title="Confirmation", message="Do you want to open Yash's Instagram Account?")
        if answer_insta:
            webbrowser.open("https://instagram.com/yash_s.h.a.r.m.a_")
    def yash_mail():
        pass
    def yash_linkedin():
        answer_linkedin = messagebox.askyesno(title="Confirmation", message="Do you want to open Yash's Linkedin Account?")
        if answer_linkedin:
            webbrowser.open("https://www.linkedin.com/in/yash-sharma-240501")

    happiness = Image.open("images/happiness.png")
    happy_image = ImageTk.PhotoImage(happiness)
    happy_label = Label(window4, image=happy_image, bg="#2C3333")
    happy_label.place(x=60, y=450)
    happy_label.dontloseit = happy_image

    photo1 = Image.open("images/deepak.jpg")
    image1 = ImageTk.PhotoImage(photo1)

    photo2 = Image.open("images/virendra.jpg")
    image2 = ImageTk.PhotoImage(photo2)

    photo3 = Image.open("images/yash.jpg")
    image3 = ImageTk.PhotoImage(photo3)

    top_label = Label(window4, text="-:  Our Developers  :-", fg="White", bg="black", font=('Comic Sans MS', 25), 
                    justify=CENTER, padx=460, pady=5)
    top_label.pack(padx=10, pady=12)

    frame1 = LabelFrame(window4, text="", padx=5, pady=5, bg="black", highlightbackground="white", highlightthickness=1)
    frame1.place(x=40, y=85)

    photo_label = Label(frame1, image=image1, bg="black")
    photo_label.grid(row=0, column=0, padx=2, pady=2, sticky='w')
    photo_label.dontloseit = image1

    sub_frame1 = LabelFrame(frame1, text="", bg="black", bd=0, padx=20, pady=2)
    sub_frame1.grid(row=0, column=1)
    label1 = Label(sub_frame1, text="Deepak Sarangi", fg="#00FFD1", bg="black", font=("Comic Sans MS", 25, "bold"))
    label1.pack(padx=8, pady=2)

    label2 = Label(sub_frame1, text="Python Developer", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label2.pack(padx=10, pady=2)

    label3 = Label(sub_frame1, text="Full-Stack Web Developer", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label3.pack(padx=10, pady=2)
    
    label4 = Label(sub_frame1, text="Degree: B.Tech(ECE) 2019-23", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label4.pack(padx=10, pady=2)

    label5 = Label(sub_frame1, text="Age: 22", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label5.pack(padx=7, pady=2)

    label6 = Label(sub_frame1, text="Email ID: deepak29701@gmail.com", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label6.pack(padx=7, pady=2)

    fb = icon_to_image("facebook", fill="#4267B2", scale_to_width=28)
    fb_button = Button(sub_frame1, image=fb, padx=2, bg="black", bd=0, command=deepak_fb, activebackground="black")
    fb_button.pack(side=LEFT, padx=(47,10), pady=4)
    fb_button.dontloseit = fb

    insta = icon_to_image("instagram", fill="#4267B2", scale_to_width=26)
    insta_button = Button(sub_frame1, image=insta, padx=2, bg="black", bd=0, command=deepak_insta, activebackground="black")
    insta_button.pack(side=LEFT, padx=10, pady=4)
    insta_button.dontloseit = insta

    linkedin = icon_to_image("linkedin", fill="#4267B2", scale_to_width=26)
    linkedin_button = Button(sub_frame1, image=linkedin, padx=2, bg="black", bd=0, command=deepak_linkedin, activebackground="black")
    linkedin_button.pack(side=LEFT, padx=10, pady=4)
    linkedin_button.dontloseit = linkedin

    mail = icon_to_image("envelope", fill="#4267B2", scale_to_width=30)
    mail_button = Button(sub_frame1, image=mail, padx=2, bg="black", bd=0, command=deepak_mail, activebackground="black")
    mail_button.pack(side=LEFT, padx=10, pady=4)
    mail_button.dontloseit = mail

    frame2 = LabelFrame(window4, text="", padx=5, pady=5, bg="black", highlightbackground="white", highlightthickness=1)
    frame2.place(x=635, y=85)

    photo_label = Label(frame2, image=image2, bg="black")
    photo_label.grid(row=0, column=0, padx=2, pady=2, sticky='w')
    photo_label.dontloseit = image2

    sub_frame2 = LabelFrame(frame2, text="", bg="black", bd=0, padx=20, pady=2)
    sub_frame2.grid(row=0, column=1)
    label1 = Label(sub_frame2, text="Raja Virendra Mohan", fg="#00FFD1", bg="black", font=("Comic Sans MS", 25, "bold"))
    label1.pack(padx=8, pady=2)

    label2 = Label(sub_frame2, text="Python Developer", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label2.pack(padx=10, pady=2)

    label3 = Label(sub_frame2, text="Web Developer", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label3.pack(padx=10, pady=2)
    
    label4 = Label(sub_frame2, text="Degree: B.Tech(ECE) 2019-23", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label4.pack(padx=10, pady=2)

    label5 = Label(sub_frame2, text="Age: 22", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label5.pack(padx=10, pady=2)

    label6 = Label(sub_frame2, text="Email ID: mvirendra0926@gmail.com", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label6.pack(padx=7, pady=2)

    fb = icon_to_image("facebook", fill="#4267B2", scale_to_width=28)
    fb_button = Button(sub_frame2, image=fb, padx=2, bg="black", bd=0, command=virendra_fb, activebackground="black")
    fb_button.pack(side=LEFT, padx=(67,10), pady=4)
    fb_button.dontloseit = fb

    insta = icon_to_image("instagram", fill="#4267B2", scale_to_width=26)
    insta_button = Button(sub_frame2, image=insta, padx=2, bg="black", bd=0, command=virendra_insta, activebackground="black")
    insta_button.pack(side=LEFT, padx=10, pady=4)
    insta_button.dontloseit = insta

    linkedin = icon_to_image("linkedin", fill="#4267B2", scale_to_width=26)
    linkedin_button = Button(sub_frame2, image=linkedin, padx=2, bg="black", bd=0, command=virendra_linkedin, activebackground="black")
    linkedin_button.pack(side=LEFT, padx=10, pady=4)
    linkedin_button.dontloseit = linkedin

    mail = icon_to_image("envelope", fill="#4267B2", scale_to_width=30)
    mail_button = Button(sub_frame2, image=mail, padx=2, bg="black", bd=0, command=virendra_mail, activebackground="black")
    mail_button.pack(side=LEFT, padx=10, pady=4)
    mail_button.dontloseit = mail

    frame3 = LabelFrame(window4, text="", padx=5, pady=5, bg="black", highlightbackground="white", highlightthickness=1)
    frame3.place(x=355, y=375)

    photo_label = Label(frame3, image=image3, bg="black")
    photo_label.grid(row=0, column=0, padx=2, pady=2, sticky='w')
    photo_label.dontloseit = image3

    sub_frame3 = LabelFrame(frame3, text="", bg="black", bd=0, padx=20, pady=2)
    sub_frame3.grid(row=0, column=1)
    label1 = Label(sub_frame3, text="Yash Sharma", fg="#00FFD1", bg="black", font=("Comic Sans MS", 25, "bold"))
    label1.pack(padx=8, pady=2)

    label2 = Label(sub_frame3, text="Python Developer", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label2.pack(padx=10, pady=2)
    
    label3 = Label(sub_frame3, text="Web Developer", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label3.pack(padx=10, pady=2)

    label4 = Label(sub_frame3, text="Degree: B.Tech(ECE) 2019-23", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label4.pack(padx=10, pady=2)

    label5 = Label(sub_frame3, text="Age: 22", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label5.pack(padx=10, pady=2)

    label6 = Label(sub_frame3, text="Email ID: yash240501@gmail.com", font=("Helvetica", 13, "bold"), fg="white", bg="black")
    label6.pack(padx=7, pady=2)

    fb = icon_to_image("facebook", fill="#4267B2", scale_to_width=28)
    fb_button = Button(sub_frame3, image=fb, padx=2, bg="black", bd=0, command=yash_fb, activebackground="black")
    fb_button.pack(side=LEFT, padx=(57,10), pady=4)
    fb_button.dontloseit = fb

    insta = icon_to_image("instagram", fill="#4267B2", scale_to_width=26)
    insta_button = Button(sub_frame3, image=insta, padx=2, bg="black", bd=0, command=yash_insta, activebackground="black")
    insta_button.pack(side=LEFT, padx=10, pady=4)
    insta_button.dontloseit = insta

    linkedin = icon_to_image("linkedin", fill="#4267B2", scale_to_width=26)
    linkedin_button = Button(sub_frame3, image=linkedin, padx=2, bg="black", bd=0, command=yash_linkedin, activebackground="black")
    linkedin_button.pack(side=LEFT, padx=10, pady=4)
    linkedin_button.dontloseit = linkedin

    mail = icon_to_image("envelope", fill="#4267B2", scale_to_width=30)
    mail_button = Button(sub_frame3, image=mail, padx=2, bg="black", bd=0, command=yash_mail, activebackground="black")
    mail_button.pack(side=LEFT, padx=10, pady=4)
    mail_button.dontloseit = mail