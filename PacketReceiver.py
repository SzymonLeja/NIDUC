class PacketReceiver:
    encodedPacket = None
    encodedBit = None
    decodedPacket = None

    def receive_packet(self, packet):
        self.encodedPacket = packet
        return self.packet_decoder()

    def packet_decoder(self):
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
