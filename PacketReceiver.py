class PacketReceiver:
    encodedPacket = None
    encodedBit = None
    decodedPacket = None

    def receive_packet(self, packet, method):
        self.encodedPacket = packet
        if method == "parity":
            return self.parity_bit_decoder()
        else:
            return self.two_from_five_decoder()

    def parity_bit_decoder(self):
        self.decodedPacket = self.encodedPacket[:-1]
        self.encodedBit = self.encodedPacket[-1]
        if (self.decodedPacket[0:len(self.decodedPacket)].count("1")) % 2 == 0 and \
                self.encodedBit == "0":
            return True
        elif (self.decodedPacket[0:len(self.decodedPacket)].count("1")) % 2 == 1 and \
                self.encodedBit == "1":
            return True
        else:
            return False

    def two_from_five_decoder(self):
        for i in range(0, int(len(self.encodedPacket) / 5 - 1), 5):
            tempValue = self.encodedPacket[i: i+5]
            if tempValue in ["11000", "10100"]:
                temp = 0
            else:
                return False
        return True
