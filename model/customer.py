class Customer:
    def __init__(self, name, phone_number):
        self.customer_id = None
        self.name = name
        self.phone_number = phone_number
        self.is_banned = False

    def __str__(self):
        return f'{self.customer_id}. {self.name} - {self.phone_number}'
