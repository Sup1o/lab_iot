import sys
from Adafruit_IO import MQTTClient
import time
import random
from simple_ai import *
from uart import *

AIO_FEED_IDs = ["nutnhan1","nutnhan2"]
AIO_USERNAME = "KietHuynh0810"
AIO_KEY = "aio_UkIl76A6OFkZmgHl0ylNGqBQpsDN"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)


def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + ", feed id: " + feed_id)

    write_data(payload)
    # if feed_id == "nutnhan1":
    #     if payload == "0":
    #         write_data("1")
    #     else:
    #         write_data("2")
    # elif feed_id == "nutnhan2":
    #     if payload == "0":
    #         write_data("3")
    #     else:
    #         write_data("4")


client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 5
sensor_type = 0
counter_ai = 2
ai_result = ""
while True:
    counter = counter - 1
    counter_ai = counter_ai - 1
    if counter_ai <= 0:
        counter_ai = 2
        if (ai_result != image_detector()):
            ai_result = image_detector()
            client.publish("ai",ai_result)
            
        
    # if counter <= 0:
    #     counter = 5
    #     print("Random data is publishing...")
    #     if sensor_type == 0:

    #         temp = random.randint(10, 20)
    #         print("Temperature..." + str(temp))
    #         client.publish("cambien1", temp)
    #         sensor_type = 1
    #     elif sensor_type == 1:

    #         humi = random.randint(50, 70)
    #         print("Humidity..."+ str(humi))
    #         client.publish("cambien2", humi)
    #         sensor_type = 2
    #     elif sensor_type == 2:
    #         light = random.randint(100, 500)
    #         print("Light..." + str(light))
    #         client.publish("cambien3", light)
    #         sensor_type = 0
    readSerial(client)
    time.sleep(1)
