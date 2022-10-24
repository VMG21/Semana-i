import paho.mqtt.client as paho
import time
import re
import psutil

def on_publish(client, userdata, mid): print("mid: "+ str(mid))

def getListOfProcessSortedByMemory():
    listOfProcObjects = []

    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           listOfProcObjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass

    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    return listOfProcObjects

def parse_frec(message):
    x = re.search("\(([^\)]+)\)", message)
    a = x.group()
    a = a.replace("(", "")
    a = a.replace(")", "")
    a = a.replace(" ", "")
    a = a.split(",")
    a = a[0].replace("current=", "")
    return float(a)

def parse_nuc(message): return int(message[0])

def parse_uso(message): return int(message[0])

def parse_mem(message):
    x = message.split(",")
    x = x[2]
    x = x.replace(" ", "")
    x = x.replace("percent=", "")
    return float(x)

def parse_proc(message):
    x = re.search("name[^,]+", message)
    a = x.group()
    a = a.replace("name': '", "")
    a = a.replace("'", "")
    return a


client = paho.Client()
client.username_pw_set("victor", "G4t0")
client.on_publish = on_publish
client.connect("broker.mqttdashboard.com", 1883)
client.loop_start()

while True:
    listOfRunningProcess = getListOfProcessSortedByMemory()

    client.publish("victor/frec", parse_frec(str(psutil.cpu_freq())), qos=1)
    client.publish("victor/nuc",  parse_nuc(str(psutil.cpu_count())), qos=1)
    client.publish("victor/uso",  parse_uso(str(psutil.cpu_percent(4))), qos=1)
    client.publish("victor/mem",  parse_mem(str(psutil.virtual_memory())), qos=1)
    client.publish("victor/proc", parse_proc(str(listOfRunningProcess[0])), qos=1)

    time.sleep(30)
