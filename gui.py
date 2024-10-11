from main import main
import tkinter as tk
from tkinter import filedialog

def directory_select():
    file_path = filedialog.askdirectory()
    print(file_path)

def mainwindow():
    main_window = tk.Tk()
    main_window.config(width=400, height=300)
    main_window.title("Main Window")
