# question 2 and 3
from credit_card import CreditCard


class PredatoryCreditCard(CreditCard):
    # an extension to CreditCard that compounds interest and fees
    def __init__(self, customer, bank, acnt, limit, apr):
        """create a new predatory credit card instance
        the initial balance is zero

        customer    the name of the customer
        bank        the name of the bank
        acnt        account identifier
        limit       credit limit
        apr         annual percentage rate
        """
        super().__init__(customer, bank, acnt, limit)  # call super constructor, one of the eQuiz question
        self._apr = apr
        self._charge_count = 0

    def charge(self, price):
        """charge given price to the card, assuming sufficient credit limit
        Return true if charge was processed.
        Return false and assess $5 fee if charge is denied"""

        # for question 3
        self._charge_count += 1
        if self._charge_count > 10:
            self._balance += 1
            print('charge count =', self._charge_count)

        success = super().charge(price)
        # ^^ call inherited method, calling the parent class (calling the charge from the creditcard)
        # ^^ returns true or false. If false, it means that the charge is more than the amount, hence penalty will be given
        if not success:  # if success==False:
            self._balance += 5  # assess penalty. 'balance' means how much you owe the bank
            print('$5 penalty charge')
        print(success)  # caller expects return value

    def process_month(self):
        """assess monthly interest on outstanding balance"""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor



# test code
if __name__ == '__main__':
    wallet = []
    wallet.append(PredatoryCreditCard('John Lee', 'DBS', '5391 0375 9387 5309', 2000, 0.0825))
    print('Customer =', wallet[0].get_customer())
    print('Bank =', wallet[0].get_bank())
    print('Account =', wallet[0].get_account())
    print('Limit =', wallet[0].get_limit())
    print('Balance =', wallet[0].get_balance())

    for val in range(1, 17): # where we start to charge the card
        wallet[0].charge(200)
        print('Transaction number:', val)
        print('Charge $200 Balance =', wallet[0].get_balance())

    """ run process month"""
    wallet[0].process_month()
    print('Balance after process month:', wallet[0].get_balance())
