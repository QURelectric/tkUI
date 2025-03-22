# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 11:24:04 2025

@author: m_epo
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
