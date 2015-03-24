import threading
import pickle
import _thread
from NetworkManager import *
from collections import deque
from socket import *
import pygame

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

        # For continuing to check for messages or not
        self.running = True

        self.messageQueue = deque()
        self.messageLock = threading.Lock()
        self.messageThread = threading.Thread(target=self.checkForMessages)
        self.messageThread.daemon = True
        self.messageThread.start()

        # Timers to check player alive
        self.aliveClock = pygame.time.Clock()
        self.aliveTimer = 0

    # Receives packets(messages) and puts them into queue
    def checkForMessages(self):
        while self.running:
            try:
                pickledData = self.socket.recv(4096)

                data = pickle.loads(pickledData)
            
                print(data)

                # Remember to lock so that we don't run into conflict accessing it
                self.messageLock.acquire()

                # Receives a message and puts it into the message queue
                self.messageQueue.append(data)
                
                self.messageLock.release()
            except:
                pass

    def sendPacket(self, content):
        packet = pickle.dumps(content)
        self.socket.send(bytes(packet))

    def disconnect(self):
        self.running = False
        print('1')
        self.socket.shutdown(SHUT_RDWR)
        print('2')
        self.socket.close()

        print('4')
        self.messageThread.join()
        print('5')
