import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
simpledialog.askstring(title='8-ball',prompt="ask me a yes or no question ad I'll answer it.")
    # Make a variable and initialize it to a random number between 0 and 3
random_number = random.randint(0, 3)
    # If the random number is 0
if random_number==0:
    messagebox.showinfo(message="No")
        # tell the user "Yes"
if random_number==1:
    messagebox.showinfo(message="Yes")
    # If the random number is 1
if random_number==2:
    messagebox.showinfo(message="Maybe you should ask Google?")
        # tell the user "No"
if random_number==3:
    messagebox.showinfo(message="💀")
    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
