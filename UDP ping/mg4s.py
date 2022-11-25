from socket import * 
import time
import random

# Create a UDP socket 
serverSocket = socket(AF_INET, SOCK_DGRAM) 
# Assign IP address and port number to socket 
serverSocket.bind(('localhost', 12000)) 
serverSocket.settimeout(20.0)

while True: 
    # Receive the client packet along with the address it is coming from 
    try:
        current_time = time.time()
        message, address = serverSocket.recvfrom(1024) 
        recieve_time = time.time()
        serverSocket.sendto(message,('localhost', 1024))
        timelapse = recieve_time - current_time
        # The server responds 
        print('Server recieved: ' + message.decode())
        print('heartbeat recieved ' + str(round(timelapse)) + ' seconds ago') 
    except:
        print('No heartbeat after 20 seconds. Server quits.')
        print('Server stops')
        break
serverSocket.close() 