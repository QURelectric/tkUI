import tkinter as tk
from PIL import Image, ImageTk
import os

# Initialize the root window
root = tk.Tk()
root.title("Dashboard Window")
root.geometry("2048x648")  # Set initial size of the window

# Create a canvas
canvas = tk.Canvas(root, width=2048, height=648)
canvas.pack()

class DashElement:
    def __init__(self, canvas, image_path, x=0, y=0, visible=False):
        self.canvas = canvas
        self.image_path = image_path
        self.frames = self.load_frames(image_path)
        self.current_frame = 0
        self.image_id = None
        self.blinking = False
        self.blink_task = None  # Holds the ID of the `after()` event
        self.set_position(x, y)
        self.set_visibility(visible)
        self.speed = 0

    def load_frames(self, image_path):
        frames = []
        img = Image.open(image_path)
        try:
            while True:
                frames.append(ImageTk.PhotoImage(img.copy()))
                img.seek(len(frames))  # Move to the next frame
        except EOFError:
            pass
        return frames

    def set_position(self, x, y):
        self.x = x
        self.y = y
        if self.image_id is not None:
            self.canvas.coords(self.image_id, x, y)

    def set_visibility(self, visible):
        self.visible = visible
        if visible:
            if self.image_id is None:
                self.image_id = self.canvas.create_image(self.x, self.y, anchor=tk.NW, image=self.frames[self.current_frame])
            else:
                self.canvas.itemconfigure(self.image_id, state='normal')
        else:
            if self.image_id is not None:
                self.canvas.itemconfigure(self.image_id, state='hidden')

    def update_image(self):
        """Update the displayed image with the current frame."""
        if self.image_id is not None:
            self.canvas.itemconfig(self.image_id, image=self.frames[self.current_frame])

    def next_frame(self):
        """Cycle through animation frames if multiple exist."""
        if len(self.frames) > 1:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.update_image()

    def set_speed(self, speed):
        """Set the speed and update the frame accordingly."""
        self.speed = speed
        self.current_frame = int(len(self.frames) * (speed / 100))
        self.update_image()

    def blink(self, interval=750):
        """Toggle visibility at a set interval."""
        if not self.blinking:
            self.blinking = True
            self._blink(interval)

    def _blink(self, interval):
        """Internal method for recursive blinking."""
        if self.blinking:
            self.set_visibility(not self.visible)
            self.blink_task = self.canvas.after(interval, self._blink, interval)

    def stop_blinking(self):
        """Stop blinking and hide the element."""
        if self.blinking:
            self.blinking = False
            if self.blink_task:
                self.canvas.after_cancel(self.blink_task)
                self.blink_task = None
            self.set_visibility(False)  # Ensure it is hidden when blinking stops

script_location = os.path.dirname(os.path.abspath(__file__))

background_image_path = os.path.join(script_location, "assets/dashboard/images/background.gif")
background = DashElement(canvas, background_image_path, x=0, y=0, visible=True)

# Speedometer in the center of the screen
speedometer_image_path = os.path.join(script_location, "assets/dashboard/images/Speedometer.gif")
speedometer = DashElement(canvas, speedometer_image_path, x=0, y=0, visible=True)
speed = 0

# Add a text widget to display the speed
speed_text = canvas.create_text(610, 420, text=f"{speed}", font=("Ubuntu",64), fill="white")

# Turn signals
right_turn_signal_image_path = os.path.join(script_location, "assets/dashboard/images/RightTurn.gif")
right_turn_signal = DashElement(canvas, right_turn_signal_image_path, x=0, y=0, visible=False)

left_turn_signal_image_path = os.path.join(script_location, "assets/dashboard/images/LeftTurn.gif")
left_turn_signal = DashElement(canvas, left_turn_signal_image_path, x=0, y=0, visible=False)

def blink_left_signal():
    right_turn_signal.stop_blinking()  # Stop right if active
    if left_turn_signal.blinking:
        left_turn_signal.stop_blinking()
    else:
        left_turn_signal.blink()

def blink_right_signal():
    left_turn_signal.stop_blinking()  # Stop left if active
    if right_turn_signal.blinking:
        right_turn_signal.stop_blinking()
    else:
        right_turn_signal.blink()

def blink_hazard():
    if right_turn_signal.blinking or left_turn_signal.blinking:
        right_turn_signal.stop_blinking()
        left_turn_signal.stop_blinking()
    else:
        right_turn_signal.blink()
        left_turn_signal.blink()

def update_speed(new_speed):
    global speed
    speed = new_speed if new_speed < 95 else 0
    speedometer.set_speed(speed)
    canvas.itemconfig(speed_text, text=f"{speed}")

# Bind keys to functions
# root.bind("<Up>", lambda e: speedometer.next_frame())
root.bind("<Up>", lambda e: update_speed(speed + 1))
root.bind("<Down>", lambda e: update_speed(max(0, speed - 1)))
root.bind("<Left>", lambda e: blink_left_signal())
root.bind("<Right>", lambda e: blink_right_signal())
root.bind("h", lambda e: blink_hazard())

# Start the main loop
root.mainloop()
