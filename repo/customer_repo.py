from model.customer import Customer


class CustomerRepo:
    def __init__(self):
        self.customers = {}
        self.black_list = {}
        self.current_index = 1

    def add(self, customer: Customer):
        self.customers[self.current_index] = customer
        customer.customer_id = self.current_index
        self.current_index += 1

    def remove(self, customer_id):
        return self.customers.pop(customer_id)

    def find_by_phone_number(self, phone_number):
        for cust in self.customers.values():
            if cust.phone_number == phone_number:
                return cust
