import zipfile
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

path_and_file = filedialog.askopenfilename()

try: 
    the_zip_file = zipfile.ZipFile(path_and_file)
    ret = the_zip_file.testzip()
    print('Zip file is valid.')
except:
    print('Zip file is invalid.')

