#!/usr/bin/python3.5

"""
my very simple html tool for writing simple markups using html.
it mostly uses simple strings interpolation and the first name of
the element as the first argument and the second argument is the
content of the html tag....................
"""
__all__ = ["tag"]


class tag:

    """
    this class is mainly for the elements in the html file or the html document.
    element manipulation and the and yh what ever.
    this includes everything that an html element is made up of.

    the args is the content that is supposed to be used for the tag. though it not exactly necessary for all
    elements. and then the class is implemented, in case you want to add a class on the spot and the key word
    arguments are just a set of other attributes you would like to define on your element.
    """

    def __init__(self, name, *args, cls=None, **kwargs):
        self.__cls = cls
        self.__kwargs = kwargs
        self.__formatAttr = "%s=\"%s\" "
        self.__formatReturn0 = "<%s %s>\t%s\t</%s>"
        self.__formatReturn1 = "<%s %s>\t%s\n</%s>"
        self.__formatReturn2 = "<%s %s/>"
        self.__content = " " + " ".join(list(args))
        self.__name = name

        if cls is not None:
            self.__kwargs["class"] = self.__cls
        if kwargs:
            self.__attributes = " ".join(self.__formatAttr % item for item in self.__kwargs.items())
        else:
            self.__attributes = " "

        if args:
            self.returnValue = "".join(self.__formatReturn1 % (self.__name,
                                                               self.__attributes, self.__content, self.__name))
        else:
            self.returnValue = "".join(self.__formatReturn2 % (self.__name, self.__attributes))

    def __call__(self, *args, cls=None, **kwargs):
        """
        :param args: More content maybe including a tag itself
        :param kwargs: more attributes to the element
        :return: should the return the corrected values of the tag
        """
        if cls is not None:
            cls = self.__cls + " " + cls
            self.__kwargs["class"] = cls
        if kwargs:
            self.__kwargs.update(kwargs)
            self.__attributes = " ".join(self.__formatAttr % item for item in self.__kwargs.items())
        if args:
            self.__content += ".\n\t " + " ".join(list(args))
            self.returnValue = "".join(self.__formatReturn1 % (self.__name,
                                                               self.__attributes, self.__content, self.__name))
        else:
            self.returnValue = "".join(self.__formatReturn2 % (self.__name, self.__attributes))

        return self.__str__()

    def __str__(self):
        return str(self.returnValue)

    def __repr__(self):
        return "{}".format(self.returnValue)


""""
def kw_only(a: str, letter: int=20, **kwargs) -> dict:
    b = a[0]
    lt = letter * 2
    kw_only.__dict__["name"] = kw_only.__name__
    print(a, letter, b, lt)
    return kwargs


def mul(a, b):
    return a*b


def fact(n):
    return reduce(mul, range(1, n+1))


def partial(func, arg):

    def inner(arg2):
        return func(arg, arg2)

    return inner

# write a text clipping tool too.
# write a tool to get all the arguments in the function.
# And other things about the function too.( make it  a decorator)
# try to create a partial function. -- takes a function and an
# argument and then returns the a function that can execute whatever.

# print(kw_only("s", name="danny mcwaves", age=18, year=1996))
# print(kw_only.__defaults__)
# print(kw_only.__code__.co_varnames)
# print(kw_only.__dict__)
# print(kw_only.__annotations__

"""


if __name__ == '__main__':
    img = tag("img", src="images/logo.png", cls="image")
    img(cls="new studios", id="man")
    print(img)

    div = tag("div", tag("h1", "Danny Mcwaves").__str__(), tag("small", "the boy. the man, the legend").__str__(),
              cls="navigate", role="navigation", id="nav")
    div(tag("p", "i am the legend of the Zanko thingy that i cannot mastermind.").__str__())
    div(tag("p", "i am the legend of the Danko that gives all but none to one.").__str__())
    print(div)
