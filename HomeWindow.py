# Relectric Interior Team

# *********************************************************
#                   HomeWindow.py
#       This is the file for the Home Window of the GUI
# *********************************************************

#import Libraires
import tkinter as tk

#Import Classes from SubWindows.py
from SubWindows import MusicWindow, NavagationWindow, ControlWindow

class HomeWindow:
    def __init__(self,root,size) -> None:
        root.title("Orion MK1")
        #set background color, size, etc. Raspberry Pi resolution/size is 800x480, the +400 and +200
        #sets the window to the exact middle of the 7" display
        root.configure(bg='lightblue')
        root.geometry(size)

        # Initilize main window
        # Create buttons in the main window to open new windows

        button1 = tk.Button(root, text="Music", command=lambda  : MusicWindow(root, size))
        button1.pack(pady=20)

        button2 = tk.Button(root, text="Navagation", command=lambda: NavagationWindow(root, size))
        button2.pack(pady=20)

        button3 = tk.Button(root, text="Controls", command=lambda: ControlWindow(root, size))
        button3.pack(pady=20)


        # Add Buttons for new windows as needed