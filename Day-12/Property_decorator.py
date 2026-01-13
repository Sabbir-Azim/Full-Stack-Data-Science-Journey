class Thermometer:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return (self.celsius * 1.8) + 32


t = Thermometer(100)
temp = t.fahrenheit 
print(temp) 
