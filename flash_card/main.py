from random import choice
from tkinter import *

import pandas


def next_card():
    global current_card, timer

    root.after_cancel(timer)

    current_card = choice(to_learn)

    card.itemconfig(top_text, text=current_card["Kanji"])
    card.itemconfig(mid_text, text=current_card["Kana"])
    card.itemconfig(bottom_text, text=current_card["Romaji"])
    card.itemconfig(card_image, image=cardf_img)

    timer = root.after(3000, func=flip_card)


def flip_card():
    card.itemconfig(card_image, image=cardb_img)
    card.itemconfig(mid_text, text=current_card["English"], fill="#e28c75")
    card.itemconfig(top_text, text=current_card["Kana"])
    card.itemconfig(bottom_text, text="")


BG_COLOR = "#B1DDC6"

root = Tk()
root.config(pady=50, padx=50, bg=BG_COLOR)

df = pandas.read_csv("data/word_frequency_list.csv")
to_learn = df.to_dict(orient="records")
timer = root.after(3000, func=flip_card)

cardb_img = PhotoImage(file="images/card_back.png")
cardf_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

card = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
card_image = card.create_image(400, 263, image=cardf_img)
top_text = card.create_text(400, 80, text="Kanji", font=("Arial", 60, "normal"))
mid_text = card.create_text(400, 230, text="Kana", font=("Arial", 100, "normal"), fill="#9cb4f2")
bottom_text = card.create_text(400, 380, text="Romaji", font=("Arial", 80, "normal"))
card.grid(column=0, row=0, columnspan=2)

right_bttn = Button(image=right_img, bg=BG_COLOR, highlightthickness=0, command=next_card)
right_bttn.grid(column=0, row=1)

wrong_bttn = Button(image=wrong_img, bg=BG_COLOR, highlightthickness=0, command=next_card)
wrong_bttn.grid(column=1, row=1, pady=5)

root.mainloop()
