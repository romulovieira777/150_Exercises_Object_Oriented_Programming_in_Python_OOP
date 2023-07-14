"""
Exercise No. 11

The Client class is implemented. Note the class attribute all_clients. Try to implement a special class extending the
built-in list class called ClientList, which in addition to the standard methods for the built-in class list will have
a search_email() method that allows you to return a list of Client class instances containing the text (value argument)
in the email address.

For example, the following code:

    client1 = Client('Tom', 'sample@gmail.com')
    client2 = Client('Donald', 'sales@gmail.com')
    client3 = Client('Mike', 'sales@yahoo.com')
    client4 = Client('Lisa', 'info@gmail.com')
    print(Client.all_clients.search_email('sales'))

returns:

    [Client(name='Donald', email='sales@gmail.com'), Client(name='Mike', email='sales@yahoo.com')]

Complete the implementation of the search_email() method and execute the given code:

    client1 = Client('Tom', 'sample@gmail.com')
    client2 = Client('Donald', 'sales@gmail.com')
    client3 = Client('Mike', 'sales@yahoo.com')
    client4 = Client('Lisa', 'info@gmail.com')
    print(Client.all_clients.search_email('sales'))

Expected result:

    [Client(name='Donald', email='sales@gmail.com'), Client(name='Mike', email='sales@yahoo.com')]
"""


class ClientList(list):
    def search_email(self, value):
        return [client for client in self if value in client.email]


class Client:
    all_clients = ClientList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Client.all_clients.append(self)

    def __repr__(self):
        return f"Client(name='{self.name}', email='{self.email}')"


client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@gmail.com')
client3 = Client('Mike', 'sales@yahoo.com')
client4 = Client('Lisa', 'info@gmail.com')

print(Client.all_clients.search_email('sales'))
