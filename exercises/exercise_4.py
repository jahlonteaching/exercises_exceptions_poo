class Temperature:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_celsius(self):
        if self.unit == 'Celsius':
            return self.value
        elif self.unit == 'Fahrenheit':
            return (self.value - 32) * 5 / 9
        elif self.unit == 'Kelvin':
            return self.value - 273.15
        else:
            raise ValueError('Unidad no válida')

    def to_fahrenheit(self):
        if self.unit == 'Celsius':
            return self.value * 9 / 5 + 32
        elif self.unit == 'Fahrenheit':
            return self.value
        elif self.unit == 'Kelvin':
            return (self.value - 273.15) * 9 / 5 + 32
        else:
            raise ValueError('Unidad no válida')

    def to_kelvin(self):
        if self.unit == 'Celsius':
            return self.value + 273.15
        elif self.unit == 'Fahrenheit':
            return (self.value + 459.67) * 5 / 9
        elif self.unit == 'Kelvin':
            return self.value
        else:
            raise ValueError('Unidad no válida')

    def compare(self, other_temp):
        if not isinstance(other_temp, Temperature):
            raise TypeError('Debe comparar con otra temperatura')
        if self.to_celsius() < other_temp.to_celsius():
            return -1
        elif self.to_celsius() > other_temp.to_celsius():
            return 1
        else:
            return 0
