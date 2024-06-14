class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imag})"

    def __str__(self):
        return f"({self.real} + {self.imag}i)"

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real, imag)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imag == other.imag
        return NotImplemented

    def __len__(self):
        return 2  # Since a complex number has two components

    def __getitem__(self, index):
        if index == 0:
            return self.real
        elif index == 1:
            return self.imag
        else:
            raise IndexError("Index out of range. Use 0 for real part and 1 for imaginary part.")

    def __call__(self, x):
        return ComplexNumber(self.real * x, self.imag * x)

# Usage
c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)

print("Calls __str__: ", c1)  # Calls __str__
print("Calls __repr__: ", repr(c2))  # Calls __repr__
print("Calls __add__: ", c1 + c2)  # Calls __add__
print("Calls __sub__: ", c1 - c2)  # Calls __sub__
print("Calls __mul__: ", c1 * c2)  # Calls __mul__
print("Calls __eq__: ", c1 == c2)  # Calls __eq__
print("Calls __len__: ", len(c1))  # Calls __len__
print("Calls __getitem__: ", c1[0], c1[1])  # Calls __getitem__
print(c1(2))  # Calls __call__, scales the complex number by 2
