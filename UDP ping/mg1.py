from logging import exception
from socket import *
import time

# Establish host information
recieve_port = 1024

# Establish server information
remote_host = 'localhost'
remote_port = 12000

# Create our socket for sending and recieveing messages from server
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)
clientSocket.bind((remote_host, recieve_port))

# Set up varriables we will be using
num_pings = 50
ping_num = 1
min_rtt = 0
max_rtt = 0
avg_rtt = 0
packets_dropped = 0.0
total_packets = 0.0
packet_loss_rate = 0.0

# Loop for 10 pings
while ping_num <= num_pings:
    # Create a message to output later
    initial_time = time.time() 
    message = 'Mina ' + str(ping_num) + ': ' + time.ctime(initial_time)
    clientSocket.sendto(message.encode(),(remote_host, remote_port))
    try:
        recieved_message, server_address = clientSocket.recvfrom(remote_port)
        post_time = time.time() 
        rtt = (post_time - initial_time)* 1000
        print('Mina ' + str(ping_num) + ': server reply: ' +
        recieved_message.decode() + ', RTT = ' + str(round(rtt, 2)) + ' ms')
        avg_rtt += rtt
        total_packets += 1
        if rtt < min_rtt or min_rtt == 0:
            min_rtt = rtt
        if rtt > max_rtt or max_rtt == 0:
            max_rtt = rtt
    except:
        print('Packet lost')
        packets_dropped += 1
    ping_num += 1
            
# Out of loop printing
print('Min RTT = ' + str(round(min_rtt, 2)) + ' ms')
print('Max RTT = ' + str(round(max_rtt, 2)) + ' ms')
avg_rtt = str(round((avg_rtt / total_packets), 2))
print('Avg RTT = ' + avg_rtt + ' ms')
packet_loss_rate = str(round((packets_dropped / ping_num), 2) * 100)
print('Packet lost = ' + packet_loss_rate + ' %')

clientSocket.close() 