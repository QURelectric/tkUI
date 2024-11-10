# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:03:21 2024

@author: m_epo
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 19:15:53 2024

@author: m_epo
"""

#Head Unit GUI Template

#This sketch is the template for the Tkinter GUI we will be running on the
#Raspberry Pi, this will be what the user sees and interacts with 
#on the touchscreen digital display


#This is purely a template, all of the functions called by the buttons are just
#print statements and will be changed to have actual functionality when
#implemented on the Pi

#This will give interior a good practice space to design what we want the
#finished product to look like, we can go in and change the functions to have
#proper functionality later





#*********************************GUI CODE BELOW*******************************
#If editing, be sure to leave comments!


#LIBRARY INITIALIZATION * * * * * * * * *
import tkinter as tk
import webbrowser as wb
from PIL import Image, ImageTk
from tkinter import font, messagebox
import subprocess as sb
#import pyautogui


#BASE SETUP, ROOT TKINTER WINDOW
root = tk.Tk()
root.title("Orion Mk.I GUI")
#set background color, size, etc. Raspberry Pi resolution/size is 800x480, the +400 and +200
root.geometry("800x480+400+240")


#***** NEW ADDITIONS ******

#set the image as our background
back_Image = Image.open('C:/Users/m_epo/OneDrive/Documents/RELECTRIC/Misc/Queens_Flag_.png')
back_photo = ImageTk.PhotoImage(back_Image)

background_label = tk.Label(root, image=back_photo)
background_label.place(relwidth=1, relheight=1)


#custom font line
custom_font = font.Font(family="Helvetica", size=11, weight="bold", slant="italic")


#button states
global SpotifyState
SpotifyState = 0
global GoogleState 
GoogleState = 0



#BUTTON COMMANDS, EXECUTED WHEN BUTTONS ARE PRESSED
def Spotify_launch():
    global SpotifyState
    if SpotifyState == 0:
        wb.open('https://www.spotify.com')
        #set the state of Spotify client to 1, so the button cannot
        #be pressed a second time
        SpotifyState = 1
    else:
        messagebox.showinfo(title='Spotify Client Status', message='Spotify client is running')
            
    return

def GMaps_launch():
    global GoogleState 
    if GoogleState == 0:
        wb.open('https://www.googlemaps.com')
        #set the state of Spotify client to 1, so the button cannot
        #be pressed a second time
        GoogleState = 1
    else:
        messagebox.showinfo(title='Google Maps Status', message='Google Maps is open,\nnavigate to tab')
    
    return

def Ignition():
    print("Ignition Started")
    return

def VolumeUp():
    #something here for volume up on the sound system of the RaspBerry Pi
    print("Volume Up")
    return

def VolumeDown():
    #something here for volume up on the sound system of the RaspBerry Pi
    print("Volume Down")
    return

def FourWays():
    print("Four Ways toggled")
    return

def SetVolume():
    #This is our new function for setting the volume. We need to read the slider widget's value,
    #and send it to the CLI using subprocess with an amixer command
    
    
    """"
    #First, grab the value of the slider
    Volume_Level = VolumeSlider.get()
    #now, we want to build the 'amixer set Master' command string, and send it to the CLI using subprocess
    command = ["amixer","-c2","sset","'PCM'",f"{Volume_Level}"]
    sb.run(command)
    
    """
    
    #The above will only run on the Pi^^^
    return

#ButtonFrame Setup



#BUTTONS, FOR EACH FUNCTION ON THE CAR

#Spotify Launch - Upload image for spotify logo to add here!
SpotifyLaunchButton = tk.Button(root, text="Launch Spotify\nClient", width=20, height=5, font=custom_font, relief='raised', bd=5, command=Spotify_launch)
SpotifyLaunchButton.grid(row=0, column=0, sticky='news')

#Google Launch - Upload image for google maps logo to add here!
GoogleMapsLaunchButton = tk.Button(root, text="Launch Google Maps", width=20, height=5, font=custom_font, relief='raised', bd=5, command=GMaps_launch)
GoogleMapsLaunchButton.grid(row=1, column=0, sticky='news')

#Volume Buttons
VolumeSlider = tk.Scale(root, from_=0, to=100, length=175, width=75, font=custom_font, relief='raised', bd=5, orient=tk.HORIZONTAL)
VolumeSlider.grid(row=0, column=1, sticky='news')
#
SetVolButton = tk.Button(root, text="Set Volume", width=10, height=5, font=custom_font, relief='raised', bd=5, command=SetVolume)
SetVolButton.grid(row=0, column=3, sticky='news')


#Exit button --> TEMPORARY, REMOVE FOR FINAL IMPLEMENTATION IN THE CAR
QuitButton = tk.Button(root, text="Quit GUI (Demo)", width=20, height=10, font=custom_font, relief='raised', bd=5, command=lambda: [print("Quit Window"), root.destroy()])
QuitButton.grid(row=3, column=3, rowspan=2, columnspan=2)


#Messagebox test button
MsgBoxButton = tk.Button(root, text="Messagebox test", width=20, height=10, font=custom_font, relief='raised', bd=5, command=lambda: [messagebox.showinfo(title='Messagebox Test', message='Test Error Thrown')])
MsgBoxButton.grid(row=3, column=5, columnspan=2)




#somewhere in here, 


#START THE PIN READING FUNCTIONS HERE, REFRESH RATE/DELAY 1ms. Call the functions
#One after the other to start taking readings and update the values as needed



#BEGIN THE MAIN LOOP TO EXECUTE GUI. NOTHING AFTER THIS LINE OF CODE WILL
#EXECUTE UNTIL THE LOOP IS TERMINATED
root.mainloop()




#CODING/BUILD NOTES************************************************************