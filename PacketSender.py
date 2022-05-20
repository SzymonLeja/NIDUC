import random

import numpy.random


class PacketSender:
    packetValue = ""

    def __init__(self, packet):
        self.packetValue = packet.value

    def set_packet(self, packet):
        self.packetValue = packet

    def send_packet(self, p):
        if p == 0:
            self.CEC()
        else:
            self.BSC(p)

    def BSC(self, p):
        listValue = list(self.packetValue)
        randomNumber = random.random()
        if randomNumber < p:
            for packetIndex in range(0, len(listValue) - 1):
                packetBit = listValue[packetIndex]
                randomNumber = random.random()
                if randomNumber < p:
                    if packetBit == "0":
                        listValue[packetIndex] = "1"
                    else:
                        listValue[packetIndex] = "0"
            self.packetValue = "".join(listValue)

    def CEC(self):
        listValue = list(self.packetValue)
        cyclicErrorRate = 2
        for packetIndex in range(0, len(listValue)):
            packetBit = listValue[packetIndex]
            if(packetIndex%cyclicErrorRate==0):
                if packetBit == "0":
                    listValue[packetIndex] = "1"
                else:
                    listValue[packetIndex] = "0"
        self.packetValue = "".join(listValue)
