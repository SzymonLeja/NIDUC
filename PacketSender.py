import random


class PacketSender:
    packetValue = ""

    def __init__(self, packet):
        self.packetValue = packet.value

    def set_packet(self,packet):
        self.packetValue = packet

    def send_packet(self):
        self.noise_generator()

    def noise_generator(self):
        randomNumber = int(random.random() * 10)
        if randomNumber % 99 != 0:
            if self.packetValue[0:len(self.packetValue) - 1].count("1") % 2 == 0 and (
            self.packetValue[0:len(self.packetValue) - 1].count("1")) != 0:
                self.packetValue = self.packetValue[:-1] + "1"
            else:
                self.packetValue = self.packetValue[:-1] + "0"


