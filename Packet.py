import random

class Packet:
    value = ""
    packet_length = 5

    def __init__(self):
        self.packet_generator()

    def packet_generator(self):
        for i in range(0, self.packet_length):
            self.value += str(int((random.random() * 10)) % 2)
        self.packet_encoder()

    def packet_encoder(self):
        if self.value.count("1") % 2 == 0 and self.value.count("1") != 0:
            self.value += "0"
        else:
            self.value += "1"
        return self.value