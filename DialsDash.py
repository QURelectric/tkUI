#Quick Sketch to test out Tkinter graphics for Dashboard. Trying out a basic dials design, class organization for compatibility

#Import statements
import tkinter as tk
import math
import time

class MovingDialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Moving Dial Demo")

        #Set window size
        self.offset = 75
        self.radius = 150
        self.canvas_width = 800
        self.canvas_height = 480
        self.center_x = self.canvas_width // 2 - (self.radius + self.offset)
        self.center_y = self.canvas_height // 2
        self.center_x2 = self.canvas_width // 2 + (self.radius + self.offset)
        self.center_y2 = self.canvas_height // 2


        #Create canvas
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()



	#Angle Variables for both dials
        #Initial angle and the movement speed
        self.angle = 180
        self.speed = 2  # degrees per update

        #Draw semi-circle dial 1
        self.canvas.create_arc(self.center_x - self.radius, self.center_y - self.radius,
                               self.center_x + self.radius, self.center_y + self.radius,
                               start=0, extent=180, style=tk.PIESLICE, width=2, fill="lightblue")
        #Draw semi-circle dial 2
        self.canvas.create_arc(self.center_x2 - self.radius, self.center_y2 - self.radius,
                                self.center_x2 + self.radius, self.center_y2 + self.radius,
                                start=0, extent=180, style=tk.PIESLICE, width=2, fill="lightgreen")


        #Draw dial, initially pointing to the left
        self.pointer = self.canvas.create_line(self.center_x, self.center_y,
                                               self.center_x - self.radius, self.center_y,
                                               width=4, fill="red")

        self.pointer2 = self.canvas.create_line(self.center_x2, self.center_y2,
                                                self.center_x2 - self.radius, self.center_y2,
                                                width=10, fill="blue")

        #Call dial updating functions
        self.update_dial()


#FUNCTION CALL BELOW TAKEN OUT FOR DEBUGGING
#        self.update_dial2()

    def update_dial(self):
        #Calculate the new pointer position based on current angle
        angle_rad = math.radians(self.angle)
        pointer_x = self.center_x + self.radius * math.cos(angle_rad)
        pointer_y = self.center_y + self.radius * math.sin(angle_rad)

        #Update pointer position
        self.canvas.coords(self.pointer, self.center_x, self.center_y, pointer_x, pointer_y)

        #Increment angle for movement condition
        self.angle += self.speed

        #Angle reset condition, will go back to 9 'oclock when dial hits 3 'oclock
        if self.angle >= 360:
            #delay for debugging
            time.sleep(1)
            self.angle = 180

        #Schedule update after 50ms
        self.root.after(50, self.update_dial)




    def update_dial2(self):
        #perform functions of above dial
        self.root.after(50, self.update_dial2)

#Create Tkinter root window
root = tk.Tk()

#Create MovingDialApp instance
app = MovingDialApp(root)

#Run Tkinter event loop
root.mainloop()
