"""
this is going to use optParse on the argument vector from the cli.
simple right huh?
"""
import optparse
from notes import notes

__all__ = ["parse"]


def parse(usage=None, *args):
    """
    all you need to do is to pass the usage and
    :param usage: how to pass the command line args manual
    :param args: the command line args with key word definitions and all that stuff.
    :return: dictionary of the passed arguments.
    """
    if usage is None:
        usage = " %prog "
    else:
        usage += " %prog"

    parser = optparse.OptionParser(usage)
    arguments = [x for x in args]
    i = 0

    while i < len(arguments) + 1:
        try:
            parser.add_option(arguments[i], dest=arguments[i+1], type="string")
        except IndexError:
            pass
        i += 2

    (options, arg) = parser.parse_args()

    return options


if __name__ == '__main__':
    # parsed = parse("Usage %prog", "-f", "filename", "-a", "read")
    # print(parsed.filename)

    n = notes.Notes(globals(), api=__all__)
    n += "Owner: Danny Mcwaves"
    n(print)

