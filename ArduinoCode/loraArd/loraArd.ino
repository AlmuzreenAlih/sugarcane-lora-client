// rf95_datagram_server.pde
// -*- mode: C++ -*-
// Example sketch showing how to create a simple addressed, messaging server
// with the RHDatagram class, using the RH_RF95 driver to control a RF95 radio.
// It is designed to work with the other example rf95_datagram_client


#include <RHDatagram.h>
#include <RH_RF95.h>
#include <SPI.h>

#define CLIENT_ADDRESS 1
#define SERVER_ADDRESS 2
// Setup GPIO Pins
#define RFM95_CS 4
#define RFM95_RST 2
#define RFM95_INT 3

// Change to 434.0 or other frequency, must match RX's freq!
#define RF95_FREQ 915.0

// Singleton instance of the radio driver
RH_RF95 rf95(RFM95_CS, RFM95_INT);

// Class to manage message delivery and receipt, using the driver declared above
RHDatagram manager(rf95, SERVER_ADDRESS);

// Need this on Arduino Zero with SerialUSB port (eg RocketScream Mini Ultra Pro)
//#define Serial SerialUSB

void setup()
{
  // Rocket Scream Mini Ultra Pro with the RFM95W only:
  // Ensure serial flash is not interfering with radio communication on SPI bus
  //  pinMode(4, OUTPUT);
  //  digitalWrite(4, HIGH);
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);
  Serial.begin(115200);
  if (!manager.init()) {
    Serial.println("init failed");
    // Defaults after init are 434.0MHz, 13dBm, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on
  }
  else {
    Serial.println("Success");
  }
  if (!rf95.setFrequency(RF95_FREQ)) {
    Serial.println("setFrequency failed");
    while (1);
  }
  // The default transmitter power is 13dBm, using PA_BOOST.
  // If you are using RFM95/96/97/98 modules which uses the PA_BOOST transmitter pin, then
  // you can set transmitter powers from 5 to 23 dBm:
  //  driver.setTxPower(23, false);
  // If you are using Modtronix inAir4 or inAir9,or any other module which uses the
  // transmitter RFO pins and not the PA_BOOST pins
  // then you can configure the power transmitter power for -1 to 14 dBm and with useRFO true.
  // Failure to do that will result in extremely low transmit powers.
  rf95.setTxPower(14, true);
  // You can optionally require this module to wait until Channel Activity
  // Detection shows no activity on the channel before transmitting by setting
  // the CAD timeout to non-zero:
  //  driver.setCADTimeout(10000);
}

uint8_t data[] = "And hello back to you";
// Dont put this on the stack:
uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];

void loop()
{
  if (manager.available()) {
    uint8_t len = sizeof(buf);
    uint8_t from;
    if (manager.recvfrom(buf, &len, &from)) {
      //      Serial.print("got request from : 0x");
      //      Serial.print(from, HEX);
      //      Serial.print(": ");
      Serial.println((char*)buf);

      if (Serial.available()) {
        char Recv;
        data[] = Serial.readString();
        manager.sendto(data, sizeof(data), from);
      }

      // Send a reply back to the originator client
      //      manager.sendto(data, sizeof(data), from);
    }
  }
}
