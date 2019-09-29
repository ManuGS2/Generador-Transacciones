import threading
import time

#Global Variables 
balance = 100.0

class Coordinator():
    def __init__(self):
        global balance
        self.balance = balance 

    def get_balance(self):
        return str(self.balance)

    def deposit(self, amount):
        self.balance += amount
        return "Deposit successfully: "+str(self.balance)

    def withdraw(self, amount):
        aux = self.balance - amount
        if aux >= 0:
            self.balance = aux
            return "Cash withdrawal successfully: "+str(self.balance)
        else:
            return "Not enough money: "+str(self.balance)
        
