# Prime factorization
import math


def prime_factorization(number):
    divider = 2
    while divider <= number:
        if number % divider == 0:
            print(divider, end=' ')
            number /= divider
            divider = 2
        else:
            divider += 1


def prime_factorization_rec(number):
    pass


if __name__ == '__main__':
    prime_factorization(5320)