from socket import *

serverPort = 12005
# AF_INET -> IPv4 network
# SOCK_STREAM -> TCP socket
serverSocket = socket(AF_INET,SOCK_STREAM)
# binding the server port number to a socket
serverSocket.bind(('', serverPort))
# listening for at least 1 queued connection
TCPConnections = 1
serverSocket.listen(TCPConnections)

# creates TCP connection socket after a request has been made to the welcoming socket
connectionSocket, address = serverSocket.accept()
# this completes the 3 way handshake

# Textbook
# "With TCP, all bytes sent from one side are not only guaranteed to arrive
# at the other side but also guaranteed arrive in order."
sentence = ''
bufferSize = 1024

sentence = connectionSocket.recv(bufferSize).decode("UTF-8")
# 1024 = the receive buffer size
print(sentence)
# Doing server manipulation on received data
capitalizedSentence = sentence.upper()
# sending modified data back to client
connectionSocket.sendall(capitalizedSentence.encode("UTF-8"))

connectionSocket.close()
