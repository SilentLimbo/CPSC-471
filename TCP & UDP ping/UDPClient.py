from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),(serverName, serverPort))
receivedMessage, serverAddress = clientSocket.recvfrom(2048)
print('From Server: ', receivedMessage.decode())
clientSocket.close()