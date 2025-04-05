# Relectric Interior Team 

# ***********************************************************************
#                       DashboardWindow.py
# File Contains The Classe for the Dashboard shown on the second display
# ***********************************************************************

# Library Imports
import tkinter as tk
from PIL import Image
from enum import Enum

#Import Global Variables from Globals
import Globals

# DashElement Class
class DashElement:
    def __init__(self, parent, gif_path, x, y):
        self.frames = [Image.open(gif_path).copy()]
        try:
            while True:
                self.frames.append(self.frames[-1].copy())
                self.frames[-1].seek(len(self.frames))
        except EOFError:
            pass

        self.label = tk.Label(parent)
        self.label.place(x=x, y=y)
        self.current_frame = 0
        self.update_frame()

    def update_frame(self, frame=None):
        if frame is not None:
            self.current_frame = frame
        self.label.config(image=self.frames[self.current_frame])
        self.label.image = self.frames[self.current_frame]

# Dashboard Class
class DashboardWindowApp:
    TURN_SIGNAL_STATES = {
        'LRoff': 0,
        'Lon': 1,
        'Ron': 2,
        'LRon': 3
    }

    def __init__(self, root, size) -> None:
        self.display = tk.Toplevel(root)
        self.display.title("Second Display")
        self.display.geometry(size)

        self.label = tk.Label(self.display, text="CAN Bus Value: ")
        self.label.pack(pady=20)

        # Create DashElement instances
        self.background = DashElement(self.display, "assets/dashboard/images/background.gif", 0, 0)
        self.speedometer = DashElement(self.display, "assets/dashboard/images/speedometer.gif", 100, 100)
        self.tachometer = DashElement(self.display, "assets/dashboard/images/tachometer.gif", 200, 100)
        self.battMeter = DashElement(self.display, "assets/dashboard/images/battMeter.gif", 300, 100)
        self.turnSignal = DashElement(self.display, "assets/dashboard/images/turnSignal.gif", 400, 100)

        # Start the GUI update loop
        self.display.after(200, self.updateGUI)

    def activate_left_turn(self):
        self.turnSignal.update_frame(self.TURN_SIGNAL_STATES['Lon'])

    def activate_right_turn(self):
        self.turnSignal.update_frame(self.TURN_SIGNAL_STATES['Ron'])

    def activate_four_way_signal(self):
        self.turnSignal.update_frame(self.TURN_SIGNAL_STATES['LRon'])

    # GUI Update Function
    def updateGUI(self):
        with Globals.data_lock:
            value = Globals.can_bus_value

        # Update the label text
        if value is not None:
            self.label.config(text=f"CAN Bus Value: {value}")

        self.display.after(200, self.updateGUI)
