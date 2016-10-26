"""
Without @ syntax (Python <= 2.4)
"""


def prepare(func):
    def wrapper():
        print "[DEBUG]: enter {}()".format(func.__name__)
        print 'Prepare and say...',
        return func()

    return wrapper


def say_hello():
    print "hello!"


say_hello = prepare(say_hello)


def say_goodbye():
    print "goodbye!"


say_goodbye = prepare(say_goodbye)


def say_yes():
    print "yes!"


say_yes = prepare(say_yes)


def say_no():
    print "no!"


say_no = prepare(say_no)

if __name__ == '__main__':
    say_hello()
    say_yes()
    say_no()
    say_goodbye()
