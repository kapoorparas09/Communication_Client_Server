import pyModbusTCP
from pyModbusTCP.client import ModbusClient
import random
import time

client = ModbusClient(host='113.193.232.118', port= 502)
# print(client.connect())

while True:
    print(client.open())
    data = random.randint(25,35)

    # To write multiple registers
    # list = []
    # for i in range (10):
    #     data = random.randint(25,35)
    #     list.append(data)
    wr = client.write_single_register(1000, data)

    # Write multiple registers
    # wr = client.write_multiple_registers(1000,list, unit=1)
    time.sleep(3)
# print(client.open())
# print(client.read_holding_registers(0))
# print(client.write_single_register(1,[10]))