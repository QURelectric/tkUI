# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:07:49 2025

@author: m_epo
"""

import tkinter as tk
import math
import time

class MovingDialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Moving Dial Demo With Notches")

        #define window size
        self.offset = 75
        self.radius = 150
        self.canvas_width = 800
        self.canvas_height = 480
        self.center_x = self.canvas_width // 2 - (self.radius + self.offset)
        self.center_y = self.canvas_height // 2
        self.center_x2 = self.canvas_width // 2 + (self.radius + self.offset)
        self.center_y2 = self.canvas_height // 2

        #Make canvas
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        #Angle & Speed variables for both dials
        self.angle = 180
        self.speed = 2

        #Draw semi-circle dial 1
        self.canvas.create_arc(self.center_x - self.radius, self.center_y - self.radius,
                               self.center_x + self.radius, self.center_y + self.radius,
                               start=0, extent=180, style=tk.PIESLICE, width=2, fill="lightblue")
        #Draw semi-circle dial 2
        self.canvas.create_arc(self.center_x2 - self.radius, self.center_y2 - self.radius,
                                self.center_x2 + self.radius, self.center_y2 + self.radius,
                                start=0, extent=180, style=tk.PIESLICE, width=2, fill="lightgreen")

        #create notches on both dials
        self.draw_notches(self.center_x, self.center_y, self.radius)
        self.draw_notches(self.center_x2, self.center_y2, self.radius)

        #draw needle, initially pointing to the left
        self.pointer = self.canvas.create_line(self.center_x, self.center_y,
                                               self.center_x - self.radius, self.center_y,
                                               width=4, fill="red")

        self.pointer2 = self.canvas.create_line(self.center_x2, self.center_y2,
                                                self.center_x2 - self.radius, self.center_y2,
                                                width=10, fill="blue")

        #call dial updating functions
        self.update_dial()

    def draw_notches(self, center_x, center_y, radius):
    #set number of notches you want (e.g., 10)
        num_notches = 10
        for i in range(num_notches):
            #calculate the angle for each notch
            angle = math.radians(i * (180 / (num_notches - 1))) + math.pi
            notch_x1 = center_x + (radius - 10) * math.cos(angle)
            notch_y1 = center_y + (radius - 10) * math.sin(angle)
            notch_x2 = center_x + radius * math.cos(angle)
            notch_y2 = center_y + radius * math.sin(angle)
    
            #draw the notch
            self.canvas.create_line(notch_x1, notch_y1, notch_x2, notch_y2, width=2, fill="black")

    def update_dial(self):
        #calculate the new needle position based on current angle
        angle_rad = math.radians(self.angle)
        pointer_x = self.center_x + self.radius * math.cos(angle_rad)
        pointer_y = self.center_y + self.radius * math.sin(angle_rad)

        #update needle position
        self.canvas.coords(self.pointer, self.center_x, self.center_y, pointer_x, pointer_y)

        #update angle for movement condition
        self.angle += self.speed

        #needle reset condition, will go back to 9 o'clock when dial hits 3 o'clock
        if self.angle >= 360:
            # Delay for debugging
            time.sleep(1)
            self.angle = 180

        #schedule 'frame' update after 50ms
        self.root.after(50, self.update_dial)

# Create Tkinter root window
root = tk.Tk()

# Create MovingDialApp instance
app = MovingDialApp(root)

# Run Tkinter event loop
root.mainloop()
