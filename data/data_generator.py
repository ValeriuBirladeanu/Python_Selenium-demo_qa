from faker import Faker


class TestDataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_full_name(self):
        return self.fake.name()

    def generate_first_name(self):
        return self.fake.first_name()

    def generate_last_name(self):
        return self.fake.last_name()

    def generate_email(self):
        return self.fake.email()

    def generate_current_address(self):
        return self.fake.street_address()

    def generate_permanent_address(self):
        return self.fake.street_address()

    def generate_age(self, min_age=18, max_age=90):
        return self.fake.random_int(min=min_age, max=max_age)

    def generate_salary(self, min_salary=10000, max_salary=90000):
        return self.fake.random_int(min=min_salary, max=max_salary)

    def generate_department(self):
        return self.fake.job()

    def generate_text(self):
        return self.fake.text()

    def generate_mobile_number(self):
        return f'07{self.fake.random_number(digits=8, fix_len=True)}'

    def generate_png_fail_name(self):
        return self.fake.file_name(extension='png')