from random import choice, shuffle
from string import ascii_letters, digits, punctuation
from tkinter import *


# Password Generator
def generate_password():
    letters = list(ascii_letters)
    numbers = list(digits)
    symbols = list(punctuation)
    password = []

    for _ in range(6):
        password.append(choice(letters))
    for _ in range(6):
        password.append(choice(numbers))
    for _ in range(6):
        password.append(choice(symbols))

    shuffle(password)
    new_password = ''.join(password)

    pass_entry.delete(0, "end")
    pass_entry.insert(0, new_password)


def add_password():
    pass


BG_COLOR = '#444444'
FG_COLOR = '#70A3CC'
FONT = ('default', 12, 'normal')

root = Tk()
root.config(bg=BG_COLOR, padx=20, pady=20)

# new_password = StringVar(root)

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

web_entry = Entry(root, font=FONT, fg='white', bg=BG_COLOR, width=51)
web_entry.grid(column=1, row=1, columnspan=2, pady=5, sticky=W)
email_entry = Entry(root, font=FONT, fg='white', bg=BG_COLOR, width=51)
email_entry.grid(column=1, row=2, columnspan=2, pady=5, sticky=W)
pass_entry = Entry(root, font=FONT, fg='white', bg=BG_COLOR, width=33)
pass_entry.grid(column=1, row=3, pady=5, sticky=W)

# Create Buttons

generate_button = Button(root, text="Generate Password",
                         font=FONT, bg=BG_COLOR, fg=FG_COLOR,
                         command=generate_password)
generate_button.grid(column=2, row=3)
add_button = (Button(root, text="ADD", width=50,
                     font=FONT, bg=BG_COLOR, fg=FG_COLOR,
                     command=add_password))
add_button.grid(column=1, row=4, columnspan=2, pady=7)

root.mainloop()
