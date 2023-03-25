from tkinter import *
import pandas as pd
from random import choice

FONT = "Arial"
BACKGROUND_COLOR = "#B1DDC6"
DATA = "Day31FlashCardApp/data/french_words.csv"
LANG_TO_LEARN = "French"
HOME_LANG = "English"
HEIGHT = 526
WIDTH = 800

try:
    data = pd.read_csv("Day31FlashCardApp/data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv(DATA)

data_dict = data.to_dict(orient="records")
new_word = {}

#--- BUTTON COMMANDS ---#
def fail():
    next_card()
def success():
    data_dict.remove(new_word)
    data = pd.DataFrame(data_dict)
    data.to_csv("Day31FlashCardApp/data/words_to_learn.csv", index=False)
    next_card()

#--- READ CSV ---#


def next_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = choice(data_dict)
    canvas.itemconfig(card, image = front_card_img)
    canvas.itemconfig(word, text = new_word[LANG_TO_LEARN], fill="black")
    canvas.itemconfig(title, text = LANG_TO_LEARN, fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global new_word
    canvas.itemconfig(card, image = back_card_img)
    canvas.itemconfig(word, text = new_word[HOME_LANG], fill="white")
    canvas.itemconfig(title, text = HOME_LANG, fill="white")

#--- UI ---#
window = Tk()
window.title("Flash Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=HEIGHT, width=WIDTH, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="Day31FlashCardApp/images/card_front.png")
back_card_img = PhotoImage(file="Day31FlashCardApp/images/card_back.png")
card = canvas.create_image(WIDTH/2, HEIGHT/2, image=front_card_img)
canvas.grid(row=0, column=0, columnspan=2)
title = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"))
word = canvas.create_text(400, 263, text= "", font=(FONT, 60, "bold"))

# Buttons
fail_img = PhotoImage(file="Day31FlashCardApp/images/wrong.png")
fail_button = Button(image=fail_img, command=fail, highlightthickness=0)
fail_button.grid(row=1, column=0)
success_img = PhotoImage(file="Day31FlashCardApp/images/right.png")
success_button = Button(image=success_img, command=success, highlightthickness=0)
success_button.grid(row=1, column=1)

next_card()
window.mainloop()