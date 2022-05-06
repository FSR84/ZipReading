import pandas as pd
import zipfile
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

path_and_file = filedialog.askopenfilename()


# unzip all files in the same folder as the zip file
with zipfile.ZipFile(path_and_file, 'r') as myzip:
    names = myzip.namelist()
    myzip.extractall(path_and_file)


# create a table with unzipped files and path
df = pd.DataFrame({"Files":names,"Path":path_and_file}) 
