import socket
import time
#______________________________________________________________________
#                       socket
#______________________________________________________________________
client_socket = socket.socket()  # instantiate
host = "192.168.10.251"  # as both code is running on same pc
port = 3000

def socket_connect():
      # socket server port number
    try:
        client_socket.connect((host, port))
        print("zdroj pripojen")  # connect to the server
    except:
        print("could not connect")

        
def socket_disconnect():
    try:
        client_socket.close()  # close the connection
        print("client disconnected")
    except:
        print("couldnt disconnect")


#funkce pro nastaveni vsech hodnot na vybranem kanale
def set_channel(channel,voltage,current,limitV,limitC):
    channel = f"INST CH{channel}"
    voltage = f";VOLT {voltage}"
    current = f";CURR {current}"
    limitV = f";VOLT:LIM {limitV}"
    limitC = f";CURR:LIM {limitC}"
    return channel + voltage + current + limitV + limitC


#______________________________________________________________________

def switch_state():
    return "CHAN:OUTP:ALL?" #return 1, 0, 1

def switch_off_channel():
    return

def switch_on_all():
    return
def switch_off_ch1():
    return
#______________________________________________________________________



#switch 1,2,3 : ON
############################################################################
def switch_ch1(): 
    state = switch_state()
    #message = command.switch_on_channel1()
    try:
        client_socket.send(state.encode())
        chan = client_socket.recv(1024).decode()
        chan1,chan2,chan3= chan.split(",")
        if chan2 and chan3 == "1":
            message = "CHAN:OUTP:ALL 1,1,1"
        elif chan2== "1" and chan3 == "0":
            message = "CHAN:OUTP:ALL 1,1,0"
        elif chan2 == "0" and chan3 == "1":
            message = "CHAN:OUTP:ALL 1,0,1"
        elif chan2 and chan3== "0":
            message = "CHAN:OUTP:ALL 1,0,0"
        client_socket.send(message.encode())
    except:
        print("setch1: failed to send/recieve message")

def switch_ch2():
    state = switch_state()
    #message = command.switch_on_channel1()
    try:
        client_socket.send(state.encode())
        chan = client_socket.recv(1024).decode()
        chan1,chan2,chan3= chan.split(",")
        #while ch2 == "0":
        if chan1 and chan3 == "1":
            message = "CHAN:OUTP:ALL 1,1,1"
        elif chan1== "1" and chan3 == "0":
            message = "CHAN:OUTP:ALL 1,1,0"
        elif chan1 == "0" and chan3 == "1":
            message = "CHAN:OUTP:ALL 0,1,1"
        elif chan1 and chan3== "0":
            message = "CHAN:OUTP:ALL 0,1,0"
        # time.sleep(0.5)
        client_socket.send(message.encode())
    except:
        print("setch1: failed to send/recieve message")

def switch_ch3():
    state = switch_state()
    #message = command.switch_on_channel1()
    try:
        client_socket.send(state.encode())
        chan = client_socket.recv(1024).decode()
        chan1,chan2,chan3= chan.split(",")
        #while ch3 == "0":
        if chan1 and chan2 == "1":
            message = "CHAN:OUTP:ALL 1,1,1"
        elif chan1== "1" and chan2 == "0":
            message = "CHAN:OUTP:ALL 1,0,1"
        elif chan1 == "0" and chan2 == "1":
            message = "CHAN:OUTP:ALL 0,1,1"
        elif chan1 and chan2== "0":
            message = "CHAN:OUTP:ALL 0,0,1"
        # time.sleep(0.5)
        client_socket.send(message.encode())
    except:
        print("setch1: failed to send/recieve message")

#######################################################################





#______________________________________________________________



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

# def get_channel(channel):
#     channel = f"INST CH{channel}"
#     voltage = f";VOLT?"
#     current = f";CURR?"
#     limitV =  f";VOLT:LIM?"
#     limitC =  f";CURR:LIM?"
#     return channel + voltage + current + limitV + limitC



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





#insert data do textbox-> takze nejspis tohle cele
#bude chtit do gui-čka

def get_channel1():
    channel = "1"
    message = get_voltage(channel)
    try:
        client_socket.send(message.encode())
    except:
        print("getvolt: failed to send message")
    try:
        data = client_socket.recv(1024).decode()
        print(data)
    except:
        print("getvolt: failed to recieve data")
    time.sleep(0.5)


    get_current(channel)
    message = get_current(channel)
    try:
        client_socket.send(message.encode())
    except:
        print("getcurr: failed to send message")
    try:
        data = client_socket.recv(1024).decode()
        print(data)
    except:
        print("getcurr: failed to recieve data")
    time.sleep(0.5)


    get_limitV(channel)
    message = get_limitV(channel)
    try:
        client_socket.send(message.encode())
    except:
        print("getlimV: failed to send message")
    try:
        data = client_socket.recv(1024).decode()
        print(data)
    except:
        print("getlimV: failed to recieve data")
    time.sleep(0.5)


    get_limitC(channel)
    message = get_limitC(channel)
    try:
        client_socket.send(message.encode())
    except:
        print("getlimC: failed to send message")
    try:
        data = client_socket.recv(1024).decode()
        print(data)
    except:
        print("getlimC: failed to recieve data")