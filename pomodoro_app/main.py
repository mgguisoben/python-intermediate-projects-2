from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=100, bg=YELLOW)

# Create Timer label

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, 'normal'))
timer_label.grid(column=1, row=0)

# Create the tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Create start and reset buttons
start_bttn = Button(text='Start')
start_bttn.grid(column=0, row=2)

reset_bttn = Button(text='Reset')
reset_bttn.grid(column=2, row=2)

# Create tick mark label

tick_label = Label(text="x")
tick_label.grid(column=1, row=4)

window.mainloop()
