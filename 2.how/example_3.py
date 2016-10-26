"""
Target function with argument, failed.
"""


def prepare(func):
    def wrapper():
        print "[DEBUG]: enter {}()".format(func.__name__)
        print 'Prepare and say...',
        return func()

    return wrapper


@prepare
def say(something):
    print "{}!".format(something)


if __name__ == '__main__':
    say('hello')
    say('yes')
    say('no')
    say('goodbye')
