# Foster Ecklund
# Relectric Interior Team 

# ***********************************************************************
#                       CANHandler.py
# File Contains The Class Used to read and write from the CAN bus
# ***********************************************************************

#Library Imports
import queue
import can
from time import sleep

#Import Global Variables form Globals
import Globals

# CanBus Handler Class
class CANHandler:
    def __init__(self) -> None:
        # Temporary Virtual Busses for Testing
        # Add real Bus when Raspberry Pi is connected
        self.bus1 = can.interface.Bus('test', interface='virtual')
        self.bus2 = can.interface.Bus('test', interface='virtual')
        # Initialize Queue for Messages
        self.write_queue = queue.Queue()
        self.running = True

    def run(self):
        # Continuously Read and Write from the CAN Bus
        while self.running:
            if not self.write_queue.empty():
                message = self.write_queue.get()
                self.writeToBus(message)

            self.readFromBus()    
            # Simulate a delay
            sleep(0.1)

    def stop(self):
        # Stop the CAN Bus Handler
        self.running = False     

    def readFromBus(self):
        # Error handling for reading from the CAN Bus
        try:
            self.reciveMessage()
        except can.CanError:
            print("Error Could not Read CAN Bus")

    def reciveMessage(self):
        # Read from the CAN Bus with a timeout of 1 second
        msg = self.bus2.recv(timeout = 1.0)
        if msg:
            # Check if the message is in the Signal Dictionary
            if msg.arbitration_id in Globals.canSignalDict:
                self.decodeMessage(msg)    
        else:
            print("No Message was read in Timeout Period") 

    def decodeMessage(self, msg):
        # Decode the message using the decode function from the Signal Dictionary
        signal = Globals.canSignalDict[msg.arbitration_id]
        value = signal['decode'](msg.data)

        # Update the Global Signal Values 
        # Ensure that the Global Data Lock is used to access the Global Variables safely across threads
        with Globals.canDataLock:
            Globals.canSignalValues[signal['name']] = value
        # Debug Print the Message
        # print(f"r: {msg}")                   

    def writeToBus(self, msg):
        # Check if the input is in the Message Dictionary
        if msg in Globals.canMessageDict:
            self.sendMessage(msg)

    def sendMessage(self, msg):
        message = Globals.canMessageDict[msg]
        # Construct the CAN Message using the fields from the Message Dictionary
        Out = can.Message(
            arbitration_id=message['TargetID'],     # Set the CAN ID here
            data=message['Payload Data'],           # Payload data (up to 8 bytes)
            is_extended_id=message['ExtendedID']    # Standard ID, not extended
        )
        # Error handling for writing to the CAN Bus
        try:
            self.bus1.send(Out)
            print(f"w: {Out}")

        except can.CanError:
            print("Message NOT sent")                

    def queueMessage(self,message):
        # Add a message to the write queue
        self.write_queue.put(message)