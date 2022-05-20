import random


class Packet:
    value = ""
    packet_length = 8

    def __init__(self,method):
        self.packet_generator(method)

    def packet_generator(self,method):
        for i in range(0, self.packet_length):
            self.value += str(int((random.random() * 10)) % 2)
        if method == "parity":
            self.packet_parity_bit_encoder()
        else:
            self.packet_two_from_five_encoder()

    def packet_parity_bit_encoder(self):
        # czy jest parzyste \/
        if self.value.count("1") % 2 == 0 and self.value.count("1") != 0:
            self.value += "0"
        else:
            self.value += "1"
        return self.value

    def packet_two_from_five_encoder(self):
        self.packet_length = self.packet_length * 5
        tempValue = ""
        for packetBit in self.value:
            if (packetBit == 0):
                tempBit = "11000"
            else:
                tempBit = "10100"
            tempValue += tempBit
        self.value = tempValue
