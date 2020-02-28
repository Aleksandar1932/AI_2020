# Method to return all the divisors of a given number as argument in O(sqrt(n)) complexity;
import math


def find_divisors(number):
    divisors = [1]
    i = 2
    while i < math.sqrt(number):
        if number % i == 0:
            if number/i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(number/i)
        i += 1

    return divisors


def sovrshen_broj(number):
    if number != sum(find_divisors(number)) or number == 1:
        print(f"Brojot {number} ne e sovrshen")
    else:
        print(f"Brojot {number} e sovrshen")


if __name__ == "__main__":
    number = input()
    sovrshen_broj(number)
