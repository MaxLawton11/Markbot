#!/usr/bin/env python
import time
import serial
ser = serial.Serial(
port='/dev/pts/0',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)

for i in range(100)
    x=ser.readline()
    print(x)