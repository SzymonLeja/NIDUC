import math
import random
import time

import numpy as numpy

from Packet import Packet
from PacketReceiver import PacketReceiver
from PacketSender import PacketSender

result = {}
numOfTests = 1000
fileData = open(str(numOfTests) + "data.csv", "w")
dataString = ""
startTime = time.process_time()
for j in numpy.arange(0.8,0.0,-0.1):
    for i in range(0, numOfTests):
        innerResult = []
        createdPacket = Packet()
        packetSender = PacketSender(createdPacket)
        packetReceiver = PacketReceiver()
        createdPacket = Packet()
        packetSender = PacketSender(createdPacket)
        packetReceiver = PacketReceiver()
        packetSender.send_packet(j)
        encodedPacket = packetSender.packetValue
        packetReceiver.receive_packet(encodedPacket)
        counter = 0
        while not packetReceiver.receive_packet(encodedPacket):
            packetSender.set_packet(createdPacket.value)
            packetSender.send_packet(j)
            encodedPacket = packetSender.packetValue
            packetReceiver.receive_packet(encodedPacket)
            counter += 1

        if (createdPacket.value == packetReceiver.encodedPacket):
            result[counter] = result.get(counter, 0) + 1
        else:
            result["broken - not detected"] = result.get("broken - not detected", 0) + 1

    dataString += "P= " + str(j)+"\n" +"Liczba powtorzen sygnalu; Liczba wystapien; Udzial procentowy\n"
    for k, v in result.items():
        dataString += str(k) + ";" + str(v) + ";" + str(round(float(v / (numOfTests * 1.00) * 100.00), 2))+"%" + "\n"
    dataString+= "\n"
    result = {}

elapsed = time.process_time()
print(elapsed - startTime)
fileData.write(dataString)
# print("\n-- Packet status at the end --")
# print("Packet sent: " + str(packetSender.packetValue))
# print("Packet received: " + str(packetReceiver.encodedPacket))
# print("Original encoded: " + str(createdPacket.value))
# print("----")