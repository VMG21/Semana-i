import paho.mqtt.client as paho

table = [
["", "minimo", "equipo", "maximo"], 
["freq", 0, 0, 0], 
["nuc", 0, 0, 0], 
["uso", 0, 0, 0], 
["mem", 0, 0, 0] 
]

teams = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

def format_string(data):
    x = str(data)
    x = x.replace("b", "")
    x = x.replace("'", "")
    return x

def insert_data(string, pos, data):
    if "frec" in string:
        x = format_string(data)
        x = float(x)
        teams[pos][0] = x     
        
    elif "nuc" in string:
        x = format_string(data)
        x = int(x)
        teams[pos][1] = x

    elif "uso" in string:
        x = format_string(data)
        x = float(x)
        teams[pos][2] = x

    else:
        x = format_string(data)
        x = float(x)
        teams[pos][3] = x

def who_is(string, data):
    if "dafne" in string: insert_data(string, 0, data)

    elif "miles" in string: insert_data(string, 1, data)
    
    elif "dafne_badillo" in string: insert_data(string, 2, data)
    
    elif "victor" in string: insert_data(string, 3, data)
    
    elif "joseduardo" in string: insert_data(string, 4, data)
    
    elif "alonso" in string: insert_data(string, 5, data)
    
    else: insert_data(string, 6, data)

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    team = str(msg.topic)
    data = str(msg.payload)
    who_is(team, data)

    zip_list = list(zip(*teams))

    frec = [max(zip_list[0]), min(zip_list[0])]
    nuc = [max(zip_list[1]), min(zip_list[1])]
    uso = [max(zip_list[2]), min(zip_list[2])]
    mem = [max(zip_list[3]), min(zip_list[3])]


    table[1][1] = frec[0]
    table[1][2] = teams[3][0]
    table[1][3] = frec[1]

    table[2][1] = nuc[0]
    table[2][2] = teams[3][1]
    table[2][3] = nuc[1]

    table[3][1] = uso[0]
    table[3][2] = teams[3][2]
    table[3][3] = uso[1]
    
    table[4][1] = mem[0]
    table[4][2] = teams[3][3]
    table[4][3] = mem[1]

    print(table[0])
    print(table[1])
    print(table[2])
    print(table[3])
    print(table[4])
    print("\n")


client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("broker.mqttdashboard.com", 1883)

# client.subscribe("dafne/frec", qos=1)
# client.subscribe("dafne/nuc", qos=1)
# client.subscribe("dafne/uso", qos=1)
# client.subscribe("dafne/mem", qos=1)

client.subscribe("miles/frec", qos=1)
client.subscribe("miles/nuc", qos=1)
client.subscribe("miles/uso", qos=1)
client.subscribe("miles/mem", qos=1)

# client.subscribe("dafne_badillo/frec", qos=1)
# client.subscribe("dafne_badillo/nuc", qos=1)
# client.subscribe("dafne_badillo/uso", qos=1)
# client.subscribe("dafne_badillo/mem", qos=1)

client.subscribe("victor/frec", qos=1)
client.subscribe("victor/nuc", qos=1)
client.subscribe("victor/uso", qos=1)
client.subscribe("victor/mem", qos=1)

client.subscribe("joseduardo/frec", qos=1)
client.subscribe("joseduardo/nuc", qos=1)
client.subscribe("joseduardo/uso", qos=1)
client.subscribe("joseduardo/mem", qos=1)

client.subscribe("alonso/frec", qos=1)
client.subscribe("alonso/nuc", qos=1)
client.subscribe("alonso/uso", qos=1)
client.subscribe("alonso/mem", qos=1)

client.subscribe("anthony/frec", qos=1)
client.subscribe("anthony/nuc", qos=1)
client.subscribe("anthony/uso", qos=1)
client.subscribe("anthony/mem", qos=1)

client.loop_forever()
