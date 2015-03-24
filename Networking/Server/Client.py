import threading
import pickle
import _thread
from NetworkManager import *
from collections import deque
from socket import *

class Client:
    def __init__(self, socket, addr, networkManager):
        self.networkManager = networkManager
        self.socket = socket
        self.addr = addr
        self.name = ""
        self.win = False
        self.lose = False
        self.active = 0
        # Drafted 3 pokemans of client, gets replaced over 3 drafts
        self.draft = []
        # Selected 3 pokemans
        self.pokemans = []
        self.ready = False
        self.waitingCommand = []
        self.messageQueue = deque()
        self.messageLock = threading.Lock()
        self.messageThread = threading.Thread(target=self.checkForMessages)
        self.messageThread.daemon = True
        self.messageThread.start()

    # Receives packets(messages) and puts them into queue
    def checkForMessages(self):
        while self.networkManager.server.running:
            pickledData = self.socket.recv(4096)
            data = pickle.loads(pickledData)
            
            # Remember to lock so that we don't run into conflict accessing it
            self.messageLock.acquire()

            # Receives a message and puts it into the message queue
            self.messageQueue.append(data)

            self.messageLock.release()

    def sendPacket(self, content):
        packet = pickle.dumps(content)
        self.socket.send(bytes(packet))
