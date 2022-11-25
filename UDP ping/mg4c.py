from logging import exception
from socket import *
import time
import random

# Establish host information
recieve_port = 1024

# Establish server information
remote_host = 'localhost'
remote_port = 12000

# Create our socket for sending and recieveing messages from server
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(20.0)
clientSocket.bind((remote_host, recieve_port))

# Continuously send out messages with a 2-25 second delay
while True:
    delay = random.randint(2,25)
    time.sleep(delay)
    # Create a message to output later
    message = 'Mina client1: sent heartbeat to server ' + time.ctime()
    clientSocket.sendto(message.encode(),(remote_host, remote_port))
    try:
        recieved_message, server_address = clientSocket.recvfrom(remote_port)
        print(recieved_message.decode())
    except:
        print('Server has closed')
        break
clientSocket.close()