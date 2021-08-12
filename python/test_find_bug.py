import logging

from hypothesis import given, strategies as st

from python.raincounter_pb2 import DataPacket

log = logging.getLogger("proto")


def make_temp_packet(value):
    d = DataPacket()
    d.packetType = d.PacketType.TEMPERATURE_F
    d.value = value
    serialized = d.SerializeToString()
    log.info(serialized)
    return serialized


def decode_temp_packet(packet):
    d = DataPacket()
    d.ParseFromString(packet)
    val = d.value
    log.info(val)
    return val


MIN_INT32 = (-(2 ** 16)) + 1
MAX_INT32 = (2 ** 16) - 1


class TestProtobuf:
    @given(st.integers(min_value=MIN_INT32, max_value=MAX_INT32))
    # @given(st.just(0))
    def test_encode_decode(self, value):
        encoded = make_temp_packet(value)
        decoded = decode_temp_packet(encoded)
        assert decoded == value
