"""
Exercise No. 18

The implementation of the classes: Product and Warehouse is given. To the Warehouse class, add a method named
add_product() that allows you to add an instance of the Product class to the products list. If the product name is
already in the products list, skip adding the product.

Next, create an instance of the Warehouse class named warehouse. Using the add_product() method add the following
products:

    - 'Laptop', 3900.0'
    - 'Mobile Phone', 1990.0'
    - 'Mobile Phone', 1990.0'

Note that the second and third products are duplicates. The add_product() method should avoid adding duplicates. Print
the products attribute of the warehouse instance to the console.

Expected result:

    [Product(product_name='Laptop', price=3900.0), Product(product_name='Mobile Phone', price=1990.0)]
"""
# Solution I
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


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product.product_name not in [p.product_name for p in self.products]:
            self.products.append(product)


warehouse = Warehouse()

warehouse.add_product(Product('Laptop', 3900.0))
warehouse.add_product(Product('Mobile Phone', 1990.0))
warehouse.add_product(Product('Mobile Phone', 1990.0))

print(warehouse.products)


# Solution II
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


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product_name, price):
        product_names = [
            product.product_name for product in self.products
        ]
        if not product_name in product_names:
            self.products.append(Product(product_name, price))


warehouse = Warehouse()

warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)

print(warehouse.products)
