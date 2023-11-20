import BlynkLib
from machine import Pin

WIFI_SSID="..."
WIFI_PASS="..."
BLYNK_AUTH='...'

blynk = BlynkLib.Blynk(wifi_ssid=WIFI_SSID, wifi_pass=WIFI_PASS, auth=BLYNK_AUTH)

@blynk.on("V0")
def v0_write_handler(value):
    if int(value[0]) == 1:
        print("Led 1")
        led.value(1)
    else:
        print("Led 0")
        led.value(0)

led=machine.Pin("LED", machine.Pin.OUT)

blynk.sync_virtual(0)

while True:
    blynk.run()
