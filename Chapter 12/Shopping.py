# -*- coding: utf-8 -*-


def main():
    # Alef
    prices = {'banana': 10, 'apple': 8, 'bread': 7, 'cheese': 20, 'juice': 15}
    print prices
    # Bet
    shopping_cart = {'banana': 2, 'bread': 3, 'cheese': 1, 'chicken': 4}
    total = 0
    for key in shopping_cart:
        if key in prices:
            total += prices[key] * shopping_cart[key]
        else:
            print "{} doesn't have a price".format(key)
    print total



if __name__ == '__main__':
    main()