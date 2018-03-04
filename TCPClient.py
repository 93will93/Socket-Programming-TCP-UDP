from socket import *
serverName = gethostname()
serverPort = 12005
clientSocket = socket(AF_INET, SOCK_STREAM)

# connect() addresses server welcoming TCP socket
address = (serverName, serverPort)
clientSocket.connect(address)

# setting sentence buffer
sentence = ''
bufferSize = 1024

sentence = input('Input lowercase sentence:')

clientSocket.sendall(sentence.encode("UTF-8"))
modifiedSentence = clientSocket.recv(bufferSize).decode("UTF-8")

# will receive at most 1024 bits
print('Server replies:', modifiedSentence)
clientSocket.close()
