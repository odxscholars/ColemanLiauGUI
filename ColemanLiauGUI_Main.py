
from tkinter import *
import sys
import os

def split(word):
    return [char for char in word]


def L(word):
    letterc = 0
    spacec = 1
    test = word
    string_length = len(test)
    for i in range(0, string_length, 1):
        if test[i].isalpha() == True:
            letterc += 1
        elif test[i].isspace() == True:
            spacec += 1
        
    final_result = (letterc / (spacec - 1) * 100)
    return final_result
            
        

def S(word):
    spacec = 1
    puncc = 0
    test = word
    string_length = len(test)
    for i in range(0, string_length, 1):
        if test[i] == ".":
            puncc += 1
        elif test[i].isspace() == True:
            spacec += 1
    final_result = (puncc / (spacec - 1) * 100)
    return final_result

def CLI_(word):
    func_word = word
    # CLI = 0.0588L - 0.296S - 15.8
    # L = l / w * 100
    # S = s / w *100
    word_count = L(word)
    sentence_count = S(word)
    final_result = ((0.0588 * word_count) - 0.296 * sentence_count) - 15.8
    return final_result

def main_test(param_):
    test = open(param_)
    t_var = test.read()
    text_edited = t_var.replace("!", ".").replace("?",".")
    value = CLI_(text_edited)
    return value

root= Tk()
root.title('My DefHacks 3.0 submission')
col_ = '#786A4D'
# bg = col changes the color of background
canvas1 = Canvas(root, width = 800, height = 600, bg = col_, highlightthickness= 0) #honestly don't know what canvas does
canvas1.pack()
canvas2 = Canvas(root, width = 800, height = 600, bg = col_, highlightthickness= 0)
canvas2.pack()
root['bg'] = col_
entry1 = Entry()
canvas1.create_window(400, 400, window=entry1)

def driverFunc(): 
    x1 = entry1.get()
    print_this = str(round(main_test(x1)))
    label1 = Label(root, text= ("This given text is for Grade " + print_this + " students"))
    label2 = Label(root,text =("Run the program again to check for more text files!"))
    canvas1.create_window(300, 120, window=label1)
    canvas2.create_window(230, 230, window=label2) 
    
button1 = Button(text='Get CLI Index', command=driverFunc, bg = '#795548')
canvas1.create_window(400, 500, window=button1)

root.mainloop()
