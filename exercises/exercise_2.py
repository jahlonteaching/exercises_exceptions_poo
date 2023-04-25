import math


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        return self

    def is_valid(self):
        return self.denominator != 0

    def check_validity(self):
        if not self.is_valid():
            raise ValueError('Denominator cannot be zero')

    def add(self, other):
        self.check_validity()
        other.check_validity()
        return (self + other).reduce()

    def subtract(self, other):
        self.check_validity()
        other.check_validity()
        return (self - other).reduce()

    def multiply(self, other):
        self.check_validity()
        other.check_validity()
        return (self * other).reduce()

    def divide(self, other):
        self.check_validity()
        other.check_validity()
        return (self / other).reduce()
