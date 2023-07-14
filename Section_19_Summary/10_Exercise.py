"""
Exercise No. 10

Implement a class named Client which has a class attribute named all_clients (as a list). Then the __init__() method
sets two instance attributes (no validation):

    - name
    - email

Add this instance to the all_clients list (Client class attribute). Also add a __repr__() method the Client class (see
below).

Create three clients by executing the following code:

    client1 = Client('Tom', 'sample@gmail.com')
    client2 = Client('Donald', 'sales@yahoo.com')
    client3 = Client('Mike', 'sales-contact@yahoo.com')

In response, print the all_clients attribute of the Client class.

Expected result:

    [Client(name='Tom', email='sample@gmail.com'), Client(name='Donald', email='sales@yahoo.com'), Client(name='Mike',
    email='sales-contact@yahoo.com')]
"""


class Client:
    all_clients = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Client.all_clients.append(self)

    def __repr__(self):
        return f"Client(name='{self.name}', email='{self.email}')"


client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@yahoo.com')
client3 = Client('Mike', 'sales-contact@yahoo.com')

print(Client.all_clients)
