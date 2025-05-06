class Bank:
    bank_name = "Money Bank" #class variable
    # def __init__(self):
    #     pass
    def show_bank_name(self):
        print(f'The bank name is {self.bank_name}.')

    # class method
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
        print(f'The bank_name is changed to {cls.bank_name}.')

# creating two objects(instances)   
bank1 = Bank()
bank2 = Bank()

# show the initial bank_name
bank1.show_bank_name()
bank2.show_bank_name()
# change the bank name through class method
Bank.change_bank_name("Dubai_Bank")
bank1.show_bank_name()
bank2.show_bank_name()
