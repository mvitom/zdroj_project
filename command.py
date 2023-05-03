

def set_channel(channel,voltage,current,limitV,limitC):
    channel = f"INST CH{channel}"
    voltage = f";VOLT {voltage}"
    current = f";CURR {current}"
    limitV = f";VOLT:LIM {limitV}"
    limitC = f";CURR:LIM {limitC}"
    return channel + voltage + current + limitV + limitC

def get_channel(channel):
    channel = f"INST CH{channel}"
    voltage = f";VOLT?"
    current = f";CURR?"
    limitV =  f";VOLT:LIM?"
    limitC =  f";CURR:LIM?"
    return channel + voltage + current + limitV + limitC
    
def switch_state():
    return "CHAN:OUTP:ALL?"
def switch_on_channel1():
    return "CHAN:OUTP:ALL 1,0,0"
def switch_on_channel2():
    return "CHAN:OUTP:ALL 0,1,0"
def switch_on_channel3():
    return "CHAN:OUTP:ALL 0,0,1"

def switch_off_channel():
    return

# def get_channel(channel,voltage,current,limitV,limitC):
#     get_voltage(channel,voltage)
#     get_current(channel,current)
#     get_limitV(channel,limitV)
#     get_limitC(channel,limitC) 

#####################################

def get_voltage(channel):
    channel = f"INST CH{channel}"
    voltage = f";VOLT"
    return channel + voltage

def get_current(channel):
    channel = f"INST CH{channel}" 
    current = f";CURR?"
    return channel + current

def get_limitV(channel):
    channel = f"INST CH{channel}"
    limitV = f";VOLT:LIM?"
    return channel + limitV

def get_limitC(channel):
    channel = f"INST CH{channel}"
    limitC = f";CURR:LIM?"
    return channel + limitC

# def get_voltage_ch1():
#     channel = "1"
#     message = get_voltage(channel)
#     try:
#         tcp_client.client_socket.send(message.encode())
#     except:
#         print("getch1: failed to send message")
#     try:
#         data = tcp_client.client_socket.recv(1024).decode()
#         print(data)
#     except:
#         print("getch1: failed to recieve data")
