"""
Write log when enter a function with level. You have to understand closure.
please go to http://betacat.online/posts/python-closure/
"""


def logging(level="INFO"):
    pass


@logging(level='INFO')
def say(something):
    print "say {}!".format(something)


@logging(level='DEBUG')
def do(something):
    print "do {}...".format(something)


if __name__ == '__main__':
    say('hello')
    do("my work")
    say('goodbye')
