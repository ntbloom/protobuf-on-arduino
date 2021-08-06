#include "src/raincounter.pb.h"

DataPacket makePacket() {
  DataPacket packet;
  packet.packetType = DataPacket_PacketType_TEMPERATURE;
  packet.value = 72;
  return packet;
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  DataPacket packet = makePacket();
  Serial.println(packet.value);
  delay(1000);  
}
