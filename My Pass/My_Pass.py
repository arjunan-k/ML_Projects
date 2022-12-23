from tkinter import Tk, Canvas, Label, Button, Entry, PhotoImage, NW, END
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip

# GENERATE PASSWORD
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# SAVE PASSWORD
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops Error", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# FIND PASSWORD
def find_password():

    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            password_entry.insert(0, password)
        else:
            messagebox.showinfo(title="Oops Error", message=f"No details for {website} exists.")

# WINDOW SETUP
window = Tk()
window.title("My Pass")
window.config(padx=10, pady=50, background='#FFBA47')

# CANVAS SETUP
canvas = Canvas(height=185, width=200, background='#FFBA47')
logo_img = PhotoImage(file="logo.png")
canvas.create_image(0, 0, image=logo_img, anchor=NW)
canvas.grid(row=0, column=1, pady=15, padx=15)

# ADDING LABELS
website_label = Label(
    text="Website :",
    bg='#FFBA47',
    fg='black',
    padx=5,
    pady=5,
    font=('Arial', 10, 'bold'))
website_label.grid(row=1, column=0)

email_label = Label(text="Email / Username :",
                    bg='#FFBA47',
                    fg='black',
                    padx=5,
                    pady=5,
                    font=('Arial', 10, 'bold'))
email_label.grid(row=2, column=0)

password_label = Label(text="Password :",
                       bg='#FFBA47',
                       fg='black',
                       padx=5,
                       pady=5,
                       font=('Arial', 10, 'bold'))
password_label.grid(row=3, column=0)

# ADDING ENTRY TABS
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)
# focus() to set cursor initially while running program near the desired entry tab.
website_entry.focus()
email_entry = Entry(width=25)
email_entry.grid(row=2, column=1)
# Autofill the email.
email_entry.insert(0, "appu@gmail.com")
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1, pady=5, padx=5)

# ADD BUTTONS
search_button = Button(
    text="Search",
    width=15,
    command=find_password,
    pady=1)
search_button.grid(row=1, column=2)

generate_password_button = Button(
    text="Generate Password",
    width=15,
    command=generate_password,
    pady=1)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=20, command=save)
add_button.grid(row=4, column=1, pady=5, padx=5)

# Inorder to keep window open until we close.
window.mainloop()
