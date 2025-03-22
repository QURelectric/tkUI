# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 11:24:04 2025

@author: m_epo
"""

"""
Instruction List, for operating on bits
.dbc file has the different pieces of data listed as bits, with a byte length of 8 & a starting bit
following our findings in the workshop, this corresponds to single byte array elements

ie, a message, starting at bit 0 with byte length 8 is message.data[0] (0th element in the array)
starting bit 32 would be the 4th byte, meaning message.data[3] (3rd index element in the array)


For our dashboard, we need the following pieces of data (just to start, we can get more later):
under each data piece, instructions & ID from .dbc file are listed

Car battery Level
~~~~~~~~~~~~~~~~~~~
'VCU_Vehicle_Status_1' message

ID = 1304
start bit = 32 
data type (to be interpreted as) = unsigned integer
factor = 1   #multiply value by one
offset = 0   #add 0 to the value

The above is an example of a piece of data which needs no offset or factor applied to it,
we can just pull it straight from the message.data byte array




Car Wheelspeed
~~~~~~~~~~~~~~~~~~~
'VCU_Vehicle_Status_1' message
*Byte order is listed as little Endian, I think python handles this automatically*
ID = 1304
start bit = 16 
data type = unsigned integer
factor = 1  
offset = 0  

Car RPM
~~~~~~~~~~~~~~~~~~~
'VCU_Inverter_Status_2'

ID = 1303
start bit = 0
data type = signed integer  (-10000 to 10000 min & max values)
factor = 1  
offset = 0  




"""


#To run this, we'll need to install 'python-can' (I believe it's already installed)

import can

def receive_can_messages():

    filters = [{"can_id": 0x123, "can_mask": 0x7FF, "extended": False},]
    bus = can.interface.Bus(channel='can0', bustype='socketcan', can_filters=filters)

    print("Starting to receive CAN messages...")

    try:
        while True:
            message = bus.recv()  #Receives a CAN message
            if message is not None:
                
                #**********DATA MANIPULATION HERE*******
                
                #create msg object
                #print(message.data) #print data array from message
                #returns a bytre array
                
                object_1 = message.data[0] + 256*message.data[1]
                
                
                print(object_1) #prints first data byte in message, converted to decimal
                
                
                
                
                #***************************************
                
                #print(f"Received message: {message}")
    except KeyboardInterrupt:
        print("Program interrupted by user")
    finally:
        bus.shutdown()

if __name__ == '__main__':
    receive_can_messages()
