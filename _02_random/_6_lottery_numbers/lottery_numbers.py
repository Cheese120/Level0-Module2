import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    number1 = " "
    for i in range(6):
        num = random.randint(0, 50)
        wer = str(num)
        number1 += wer + " "
    # TODO 1) Get 6 random numbers to put on your lottery ticket

    # TODO 2) Display the selected numbers to the user in a pop-up
    message = messagebox.showinfo(title="lottery ticket", message=number1

    )
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
