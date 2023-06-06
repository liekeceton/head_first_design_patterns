#Server checker once again
#HTTP server availability checker
import sys
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

        #We save the reply that we receive (recv) from the server
        reply = requests.head(F"http://{sys.argv[1]}:{port_nr}")

        #Show the replay in a textual format
        print(F'Succes! Status code:{reply.status_code}')
        print(reply.headers)

    except requests.exceptions.Timeout:
        print('A timeout occurred')
        return 3

    except:
        print('Something went wrong')
        return 4

    else:
        return None
                  
availability_checker()