import pymodbus
from pymodbus.client import ModbusSerialClient
# from pymodbus.client.sync import ModbusSerialClient
import serial
from serial import *

client = ModbusSerialClient(method = "rtu", port = "12345", stopbits=1, bytesize=8, parity='N',baudrate=9600)

print(client.connect())

# Read holding register value
client_result = client.read_holding_registers(address=40001, count=10, slave=1)
print(client_result.registers)

# Write holding register value
client_write = client.write_register(40001, 50, slave=1)
print(client_write)