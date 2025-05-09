from model.customer import Customer


class CustomerRepo:
    def __init__(self):
        self.customers = {}
        self.black_list = {}
        self.current_index = 1

    def print_customer(self):
        for cus in self.customers.values():
            print(cus)

    def add(self, customer: Customer):
        self.customers[str(self.current_index)] = customer
        customer.customer_id = self.current_index
        self.current_index += 1
        return customer

    def find_by_phone_number(self, phone_number):
        for cust in self.customers.values():
            if cust.phone_number == phone_number:
                return cust

        return False
