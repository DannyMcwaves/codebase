"""
this is just an example of a simple log file that lets you log some stuff into a file and then it create a folder
in the current directory since there can be soo many log file in this dir, it better to out it in it's own folder.

it uses the time it got created and plus a log name. and then put it in the log folder in the current directory.

--- and this is the UML for my code already.
--- first of all, it should take a pathname
--- and then if the path exists, i will change dir to that path
--- else i will create that path dir and then create the log thingy over there.
"""
import time


def log(file=False, name=None):
    """
    this is the parametrised decorator that takes a parameter for what we want to work with and all that stuff.
    :param file: you need a file to log all this nifty stuff for you hence write true for the name of the file.
    :param name: this is the name of the file.
    :return:
    """

    def decorator(function):
        """
        this is the main decorator file that looks like the first ones i have written earlier and is very useful in
        in doing the work of the decorator function.
        :param function:
        :return: the logged function necessary
        """
        nonlocal name
        current_time = time.ctime()
        if file:
            if name is None:
                name = current_time

        def logged(*args, **kwargs):
            """
            this is the function that is supposed to return the logged things
            :param args: the arguments to be passed to the function and all that.
            :return: return the value of the called function the user has created.
            """
            function_name = function.__name__
            arguments = None
            kw_arguments = None
            free_arguments = function.__code__.co_varnames
            t1 = time.perf_counter()
            result = function(*args, **kwargs)
            runtime = time.perf_counter() - t1

            if args:
                arguments = [x for x in args]
            if kwargs:
                kw_arguments = ["{x}= {y} ".format(x=kw[0], y=kw[1]) for kw in sorted(kwargs.items())]

            print(format("CREATION TIME: -->", ">25s"), current_time)
            print(format("FUNCTION NAME: -->", ">25s"), function_name)
            print(format("ARGUMENTS: -->", ">25s"), arguments)
            print(format("KEYWORD ARGUMENTS: -->", ">25s"), kw_arguments)
            print(format("ARGUMENT NAMES: -->", ">25s"), list(free_arguments))
            print(format("RUN TIME: -->", ">25s"), runtime)
            print(format("ID: -->", ">25s"), id(function))
            print(format("RETURNED: -->", ">25s"), result)

            if file:
                print("\nFILENAME: -->", name)
                with open(name, "a") as new:
                    new.write("TIME OF CREATION\n\t--- {}\n".format(current_time))
                    new.write("\nFUNCTION NAME\n\t--- {}\n".format(function_name))
                    new.write("\nARGUMENTS\n\t--- {}\n".format(arguments))
                    new.write("\nKEYWORD ARGUMENTS\n\t--- {}\n".format(kw_arguments))
                    new.write("\nARGUMENT NAME\n\t--- {}\n".format(list(free_arguments)))
                    new.write("\nRUN TIME\n\t--- {}\n".format(runtime))
                    new.write("\nID\n\t--- {}\n".format(id(function)))
                    new.write("\nRETURNED\n\t--- {}".format(result))

            return result

        return logged
    return decorator

