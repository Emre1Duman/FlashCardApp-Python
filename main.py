from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

##CANVAS##
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


##BUTTONS##
cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)










window.mainloop()