"""
http://pythonhosted.org/decorator/documentation.html
"""

from datetime import datetime
from decorator import decorate, decorator


def debug(func, *args, **kwargs):
    """print log before a function."""
    print "[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__)
    return func(*args, **kwargs)


def logging1(func):
    return decorate(func, debug)  # way #1


@logging1
def say(something):
    """say something"""
    print "say {}!".format(something)


@decorator
def logging2(func, *args, **kwargs):
    print "[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__)
    return func(*args, **kwargs)


@logging2
def do(work):
    """do work"""
    print "do {}...".format(work)  # way #2


def start_to(method, argument):
    if method.__name__ == 'say':
        print "OK, let's say the word."
        say(argument)
    elif method.__name__ == 'do':
        print "OK, let's do the work."
        do(argument)
    else:
        print "current method: {} ({})".format(method.__name__, method.__doc__)
        raise Exception("Unknown step: {}".format(method.__name__))


if __name__ == '__main__':
    start_to(say, "hello")
    start_to(do, "my work")

    import inspect

    print "INSPECT".center(60, '*')
    print inspect.getdoc(say)  # good
    print inspect.getargspec(say)  # good
    # print inspect.getsource(say)  # error

    print inspect.getdoc(do)  # good
    print inspect.getargspec(do)  # good
    print inspect.getsource(do.__wrapped__)  # good
