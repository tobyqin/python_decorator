"""
Code in outer and inner wrapper will be ran once decorator added.
"""


def html_tags(tag_name):
    print 'begin outer function.'

    def wrapper_(func):
        print "begin of inner wrapper function."

        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            return "<{tag}>{content}</{tag}>".format(tag=tag_name, content=content)

        print 'end of inner wrapper function.'
        return wrapper

    print 'end of outer function'
    return wrapper_


@html_tags('b')
def hello(name='Toby'):
    return 'Hello {}!'.format(name)


print "---------------------------------"


@html_tags('b')
def do(name='Toby'):
    return 'Hello {}!'.format(name)


print "++++++++++++++++++++++++++++++++++"

print hello()  # <b>Hello Toby!</b>
# print hello('world')  # <b>Hello world!</b>
