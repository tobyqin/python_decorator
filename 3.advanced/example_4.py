"""
Write log when enter a function. -- class based decorator
"""
from datetime import datetime


class logging(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print "[DEBUG] {time}: enter function {func}()".format(
            time=datetime.now(),
            func=self.func.__name__)
        return self.func(*args, **kwargs)


@logging
def say(something):
    print "say {}!".format(something)


@logging
def do(something):
    print "do {}...".format(something)


if __name__ == '__main__':
    say('hello')
    do("my work")
    say('goodbye')
