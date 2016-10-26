"""
How about doing something out of wrapper function?
"""

from datetime import datetime


def logging(func):
    print 'this is before wrapper...'

    def wrapper(*args, **kwargs):
        print "[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__)
        return func(*args, **kwargs)

    print 'this is after wrapper'

    return wrapper


@logging
def say(something):
    print "say {}!".format(something)


@logging
def do(something):
    print "do {}!".format(something)

if __name__ == '__main__':
    say('hello')
    say('yes')
    say('no')
    say('goodbye')
