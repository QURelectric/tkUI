# Foster Ecklund
# Relectric Interior Team 

# *******************************************************************************
#                       CANBusDemo.py
# File Contains A Demo of how the 'can' Library and CAN Bus Dictionaries are used
# *******************************************************************************

#Library Imports
import can

#Import Global Variables form Globals
import Globals

# Initialize CAN bus using the virtual interface for testing
# using two Busses because by default a bus will ignore its own messages
bus1 = can.interface.Bus('test', interface='virtual')
bus2 = can.interface.Bus('test', interface='virtual')

def writeToBus(input):
    if input in Globals.canMessageDict:
        message = Globals.canMessageDict[input]

        Out = can.Message(
            arbitration_id=message['TargetID'],  # Set the CAN ID here
            data=message['Payload Data'],  # Payload data (up to 8 bytes)
            is_extended_id=message['ExtendedID']  # Standard ID, not extended
        )
        try:
            bus1.send(Out)
            print(f"w: {Out}")

        except can.CanError:
            print("Message NOT sent")


def readFromBus():
    try:
        msg = bus2.recv(timeout = 10.0)
        if msg:
            if msg.arbitration_id in Globals.canSignalDict:

                signal = Globals.canSignalDict[msg.arbitration_id]
                value = signal['decode'](msg.data)

                with Globals.canDataLock:
                    Globals.canSignalValues[signal['name']] = value

                print(f"r: {msg}")    
        else:
            print("No Message was read in Timeout Period")
    except can.CanError:
        print("Error Could not Read CAN Bus")    

writeToBus("signalSensor")
readFromBus()
writeToBus("helloWorld")
readFromBus()

with Globals.canDataLock:
    for name in Globals.canSignalValues:
        value = Globals.canSignalValues.get(name, "No value available")
        print(value)


bus1.shutdown()
bus2.shutdown()