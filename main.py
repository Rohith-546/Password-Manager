from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def new_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password_ = "".join(password_list)

    print(password_)

    password_entry.delete(0, END)
    password_entry.insert(0, password_)
    pyperclip.copy(str(password_))
    messagebox.showinfo(title='', message='Password copied to clipboard')


# ---------------------------- Find PASSWORD ------------------------------- #


def find_password():
    try:
        with open('data.json', 'r') as f:
            read_d = json.load(f)
            messagebox.showinfo(title=site_entry.get(), message=f"Email: {read_d[site_entry.get()]['email']}\n"
                                                                f"Password: {read_d[site_entry.get()]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No data file found')
    except KeyError:
        messagebox.showinfo(title='No Data', message='No details for the website exits')

# ---------------------------- SAVE PASSWORD ------------------------------- #


def saving():
    website = site_entry.get()
    email = mail_entry.get()
    pw = password_entry.get()
    new_file = {
        website: {
            'email': email,
            'password': pw
        }
    }
    if len(website) == 0 or len(email) == 0 or len(pw) == 0:
        messagebox.showwarning(title='Oops!!', message="Don't leave any fields empty.")
    else:
        try:
            with open('data.json', 'r') as f:
                d = json.load(f)
                d.update(new_file)
            with open('data.json', 'w') as f:
                json.dump(d, f, indent=4)
                messagebox.showinfo(title='Done', message='Data saved.')
                site_entry.delete(0, END)
                password_entry.delete(0, END)
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(new_file, f, indent=4)
                messagebox.showinfo(title='Done', message='Data saved.')
                site_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg="#F5E8C7")

# Canvas
canvas = Canvas(width=300, height=200, highlightthickness=0, bg="#F5E8C7")
image = PhotoImage(file='logo.png')
canvas.create_image(180, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
site = Label(text='Website:', bg="#F5E8C7")
site.grid(column=0, row=1)
mail = Label(text='Email/Username:', bg="#F5E8C7")
mail.grid(column=0, row=2)
password = Label(text='Password:', bg="#F5E8C7")
password.grid(column=0, row=3)

# Entry
site_entry = Entry(width=35)
site_entry.grid(column=1, row=1, sticky="EW")
site_entry.focus()
mail_entry = Entry(width=35)
mail_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
mail_entry.insert(0, '197r1a0546@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
password_b = Button(text='Generate Password', bg='#A73489', command=new_pw)
password_b.grid(column=2, row=3, sticky="EW")
add_b = Button(text='Add', width=36, bg="#5089C6", command=saving)
add_b.grid(column=1, row=4, columnspan=2, sticky="EW")
search = Button(text='Search', bg="#FF4848", command=find_password)
search.grid(column=2, row=1, columnspan=2, sticky="EW")
window.mainloop()
