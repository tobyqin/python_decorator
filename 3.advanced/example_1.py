"""
Change the business a little bit.
Now we have to write log when enter a function.
"""

from datetime import datetime


def logging(func):
    def wrapper(*args, **kwargs):
        print "[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__)
        return func(*args, **kwargs)

    return wrapper


@logging
def say(something):
    print "{}!".format(something)


if __name__ == '__main__':
    say('hello')
    say('yes')
    say('no')
    say('goodbye')
