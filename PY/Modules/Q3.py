from fractions import Fraction

def fractionate(amount: int):
    return [Fraction(1, amount) for _ in range(amount)]


print()
print(fractionate(6))
