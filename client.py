import socket

def sockprogclient():

    host = "127.0.0.1"
    port = 1244

    Sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Sockobj.connect((host , port))#

    request = input(" Enter any Request to send : ")

    while request != 'end':

        Sockobj.send(request.encode())

        response = Sockobj.recv(1024).decode()

        print('Response from server: ' + str(response))#junk values may come

        request = input(" Enter another request: ")
    
    Sockobj.close()


if __name__ == '__main__':
    sockprogclient()