import socket
import json

class Client():
    server_address = ('localhost', 4444)

    def __init__(self,name):
        self.name = name
        self.sock = None

    def open_sock(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(self.server_address)
    def close_sock(self):
        self.sock.close()

    def open_session(self):
        self.open_sock()
        msg = "Connected with "+self.name
        self.sock.send(msg.encode('utf-8'))
        reply = self.sock.recv(4096).decode('utf-8')
        print(reply, self.name)

    def close_session(self):
        request = {'action':'close', 'amount':self.name}
        json_str = json.dumps(request, separators=(',', ':'))
        self.sock.send(json_str.encode('utf-8'))
        reply = self.sock.recv(4096).decode('utf-8')
        print(reply, self.name)
        self.close_sock()

    def get_balance(self):
        request = {'action':'get_balance'}
        json_str = json.dumps(request, separators=(',', ':'))
        self.sock.send(json_str.encode('utf-8'))

        reply = self.sock.recv(4096).decode('utf-8')
        print('Get Balance: ',self.name, reply)

    def deposit(self, amount):
        request = {'action':'deposit', 'amount':amount}
        json_str = json.dumps(request, separators=(',', ':'))
        self.sock.send(json_str.encode('utf-8'))

        reply = self.sock.recv(4096).decode('utf-8')
        print('Deposit: ',self.name, reply)

    def withdraw(self, amount):
        request = {'action':'withdraw', 'amount':amount}
        json_str = json.dumps(request, separators=(',', ':'))
        self.sock.send(json_str.encode('utf-8'))

        reply = self.sock.recv(4096).decode('utf-8')
        print('Withdraw: ',self.name,reply)

    

"""a = Client('Alice')
a.open_session()
a.withdraw(100)
a.get_balance()
a.close_session()

b = Client('Bob')
b.open_session()
b.get_balance()
b.close_session()"""
