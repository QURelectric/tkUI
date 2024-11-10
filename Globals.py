# Relectric Interior Team

# *******************************************
#                   Globals.py
#            Used for Global Variables
# *******************************************

# Global CAN Handler Object
 #Set up a Handler Object for the Can Bus
from CANHandler import CANHandler
Handler = CANHandler()

# Base TK object to create tkinter objects
from tkinter import Tk
root = Tk()

# Global Window sizes used to initilaze Main window and Secondary Display
# Form "X_widthxY_width+X_Offset+Y_Offset"
mainWindowSize = "800x480+800+0"
secondWindowSize = "800x480+0+0"

# Gloabal Dictonaries to store releveant CAN Bus Information

# Signal Dictionary for Incoming CAN Bus Singals
# Hashed based on Signal ID in hex (to match the msg.arbitration_id)
#   Signal ID   : {
#   'name'      : Descriptive name for what the Signal is ex: Engine RPM, Battery Level
#   'decode'    : using lambda data: func
#                 Function that can take msg.data and return data that can be displayed 
#
# Blank Copy For ease of use
#   0x___   :{'name': "___________", 'decode': lambda data: ______ },

canSignalDict = {
    #Example Dummy Sensor
    0x001   :{'name': "Sensor Name", 'decode': lambda data: data },
    # World Sensor
    # Recives helloWorld Signal
    # decode converts byte string into a char string
    0x002   :{'name': "World", 'decode': lambda data: ''.join(chr(b) for b in data)}
}

# Dictionary for Values read from CAN Bus Signals
#**********NOT THREAD SAFE USE ONLY WITH dataLock**************
# One entry for every Signal ID in canSignalDict
#  Hashed based on 'name' found in cansignalDict
#  All Values Initilized to None
canSignalValues = {
    signal['name']: None for signal in canSignalDict.values()
}

# CAN Bus Data Lock
# canDataLock is a Lock object from the Threading Library
# by using with canDataLock:
#   data in the canSignalValues Dictionary can be accessed safely between threads 
#   with canDataLock automatically handles locking and unlocking
import threading   
canDataLock = threading.Lock()

# Signal Dictionary for Outgoing CAN bus Signals
# Needs to contain all feilds relevant for sending a message using the
#   can.Message() Method
#
# Hashed based on a message. messages should be Cammel Cased and unique
#   "message"   :{
#   'Target'    : Descriptive title of Target sensor. Who is reciving this message
#   'TargetID'  : ID of target in hex
#   'Payload Data'   : Payload Data in Hex, Contains the commands to send to the Target
#                 This could be a more readable string and then converted to Hex by a fucntion
#   'ExtendedID': Usually false unless ID is long
#
# Blank Copy For ease of use
#   "signalSensor"  :{'Target': "______", 'TargetID': _____, 
#                     'Payload Data': [_____], 
#                     'ExtendedID': False(Change if needed)
#                     },   
canMessageDict = {
    #Example Dummy Sensor
    "signalSensor"  :{'Target': "Sensor Name", 'TargetID': 0x001, 
                      'Payload Data': [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08], 
                      'ExtendedID': False
                      },
    # Hellow World Command
    # Sends the ASCII byte code for "Hello World!" across the bus                  
    "helloWorld"    :{'Target': "World", 'TargetID': 0x002,
                      'Payload Data': [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33],
                      'ExtendedID': False
                      }                    
}

