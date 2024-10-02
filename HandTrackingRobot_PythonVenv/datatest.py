from ArmManager import ArdunioManager


data = ArdunioManager(baud_rate=115200, com='COM4')

data.startConnection()

num = input("What is the correct number > ")

data.sendData(num)

data.stopConnection()