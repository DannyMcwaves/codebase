#! /usr/bin/python3.5

"""
here, a customer can be able to order items an then based on the whatever conditions are set up by the store,
the customer gets a retail from the purchase.
"""
from functools import namedtuple
from pprint import pprint as log

customer = namedtuple("customer", "name fidelity")


class Order:
    """
    this is the order made by the customer and in total that includes the amount and the items
    :return: the order total of the customer. and the items the customer has to buy from the store.
    the total of everything.

    the order should return the items and the amount and the discount on them.
    """
    def __init__(self, buyer, cart, discount):
        """
        the cart is the list of items that the user is trying to buy or to acquire.
        :param cart: A LIST OF ITEMS IN THE CART
        :param discount: the discount the user is trying to get from the product and all that stuff.
        """
        self.customer = buyer
        self.cart = cart
        self.TOTAL = cart.total() - discount.discount
        self.__order = namedtuple("ORDER", "CUSTOMER FIDELITY ITEMS TOTAL_ITEMS TOTAL_AMOUNT")

    def issue(self):
        return self.__order(self.customer.name, self.customer.fidelity, self.cart.cartList(),
                            self.cart.quantity(), self.TOTAL)


class Item:
    """
    this is the items region that takes the items and then sets parameters for the items
    as the quantity, price
    """
    def __init__(self, item, quantity, price):
        # the items should be a list of things only.
        self.item = item
        self.quantity = quantity
        self.price = price
        self.amount = self.quantity * self.price

    def __repr__(self):
        return " {} ".format(self.item)


class Cart:
    items = []

    def add(self, item, qty, price):
        """
        add an item to the cart and all that stuff that you can have.
        :return: a none.
        """
        self.items.append(Item(item, qty, price))

    def total(self):
        return sum([x.amount for x in self.items])

    def distinct(self):
        return len({x.item for x in self.items})

    def quantity(self):
        return len([x.item for x in self.items])

    def cartList(self):
        return [repr(x) for x in self.items]


class Discount:

    def __init__(self, buyer, cart):
        """
        based on the fidelity points of the customer or the the items in the cart and the distinct items in the
        cart.
        5 - fidelity
        10 - bulk item
        7 for distinct
        :param buyer:
        :param cart:
        """
        self.__discount = 0

        self.__discount += 5 if buyer.fidelity >= 1000 else 0
        self.__discount += 10 if cart.quantity() >= 20 else 0
        self.__discount += 7 if cart.distinct() >= 10 else 0

        self.discount = cart.total() * (self.__discount / 100)


if __name__ == '__main__':
    me = customer("DANNY McWAVES", 1000)

    c = Cart()
    c.add("banana", 15, 3)
    c.add("Apricot", 5, 10)
    c.add("Carrot", 3, 5)
    c.add("Calico", 10, 2)
    c.add("beans", 2, 15)
    c.add("Yam", 2, 5)
    c.add("Egg", 25, 10)
    c.add("Sugar", 2, 6)
    c.add("Beef", 10, 2)
    c.add("Papaya", 7, 7)
    c.add("Orange", 15, 3)
    c.add("tomato", 23, 2)
    c.add("Salad", 2, 15)
    c.add("Waffles", 10, 7)
    c.add("Pineapple", 5, 15)
    c.add("Juice Box", 5, 20)

    d = Discount(me, c)
    o = Order(me, c, d)

    log(o.issue())

