# Relectric Interior Team

# *******************************************
#                   MainApp.py
#       This is the main file for the GUI
# *******************************************

#Import Libraries
import threading

#Import Classes
from DashboardWindow import DashboardWindowApp
from HomeWindow import HomeWindow

#Import Globals for Global Variables
import Globals

if __name__ == "__main__":
    #Initilize Homewindow Object
    HomeWindow(Globals.root, Globals.mainWindowSize)
    #Initilize Secondary window
    DashboardWindowApp(Globals.root, Globals.secondWindowSize)

    # ***********************************************************************
    #                               IMPORTANT: 
    # CAN bus thread has been disabled as no bus is connected and would 
    # Just throw errors repeatedly
    # Uncomment the following code to enable the CAN bus thread
    # ***********************************************************************

    # Create and start the CAN bus reading thread
    # CAN_thread = threading.Thread(target= Globals.Handler.run, daemon=True)
    # CAN_thread.start()
   
    Globals.root.mainloop()    
