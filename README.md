Using the feather Huzzah IoT kit and included ESP8266 I created a temperature 
logger for my home office.

![](https://jduckles-dropshare.s3-us-west-2.amazonaws.com/IMG_3266-lFmLo2Ak48.JPG)

I flashed the firmware from the factory Lua interpreter to micropython using 
[these instructions](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html).

Then using the AdaFruit Micropython Tool (ampy), I place config.py and main.py over USB:

```
ampy -p <your usb device> put main.py /main.py
ampy -p <your usb device> put config.py /config.py
```

You'll also need a MQTT broker (i.e. [mosquitto](https://mosquitto.org/man/mosquitto-8.html)) 
up and listening on port 1883.

What you do with it from there is up to you.

