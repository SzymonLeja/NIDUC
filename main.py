import math
import random
import time
import os
import numpy as numpy
import operator

from Packet import Packet
from PacketReceiver import PacketReceiver
from PacketSender import PacketSender
result = {}
numOfTests = 500
Packet.packet_length = 1080

filename = "./dataResult/" + str(numOfTests) + "data_"+ str(Packet.packet_length)+ "bit_packet.csv"
os.makedirs(os.path.dirname(filename), exist_ok=True)
fileData = open(filename, "w")

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
    sorted_keys = sorted(list(result.keys()), key = lambda x: (len(str(x)),x))
    sorted_result = sorted_dict = {k:result[k] for k in sorted_keys}
    dataString += "P= " + str(j)+"\n" +"Liczba powtorzen sygnalu; Liczba wystapien; Udzial procentowy\n"
    for k, v in sorted_result.items():
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