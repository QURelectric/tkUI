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
        self.radius = 200
        self.canvas_width = 1600
        self.canvas_height = 480
        self.center_x = self.canvas_width // 2 - (self.radius + self.offset) - 300
        self.center_y = self.canvas_height // 2 + 90
        self.center_x2 = self.canvas_width // 2 + (self.radius + self.offset) - 300
        self.center_y2 = self.canvas_height // 2 + 90

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
        
        #Create the battery bars for visual display of battery levels
        self.create_battery_bar(self.center_x2 + self.radius + 250, self.center_y2 - 200, "Battery Level")

        #Turn signal indicator code
        # Define turn signal states (0: off, 1: on)
        self.left_signal_on = 1
        self.right_signal_on = 1
        
        # Create arrows
        self.create_arrow(self.center_x - 250, self.center_y, "left")
        self.create_arrow(self.center_x2 + 250, self.center_y, "right")
        
        # Start blinking turn signals
        self.blink_signals()


        


    def create_arrow(self, x, y, direction):
        size = 30  # Arrow size
        
        if direction == "left":
            # Create left arrow and store it as an instance variable
            self.left_arrow = self.canvas.create_polygon(x, y,
                                                         x - size, y - size / 2,
                                                         x - size, y + size / 2,
                                                         outline="yellow", fill="red")
            # Initially hide the left arrow
            self.canvas.itemconfig(self.left_arrow, state="normal")
        elif direction == "right":
            # Create right arrow and store it as an instance variable
            self.right_arrow = self.canvas.create_polygon(x, y,
                                                          x + size, y - size / 2,
                                                          x + size, y + size / 2,
                                                          outline="yellow", fill="red")
            # Initially hide the right arrow
            self.canvas.itemconfig(self.right_arrow, state="hidden")


    def blink_signals(self):
        # Toggle the visibility of the arrows based on signal states
        """
        if self.left_signal_on == 1:
            self.canvas.itemconfig(self.left_arrow, state="normal")
        else:
            self.canvas.itemconfig(self.left_arrow, state="hidden")
        """
        
        if self.right_signal_on == 1:
            self.canvas.itemconfig(self.right_arrow, state="normal")
        else:
            self.canvas.itemconfig(self.right_arrow, state="hidden")
        
        # Toggle the signal states for next blink (left and right independently)
        self.left_signal_on = 1 - self.left_signal_on
        self.right_signal_on = 1 - self.right_signal_on
        
        # Continue blinking every 500 milliseconds
        self.root.after(500, self.blink_signals)



    def create_battery_bar(self, x, y, label_text):
        #create the battery level bar (a rectangle that will be filled)
        bar_width = 400
        bar_height = 40
        self.battery_bar = self.canvas.create_rectangle(x - 100, y, x + bar_width, y + bar_height, outline="black", fill="gray")

        #simulate the battery level as a percentage (will need input from CAN/GPIO here)
        #variable for battery percentage
        battPercent = 15
        self.update_battery_bar(battPercent, self.battery_bar)
        
        #label for the battery bar (FIX FONT)
        label = tk.Label(self.root, text=f"{label_text} ({battPercent}%)")
        label.place(x=x - 100, y=y - 25)

    def update_battery_bar(self, percent, battery_bar):
        #update the width of the battery bar based on the percent
        bar_width = 400  #total width of the battery bar
        filled_width = bar_width * (percent / 100)  #calculate the filled portion of the bar

        self.canvas.coords(battery_bar, self.canvas.bbox(battery_bar)[0], self.canvas.bbox(battery_bar)[1],
                           self.canvas.bbox(battery_bar)[0] + filled_width, self.canvas.bbox(battery_bar)[3])
        self.canvas.itemconfig(battery_bar, fill="green" if percent > 20 else "red")  #color it based on the level

    def draw_notches(self, center_x, center_y, radius):
        num_notches = 10
        for i in range(num_notches):
            angle = math.radians(i * (180 / (num_notches - 1))) + math.pi  # Flip by adding math.pi (180 degrees)
            notch_x1 = center_x + (radius - 10) * math.cos(angle)  # Short line for the notch
            notch_y1 = center_y + (radius - 10) * math.sin(angle)
            notch_x2 = center_x + radius * math.cos(angle)  # Longer line for the end of the notch
            notch_y2 = center_y + radius * math.sin(angle)

            #draw the notch
            self.canvas.create_line(notch_x1, notch_y1, notch_x2, notch_y2, width=2, fill="black")

    def draw_numbers(self, center_x, center_y, radius):
        #number of numbers you want, should be one or two per notch
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
