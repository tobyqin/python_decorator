"""
Write log when enter a function with level. -- class based decorator
"""
from datetime import datetime


class logging(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print "[{level}] {time}: enter function {func}()".format(
                level=self.level,
                time=datetime.now(),
                func=func.__name__)
            func(*args, **kwargs)

        return wrapper


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

    # print say.__name__
