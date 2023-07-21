"""
Exercise No. 20

The implementation of the classes: Product and Warehouse is given. To the Product class, add a __str__() method that is
an informal representation of the Product class.

An example of how the __str__() method works. The code below:

    product = Product('Laptop', 3900.0)
    print(product)

Returns:

    Product(product_name='Laptop' | price=3900.0)

Then create an instance of the Product class named product with the arguments passed:

    - 'Mobile Phone', 1990.0

In response, print the product instance to the console.

Expected result:

    Product(product_name='Mobile Phone' | price=1990.0)
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

    def __str__(self):
        return f'Product Name: {self.product_name} | Price: {self.price}'

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product_name, price):
        product_names = [
            product.product_name for product in self.products
        ]
        if not product_name in product_names:
            self.products.append(Product(product_name, price))

    def remove_product(self, product_name):
        for product in self.products:
            if product_name == product.product_name:
                self.products.remove(product)


product = Product('Mobile Phone', 1990.0)
print(product)
