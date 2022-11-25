from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = input('Input lowercase sentence:')
clientSocket.send(message.encode())
receivedMessage = clientSocket.recv(1024)
print('From Server: ', receivedMessage.decode())
clientSocket.close()