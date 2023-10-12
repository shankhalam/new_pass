from tkinter import *
from tkinter import messagebox
import random
import pyperclip as pc
import json

# --------------------------VARIABLES------------------------------------------- #
BLUE = "#632780"
DARK_BLUE = "#352962"
WHITE = "#FFFFFF"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_numbers = random.randint(3, 4)
    nr_symbols = random.randint(2, 3)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pc.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_entry = website_entry.get().lower()
    user_name = user_entry.get()
    pass_word = password_entry.get()

    if len(web_entry) == 0:
        messagebox.showwarning(title="Empty Website", message="Please fill up Website field")
    elif len(user_name) == 0:
        messagebox.showwarning(title="Empty Username/Email", message="Please fill up Username field")
    elif len(pass_word) == 0:
        messagebox.showwarning(title="Empty Password", message="Please fill up Password field")
    else:
        new_data = {
            web_entry: {
                "Email": user_name,
                "Password": pass_word
            }
        }
        # if Database not exist,
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
                messagebox.showinfo(title="Success", message="Your entry was saved successfully.")
        else:
            if web_entry in data:
                answer = messagebox.askokcancel(title=f"{web_entry} exist", message=f"{web_entry} already exists.")
                if answer:
                    data.update(new_data)
                    with open('data.json', 'w') as file:
                        json.dump(data, file, indent=4)
                        messagebox.showinfo(title="Success", message="Your entry was saved successfully.")
            else:
                data.update(new_data)
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)
                    messagebox.showinfo(title="Success", message="Your entry was saved successfully.")
        finally:
            website_entry.delete(0, END)
            user_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH DATA --------------------------- #
def find_data():
    web_entry = website_entry.get().lower()
    if len(web_entry) == 0:
        messagebox.showwarning(title="Empty", message="Empty field. Type Website to search.")
    else:
        try:
            with open('data.json', 'r') as file:
                search_file = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No data file found.")
        else:
            if web_entry in search_file:
                email = search_file[web_entry]["Email"]
                password = search_file[web_entry]["Password"]
                messagebox.showinfo(title=web_entry, message=f"Email: {email}\nPassword: {password}"
                                                             f"\n---------------------------------------"
                                                             f"\nPassword copied to clipboard")
                pc.copy(password)
            else:
                messagebox.showwarning(title="No Entry", message=f"No details for {web_entry} Found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("New Pass - Password Manager")
window.config(padx=50, pady=50)
window.iconbitmap("icon.ico")

# Canvas
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="newpass_img.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1, pady=10)

# Labels
website = Label(text="Website :")
website.grid(row=1, column=0)
username = Label(text="Email/Username :")
username.grid(row=2, column=0)
password = Label(text="Password :")
password.grid(row=3, column=0)

# Entries
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()
user_entry = Entry(width=52)
user_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons
generate_pass = Button(text="Generate Password", command=generate_password, bg=DARK_BLUE, fg=WHITE)
generate_pass.grid(row=3, column=2)
save_data = Button(text="Save Data", width=44, bg=BLUE, fg=WHITE, command=save)
save_data.grid(row=4, column=1, columnspan=2, pady=10)
search_data = Button(text="Search Website", command=find_data, bg=DARK_BLUE, fg=WHITE, width=14)
search_data.grid(row=1, column=2)

window.mainloop()
