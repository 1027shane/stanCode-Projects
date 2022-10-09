import pypal


def bank():
    jerry_a = pypal.Pypal('Jerry', money=1000, withdraw_limit=700)
    # Setter Method 1:
    jerry_a.set_name('Shane')
    print(jerry_a)
    # Setter Method 2:
    jerry_a.name = 'Zoey'
    print(jerry_a)

    jerry_a.__m = 100000  # No error, but can not be modified
    # Getter Method 1:
    print(jerry_a.get_money())
    # Getter Method 2:
    print(jerry_a.money)

    jerry_a.withdraw(1000)
    jerry_a.withdraw(500)
    jerry_a.withdraw(600)


if __name__ == '__main__':
    bank()
