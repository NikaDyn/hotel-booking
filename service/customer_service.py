from functions import validate_phone
from model.customer import Customer
from repo.customer_repo import CustomerRepo


class CustomerService:
    def __init__(self):
        self.repo = CustomerRepo()

    def print_customer(self):
        self.repo.print_customer()

    def find_by_index(self, customer_id):
        for index in self.repo.customers.keys():
            if index == customer_id:
                return self.repo.customers[index]

        return False

    def add(self, name, phone_number):
        if not validate_phone(phone_number):
            return False

        if self.repo.find_by_phone_number(phone_number):
            return False

        return self.repo.add(Customer(name, phone_number))
