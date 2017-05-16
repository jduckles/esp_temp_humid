import config # Bring in config file for configuration parameters
import time

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(config.WIFI_SSID, config.WIFI_PASS)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def formatted_time():
    import machine
    rtc = machine.RTC()
    curtime = rtc.datetime()
    return "%s-%02d-%02dT%02d:%02d:%02d" % (curtime[0],curtime[1],
                                            curtime[2],curtime[4],
                                            curtime[5],curtime[6])

def get_temp_humid():
    import ujson
    import machine
    import dht
    d = dht.DHT22(machine.Pin(4))
    d.measure()
    return ujson.dumps({"time": formatted_time(),
                        "temp": d.temperature(),
                        "humid": d.humidity()})

def post_data(payload):
    from umqtt.simple import MQTTClient
    c = MQTTClient(config.MQTT_CLIENT,config.MQTT_BROKER)
    c.connect()
    c.publish(config.MQTT_NAME,payload)
    c.disconnect()

do_connect()
import ntptime
ntptime.settime()

while True:
    time.sleep(config.SAMPLE)
    post_data(get_temp_humid())
