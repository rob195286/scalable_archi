from dataclasses import dataclass
from math import sqrt, fabs


@dataclass
class Complex_number:

    def __init__(self, real_part, img_part):
        self.real_part = real_part
        self.img_part = img_part
        self.module = sqrt(self.real_part**2 + self.img_part**2)

    def __add__(self, other_complex):
        return Complex_number(
                    self.real_part + other_complex.real_part,
                    self.img_part + other_complex.img_part
                )

    def __mul__(self, other_complex):
        return Complex_number(
                    (self.real_part * other_complex.real_part - self.img_part * other_complex.img_part),
                    (self.real_part * other_complex.img_part + self.img_part * other_complex.real_part)
                )

    def __pow__(self, power, modulo=None):
        result = self
        for nbr in range(power-1):
            result *= self
        return result

    def __eq__(self, other):
        return True if (other.real_part == self.real_part and other.img_part == self.img_part) else False

    def __repr__(self):
        signe = "+" if(self.img_part >= 0) else "-"
        return "{} {} {} i".format(self.real_part, signe, fabs(self.img_part))


def complex_mapper(complex_number_dict: dict):
    return Complex_number(complex_number_dict['real'], complex_number_dict['img'])


if __name__ == "__main__" :
    c1 = Complex_number(3, 8)
    c2 = Complex_number(2, 4)
    print(c1 + c2)
    print(c1 * c2)
    print(c1.module)