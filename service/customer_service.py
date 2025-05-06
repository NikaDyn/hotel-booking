from model.customer import Customer
from repo.customer_repo import CustomerRepo


class CustomerService:
    def __init__(self):
        self.repo = CustomerRepo()

    def add(self, name, phone_number):
        c = self.repo.find_by_phone_number(phone_number)
        if c is not None:
            raise Exception("Phone already exist")
        customer = Customer(name, phone_number)
        self.repo.add(customer)
        return customer

