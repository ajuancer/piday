"""
Bellard formula (Bailey-Borwein-Plouffe algorithm for based 2 calculation)
Calculate pi by a precision of n decimals

by juancer on pi/2022
https://github.com/ajuancer
"""

from decimal import Decimal, getcontext


def get_pi(decimals):
    getcontext().prec = decimals
    return Decimal(1/64) * sum(
        Decimal((-1)**n/2**(10*n)) * (
            Decimal(-(32/(4*n+1)))
            + Decimal(-(1/(4*n+3)))
            + Decimal(+(256/(10*n+1)))
            + Decimal(-(64/(10*n+3)))
            + Decimal(-(4/(10*n+5)))
            + Decimal(-(4/(10*n+7)))
            + Decimal(+(1/(10*n+9)))
        ) for n in range(decimals))


print(get_pi(int(input("type nth: "))))
# print(get_pi(3))
