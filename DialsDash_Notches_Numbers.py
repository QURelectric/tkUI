# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:10:22 2025

@author: m_epo
"""

"""
SEE OTHER FILE FOR COMMENTS, ONLY COMMENTS ON THIS FILE ARE FOR THE CREATION
& PLACING OF NUMBERS ON THE DIAL
"""




import tkinter as tk
import math
import time

class MovingDialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Moving Dial Demo With Notches & Numbers")

        self.offset = 75
        self.radius = 150
        self.canvas_width = 800
        self.canvas_height = 480
        self.center_x = self.canvas_width // 2 - (self.radius + self.offset)
        self.center_y = self.canvas_height // 2
        self.center_x2 = self.canvas_width // 2 + (self.radius + self.offset)
        self.center_y2 = self.canvas_height // 2

        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.angle = 180
        self.speed = 2  

        self.canvas.create_arc(self.center_x - self.radius, self.center_y - self.radius,
                               self.center_x + self.radius, self.center_y + self.radius,
                               start=0, extent=180, style=tk.PIESLICE, width=2, fill="lightblue")
        self.canvas.create_arc(self.center_x2 - self.radius, self.center_y2 - self.radius,
                                self.center_x2 + self.radius, self.center_y2 + self.radius,
                                start=0, extent=180, style=tk.PIESLICE, width=2, fill="lightgreen")

        self.draw_notches(self.center_x, self.center_y, self.radius)
        self.draw_notches(self.center_x2, self.center_y2, self.radius)

        self.draw_numbers(self.center_x, self.center_y, self.radius)
        self.draw_numbers(self.center_x2, self.center_y2, self.radius)

        self.pointer = self.canvas.create_line(self.center_x, self.center_y,
                                               self.center_x - self.radius, self.center_y,
                                               width=4, fill="red")

        self.pointer2 = self.canvas.create_line(self.center_x2, self.center_y2,
                                                self.center_x2 - self.radius, self.center_y2,
                                                width=10, fill="blue")

        self.update_dial()

    def draw_notches(self, center_x, center_y, radius):
        num_notches = 10
        for i in range(num_notches):
            angle = math.radians(i * (180 / (num_notches - 1))) + math.pi  # Flip by adding math.pi (180 degrees)
            notch_x1 = center_x + (radius - 10) * math.cos(angle)  # Short line for the notch
            notch_y1 = center_y + (radius - 10) * math.sin(angle)
            notch_x2 = center_x + radius * math.cos(angle)  # Longer line for the end of the notch
            notch_y2 = center_y + radius * math.sin(angle)

            # Draw the notch
            self.canvas.create_line(notch_x1, notch_y1, notch_x2, notch_y2, width=2, fill="black")

    def draw_numbers(self, center_x, center_y, radius):
        #nNumber of numbers you want, should be one or two per notch
        num_numbers = 10
        for i in range(num_numbers):
            #calculate the angle for each number
            angle = math.radians(i * (180 / (num_numbers - 1))) + math.pi
            number_x = center_x + (radius - 20) * math.cos(angle)
            number_y = center_y + (radius - 20) * math.sin(angle)
            #write numbers to canvas
            self.canvas.create_text(number_x, number_y, text=str(i * 10), font=("Arial", 10, "bold"), fill="black")

    def update_dial(self):
        angle_rad = math.radians(self.angle)
        pointer_x = self.center_x + self.radius * math.cos(angle_rad)
        pointer_y = self.center_y + self.radius * math.sin(angle_rad)

        self.canvas.coords(self.pointer, self.center_x, self.center_y, pointer_x, pointer_y)

        self.angle += self.speed

        if self.angle >= 360:
            #delay for debugging
            time.sleep(1)
            self.angle = 180

        self.root.after(50, self.update_dial)

root = tk.Tk()

app = MovingDialApp(root)

root.mainloop()
