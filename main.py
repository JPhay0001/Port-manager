from tkinter import *
import socket
import random

def create_server(portval, password=""):

    host= socket.gethosname()
    port= portval #initiate port not over 1024

    assemble= ""
    letters= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    if password == "":

        for i in range(5):

            assemble+= str(random.randint(0,9))
            assemble+= random.choice(letters)

        password= assemble
            

    server_socket= socket.socket()
    server_socket.bind((host,port))

    server_socket.listen(30) #do not change the amount of  clients it can hear simultaneously
    connection, address= server_socket.accept()
    print("Client conected from: " + str(address) + ",  cheking if trustable...")

    pass_=  connection.recv(1000).decode() #receives 1 kb

    if pass_ == password:

        print("client approved")
        connection.close()

    else:
        connection.close()
        print("Conection was closed because unkown client tryied to enter with the wrong password.\nPlease restart the server")
        
