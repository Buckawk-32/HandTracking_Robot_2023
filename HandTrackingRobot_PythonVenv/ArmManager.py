import serial
import threading
import time

# TODO: Make threading possible, so you can have a countinous stream of data on both ends

# * https://forum.arduino.cc/t/two-ways-communication-between-python3-and-arduino/1219738
# * This is a forum post for a polished 2 way echo from python to arduino
# * Check this when you want to polish up the UI of this program or when you want to add threading to this program

class ArdunioManager:

    def __init__(self, baud_rate):
        self.baud_rate = baud_rate
        self.COM = None
        self.devID = None
        self.threadRun = False
        self.thread = None
        self.srl = None

        self.findDevice()
        

    def findDevice(self):
        ports = serial.tools.list_ports.comports()
        choices = []
        print("")
        print('PORT\tDEVICE\t\t\tMANUFACTURER')
        for index, vaule in enumerate(sorted(ports)):
            if (vaule.hwid != 'n/a'):
                choices.append(index)
                print(index, '\t', vaule.name, '\t', vaule.manufacturer)

        choice = -1
        while choice not in choices:
            selectedPort = input("Select Which Port >> ")
            
            if selectedPort == "q":
                exit(0)

            if selectedPort.isnumeric and int(selectedPort) <= int(max(choices)):
                choice = int(selectedPort)

        print("Selecting >> ", ports[choice].name)
        print("")
        print("Device Port >> ", ports[choice].device)
        print("Device ID >> ", ports[choice].hwid)
        print("")

        self.COM = ports[choice].device
        self.devID = ports[choice].hwid


    def start(self):
        if self.srl == None:
            self.srl = serial.Serial(port=self.COM, baudrate=self.baud_rate, timeout=0.1)
        else:
            self.srl.open()

        self.threadRun = True
        self.thread = threading.Thread(target=self.sendData())


    def stop(self):
        if self.threadRun == True:
            self.threadRun = False
            self.thread.join()
            self.srl.close()

    
    def sendData(self, data):
        self.srl.write(bytes(data, 'utf-8'))
        time.sleep(0.05)
        x = self.srl.readline()
        print(x)
        if x == b"correct":
            print(f"Both sites comfirmed password: {x}")
        
            





class ServoManager:
    pass

