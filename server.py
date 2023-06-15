import pyModbusTCP
from pyModbusTCP.server import ModbusServer, DataBank
# import time
# from time import sleep
# from random import uniform

# Creating an instance

server = ModbusServer("113.193.232.118", 502, no_block=True)

try:
    print("Start Server.....")
    server.start()
    print("Server is online")
    # state = [0]
    while True:
    #     DataBank.set_words(0, [int(uniform(0, 100))])
    #     if state != DataBank.get_words(1):
    #         state = DataBank.get_words(1)
    #         print("Value of Register 1 has changed to : "+ str(state))
    #         sleep(0.5)
        continue
except:
    print("Shutdown Server.....")
    server.stop()
    print("Server is offline")