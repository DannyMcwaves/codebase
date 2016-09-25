"""
this is just  a simple credit card validation where you have a credit card from a holder and then you validate it
by checking it against a pre-existent algorithm and then when the return value is true the card is valid else
it is not valid.

this should rather be simple than my first attempt at it.
My fingers are tightly crossed like the thingy on the first day at a strange place.
so here comes the algorithm.

   #this is the program that does validation of credit cards
--------------------------------------------------------------------
    # credit cards follow a certain pattern.
    # it must contain between 13 and 16 numbers. it must start with;
    # 4 for visa cards
    # 37 for american express card
    # 5 for mastercard credit cards
    # 6 for discover cards
"""


class CardError(Exception):
    """
    this is supposed to be raised when the card number has a validation error.
    """
    def message(self):
        return self.args


def card():
    """
    this part has the card and then validate the card against any entering errors and then returns the unstained card
    number that is a number strings.
    :return:
    """
    number = input("Please enter your credit card number:  ")

    if number.isspace():
        raise CardError("card cannot contain space")
    elif number.isalpha():
        raise CardError("card cannot be letters. must be numbers only")
    elif not number.isdigit():
        raise CardError("card is not numbers only")

    return number


def validation(number):
    """
    this one is supposed to validate the credit card number and then return the the parameters necessary for the
    manipulation of the card. in the other retrospect of the process.
    :param number: the credit card number as the parameter.
    :return:
    """
    if len(number) < 13 or len(number) > 16:
        raise CardError("The card should have a length between 13 and 16")
    if number[0] not in ["4", "5", "6", "3"]:
        raise CardError("card must begin with 4, 5, 6, 3")
    if number[0] == "3":
        if number[:2] != "37":
            raise CardError("if card begins with 3, 7 must be the next number")

    even = number[-2::-2]
    odd = number[0::2]
    ex2 = []
    ox2 = [int(x) for x in odd]

    for i in even:
        nw = 2 * int(i)
        if nw > 9:
            o = nw // 10
            t = nw % 10
            nw = o + t
        ex2.append(nw)

    total = sum(ox2) + sum(ex2)
    print(total)
    first = number[0]

    if first == "4":
        cty = "VISA CARDS"
    elif first == "3":
        cty = "AMERICAN EXPRESS CARD"
    elif first == "6":
        cty = "DISCOVER CARD"
    else:
        cty = "MASTER CARD"

    return [cty, total % 10 == 0]


def card_validation():
    try:
        number = card()
        passed = validation(number)
        print(passed)

        if passed[1]:
            print(passed[0], "CREDIT CARD IS VALID AS PER THE ALGORITHM")
        else:
            print(passed[0], "CREDIT CARD NOT VALID, AS PER THE ALGORITHM")
    except CardError as cr:
        print(cr.message()[0] + "\n")
        card_validation()
    except KeyboardInterrupt:
        print("exited through keyboard")

if __name__ == '__main__':
    card_validation()
