# an-automatic-pdf-file-printing-app
This repository contains the source code and executable file of an automatic pdf file printing app, which works the best together with a barcode scanner to print out pdf format labels named with the bar codes. 

# The normal workflow for the executable is:
1. User double click the executable file
2, User copys paste the folder path that contains the pdf files to be printed to the "filefolder path" entry box
3, User scans a barcode with the barcode scanner (barcode reader) hardware, which will act as a keyboard that inputs the bar code to the "label reading" entry box
4, The program will search for the files whose file name include the bar code
5, If and only if one file is found, it will be printed out autmatically through the default printer connected to the Windows PC
6. If no file or multiple files is found whose filename matches the bar code, the status box will show warning and further instructions

The executable was generated from the source code with "pyinstaller --onefile -w pakage_label_change_assistant_v8.py" in the terminal.
Both the source code and the executable runs well on my own Windows 7 PC with a virtual printer configured without any problem, but somehow the executable is not stable on a client's Windows 10 computer which has a printer and a barcode scanner connected. 
I have no acess to client's computer to test and debug this program at this moment. Only way is to send them the executable file and ask them to test. By far, we haven't figured out what is the reason that sometimes the executable works, and sometimes not, in other words, the printer doesn't print anything.

# I am posting the source code and executable here with two purposes:
1. Let the community use and test the code, and offer feedback and suggestions to me to hopefully solve the problem together
2. Help those who are working on a similar task to have a good start point

