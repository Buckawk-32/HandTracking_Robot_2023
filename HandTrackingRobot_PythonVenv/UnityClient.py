import socket
import threading

class UnityClient:

    HOST, PORT = '127.0.0.1', 25001

    def __init__(self, data):
        self.socket = socket.socket(socket.AddressFamily.AF_INET, socket.SOCK_STREAM)

        self.thread = None
        self.isThreadRunning = False

        self.data = data

        self.serverCheck = False

        print("Started Unity Client...")
        self.start()


    def __del__(self):
        self.stop()


    def start(self):
        print("Started Unity Client thread...")
        self.thread = threading.Thread(target=self.sendData)

        self.isThreadRunning = True

        self.thread.start()
    

    def sendData(self):
        print("UnityClient Connecting to Server...")
        self.socket.connect((self.HOST, self.PORT))
    
        while True:
            if self.data != None:
                self.socket.sendall(self.data)
                self.serverCheck = False
            else:  
                self.serverCheck = True

            # while self.serverCheck == False:
            #     serverResponse = self.socket.recv(1024).decode("utf-8")

            #     if (serverResponse == "got data"):
            #         self.serverCheck = True


    def refreshData(self, data):
        self.data = data


    def stop(self):
        if self.isThreadRunning:
            self.socket.close()
            self.thread.join()

            self.isThreadRunning = False
            self.serverCheck = False











