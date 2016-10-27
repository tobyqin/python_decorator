"""
Extract common business out of say function, improved, but not best.
"""


def prepare():
    import inspect
    caller_name = inspect.stack()[1][3]
    print "[DEBUG]: enter {}()".format(caller_name)
    print 'Prepare and say...',


def say_hello():
    prepare()
    print "hello!"


def say_goodbye():
    prepare()
    print "goodbye!"


def say_yes():
    prepare()
    print "yes!"


def say_no():
    prepare()
    print "no!"


if __name__ == '__main__':
    say_hello()
    say_yes()
    say_no()
    say_goodbye()
