"""
Exercise No. 03

The Product class is specified. An instance of this class named product was created. Display the namespace (value of the
__dict__ attribute) of this instance as shown below.

Expected result:

    {'product_name': 'Mobile Phone', 'product_id': '54274', 'price': 2900}
"""
import uuid


class Product:

    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return (
            f"Product(product_name='{self.product_name}', "
            f"price={self.price})"
        )

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]


product = Product('Mobile Phone', 2900)

print(product.__dict__)
