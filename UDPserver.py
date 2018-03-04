from socket import *
serverPort = 12008
# AF_INET -> IPv4 network
# SOCK_DGRAM -> UDP connection
serverSocket = socket(AF_INET, SOCK_DGRAM)

# operating system will specifies port number not done manually
# binding server port number to the socket
serverSocket.bind(('', serverPort))

print('The server is ready to receive')
sentence = ''
while True:
    #  max of 2048 bytes
    s, clientAddress = serverSocket.recvfrom(2048)
    sentence = s.decode('UTF-8')

    if sentence == 'stop':
        break

    print(sentence)
    # manipulating data received from client
    capitalizedSentence = sentence.upper().encode('UTF-8')
    # sending data to client
    serverSocket.sendto(capitalizedSentence, clientAddress)
    # address destination is attached to the message - automatically by OS

# we can have multiple on UDP
