#
# A Supermarket simulation
#

import sys
sys.path.append("..")

from queue import Queue
import random


# A Customer has an ID and a random number of items
class Customer:
    def __init__(self, number, max_items):
        self.id = number
        # generate a random number of item between 1 and max_items
        self.items = random.randint(1, max_items + 1)


# A cash desk has and ID, a queue of clients and can serve one Customer at a time
class Cashdesk:
    def __init__(self, number):
        self.id = number
        self.queue = Queue()
        self.tot_customers_served = 0
        self.current_customer = None

    # Method to enqueue a new Customer c
    def addCustomer(self, c):
        self.queue.enqueue(c)


    # Method for check out
    #
    # if current_customer = None and queue not empty, then dequeue a Customer that becomes the current_customer
    #
    # if current_customer != None check the number of items:
    #     if it is zero: print a message with the cash desk and Customer ids, reset current_customer to None
    #                    and increase the tot_customers_served counter
    #     else: decrease the number of items of current_customer by 1
    #
    # Example of message: "Cash desk 1 served Customer number 2"
    #
    def checkOut(self):
        if self.current_customer != None:
            if self.current_customer.items == 0:
                print(f'Cash desk {self.id} served Customer {self.current_customer.id}')
                self.current_customer = None
                self.tot_customers_served += 1
            else:
                self.current_customer.items -= 1
        elif not self.queue.isEmpty():
            self.current_customer = self.queue.dequeue()

# A Supermarket has a number of check desks specified by user
class Supermarket:
    def __init__(self, num_checkdesks):
        # Initialize a list of check decks with dimension num_checkdesks
        self.cashdesks_list =  [Cashdesk(i) for i in range(1, num_checkdesks + 1)]


    # Return True if all the check desks are empty, False otherwise
    def isEmpty(self):
        for i in self.cashdesks_list:
            if not i.queue.isEmpty():
                return False
        return True


    # Add a new Customer to the check desk with the shortest queue
    def newCustomer(self, new_customer):
        short_id = 0
        for i in range(1, len(self.cashdesks_list)):
            if self.cashdesks_list[short_id].queue.size() > self.cashdesks_list[i].queue.size():
                short_id = i
        self.cashdesks_list[short_id].queue.enqueue(new_customer)


    # Execute the method checkOut for each check desks
    def run(self):
        for desk in self.cashdesks_list:
            desk.checkOut()

    # Print the total number of customers served by each check desks
    #
    # E.g.: Cash deck 1 served 2426 clients
    #       Cash deck 2 served 2361 clients
    #       ...
    #
    def printRecap(self):
        for desk in self.cashdesks_list:
            print(f'Cash desk {desk.id} served {desk.tot_customers_served} clients')


# Test code
if __name__ == "__main__":
    num_checkdesks = 5    # number of check desks
    max_num_items = 20    # max number of items for each Customer
    num_customers = 10000 # total number of customers

    # Create an object Supermarket
    mySupermarket = Supermarket(num_checkdesks)
    # Create a list of Customer objects
    customers_list = [Customer(i, max_num_items) for i in range(num_customers, 0, -1)]

    #
    # Loop until all the customers are entered and served (i.e. both customer_list and all the queues are empty
    # A new Customer enters in the Supermarket with probability of 30% (use random function)
    # The function run is always called at each iteration

    while customers_list != [] or not mySupermarket.isEmpty():
        if random.random() >= 0.3 and len(customers_list) > 0:
            c = customers_list.pop()
            mySupermarket.newCustomer(c)
        mySupermarket.run()



    # Print the total number of customers served by each check desk
    mySupermarket.printRecap()
