import serial
import time

ser = serial.Serial('COM3', 9600)

def send_data_to_serial(port, data):
    ser.write(data)


# Code for testing serial connection

# while True:
#     send_data_to_serial('COM3', b'k')
#     time.sleep(1)
#     send_data_to_serial('COM3', b's')
#     time.sleep(1)
#     send_data_to_serial('COM3', b'p')
#     time.sleep(1)