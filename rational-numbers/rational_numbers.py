''' Rational Numbers class '''
#!/usr/bin/env python3

from __future__ import division
from fractions import gcd

class Rational(object):
    ''' Initializes with the greatest common denominator values. '''
    def __init__(self, numer, denom):
        self.numer = numer / gcd(numer, denom)
        self.denom = denom / gcd(numer, denom)

    def __eq__(self, other):
        ''' Determines if fractions are equal. '''
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        ''' Representation of instance. '''
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        ''' Adds fractions. '''
        numer = (self.numer * other.denom + other.numer * self.denom)
        denom = (self.denom * other.denom)
        return Rational(numer, denom)

    def __sub__(self, other):
        ''' Subtracts Fractions. '''
        numer = (self.numer * other.denom - other.numer * self.denom)
        denom = (self.denom * other.denom)
        return Rational(numer, denom)

    def __mul__(self, other):
        ''' Multiply Fractions. '''
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        ''' Divides Fractions. '''
        if other.numer * self.denom == 0:
            return 'Divide by 0'
        return Rational(self.numer * other.denom, other.numer * self.denom)

    def __abs__(self):
        ''' Absolute value. '''
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        ''' Exponential value of fraction. '''
        if power > 0:
            return Rational(self.numer**power, self.denom**power)
        if power < 0:
            return Rational(self.denom**power, self.numer**power)
        return Rational(1, 1)

    def __rpow__(self, base):
        ''' Value raised to fraction. '''
        return base **(self.numer / self.denom)

    def __str__(self):
        ''' Print class attributes. '''
        return str(self.numer) + '\\' + str(self.denom)
    
        



test = Rational(1, 2)
test2 = Rational(-2, 3)
print(test + test2)
print(test)
print(test2)