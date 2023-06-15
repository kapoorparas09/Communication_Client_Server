import serial
from pyModbusTCP.server import ModbusServer, DataBank
server = ModbusServer("113.193.232.118", 502, no_block = True)
try:
    print("start Server")
    server.start()
    print("server is online")
    while True:
        continue
except:
    print("shutdown Server" )
    server.stop()
    print("server is offline") 