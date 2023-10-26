from random import choice, shuffle
from string import ascii_letters, digits, punctuation
from tkinter import *
from tkinter import messagebox

import pandas as pd
import pyperclip


# Password Generator
def generate_password():
    letters = list(ascii_letters)
    numbers = list(digits)
    symbols = list(punctuation)
    password = []

    for _ in range(6):
        password.append(choice(letters))
        password.append(choice(numbers))
        password.append(choice(symbols))

    shuffle(password)
    new_password = ''.join(password)

    pass_entry.delete(0, "end")
    pass_entry.insert(0, new_password)

    pyperclip.copy(new_password)


# Add password to csv
def save():
    # Check if csv exists, creates one if none
    try:
        df = pd.read_csv("password_manager.csv")

        saved_password = {
            'Website': df.Website.to_list(),
            'Username': df.Username.to_list(),
            'Password': df.Password.to_list()
        }

        get_password(saved_password)

    except pd.errors.EmptyDataError:
        saved_password = {'Website': [], 'Username': [], 'Password': []}
        get_password(saved_password)

    except FileNotFoundError:
        saved_password = {'Website': [], 'Username': [], 'Password': []}
        get_password(saved_password)

    df = pd.DataFrame(saved_password)
    df.to_csv("password_manager.csv")

    web_entry.delete(0, "end")
    email_entry.delete(0, "end")
    pass_entry.delete(0, "end")


def get_password(saved_password):
    website = web_entry.get()
    username = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(message="Do not leave empty fields.")
    else:
        prompt = f"Is this information correct?\n\nWebsite: {website}\nEmail/Username: {username}\nPassword: {password}"
        is_ok = messagebox.askokcancel(title=website, message=prompt)

        if is_ok:
            saved_password['Website'].append(website)
            saved_password['Username'].append(username)
            saved_password['Password'].append(password)


def search_passwords():
    website = web_entry.get()

    try:
        df = pd.read_csv("password_manager.csv")

        if website in df.Website.to_list():
            password = df[df.Website == website].Password.to_string(index=False)
            username = df[df.Website == website].Username.to_string(index=False)
            messagebox.showinfo(title=website, message=f"Email/Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message="Website not found.")

    except FileNotFoundError:
        messagebox.showinfo(title=website, message="No passwords saved.")


BG_COLOR = '#444444'
FG_COLOR = 'white'
FONT = ('default', 12, 'normal')

# Create root window
root = Tk()
root.config(bg=BG_COLOR, padx=20, pady=20)

# Create Logo
logo_img = PhotoImage(file='locked.png')
logo_img = logo_img.subsample(2, 2)

logo = Canvas(root, height=256, width=256, bg=BG_COLOR, highlightthickness=0)
logo.create_image(128, 130, image=logo_img)
logo.grid(column=0, row=0, columnspan=3)

# Create Labels
web_label = Label(root, text="Website:", font=FONT, bg=BG_COLOR, fg=FG_COLOR)
web_label.grid(column=0, row=1, sticky=E)

email_label = Label(root, text="Email/Username:", font=FONT, bg=BG_COLOR, fg=FG_COLOR)
email_label.grid(column=0, row=2, sticky=E)

pass_label = Label(root, text="Password:", font=FONT, bg=BG_COLOR, fg=FG_COLOR)
pass_label.grid(column=0, row=3, sticky=E)

# Create Entries
web_entry = Entry(root, font=FONT, fg=FG_COLOR, bg=BG_COLOR, width=33)
web_entry.grid(column=1, row=1, pady=5, sticky=W)
web_entry.focus()  # Initialize with cursor on entry

email_entry = Entry(root, font=FONT, fg=FG_COLOR, bg=BG_COLOR, width=51)
email_entry.grid(column=1, row=2, columnspan=2, pady=5, sticky=W)

pass_entry = Entry(root, font=FONT, fg='#60CAAD', bg=BG_COLOR, width=33)
pass_entry.grid(column=1, row=3, pady=5, sticky=W)

# Create Buttons
generate_button = Button(root, text="Generate Password", font=FONT, bg=BG_COLOR, fg=FG_COLOR, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = (Button(root, text="ADD", width=50, font=FONT, bg=BG_COLOR, fg=FG_COLOR, command=save))
add_button.grid(column=1, row=4, columnspan=2, pady=7)

search_button = Button(root, text="Search", width=16, font=FONT, bg=BG_COLOR, fg=FG_COLOR, command=search_passwords)
search_button.grid(column=2, row=1)

root.mainloop()
