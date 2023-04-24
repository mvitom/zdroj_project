import socket
import command


def client_program():
    host = "192.168.10.251"  # as both code is running on same pc
    port = 3000  # socket server port number
    try:
        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server
    except:
        print("Could not connect")
    message = command.set_channel()
    #time.sleep(2) #input(" -> ")#  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print(data)  #recieved from server: # show in terminal

        message = input(" ..-> ")#command.set_voltage(2,2)#  # again take input
    
    client_socket.close()  # close the connection
    


if __name__ == '__main__':
    client_program()