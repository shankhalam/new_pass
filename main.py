from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("New Pass - Password Manager")
window.config(padx=25, pady=25)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="newpass_img.png")
canvas.create_image(100, 100, image=logo_image)
canvas.pack()

window.mainloop()