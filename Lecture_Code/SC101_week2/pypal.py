WITHDRAW_LIMIT = 1000
MONEY = 10


class Pypal:
    def __init__(self, name, money=MONEY, withdraw_limit=WITHDRAW_LIMIT):
        # visibility of instance: private
        self._n = name
        self.__m = money
        self.w_l = withdraw_limit

    # Setter Method 1:
    def set_name(self, new_name):
        print(f'Successfully updated! from {self._n} to {new_name}')
        self._n = new_name

    # Setter Method 2:
    @ property
    def name(self):
        return self._n

    @ name.setter
    def name(self, new_name):
        print(f'Successfully updated! from {self._n} to {new_name}')
        self._n = new_name

    # Getter Method 1:
    def get_money(self):
        return self.__m

    # Getter Method 2:
    @ property
    def money(self):
        return self.__m

    def withdraw(self, amount):
        if amount > self.w_l:
            print('Exceed Limit')
        elif amount > self.__m:
            print('Illegal')
        else:
            self.__m -= amount
            print(f"{self._n} remains: {self.__m}")

    def __str__(self):
        return f'name: {self._n} / money: {self.__m} / limitation: {self.w_l}'
