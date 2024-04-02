"""BankAccount"""


class Customer:
    """Customer"""
    def __init__(self, name, email, customer_id):
        self.name = name
        self.email = email
        self.customer_id = customer_id

    def get_name(self):
        """client_name"""
        return self.name

    def get_email(self):
        """client_email"""
        return self.email

    def get_customer_id(self):
        """client_customer_id"""
        return self.customer_id

    def get_info(self):
        """all info"""
        return f"Customer_id: {self.customer_id}, Name: {self.name}, Email: {self.email}"


class BankAccount(Customer):
    """BankAccount"""
    def __init__(self, balance, customer):
        super().__init__(customer.name, customer.email, customer.customer_id)
        self.owner = self.name
        self.account_number = self.customer_id
        self.balance = balance

    def get_account_number(self):
        """account number"""
        return self.account_number

    def add_balance(self, count):
        """add balance"""
        if count > 0:
            self.balance += count
            return f"The operation is successful. New balance: {self.balance}"
        else:
            return "Count can not be less than 0"

    def reduce_balance(self, count):
        """reduce balance"""
        if count < self.balance:
            self.balance -= count
            return f"The operation is successful. New balance: {self.balance}"
        else:
            return "Count can not be more than your balance"


customer1 = Customer("John Doe", "john@example.com", "C001")
account1 = BankAccount(1000, customer1)

print(account1.add_balance(50))
print(account1.get_account_number())
print(customer1.get_info())
