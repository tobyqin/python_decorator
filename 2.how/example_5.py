"""
Fit for all kinds of arguments for target function.
"""


def prepare(func):
    def wrapper(*args, **kwargs):
        print "[DEBUG]: enter {}()".format(func.__name__)
        print 'Prepare and say...',
        return func(*args, **kwargs)

    return wrapper


@prepare
def say(something, who='Toby'):
    print "{}!({})".format(something, who)


if __name__ == '__main__':
    say('hello')
    say('yes')
    say('no')
    say('goodbye')
