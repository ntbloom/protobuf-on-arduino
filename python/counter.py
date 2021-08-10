from raincounter_pb2 import DataPacket
import serial

"""
class Packet(DataPacket):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        print(f"type={self.packetType}, value={self.value}")
"""

if __name__ == "__main__":
    timeout = 10
    message = DataPacket()
    with serial.Serial("/dev/ttyACM98", 9600) as serial:
        binary = serial.readline()
        print(type(binary))
        # binary = bytearray([0x10, 0x48])
        print(f"{binary=}")
        message.ParseFromString(binary)
        print(f"{message.value=}, {message.packetType=}")
