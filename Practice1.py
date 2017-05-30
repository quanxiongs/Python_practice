# -*- coding: utf-8 -*-

class Coordinate(object):#object is a parent
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return ("<" + str(self.x) + "," + str(self.y) + ">")
    
    
c = Coordinate(3,4)
origin = Coordinate(0,0)

print(c)
c.distance(origin)
#instance 안에서 Method를 호출하면 self를 줄 필요가 없지만
#class 자체를 호출하면 self자리에 argument를 제공해야 한다


class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
test = Celsius()
test.__dict__

class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
        
#An underscore (_) at the beginning is used 
#to denote private variables in Python.

"""
The big problem with the above update is that, 
all the clients who implemented our previous class in their program 
have to modify their code from obj.temperature to 
obj.get_temperature() and all assignments like 
obj.temperature = val to obj.set_temperature(val)
"""

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)
    
c = Celsius()
c.temperature
c.temperature=30
c.to_fahrenheit()
#property(fget=None, fset=None, fdel=None, doc=None)
"""    
By using property, we can see that, we modified our class and implemented the value constraint without any change required to the client code. Thus 
our implementation was backward compatible and everybody is happy.
Finally note that, the actual temperature value is stored in 
the private variable _temperature. The attribute temperature is a 
property object which provides interface to this private variable.
"""
temperature = property(get_temperature,set_temperature)
#could have been broken down as
# make empty property
temperature = property()
# assign fget
temperature = temperature.getter(get_temperature)
# assign fset
temperature = temperature.setter(set_temperature)

class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

##Decorator
def outer_function():
    print("1.this is outer function!")
    def inner_function():
        print("2.this is inner fucntion")
    print("3.This is outside inner function, inside outer function")
    return(inner_function())
outer_function()

"""
Python decorator are the function that receive a function as an argument and return another function as return value.
The assumption for a decorator is that we will pass a function as argument and the signature of the inner function 
in the decorator must match the function to decorate.
"""
import time

def timetest(input_func):

    def timed(*args, **kwargs):
        
        start_time = time.time()
        result = input_func(*args, **kwargs)
        end_time = time.time()
        print ("Method Name - {0}, Args - {1}, Kwargs - {2}, Execution Time - {3}".format(
                input_func.__name__, args, kwargs, end_time - start_time))
        return result
    return timed

@timetest
def foobar(*args,**kwargs):
    time.sleep(0.3)
    print("inside foobar")
    print(args,kwargs)
    

foobar(["hello, world"], foo=2, bar=5)

#method decorator
def method_decorator(method):

    def inner(city_instance):
        if city_instance.name == "SFO":
            print ("Its a cool place to live in.")
        else:
            method(city_instance)
    return inner

class City(object):
    def __init__(self,name):
        self.name = name
        
    @method_decorator
    def print_test(self):
        print(self.name)
        

p1 = City("SFO")
p1.print_test()

#class decorator

class decoclass(object):
    def __init__(self, f):
        self.f = f
        
    def __call__(self, *args, **kwargs):
        #befor f actions
        print("decorator initialised")
        self.f(*args, **kwargs)
        print("decorator terminated")
        #after f actions
        
        
@decoclass
def klass():
    print ('class')

klass()

#Chanining Decorators

def makebold(f):
    return lambda: "<b>" + f() + "</b>"
def makeitalic(f):
    return lambda: "<i>" + f() + "</i>"

@makebold
@makeitalic
def say():
    return "Hello"

print (say())

"""
One thing should be kept in mind that the order of decorators we set matters. When you chain decorators, 
the order in which they are stacked is bottom to top.
"""
#Functools and Wraps
def decorator(func):
    """decorator docstring"""
    def inner_function(*args, **kwargs):
        """inner function docstring """
        print (func.__name__ + " was called")
        return func(*args, **kwargs)
    return inner_function

@decorator
def foobar(x):
    """foobar docstring"""
    return x**2

print(foobar.__name__)
print(foobar.__doc__)
#the origianl function is replaced by inner_function


from functools import wraps


def wrapped_decorator(func):
    """wrapped decorator docstring"""
    @wraps(func)
    def inner_function(*args, **kwargs):
        """inner function docstring """
        print (func.__name__ + "was called")
        return func(*args, **kwargs)
    return inner_function

@wrapped_decorator
def foobar(x):
    """foobar docstring"""
    return x**2

print(foobar.__name__)
print(foobar.__doc__)

"http://blog.apcelent.com/python-decorator-tutorial-with-example.html"

