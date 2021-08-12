#include "src/pb_encode.h"
#include "src/raincounter.pb.h"

static pb_ostream_t stream;
static uint8_t buffer[64];
static DataPacket packet;
static int32_t tempF = 120;
static int32_t tempC = 25;
bool success;

static uint8_t error[] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00};

void setup() {
    Serial.begin(9600);
}

void sendData(bool metric) {
    // if (metric) {
    //    packet.value = tempC--;
    //   packet.packetType = DataPacket_PacketType_TEMPERATURE_C;
    //    } else {

    // if (tempF == 10) {
    //   tempF--;
    //  return;
    //}

    packet.value = tempF--;
    // packet.value = 10;

    packet.packetType = DataPacket_PacketType_TEMPERATURE_F;
    //   }

    stream = pb_ostream_from_buffer(buffer, sizeof(buffer));
    success = pb_encode(&stream, DataPacket_fields, &packet);
    if (!success) {
        // Serial.println(stream.errmsg);
        // Serial.println(tempF);
        Serial.write(error, sizeof(error));
    } else {
        Serial.write(buffer, stream.bytes_written);
        Serial.print("\n");
    }
}

void loop() {
    if (tempF <= -40) tempF = 72;
    if (tempC <= -40) tempC = 25;
    sendData(true);
    //  sendData(false);
    // delay(100);
}

