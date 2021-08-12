from raincounter_pb2 import DataPacket
import serial


if __name__ == "__main__":
    good = 0
    bad = 0
    bads = set()
    lastgoods = set()
    lastgood = 0
    lastbinary = None
    lastbinaries = set()
    with serial.Serial("/dev/ttyACM98", 9600) as serial:
        # for i in range(25):
        for i in range(1001):
            message = DataPacket()
            binary = serial.readline()[0:-1]
            # print(f"{binary=}")
            try:
                message.ParseFromString(binary)
                # print(f"{message.value=}, {message.packetType=}\n")
                good += 1
                lastgood = message.value
                lastbinary = binary
            except Exception as e:
                # print(f"{binary=}")
                bad += 1
                bads.add(binary)
                lastgoods.add(lastgood)
                lastbinaries.add(lastbinary)
        print(f"{bads=}")
        print(f"{lastgoods=}")
        print(f"{lastbinaries=}")
        print(f"{bad=},{good=}")
