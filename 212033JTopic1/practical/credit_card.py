# Xu Yong Lin
# 212033J
# IT2153 - 01

class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """return name of the customer"""
        return self._customer

    def get_bank(self):
        """return the bank's name"""
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        # charge given price to the card, assuming sufficient credit limit
        # return True if charge was processed; False if charge was denied
        if price + self._balance > self._limit:     # if charge would exceed limit
            return False                            # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount


# Testing the CreditCard class, test codes
if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Lee', 'DBS', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Lee', 'OCBC', '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Lee', 'Maybank', '5391 0375 9387 5309', 5000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()
