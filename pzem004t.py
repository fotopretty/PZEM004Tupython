#!/usr/bin/env python3 
#coding=utf-8
# PZEM-004T library for ESP32 ESP32s by Voravit Euavatanakorn araiwah.com

from machine import UART
import time
import ustruct as struct		

class Pzem:
    setAddrBytes        =   b'\xB4\xC0\xA8\x01\x01\x00\x1E'
    readVoltageBytes 	= 	b'\xB0\xC0\xA8\x01\x01\x00\x1A'
    readCurrentBytes 	= 	b'\xB1\xC0\xA8\x01\x01\x00\x1B'
    readPowerBytes 		= 	b'\xB2\xC0\xA8\x01\x01\x00\x1C'
    readRegPowerBytes 	= 	b'\xB3\xC0\xA8\x01\x01\x00\x1D'

    def __init__(self):
        self.ser = UART(2, baudrate=9600, rx=16, tx=17, timeout=500)
        self.ser.init(9600, bits=8, parity=None, stop=1)
                
    def isReady(self):
        self.ser.write(self.setAddrBytes)
        time.sleep(1)
        rcv = self.ser.read(7)
        #print(rcv)
        if len(rcv) == 7:
            unpacked = struct.unpack("!7B", rcv)
            if(self.checkChecksum(unpacked)):
                return True
            

    def readVoltage(self):
        self.ser.write(self.readVoltageBytes)
        #print(self.readVoltageBytes)
        time.sleep(1)
        rcv = self.ser.read(7)
        #print(rcv)
        if len(rcv) == 7:
            unpacked = struct.unpack("!7B", rcv)
            if(self.checkChecksum(unpacked)):
                tension = unpacked[2] + unpacked[3]/10.0
                return tension

    def readCurrent(self):
        self.ser.write(self.readCurrentBytes)
        time.sleep(1)
        rcv = self.ser.read(7)
        #print(rcv)
        if len(rcv) == 7:
            unpacked = struct.unpack("!7B", rcv)
            if(self.checkChecksum(unpacked)):
                current = unpacked[2]+unpacked[3]/100.0
                return current

    def readPower(self):
        self.ser.write(self.readPowerBytes)
        time.sleep(1)
        rcv = self.ser.read(7)
        #print(rcv)
        if len(rcv) == 7:
            unpacked = struct.unpack("!7B", rcv)
            if(self.checkChecksum(unpacked)):
                power = unpacked[1]*256+unpacked[2]
                return power

    def readRegPower(self):
        self.ser.write(self.readRegPowerBytes)
        time.sleep(1)
        rcv = self.ser.read(7)
        #print(rcv)
        if len(rcv) == 7:
            unpacked = struct.unpack("!7B", rcv)
            if(self.checkChecksum(unpacked)):
                regPower = unpacked[1]*256*256+unpacked[2]*256+unpacked[3]
                return regPower

    def checkChecksum(self, _tuple):
		_list = list(_tuple)
		_checksum = _list[-1]
		_list.pop()
		_sum = sum(_list)
		if _checksum == _sum%256:
			return True
		else:
			return False

#print("Checking readiness")
#sensor = Pzem()
#sensor.isReady()         

#while True:
#    print(sensor.readVoltage(),sensor.readCurrent(),sensor.readPower(),sensor.readRegPower())
#    time.sleep(1)