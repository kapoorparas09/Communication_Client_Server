from pymodbus.client import ModbusTcpClient
from datetime import datetime, time
import random 
import time

host = '169.254.16.200'
port = 502
client = ModbusTcpClient(host, port)
while True:
    client.connect()
    data = random.randint(25, 35)
    rd = client.read_holding_registers(0)
    print(rd.registers)
    wr = client.write_registers(1000, data)
    time.sleep(5)