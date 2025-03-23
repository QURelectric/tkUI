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




def CAN_DECODER(CAN_msg):
    #following our instructions in the GitHub file, here is the framework
    #for decoding the CAN message
    
    #pull the ID
    ID = CAN_msg.arbitration_id
    #data list to return
    #1st element speed, 2nd rpm, 3rd battery level
    data_array = []
    
    #decision tree with instructions based on ID  
    if ID == 1303:
        #we have the 'VCU_Inverter_Status_2' message, containing 
        #inverter RPM
        data_array[1] = int(CAN_msg.data[0]) #start bit 0     
    elif ID == 1304:
        #we have the 'VCU_Vehicle_Status_1' message
        #we need both the wheelspeed & battery level
        data_array[0] = int(CAN_msg.data[2]) #start bit 16
        data_array[2] = int(CAN_msg.data[4]) #start bit 32    
    else:
        1
        #do nothing
    
    return data_array




def receive_can_messages():
    bus = can.interface.Bus(channel='can0', bustype='socketcan')

    print("Starting to receive CAN messages...")

    try:
        while True:
            message = bus.recv()  #Receives a CAN message
            if message is not None:
                
                #pull CAN values from decoder function
                speed = CAN_DECODER(message)[0]
                rpm = CAN_DECODER(message)[1]
                batt_lvl = CAN_DECODER(message)[2]
                
                
                #This is technically still a test structure/format
                #so during implementation we're going to need
                #to do this in a single thread approach, and squeeze it into
                #our TKinter UI event loop
                #this means we may need to write a function which runs
                #using our scheduling loop, or something of the sort
                
                
    except KeyboardInterrupt:
        print("Program interrupted by user")
    finally:
        bus.shutdown()

if __name__ == '__main__':
    receive_can_messages()
