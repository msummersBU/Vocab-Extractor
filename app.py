import tkinter as tk
from tkinter import filedialog, Text, Canvas, ttk, Label
import os
import vocabextractor as ve
import webbrowser as wb

fileName, outputPath, output = "", "", ""

# User selects a text file
def getFile():
    global fileName, opfilePath, output
    fileName = filedialog.askopenfilename(initialdir="./", title="Select File", 
                                          filetypes=(("Text Documents","*.txt"), ("All files", "*.*")))
    opfilePath.config(text="File: " + fileName)
    try:
        output = ve.extractVocab(fileName)
    except:
        print("No file selected.")

# User selects the outputPath
def getOutputFile():
    global outputPath, outfilePath
    outputPath = filedialog.asksaveasfilename(initialdir="./", defaultextension="*.*", title="Select Output", 
                                          filetypes=(("Text Documents","*.txt"), ("All files", "*.*")))
    outfilePath.config(text="File: " + outputPath)
    
def outputToFile():
    global output, outputPath
    if (output != None):
        f = open(outputPath, "x")
        f.write(output)
    wb.open(outputPath)
    output = None

root = tk.Tk()
root.title("Japanese Vocab Extractor")
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(500, 160))

# select file
openFile = tk.Button(root, width=root.winfo_reqwidth(), text="Open File", padx=10, 
                     pady=5, fg="white", bg="gray", command=getFile)
opfilePath = Label (root, width=root.winfo_reqwidth(), text="File: " + fileName, padx=10,
                    pady=5)

openFile.pack()
opfilePath.pack()

# select output file
outputFile = tk.Button(root, width=root.winfo_reqwidth(),text="Select Output", padx=10, 
                     pady=5, fg="white", bg="gray", command=getOutputFile)
outfilePath = Label (root, width=root.winfo_reqwidth(), text="File: " + outputPath, padx=10,
                    pady=5)

outputFile.pack()
outfilePath.pack()

# extract
extractVocab = tk.Button(root, width=root.winfo_reqwidth(), text="Extract", padx=10,
                         pady=5, fg="white", bg="green", command=outputToFile)
extractVocab.pack()

# run the UI
root.mainloop()