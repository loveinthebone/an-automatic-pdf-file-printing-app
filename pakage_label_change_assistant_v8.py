"""
Created by Kingson Zhou,
on July, 28, 2020,
with Python 3.7.3

main manual for the tkinter module: https://effbot.org/tkinterbook/

make exe file: 
pyinstaller --onefile -w pakage_label_change_assistant_v8.py

According to here:http://www.columbia.edu/~em36/pdftoprinter.html
PDFxchange is the only pdf viewer than directly support silent printing

# Zhengge pdf filefolder:  E:\FWRU0040890
# Example pdf file name: 1Z69W94R6830809564
"""

from tkinter import *
import time
import os

import winsound

# GUI to extract_QR_label:
import tkinter as tk


# import tempfile
import win32api
import win32print



window = tk.Tk()
window.title("贴单助手_v8")
window.geometry("800x300")
status = StringVar()


#  FUNCTIONS
def find_then_print(search_keywords, path):

    # # kill the pdf viewer before opening a new file
    # try:
    #     os.system('TASKKILL /F /IM PDFXCview.exe')
    # except:
    #     pass
    #     print("Can't close the pdf file")

    results = []
    # status =""
    output = ""
    for root, dirs, files in os.walk(path):
        for file_name in files:
            if search_keywords.lower() in file_name.lower():
                results.append(file_name)
    if len(results) == 0:
        status = "No file matching the search. Please choose the right file and print manually!"

    elif len(results) == 1:
        status = "Printing..."
        output = os.path.join(path, results[0])
        
    else:
        status = "Multiple files matching the search. Please choose the right one and print manually!"
    return status, output
    # print_status_update(status)
    # os.startfile(output, "print") # https://stackoverflow.com/questions/12723818/print-to-standard-printer-from-python

def print_status_update(status, output):
    text1.configure( background="white", foreground="black")
    text1.delete(1.0, END) # clean out the text box first
    text1.insert(tk.END, status)
    
    
    if status == "Printing...":
        # print ('\a\a') # make a sound
        winsound.Beep(600, 400)
        
        # print("before print")

        printer_name = win32print.GetDefaultPrinter()
        out = '/d:"%s"' % (printer_name)
        win32api.ShellExecute(0, "print", output, out, ".", 0)
        # print("after print")

        text1.after(2100, back_to_ready) #this line of code only delay the text1 refresh, the program doesn't have any delay here
        # print("after update text")

        time.sleep(2)
        # print("after sleep")
        # os.startfile(output,"print") # https://stackoverflow.com/questions/12723818/print-to-standard-printer-from-python
       
    else:
        text1.configure( background="yellow", foreground="red")
        winsound.Beep(4000, 800)
        
def run_it(event):
    path = entry2.get()
    search_keywords = entry1.get()
    status, output = find_then_print(search_keywords, path)
    print_status_update(status, output)
    entry1.delete(0, END)
    entry1.focus()
window.bind('<Return>', run_it)

def back_to_ready():
    text1.delete(1.0, END) # clean out the text box first
    text1.insert(tk.END, "Ready")



# LABELS
label1 =tk.Label(text="Label reading: ", font=("Courier", 20))
label1.grid(column=0, row=2, sticky="W")

label2 =tk.Label(text="Filefolder path: ", font=("Courier", 20))
label2.grid(column=0, row=0, sticky="W")

label3 =tk.Label(text="Status: ", font=("Courier", 20))
label3.grid(column=0, row=3, sticky="W")

# TEXTS it only run once when start the program
text1 = tk.Text(master=window, height=5, width=30, font=("Courier", 20))
text1.grid(column=1, row=3, sticky="W")
# print("text1 run once")

# ENTRIES
# entry for label reading
entry1 = tk.Entry(bd=5, width=30, font=("Courier", 20))
entry1.grid(column=1, row=2, sticky="W")
entry1.focus()

# entry for filefolder path
entry2 = tk.Entry(bd=5, width=30, font=("Courier", 20))
entry2.grid(column=1, row=0)
# entry2.insert(0,"C:/Users/kingson/Downloads/file_path_to_test")

entry2.insert(0,"E:\\FWRU0040890")

window.mainloop()









# root = Tk()
# frame=Frame(root,width=200,heigh=100,bd=11)
# frame.pack()
# label = Label(frame,text="Scan the labels").pack()
# entry= Entry(frame,bd=4)
# entry.pack()
# entry.focus() # https://stackoverflow.com/questions/13626406/setting-focus-to-specific-tkinter-entry-widget
# barcode = entry.get()

# find_then_print(barcode) # find the barcode in the filepath. If exist, print it with default printer

# entry.delete(0, END) # https://effbot.org/tkinterbook/entry.htm

# button1=Button(root,width=4,height=1,text='ok')
# button1.pack()


# root.mainloop()


