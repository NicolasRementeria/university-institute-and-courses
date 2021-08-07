# Whenever you import a library, you will import ALL classes inside the library

# This is bad memory management

# For that, it's utilized FROM

# in this case will import the entire "abc" library
import abc

# will also import everything
from abc import *

# in this case, from abc library will import only ABC and abstractmethod classes
from abc import ABC, abstractmethod
