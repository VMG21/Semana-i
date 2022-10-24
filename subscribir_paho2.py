import paho.mqtt.client as paho
import re


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    # if "frec" in str(msg.topic):
    #     x = parse_frec(str(msg.payload))
    #     print(x[0])

    # if "nuc" in str(msg.topic): print(str(msg.payload)[2])

    # if "uso" in str(msg.topic): print(str(msg.payload)[2])
    
    # if "mem" in str(msg.topic):
    #     x = parse_mem(str(msg.payload))
    #     print(x)

    # if "proc" in str(msg.topic):
    #    x = parse_proc(str(msg.payload))
    #    print(x)
        
    
def parse_frec(message):
    x = re.search("\(([^\)]+)\)", message)
    a = x.group()
    a = a.replace("(", "")
    a = a.replace(")", "")
    a = a.replace(" ", "")
    a = a.split(",")
    return a

def parse_mem(message):
    x = message.split(",")
    x = x[2]
    x = x.replace(" ", "")
    x = x.replace("percent=", "")
    return x

def parse_proc(message):
    x = message.split("'")
    a = x[3]
    a = a.replace("'", "")
    return a
    

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("broker.mqttdashboard.com", 1883)
# client.subscribe("dafne/frec", qos=1)
# client.subscribe("dafne/nuc", qos=1)
# client.subscribe("dafne/uso", qos=1)
# client.subscribe("dafne/mem", qos=1)
# client.subscribe("dafne/proc", qos=1)
# client.subscribe("miles/frec", qos=1)
# client.subscribe("miles/nuc", qos=1)
# client.subscribe("miles/uso", qos=1)
# client.subscribe("miles/mem", qos=1)
# client.subscribe("miles/proc", qos=1)
# client.subscribe("dafne_badillo/frec", qos=1)
# client.subscribe("dafne_badillo/nuc", qos=1)
# client.subscribe("dafne_badillo/uso", qos=1)
# client.subscribe("dafne_badillo/mem", qos=1)
# client.subscribe("dafne_badillo/proc", qos=1)
client.subscribe("victor/frec", qos=1)
client.subscribe("victor/nuc", qos=1)
client.subscribe("victor/uso", qos=1)
client.subscribe("victor/mem", qos=1)
client.subscribe("victor/proc", qos=1)
# client.subscribe("joseduardo/frec", qos=1)
# client.subscribe("joseduardo/nuc", qos=1)
# client.subscribe("joseduardo/uso", qos=1)
# client.subscribe("joseduardo/mem", qos=1)
# client.subscribe("joseduardo/proc", qos=1)
# client.subscribe("alonso/frec", qos=1)
# client.subscribe("alonso/nuc", qos=1)
# client.subscribe("alonso/uso", qos=1)
# client.subscribe("alonso/mem", qos=1)
# client.subscribe("alonso/proc", qos=1)
# client.subscribe("anthony/frec", qos=1)
# client.subscribe("anthony/nuc", qos=1)
# client.subscribe("anthony/uso", qos=1)
# client.subscribe("anthony/mem", qos=1)
# client.subscribe("anthony/proc", qos=1)
client.loop_forever()
