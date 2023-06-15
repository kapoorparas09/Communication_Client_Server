import pyModbusTCP
from pymodbus.client.sync_diag import ModbusTcpClient
import random
import time
import json

client = ModbusTcpClient(host='113.193.232.118', port= 502)
# client = ModbusTcpClient(host='169.254.16.200', port= 1234)


while True:
    # print(client.open())
    client.connect()

    rr = client.read_holding_registers(1000, 1)
    # rr = client.read_holding_registers(1000, 10) # FOr reading 10 registers value at a time


    data = {
        "data": rr.registers[0]
        # "data": rr.registers  # For reading multiple values

    }

    print(json.dumps(data))
    time.sleep(4)