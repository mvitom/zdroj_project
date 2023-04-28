

# client_socket = socket.socket()  # instantiate
# host = "192.168.10.251"  # as both code is running on same pc
# port = 3000

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


