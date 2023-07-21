"""
Exercise No. 13

The Client class is implemented. The following four instances of the Client class was created:

    client1 = Client('Tom', 'sample@gmail.com')
    client2 = Client('Donald', 'sales@gmail.com')
    client3 = Client('Mike', 'sales@yahoo.com')
    client4 = Client('Lisa', 'info@gmail.com')

Search for all customers with the word 'sales' in email address. In response, print the names of the customers as a list
to the console.

Expected result:

    ['Donald', 'Mike']
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

print([client.name for client in Client.all_clients.search_email('sales')])
