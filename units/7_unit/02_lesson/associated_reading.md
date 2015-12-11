# Associated Reading

## The init method

The init method (short for “initialization”) is a special method that gets invoked when an object is instantiated. Its full name is __init__ (two underscore characters, followed by init, and then two more underscores). An init method for the Time class might look like this:

```
class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
```

It is common for the parameters of __init__ to have the same names as the attributes. The statement

```
        self.hour = hour
```
stores the value of the parameter hour as an attribute of self.
The parameters are optional, so if you call Time with no arguments, you get the default values.

```
>>> time = Time()
>>> time.print_time()
00:00:00
If you provide one argument, it overrides hour:
>>> time = Time (9)
>>> time.print_time()
09:00:00
If you provide two arguments, they override hour and minute.
>>> time = Time(9, 45)
>>> time.print_time()
09:45:00
```

And if you provide three arguments, they override all three default values.

## Debugging

It is legal to add attributes to objects at any point in the execution of a program, but if you are a stickler for type theory, it is a dubious practice to have objects of the same type with different attribute sets. It is usually a good idea to initialize all of an object’s attributes in the init method.

If you are not sure whether an object has a particular attribute, you can use the built-in function hasattr (see Section 15.7).

Another way to access the attributes of an object is through the special attribute __dict__, which is a dictionary that maps attribute names (as strings) and values:

>>> p = Point(3, 4)
>>> print p.__dict__
{'y': 4, 'x': 3}
For purposes of debugging, you might find it useful to keep this function handy:
def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)
print_attributes traverses the items in the object’s dictionary and prints each attribute name and its corresponding value.
The built-in function getattr takes an object and an attribute name (as a string) and returns the attribute’s value.
