from tkinter import *


def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0:
        count_down(WORK_SEC)
        timer_label.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(LONG_BREAK_SEC)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(SHORT_BREAK_SEC)
        timer_label.config(text="Break", fg=PINK)


def count_down(count):
    minute = int(count / 60)
    sec = count % 60

    current_time = f"{minute:02d}:{sec:02d}"
    canvas.itemconfig(timer_text, text=current_time)

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_done = ""
        for _ in range(int(reps / 2)):
            work_done += "👌"
            tick_label.config(text=work_done)


def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    tick_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 25 * 60
SHORT_BREAK_SEC = 5 * 60
LONG_BREAK_SEC = 20 * 60

reps = 0
timer = None

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=100, bg=YELLOW)

# Create Timer label

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, 'normal'), bg=YELLOW, highlightthickness=0)
timer_label.grid(column=1, row=0)

# Create the tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Create start and reset buttons
start_bttn = Button(text='Start', highlightthickness=0, command=start_timer)
start_bttn.grid(column=0, row=2)

reset_bttn = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_bttn.grid(column=2, row=2)

# Create tick mark label

tick_label = Label(bg=YELLOW, highlightthickness=0)
tick_label.grid(column=1, row=4)

window.mainloop()
