import threading
import pickle
import _thread
from collections import deque
from socket import *
from Game import *

# Change this value if you want another computer to host server
# Winston:
TCP_IP = '192.168.42.125'
# Max:
#TCP_IP = '192.168.42.106'


class NetworkManager:
    def __init__(self, game):
        self.game = game

        self.socket = socket(AF_INET, SOCK_STREAM) #TCP

        # Enables ReuseAddr, seems to be not necessary but I have here just in case
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        self.socket.connect((TCP_IP, 6969))

        # Gets IP address
        self.ip = gethostbyname(gethostname())
        print(self.ip)

        self.messageQueue = deque()
        self.messageLock = threading.Lock()
        self.messageThread = threading.Thread(target=self.checkForMessages)
        self.messageThread.daemon = True
        self.messageThread.start()

    def getSocket(self): return self.socket
    def getMessageQueue(self): return self.messageQueue

    # Receives packets(messages) and puts them into queue
    def checkForMessages(self):
        while self.game.running:
            try:
                pickledData = self.socket.recv(4096)
                data = pickle.loads(pickledData)
            
                # Remember to lock so that we don't run into conflict accessing it
                self.messageLock.acquire()
                # Receives a message and puts it into the message queue
                self.messageQueue.append(data)
                self.messageLock.release()
            except:
                pass

    def disconnect(self):
        content = ['Disconnect']
        self.sendPacket(content)
        self.socket.shutdown(SHUT_RDWR)
        self.socket.close()
        self.game.running = False
        self.messageThread.join()
        
    def sendPacket(self, content):
        packet = pickle.dumps(content)
        self.socket.send(bytes(packet))
