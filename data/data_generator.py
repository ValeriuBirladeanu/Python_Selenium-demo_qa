from faker import Faker

class TestDataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_full_name(self):
        return self.fake.name()

    def generate_email(self):
        return self.fake.email()

    def generate_current_address(self):
        return self.fake.street_address()

    def generate_permanent_address(self):
        return self.fake.street_address()