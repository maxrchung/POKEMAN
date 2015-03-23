import threading
import pickle
import _thread
from Client import *
from collections import deque
from socket import *
from Server import *

class NetworkManager:
    def __init__(self, server):
        # Tells whether the server should running
        # Should always be true, but it's good to include this here for clarity
        self.server = Server

        # Keeps track of the clients
        self.clients = []

        self.socket = socket(AF_INET, SOCK_STREAM) #TCP

        # Gets IP address
        self.ip = gethostbyname(gethostname())
        print('IP Address', self.ip)
        
        # Enables ReuseAddr, seems to be not necessary but I have here just in case
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        # Port 6969
        self.socket.bind((self.ip, 6969))
        self.socket.listen(1)

        self.connectionLock = threading.Lock()

        # Starts a connection thread that will wait for a client to connect to it
        self.connectionThread = threading.Thread(target=self.checkForConnections)
        # Tells connection thread to stop if the main program stops
        self.connectionThread.daemon = True
        self.connectionThread.start()

    def getSocket(self): return self.socket

    def getMessageQueue(self): return self.messageQueue

    def checkForConnections(self):
        while self.server.running:
            # We want to limit strain on the server, so put a limit
            # on the total number of allowed connected users
            if len(self.clients) <= 16:
                socket, addr = self.socket.accept()
                print("self.socket.accept()", (socket, addr))
                client = Client(socket, addr)

                self.connectionLock.acquire()
                self.clients.append(client)
                self.connectionLock.release()
