"""
Failed to get correct function name and doc - fixed.
"""

from datetime import datetime
from functools import wraps


def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """print log before a function."""
        print "[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__)
        return func(*args, **kwargs)

    return wrapper


@logging
def say(something):
    """say something"""
    print "say {}!".format(something)


@logging
def do(something):
    """do something"""
    print "do {}...".format(something)


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

    # import inspect
    # print inspect.getdoc(say)  # good
    # print inspect.getargspec(say)  # failed
    # print inspect.getsource(say)  # failed
