from tkinter import *
# --------------------------VARIABLES------------------------------------------- #
BLUE = "#632780"
DARK_BLUE ="#352962"
WHITE = "#FFFFFF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("New Pass - Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="newpass_img.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website = Label(text="Website :")
website.grid(row=1, column=0)
username = Label(text="Email/Username :")
username.grid(row=2, column=0)
password = Label(text="Password :")
password.grid(row=3, column=0)

# Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
user_entry = Entry(width=52)
user_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons
generate_pass = Button(text="Generate Password", bg=DARK_BLUE, fg=WHITE)
generate_pass.grid(row=3, column=2)
save_data = Button(text="Save Data", width=44, bg=BLUE, fg=WHITE)
save_data.grid(row=4, column=1, columnspan=2)

window.mainloop()