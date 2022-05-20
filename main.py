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
numOfTests = 10000
Packet.packet_length = 16

filename = "./dataResult/" + str(numOfTests) + "data_"+ str(Packet.packet_length)+ "bit_packet_parity_BSC.csv"
os.makedirs(os.path.dirname(filename), exist_ok=True)
fileData = open(filename, "w")

dataString = ""
startTime = time.process_time()

#parity BSC
for j in numpy.arange(0.8,0.0,-0.1):
    for i in range(0, numOfTests):
        innerResult = []
        createdPacket = Packet("parity")
        packetSender = PacketSender(createdPacket)
        packetReceiver = PacketReceiver()
        createdPacket = Packet("parity")
        packetSender = PacketSender(createdPacket)
        packetReceiver = PacketReceiver()
        packetSender.send_packet(j)
        encodedPacket = packetSender.packetValue
        packetReceiver.receive_packet(encodedPacket,"parity")
        counter = 0
        while not packetReceiver.receive_packet(encodedPacket,"parity"):
            packetSender.set_packet(createdPacket.value)
            packetSender.send_packet(j)
            encodedPacket = packetSender.packetValue
            packetReceiver.receive_packet(encodedPacket,"parity")
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
fileData.write(dataString)

filename = "./dataResult/" + str(numOfTests) + "data_"+ str(Packet.packet_length)+ "bit_packet_2F5_BSC.csv"
os.makedirs(os.path.dirname(filename), exist_ok=True)
fileData = open(filename, "w")

dataString = ""
#2f5 BSC
for j in numpy.arange(0.8,0.0,-0.1):
    for i in range(0, numOfTests):
        innerResult = []
        createdPacket = Packet("2f5")
        packetSender = PacketSender(createdPacket)
        packetReceiver = PacketReceiver()
        createdPacket = Packet("2f5")
        packetSender = PacketSender(createdPacket)
        packetReceiver = PacketReceiver()
        packetSender.send_packet(j)
        encodedPacket = packetSender.packetValue
        packetReceiver.receive_packet(encodedPacket,"2f5")
        counter = 0
        while not packetReceiver.receive_packet(encodedPacket,"2f5"):
            packetSender.set_packet(createdPacket.value)
            packetSender.send_packet(j)
            encodedPacket = packetSender.packetValue
            packetReceiver.receive_packet(encodedPacket,"2f5")
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


result = {}
# filename = "./dataResult/" + str(numOfTests) + "data_"+ str(Packet.packet_length)+ "bit_packet_2F5.csv"
# os.makedirs(os.path.dirname(filename), exist_ok=True)
# fileData = open(filename, "w")
# two from five gen
# for i in range(0, numOfTests):
#     innerResult = []
#     createdPacket = Packet("2f5")
#     packetSender = PacketSender(createdPacket)
#     packetReceiver = PacketReceiver()
#     createdPacket = Packet("2f5")
#     packetSender = PacketSender(createdPacket)
#     packetReceiver = PacketReceiver()
#     # send 0 == CEC
#     packetSender.send_packet(0)
#     encodedPacket = packetSender.packetValue
#     packetReceiver.receive_packet(encodedPacket,"2f5")
#     counter = 0
#
#     while not packetReceiver.receive_packet(encodedPacket,"2f5"):
#         packetSender.set_packet(createdPacket.value)
#         packetSender.send_packet(0)
#         encodedPacket = packetSender.packetValue
#         packetReceiver.receive_packet(encodedPacket,"2f5")
#         counter += 1
#
#     if (createdPacket.value == packetReceiver.encodedPacket):
#         result[counter] = result.get(counter, 0) + 1
#     else:
#         result["broken - not detected"] = result.get("broken - not detected", 0) + 1
# sorted_keys = sorted(list(result.keys()), key=lambda x: (len(str(x)), x))
# sorted_result = sorted_dict = {k: result[k] for k in sorted_keys}
# dataString += "\n" + "Liczba powtorzen sygnalu; Liczba wystapien; Udzial procentowy\n"
# for k, v in sorted_result.items():
#     dataString += str(k) + ";" + str(v) + ";" + str(round(float(v / (numOfTests * 1.00) * 100.00), 2)) + "%" + "\n"
# dataString += "\n"
# result = {}

elapsed = time.process_time()
print(elapsed - startTime)

fileData.write(dataString)
print("\n-- Packet status at the end --")
print("Packet sent: " + str(packetSender.packetValue))
print("Packet received: " + str(packetReceiver.encodedPacket))
print("Original encoded: " + str(createdPacket.value))
print("----")