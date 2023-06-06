#HTTP server availability checker
import sys
import socket
import requests

def availability_checker():
    try:    
        #Invocation lacks any arguments
        if len(sys.argv) < 2:
            print('No arguments given: One is minimally required')
            return 1
        elif len(sys.argv) == 2:
            port_nr = 80 #Set port number to default
        elif len(sys.argv) == 3:
            try:
                port_nr = int(sys.argv[2]) #Check if the filled in port number is an integer
            except ValueError:
                print('Port number was filled in incorrectly: Not an integer')
                return 2
        else:
            print('Too many arguments given: Maximally server address and port number')
            return 1

        #Create a socket object (default configuration for sockets working on top of TCP protocol)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Connect the socket
        sock.connect((sys.argv[1], port_nr))

        #Sent a request to the server (translate to bytes, use a b-string)
        #utf-8 indicates the string encoding of the server name (best choice for modern OSs)
        sock.send(b"HEAD / HTTP/1.1\r\nHost: " +
              bytes(sys.argv[1], "utf8") +
              b"\r\nConnection: close\r\n\r\n")

        #We save the reply that we receive (recv) from the server
        reply = sock.recv(10000)

        #We close the connection
        #It should have already been closed after the get request was finished, but its good practice to close literally anyways
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()

        #Show the replay in a textual format
        print(repr(reply))

    except requests.exceptions.Timeout:
        print('A timeout occurred')
        return 3

    except:
        print('Something went wrong')
        return 4

    else:
        return None
                  
availability_checker()