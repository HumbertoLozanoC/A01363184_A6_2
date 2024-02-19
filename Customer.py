import json
import os


class Customer:
    def __init__(self, usr_name, customer_id):
        self.usr_name = usr_name
        self.customer_id = customer_id
        self.file_name = f"customer_{customer_id}.json"

    def save_to_file(self):
        """Saves customer data to a file."""
        data = {
            'customer_id': self.customer_id,
            'name': self.name

        }
        with open(self.file_name, 'w', encoding='utf-8') as _f_:
            json.dump(data, _f_)

    @staticmethod
    def create_customer(name, customer_id):
        # Read customer data from file
        customer = Customer(name, customer_id)
        customer.save_to_file()
        return customer

    @staticmethod
    def delete_customer(customer_id):
        file_name = f"customer_{customer_id}.json"
        os.remove(file_name)

    @staticmethod
    def display_customer_information(self):
        print(f"""Customer ID: {self.customer_id} ,
              Name: {self.name}""")

    def modify_customer_information(self, name=None, id=None):
        if name:
            self.name = name
        if id:
            self.id = id
        self.save_to_file()
