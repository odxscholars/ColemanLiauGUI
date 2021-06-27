from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import sys
import os

def CL_Index(txt):
    
    # opens text file 
    open_file = open(txt)
    
    # reads text file
    read_file = open_file.read()
    
    # replaces sentence-ending punctuations with periods to indicate  the end of a sentence
    text_edited = read_file.replace("!", ".").replace("?",".").replace("\n", "")
    
    # variable declarations 
    letter_counter = 0
    space_counter = 0
    punctuation_counter = 0
    
    # returns length of string used in the loops 
    string_length = len(text_edited)
    
    # counts the number of letters and spaces 
    for i in range(0, string_length, 1):
        if text_edited[i].isalpha() == True:
            letter_counter += 1
        elif text_edited[i].isspace() == True:
           space_counter += 1
    
    # counts the number of sentences based on periods
    string_length = len(text_edited)
    for i in range(0, string_length, 1):
        if text_edited[i] == ".":
            punctuation_counter += 1
    
    # CLI = 0.0588L - 0.296S - 15.8
    # L = letters / words * 100 (average number of letters per 100 words)
    # S = sentences / words * 100 (average number of sentences per 100 words)

    # prints out the number of letters
    print("# of letters: ", letter_counter)
    
    # prints out the number of sentence-ending punctuations 
    print("# of sentence-ending punctuations", punctuation_counter)
    
    # prints out the number of spaces 
    print("# of spaces: ", space_counter)
    
    # calculates coleman-liau index (CLI)
    CLI = (((0.0588 * ((letter_counter / (space_counter + 1.0)) * 100.0)) - (0.296 * ((punctuation_counter / (space_counter + 1.0)) * 100.0))) - 15.8)
    
    # prints CLI 
    print("Approximate value of the CLI: ", CLI)
    
    return CLI

# GUI 
root= Tk()
root.title('Our DefHacks 3.0 submission')

# changes the color of background
background_color = '#FF947F'

# defines what the GUI looks like 
GUI_Canvas = Canvas(root, width = 800, height = 300, bg = background_color, highlightthickness= 0)

# tells the user where to input files 
label_text = Label(text="Text file/s should be in the same directory of the program", font = 'Consolas 14', bg = background_color)

# colonel sanders logo 
my_img = ImageTk.PhotoImage(Image.open("150.png"))
my_label = Label(image=my_img)

# size of logo 
my_label.pack(pady=20)

# size of label 
label_text.pack(pady=30)

# organizes widgets in blocks 
GUI_Canvas.pack()


root['bg'] = background_color

# string input window 
text_entry = Entry()
GUI_Canvas.create_window(400, 10, window=text_entry)

# calls function 
def driverFunc(): 
    x1 = text_entry.get()
    print_this = str(round(CL_Index(x1)))
    output_text = Label(root, text= ("This given text is for Grade " + print_this + " students\nRun the program again to check for more text files!"), font= 'Consolas', bg=background_color)
    GUI_Canvas.create_window(400, 200, window=output_text)
 
# button to run program 
button1 = Button(text='Get CLI Index', command=driverFunc, bg = '#C1264E', font='Consolas 15')
GUI_Canvas.create_window(400, 50, window=button1)
root.mainloop()