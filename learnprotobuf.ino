#include "src/pb_encode.h"
#include "src/raincounter.pb.h"

static pb_ostream_t stream;
static uint8_t buffer[64];
static DataPacket packet;

void setup() {
    Serial.begin(9600);
    packet.packetType = DataPacket_PacketType_TEMPERATURE;
    packet.value = 72;
    stream = pb_ostream_from_buffer(buffer, sizeof(buffer));
    pb_encode(&stream, DataPacket_fields, &packet);
}

void loop() {
    for (uint i = 0; i < stream.bytes_written; i++) {
        Serial.print(buffer[i], HEX);
        Serial.print(";");
    }
    Serial.println();
    delay(1000);
}

