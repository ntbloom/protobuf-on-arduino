from raincounter_pb2 import DataPacket
import serial


if __name__ == "__main__":
    with serial.Serial("/dev/ttyACM98", 9600) as serial:
        for i in range(25):
            message = DataPacket()
            binary = serial.readline().rstrip()
            print(f"{binary=}")
            message.ParseFromString(binary)
            print(f"{message.value=}, {message.packetType=}\n")
