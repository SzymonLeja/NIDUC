import random
from Packet import Packet
from PacketReceiver import PacketReceiver
from PacketSender import PacketSender

createdPacket = Packet()
packetSender = PacketSender(createdPacket)
packetReceiver = PacketReceiver()

createdPacket = Packet()
packetSender = PacketSender(createdPacket)
packetReceiver = PacketReceiver()
packetSender.send_packet()
encodedPacket = packetSender.packetValue
packetReceiver.receive_packet(encodedPacket)
print("\n-- Packet status at the start --")

print("Packet sent: " + str(packetSender.packetValue))
print("Packet received: " + str(packetReceiver.encodedPacket))
print("Original encoded: " + str(createdPacket.value))
print("----")
while packetReceiver.encodedPacket != createdPacket.value:
    print("Received packet is corrupted.. repeating...")
    packetSender.set_packet(createdPacket.value)
    packetSender.send_packet()
    encodedPacket = packetSender.packetValue
    packetReceiver.receive_packet(encodedPacket)

print("\n-- Packet status at the end --")
print("Packet sent: " + str(packetSender.packetValue))
print("Packet received: " + str(packetReceiver.encodedPacket))
print("Original encoded: " + str(createdPacket.value))
print("----")
