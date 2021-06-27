from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import sys
import os

def main_test(param_):
    test = open(param_)
    t_var = test.read()
    text_edited = t_var.replace("!", ".").replace("?",".").replace("\n", " ")
    letterc = 0
    spacec = 1
    puncc = 0
    string_length = len(text_edited)
    counter_s = 0
    for i in range(0, string_length, 1):
        if text_edited[i].isalpha() == True:
            letterc += 1
        elif text_edited[i].isspace() == True:
           counter_s += 1 
    spacec = counter_s
    final_resultL = (letterc / (spacec - 1) * 100)

    string_length = len(text_edited)
    for i in range(0, string_length, 1):
        if text_edited[i] == ".":
            puncc += 1
    
    final_resultS = (puncc / (spacec - 1) * 100)
    # CLI = 0.0588L - 0.296S - 15.8
    # L = l / w * 100
    # S = s / w *100
    word_count = final_resultL
    sentence_count = final_resultS
    print("# of sentence-ending punctuations", puncc,"\n" "# of spaces: ", spacec)
    final_resultF = ((0.0588 * word_count) - 0.296 * sentence_count) - 15.8
    print("Approximate value of the CLI: ", final_resultF)
    return final_resultF

root= Tk()
root.title('Our DefHacks 3.0 submission')
col_ = '#FF947F'
# bg = col changes the color of background
canvas1 = Canvas(root, width = 800, height = 300, bg = col_, highlightthickness= 0)
text1 = Label(text="Text file/s should be in the same directory of the program", font = 'Consolas 14', bg = col_)
my_img = ImageTk.PhotoImage(Image.open("/home/shem/Python/images/150.png"))
my_label = Label(image=my_img)
my_label.pack(pady=20)
text1.pack(pady=30)
canvas1.pack()
root['bg'] = col_
entry1 = Entry()
canvas1.create_window(400, 10, window=entry1)
 
def driverFunc(): 
    x1 = entry1.get()
    print_this = str(round(main_test(x1)))
    label1 = Label(root, text= ("This given text is for Grade " + print_this + " students\nRun the program again to check for more text files!"), font= 'Consolas', bg=col_)
    canvas1.create_window(400, 200, window=label1)
 
button1 = Button(text='Get CLI Index', command=driverFunc, bg = '#C1264E', font='Consolas 15')
canvas1.create_window(400, 50, window=button1)
root.mainloop()