"""
xd
"""
from enum import Enum


class Operators(Enum):
    MULTI = '*'
    ADDI = '+'


def square_and_sum(a, b, operator: Operators):
    if operator == Operators.ADDI:
        return a + b
    if operator == Operators.MULTI:
        return a * b
    mult = a * b
    addi = a + b

    return mult, addi


x = square_and_sum(4, 3)

print(f"multi {x[0]} addi {x[1]}")
