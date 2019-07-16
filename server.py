import socket

def sockprogserver():

    host = "127.0.0.1"#
    port = 1244#should be 4 digits,if 64bit system then it should be 5digit

    print("\nServer is active and waiting for request")
    
    Sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#2 parameters :address,transfer(tcp and udp type)protocol
    
    Sockobj.bind((host , port))
    
    Sockobj.listen(1)#no of users(client) that can be connected to server

    connection, address = Sockobj.accept()#blocking funtc,waits for request,using this only coming from client side

    print("\nConnected with IP: " + str(address))#from which client

    while True:

        request = connection.recv(1024).decode()#1024bytes to receive is port takingsending or receiving traveling msg.....serverside decode..clientside encode

        if not request:
            break

        print("\nMessage from connected  user: " + str(request))

        
        #data = str(data).upper()

        #print("Response : " + str(data))
        response = input("\nResponse to Send to client: ")

        connection.send(response.encode())#send exclusively using 1024 over same connection
    
    connection.close()

if __name__ == '__main__':
    sockprogserver()