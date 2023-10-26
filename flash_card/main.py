from tkinter import *

BG_COLOR = "#B1DDC6"
root = Tk()
root.config(pady=50, padx=50, bg=BG_COLOR)

cardb_img = PhotoImage(file="images/card_back.png")
cardf_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

card = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
card.create_image(400, 263, image=cardf_img)
kanji_text = card.create_text(400, 80, text="Kanji", font=("Arial", 60, "normal"))
kana_text = card.create_text(400, 230, text="Kana", font=("Arial", 100, "normal"))
romaji_text = card.create_text(400, 380, text="Romaji", font=("Arial", 80, "normal"))
card.grid(column=0, row=0, columnspan=2)

right_bttn = Button(image=right_img, bg=BG_COLOR, highlightthickness=0)
right_bttn.grid(column=0, row=1)

wrong_bttn = Button(image=wrong_img, bg=BG_COLOR, highlightthickness=0)
wrong_bttn.grid(column=1, row=1, pady=5)

root.mainloop()
