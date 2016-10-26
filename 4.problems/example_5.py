"""
Cannot add decorator onto classmethod or staticmethod. - fixed.
"""

from datetime import datetime
from functools import wraps


def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """print log before a function."""
        print "[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__)
        return func(*args, **kwargs)

    return wrapper


class Car(object):
    def __init__(self, model):
        self.model = model

    @logging
    def run(self):
        print "{} is running!".format(self.model)

    @staticmethod
    @logging
    def check_model_for(obj):
        if isinstance(obj, Car):
            print "The model of your car is {}".format(obj.model)
        else:
            print "{} is not a car!".format(obj)


if __name__ == '__main__':
    Car.check_model_for(None)

    my_car = Car('Ferrari')
    my_car.run()
    Car.check_model_for(my_car)
