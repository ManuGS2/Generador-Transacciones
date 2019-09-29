import socket
import json
from threading import Thread,Lock
from coordinator import Coordinator

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 4444)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)

# Initialize Coordinator for transactions
c = Coordinator()

# Lock object to atomic operations
lock = Lock()

def new_client(client):
    while True:
        # Receive the data 
        data_string = client.recv(4096).decode('utf-8')
        
        if data_string:
            #Parsed Json
            p = json.loads(data_string)

            if (p['action'] == 'get_balance'):
                r = c.get_balance()
                client.sendall(r.encode('utf-8'))
            
            elif (p['action'] == 'deposit'):
                lock.acquire()
                r = c.deposit(p['amount'])
                lock.release()
                client.sendall(r.encode('utf-8'))
            
            elif (p['action'] == 'withdraw'):
                lock.acquire()
                r = c.withdraw(p['amount'])
                lock.release()
                client.sendall(r.encode('utf-8'))

            elif (p['action'] == 'close'):
                print(p['amount']+" is disconnected\n")
                client.sendall("Disconnected succesfully ".encode('utf-8'))
                break
        else:
            print('no data from', client_address)


while True:
    client, client_address = sock.accept()    # Establish connection with client.
    msg = client.recv(4096).decode('utf-8')
    print(msg+"\n")
    client.sendall("Connected succesfully ".encode('utf-8'))
    Thread(target=new_client, args=(client,)).start()

sock.close()