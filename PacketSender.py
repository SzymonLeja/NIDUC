import random


class PacketSender:
    packetValue = ""

    def __init__(self, packet):
        self.packetValue = packet.value

    def set_packet(self, packet):
        self.packetValue = packet

    def send_packet(self, p):
        self.noise_generator(p)

    def noise_generator(self,p):
        listValue = list(self.packetValue)
        for packetIndex in range(0, len(listValue) - 1):
            packetBit = listValue[packetIndex]
            randomNumber = int(random.random() * 1000)
            if(p>0):
                if randomNumber % p == 0:
                    if packetBit == "0":
                        listValue[packetIndex] = "1"
                    else:
                        listValue[packetIndex] = "0"
        self.packetValue = "".join(listValue)
