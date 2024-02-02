from tkinter import *
from tkinter import messagebox
import os
import pandas
import random



BACKGROUND_COLOR = "#B1DDC6"
learn_df = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
    print(df)
    learn_df = df.to_dict(orient="records")
else:
    learn_df = data.to_dict(orient="records")


def create_word():
    global choose_word, flip_timer
    window.after_cancel(flip_timer)
    choose_word = random.choice(learn_df)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=choose_word['French'], fill="black")
    canvas.itemconfig(card_background, image=canvas_fg)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=choose_word['English'], fill="white")
    canvas.itemconfig(card_background, image=canvas_bg)

def is_know():

    global choose_word
    if len(learn_df) > 1:
        learn_df.remove(choose_word)
        data = pandas.DataFrame(learn_df)
        data.to_csv(path_or_buf="data/words_to_learn.csv", index=False)

    else:
        messagebox.showinfo(title="There's no word to learn", message="Congratulation! You've review all the words!\nGood job, keep up the good work!\n🥳🥳🥳🥳")
        os.remove("data/words_to_learn.csv")



window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_fg = PhotoImage(file="images/card_front.png")
canvas_bg = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=canvas_fg)
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas.grid(column=0, row=0, columnspan=2)


#Button

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=lambda:[create_word(), is_know()])
correct_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=create_word)
wrong_button.grid(row=1, column=0)

create_word()
window.mainloop()