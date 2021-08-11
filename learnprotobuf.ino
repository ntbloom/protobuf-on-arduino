#include "src/pb_encode.h"
#include "src/raincounter.pb.h"


static pb_ostream_t stream;
static uint8_t buffer[64];
static DataPacket packet;
static int32_t tempF = 72;
static int32_t tempC = 25;

void setup() {
    Serial.begin(9600);
}

void sendData(bool metric) {
    if (metric) {
        packet.value = tempC--;
        packet.packetType = DataPacket_PacketType_TEMPERATURE_C;
    } else {
        packet.value = tempF--;
        packet.packetType = DataPacket_PacketType_TEMPERATURE_F;
    }

    stream = pb_ostream_from_buffer(buffer, sizeof(buffer));
    pb_encode(&stream, DataPacket_fields, &packet);
    Serial.write(buffer,stream.bytes_written);
    Serial.print("\n");
}

void loop() {
    if (tempF <= -40) tempF = 72;
    if (tempC <= -40) tempC = 25;
    sendData(true);
    sendData(false);
    delay(1000);
}

