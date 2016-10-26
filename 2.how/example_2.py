"""
With @ syntax (Python > 2.4)
"""


def prepare(func):
    def wrapper():
        print "[DEBUG]: enter {}()".format(func.__name__)
        print 'Prepare and say...',
        return func()

    return wrapper


@prepare
def say_hello():
    print "hello!"


@prepare
def say_goodbye():
    print "goodbye!"


@prepare
def say_yes():
    print "yes!"


@prepare
def say_no():
    print "no!"


if __name__ == '__main__':
    say_hello()
    say_yes()
    say_no()
    say_goodbye()
