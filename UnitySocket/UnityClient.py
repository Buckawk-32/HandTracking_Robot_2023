import socket
import threading

class UnityClient:

    HOST, PORT = '127.0.0.1', 25001

    def __init__(self, data):
        self.client = socket.socket(socket.AddressFamily.AF_INET, socket.SOCK_STREAM)

        self.clientThread = None
        self.isClientRunning = False

        self.data = data

        self.serverCheck = False

        print("Started Unity Client...")
        self.start()


    def __del__(self):
        self.stop()


    def start(self):
        print("Started Unity Client thread...")
        self.clientThread = threading.Thread(target=self.sendData)

        self.isClientRunning = True

        self.clientThread.start()
    

    def sendData(self):
        print("Unity Client Connecting to Server...")
        self.client.connect((self.HOST, self.PORT))
    
        while True:
            if self.data != None:
                self.client.sendall(self.data)
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
        if self.isClientRunning:
            try:
                self.client.close()
            except ConnectionAbortedError:
                print("Forced Abort!")

            print("UnityClient Disconneted from the Server!")
            self.clientThread.join()
            print("Stopped Unity Client Thread!")

            self.isClientRunning = False
            self.serverCheck = False











