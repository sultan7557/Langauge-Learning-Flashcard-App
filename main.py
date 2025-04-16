import tkinter as tk
import pandas as pd
import random
import os


BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- DATA ------------------------------- #
try: 
    data = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient = "records")

# ---------------------------- FUNCTIONS ------------------------------- #

current_card = {}
flip_timer = None

def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    
    if len(to_learn) == 0:
        canvas.itemconfig(card_title, text="🎉 Done!", fill="black")
        canvas.itemconfig(card_word, text="You know all the words.", fill="black")
        canvas.itemconfig(card_background, image=card_front_img)
        return
    
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    updated_data = pd.DataFrame(to_learn)
    updated_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "bold"))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# ---------------------------- BUTTONS ------------------------------- #

right_button_img = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_button_img, highlightbackground=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

wrong_button_img = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_button_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()









window.mainloop()
