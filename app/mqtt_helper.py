import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, response):
    if response == 0:
        print("Connect Success")
        client.publish('raspberry/topic', payload=str({"hellov1" : "Worldv1"}), qos=0, retain=True)
        print("SEND")
    else:
        print(f"Connection failed")
        

client = mqtt.Client()
client.on_connect = on_connect
client.connect("localhost", 1883, 60)

def publish_message():
    print("PUBLISHG message")
    client.publish('raspberry/topic', payload=1, qos=1, retain=True)
publish_message()
client.loop_forever()