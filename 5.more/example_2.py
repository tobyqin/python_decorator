"""
http://wrapt.readthedocs.io/en/latest/quick-start.html
"""

from datetime import datetime
import wrapt

# without argument in decorator
@wrapt.decorator
def logging(wrapped, instance, args, kwargs):  # instance is a must parameter
    print "[DEBUG] {}: enter {}()".format(datetime.now(), wrapped.__name__)
    return wrapped(*args, **kwargs)


@logging
def say(something):
    """say something"""
    print "say {}!".format(something)


# with argument in decorator
def logging(level):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        print "[{}] {}: enter {}()".format(level, datetime.now(), wrapped.__name__)
        return wrapped(*args, **kwargs)

    return wrapper


@logging(level="INFO")
def do(work):
    """do work"""
    print "do {}...".format(work)  # way #2


def start_to(method, argument):
    if method.__name__ == 'say':
        say(argument)
    elif method.__name__ == 'do':
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
    print inspect.getsource(say)  # good

    print inspect.getdoc(do)  # good
    print inspect.getargspec(do)  # good
    print inspect.getsource(do.__wrapped__)  # good
