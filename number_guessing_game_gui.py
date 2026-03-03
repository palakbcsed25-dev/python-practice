from tkinter import *

# create the window
window = Tk()
window.title("Number Guessing Game")
window.geometry("400x380")

# variable to store the secret number
my_number = None

# this runs when teacher clicks Set Number button
def set_number():
    global my_number
    my_number = int(teacher_input.get())
    teacher_input.delete(0, END)
    set_message.config(text="Number is set! Player can now guess.")
    set_button.config(state=DISABLED)
    teacher_input.config(state=DISABLED)

# this runs when player clicks Guess button
def check():
    player_guess = int(player_input.get())

    if player_guess == my_number:
        result.config(text="Correct! Well done!")
    elif player_guess < my_number:
        result.config(text="Too low!")
    else:
        result.config(text="Too high!")

# title
title = Label(window, text="Number Guessing Game", font=("Arial", 18))
title.pack(pady=10)

# teacher section
teacher_label = Label(window, text="Teacher: Set a number between 1 and 1000", font=("Arial", 11))
teacher_label.pack(pady=5)

teacher_input = Entry(window, font=("Arial", 13), width=15, justify="center")
teacher_input.pack(pady=5)

set_button = Button(window, text="Set Number", font=("Arial", 11), command=set_number, bg="yellow")
set_button.pack(pady=5)

set_message = Label(window, text="", font=("Arial", 10), fg="green")
set_message.pack(pady=5)

# divider
divider = Label(window, text="- - - - - - - - - -", font=("Arial", 10))
divider.pack(pady=5)

# player section
player_label = Label(window, text="Player: Guess the number", font=("Arial", 11))
player_label.pack(pady=5)

player_input = Entry(window, font=("Arial", 13), width=15, justify="center")
player_input.pack(pady=5)

guess_button = Button(window, text="Guess", font=("Arial", 11), command=check, bg="lightblue")
guess_button.pack(pady=5)

# result message
result = Label(window, text="", font=("Arial", 13))
result.pack(pady=10)

# start the window
window.mainloop()
