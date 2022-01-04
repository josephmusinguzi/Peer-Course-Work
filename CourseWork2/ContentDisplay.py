from socket import *
import json
import time

#declaring socket and port values.
udpSocket = socket(AF_INET, SOCK_DGRAM)
socketPort = 8000

udpSocket.bind(('', socketPort))  #creating the socket

new_dict = {}
x = {}

print("Listening...")

while True:
    dict, address = udpSocket.recvfrom(100240)
    data = json.loads(dict)
    for i in data["chunks"]:
        chunk_name = i
        new_dict[(chunk_name) ] = address[0]    #create dictionary to store the broken file


        a = new_dict.copy()
        a.update(x)

        file = open('dict.txt', 'w')

        conDict = file.write(json.dumps(a))
        file.close()

        ip_addr = address #its equal to ip
    print(a)
    time.sleep(5)