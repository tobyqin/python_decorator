"""
Specify argument for target function.
Only fit for specified case.
"""


def prepare(func):
    def wrapper(something):
        print "[DEBUG]: enter {}()".format(func.__name__)
        print 'Prepare and say...',
        return func(something)

    return wrapper


@prepare
def say(something):
    print "{}!".format(something)


if __name__ == '__main__':
    say('hello')
    say('yes')
    say('no')
    say('goodbye')
