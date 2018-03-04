from socket import *
from  errno import *

serverName = gethostname()
serverPort = 12008
# same as UDP server
clientSocket = socket(AF_INET,SOCK_DGRAM)

s = ''
try:
    while True:
        # obtains sentence from user until return character
        s = input('Input lowercase sentence:')

        if s == 'stop':
            break

        sentence = s.encode('UTF-8')
        clientSocket.sendto(sentence, (serverName, serverPort))
        modifiedSentence, serverAddress = clientSocket.recvfrom(2048)
        # will receive at most buffer size of 2048 bytes
        print('Received from Server:', modifiedSentence.decode('UTF-8'))
except errno as e:
        print("Error Number: ", e)
finally:
        clientSocket.close()

