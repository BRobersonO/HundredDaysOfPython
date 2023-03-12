from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_button_clicked():
    global timer, reps
    window.after_cancel(timer)
    main_label.config(text="Timer")
    checks_label.config(text = "Completed: ")
    canvas.itemconfig(timer_text, text = "00:00")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    time_length = 0
    if reps == 8:
        time_length = long_break_sec
        checks_label.config(text = "Completed: ")
        main_label.config(text="Break")
        reps = 0
        # all finished
    elif reps % 2 == 0:
        time_length = short_break_sec
        checks_label.config(text = checks_label["text"] + "✔")
        main_label.config(text="Break")
    else:
        time_length = work_sec
        main_label.config(text="Working")
    count_down(time_length)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minute = count // 60
    second = count % 60
    canvas.itemconfig(timer_text, text=f"{minute:02d}:{second:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day28DynamicTyping/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

# Label: Title
main_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"),bg=YELLOW,fg=GREEN)
main_label.grid(column=1,row=0)
main_label.config(padx=25,pady=25)

# Button: Start
button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0,row=2)

# Button: Reset
button_reset = Button(text="Reset", command=reset_button_clicked)
button_reset.grid(column=2,row=2)

# Label: Checkmarks
checks_label = Label(text="Completed: ", font=(FONT_NAME, 18, "bold"),bg=YELLOW,fg=GREEN)
checks_label.grid(column=1,row=3)

window.mainloop()