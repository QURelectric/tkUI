# Relectric Interior Team 

# *************************************************************
#                       SubWindows.py
# File Contains The Classes for Sub windows within the GUI app
# *************************************************************

#Library Imports
import tkinter as tk

#Import Globals for Global Variables
import Globals

# Music Window
class MusicWindow:
    def __init__(self, root, window_geometry):
        self.window = tk.Toplevel(root)
        self.window.title("Music")
        self.window.geometry(window_geometry)

        #Spotify Launch - Upload image for spotify logo to add here!
        SpotifyLaunchButton = tk.Button(self.window, text="Launch Spotify", command=self.SpotifyLaunch)
        SpotifyLaunchButton.pack(pady=20)

        #Volume Buttons
        #Up
        VolUpButton = tk.Button(self.window, text="Volume +", command=self.VolumeUp)
        VolUpButton.pack(pady=20)
        #Down
        VolDownButton = tk.Button(self.window, text="Volume -", command=self.VolumeDown)
        VolDownButton.pack(pady=20)
        #Close Button
        close_button = tk.Button(self.window, text="Close", command=self.window.destroy)
        close_button.pack(pady=20)

    def SpotifyLaunch(self):
        #something here for launching spotify
        return
    
    def VolumeUp(self):
        #something here for volume up on the sound system of the RaspBerry Pi
        Globals.Handler.queueMessage("Volume Up!")
        return

    def VolumeDown(self):
        #something here for volume up on the sound system of the RaspBerry Pi
        Globals.Handler.queueMessage("volume Down!")
        return

# Navagation Window
class NavagationWindow:
    def __init__(self, root, window_geometry) -> None:
        self.window = tk.Toplevel(root)
        self.window.title("Navagation")
        self.window.geometry(window_geometry)
        #Google Launch - Upload image for google maps logo to add here!
        GoogleMapsLaunchButton = tk.Button(self.window, text="Launch Google Maps", command=self.GMapsLaunch)
        GoogleMapsLaunchButton.pack(pady=20)   

        close_button = tk.Button(self.window, text="Close", command=self.window.destroy)
        close_button.pack(pady=20)

    def GMapsLaunch(self):
        #something here for launching google maps
        return
    
# Control Window        
class ControlWindow:
    def __init__(self, root, window_geometry) -> None:
        self.window = tk.Toplevel(root)
        self.window.title("Control")
        self.window.geometry(window_geometry)
        #Car Ignition Button
        IgnitionButton =tk.Button(self.window, text="Start Ignition", command=self.Ignition)
        IgnitionButton.pack(pady=20)

        #Four Ways
        FourWaysButton = tk.Button(self.window, text="Toggle Four\nWays", command=self.FourWays)
        FourWaysButton.pack(pady=20)

        #Exit button --> TEMPORARY, REMOVE FOR FINAL IMPLEMENTATION IN THE CAR
        QuitButton = tk.Button(self.window, text="Quit GUI (Demo)", command=root.destroy)
        QuitButton.pack(pady=20)

        CanBusButton = tk.Button(self.window, text= "Stop\n CAN Bus", command=lambda: Globals.Handler.stop())
        CanBusButton.pack(pady=20)

        close_button = tk.Button(self.window, text="Close", command=self.window.destroy)
        close_button.pack(pady=20)            

    def Ignition(self):
        Globals.Handler.queueMessage("Engine Started!")
        return

    def FourWays(self):
        Globals.Handler.queueMessage("Four Ways On!")
        return

