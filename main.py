from tkinter import *
import pandas, random
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- Data ------------------------------- #

data = pandas.read_csv("data/french_words.csv")
data_dictionary = data.to_dict()

def new_french_word():
    french_word = data_dictionary["French"][random.randint(0,100)]
    canvas.itemconfig(word, text=f"{french_word}")







# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

##CANVAS##
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


##BUTTONS##
cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=new_french_word)
wrong_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=new_french_word)
right_button.grid(column=1, row=1)










window.mainloop()