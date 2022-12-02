def welcome():
    print('Hello!')

def op():
    price = float(input('Please, type the value of your product: '))
    finalValue = price - (price * 10 / 100)
    print('The value was {}, and the final value with a discount of 10% is: R${}'.format(price, finalValue,))

def bye():
    print('Good choice buying this product, thank you and good week!')

welcome()
op()
bye()