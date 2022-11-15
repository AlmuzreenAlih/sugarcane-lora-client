from pyLoraRFM9x import LoRa, ModemConfig
Channel = 1 #or chip to be used
ServerAddress = 2

def on_recv(payload):
    print("From:", payload.header_from)
    print("Received:", payload.message)
    print("RSSI: {}; SNR: {}".format(payload.rssi, payload.snr))

lora = LoRa(Channel, 5, ServerAddress, reset_pin = 25, modem_config=ModemConfig.Bw125Cr45Sf128, tx_power=14, acks=False)
# lora.on_recv = on_recv
#channel 1 yun, GPIO5 for interrupts

lora.set_mode_tx()

# Sends to a recipient device with address 10
message = "Hello there!"
# status = lora.send_to_wait(message, 10, retries=2)
status = lora.send(message, 10)
# send(data, header_to, header_id=0, header_flags=0)
if status is True:
    print("Message sent!")
else:
    print("No acknowledgment from recipient")
lora.close()