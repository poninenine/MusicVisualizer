import serial
from serial.tools import list_ports

arduino_port = None

for port in list_ports.comports():
    print(port.device, port.name, port.description)
    if port.description == 'IOUSBHostDevice':
        arduino_port = port.device

ser = serial.Serial(arduino_port, 9600)

def send_data_to_serial(port, data):
    ser.write(data)


# Code for testing serial connection
# import time

# while True:
#     send_data_to_serial(arduino_port, b'k')
#     time.sleep(1)