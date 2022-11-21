#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
myConfig = {
        "identity": {
            "orgId": "ci5v5e",
            "typeId": "Rasberypi",
            "deviceId":"1234"
        },
        "auth": {
            "token": "12345678"
        }
    }
def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
while True:
    temp=random.randint(-5,100)
    flame=random.randint(0,10)
    gas=random.randint(0,100)
    if temp>50 or gas>50:
        if flame>8 and temp>50:
            myData={'temperature':temp,'flame':flame,'gas':gas,'exhaust':1,'sprinklers':1}
        else:
            myData={'temperature':temp,'flame':flame,'gas':gas,'exhaust':1,'sprinklers':0}
    else:
        myData={'temperature':temp,'flame':flame,'gas':gas,'exhaust':0,'sprinklers':0}    
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(5)
client.disconnect()

