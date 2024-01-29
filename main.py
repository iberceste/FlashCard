from tkinter import PhotoImage
from tkinter import *
import pandas
import random
import time


BACKGROUND_COLOR = "#B1DDC6"
df = pandas.read_csv("data/french_words.csv")
df.to_dict(orient='records')
learn_df = df.to_dict("records")
chosen_word = {}



def new_word():
    global choose_word, flip_timer
    window.after_cancel(flip_timer)
    choose_word = random.choice(learn_df)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=choose_word['French'], fill="black")
    canvas.itemconfig(card_background, image=canvas_fg)
    flip_timer = window.after(3000, func=new_title)



def new_title():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=choose_word['English'], fill="white")
    canvas.itemconfig(card_background, image=canvas_bg)

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=new_title)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_fg = PhotoImage(file="images/card_front.png")
canvas_bg = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=canvas_fg)
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas.grid(column=0, row=0, columnspan=2)







#Button

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=new_word)
correct_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_word)
wrong_button.grid(row=1, column=0)


new_word()
window.mainloop()