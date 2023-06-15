import pymodbus
from pymodbus.client import ModbusSerialClient
# from pymodbus.client.sync import ModbusSerialClient
import serial
from serial import *

client = ModbusSerialClient(method = "tcp", port = "502", stopbits=1, bytesize=8, parity='N',baudrate=9600)

print(client.connect())

# Read holding register value
client_result = client.read_holding_registers(address="127.0.0.1", count=1, slave=1)
print(client_result.registers)

# Write holding register value
client_write = client.write_register("127.0.0.1", 50, slave=1)
print(client_write)