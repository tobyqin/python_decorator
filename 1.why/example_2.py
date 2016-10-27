"""
We have to add debug info before say functions, there are some bugs in some say functions.
"""


def say_hello():
    print "[DEBUG]: enter say_hello()"
    print "hello!"


def say_goodbye():
    print "[DEBUG]: enter say_goodbye()"
    print "hello!"


def say_yes():
    print "[DEBUG]: enter say_yes()"
    print "hello!"


def say_no():
    print "[DEBUG]: enter say_no()"
    print "hello!"


if __name__ == '__main__':
    say_hello()
    say_yes()
    say_no()
    say_goodbye()
