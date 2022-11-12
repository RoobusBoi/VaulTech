import tkinter as tk
import string
import random
import webbrowser
import cv2
import numpy as np
import pyperclip
import requests

# Code for password generator and checker
## Generator Code
password_chars = string.ascii_letters + string.digits + string.punctuation

def password_generator():
    password_field.delete(0)
    length = int(char_input.get())
    password = "".join([random.choice(password_chars) for _ in range(length)])
    password_field.insert(0, password)
    pyperclip.copy(password)
## Compromiser checker
def open():
    webbrowser.open("https://haveibeenpwned.com")


# Code of GUI
## This is the code of the loading screen
cap = cv2.VideoCapture('Boot Config.gif')
if (cap.isOpened()== False):
  print("Error opening video stream or file")
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(70) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()


## This is code of UI and button
window = tk.Tk()
HEIGHT = 720
WIDTH = 1080

window.title("VaulTech Password Manager v1.0")
window.config(height=HEIGHT, width=WIDTH)

background_image = tk.PhotoImage(file='Background.gif')

background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(window, bg='#00dcff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

lower_frame = tk.Frame(window, bg='#00acc7', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

button = tk.Button(lower_frame, text="Check if Password has been compromised", command=open)
button.place(relx=0.35, rely=0.5, relheight=0.3, relwidth=0.3)

label_title = tk.Label(frame, text="VaulTech", bg="#00dcff",fg="#f9f4f4",font=("Helvetica", 35, "bold"))
label_title.place(relwidth=1, relheight=1)

label_before_input = tk.Label(lower_frame, text="I want a password with",bg="#383e56",fg="#c5d7bd",font=("Helvetica", 15, "bold"))
label_before_input.place(relx=0.01, rely=0.01 ,relwidth=0.3, relheight=0.1)

char_input = tk.Entry(lower_frame, bg="#f9f4f4")
char_input.place(relx=0.317, rely=0.01, relwidth=0.175, relheight=0.1)
char_input.insert(0, "Enter length of password")
char_input.focus()

label_after_input = tk.Label(lower_frame, text="characters.",bg="#383e56",fg="#f9f4f4",font=("Helvetica", 15, "bold"))
label_after_input.place(relx=0.5, rely=0.01, relwidth=0.17, relheight=0.1)

generate_password_button = tk.Button(lower_frame, text="Generate Password & Copy to Clipboard",bg="#f9f4f4",height=4,width=55,command=password_generator)
generate_password_button.place(relx=0.7, rely=0.01, relwidth=0.3, relheight=0.1)

password_field = tk.Entry(lower_frame, bg="#f9f4f4",font=("Helvetica", 15, "bold"), width=40)
password_field.place(relx=0, rely=0.15, relwidth=1, relheight=0.1)

label_thanks = tk.Label(lower_frame, text="Developed and tested by the students of VIT Bhopal. Sashwat Kumar Verma, Abhishek Shukla, Paramjit Chaudhary, Mohammad Suboor Hussain Khan", width=40)
label_thanks.place(relx=0, rely=0.85, relwidth=1, relheight=0.1)

window.mainloop()