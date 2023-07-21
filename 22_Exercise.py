"""
Exercise No. 22

The implementation of the classes: Product and Warehouse is given. Add a method called sort_by_price() to the Warehouse
class that returns an alphabetically sorted list of products. The sort_by_price() method also takes an argument
ascending set to True by default, which means an ascending sort. If False is passed, reverse the sort order.

Then create an instance of the Warehouse class named warehouse and execute the following code:

    warehouse.add_product('Laptop', 3900.0)
    warehouse.add_product('Mobile Phone', 1990.0)
    warehouse.add_product('Camera', 2900.0)
    warehouse.add_product('USB Cable', 24.9)
    warehouse.add_product('Mouse', 49.0)

In response, use the sort_by_price() method to print a sorted list of products to the console as shown below.

Expected result:

    Product Name: USB Cable | Price: 24.9
    Product Name: Mouse | Price: 49.0
    Product Name: Mobile Phone | Price: 1990.0
    Product Name: Camera | Price: 2900.0
    Product Name: Laptop | Price: 3900.0
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

    def display_products(self):
        for product in self.products:
            print(
                f'Product ID: {product.product_id} | Product name: '
                f'{product.product_name} | Price: {product.price}'
            )

    def sort_by_price(self, ascending=True):
        return sorted(
            self.products,
            key=lambda product: product.price,
            reverse=not ascending
        )


warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)

for product in warehouse.sort_by_price():
    print(product)
