'''
The prime factors of 13195 are 5,7,13 and 29.

What is the largest prime factor of a given number N?

Input Format:
First line contains T, the number of test cases. This is followed by T lines each containing an integer N.

Notes:

A factor that is a prime number. In other words: any of the prime numbers that can be multiplied to give the original number.
Example: 3 is a prime factor of 15, and so is 5, because 3 x 5 = 15 and 3 and 5 are prime numbers.

Prime Factorisation of a large number, using factor tree method

'''

import math


def get_factor(number):
    '''
    Checks if the number is even. If so, it returns 2 as 2 is the only even prime number.
    If the number is odd, it uses a for loop to iterate over odd numbers starting from 3 up to the square root of the given number (inclusive).
    All even numbers (except 2) are not prime, so checking only odd numbers as potential factors reduces the number of iterations and improves the efficiency of the algorithm.
    If no prime factor is found in the loop, it returns the input number itself, indicating that the number is prime.
    '''

    if number % 2 == 0:
        return 2
    # isqrt is more efficient that sqrt if you just need the integer part
    for i in range(3, math.isqrt(number) + 1, 2):
        if number % i == 0:
            return i
    return number


def split_number(number, hcf):
    '''
    It uses the get_factor function to find one prime factor of the given number.
    If the found factor is greater than the current highest common factor (hcf), it updates hcf.
    If the found factor is not equal to the input number, it recursively calls itself with the updated number (divided by the factor) and the updated hcf.
    If the found factor is equal to the input number, it returns the highest common factor.
    '''
    factor = get_factor(number)
    if factor > hcf:
        hcf = factor
    if factor != number:
        return split_number(number // factor, hcf)
    return hcf


def main():
    tc = int(input().strip())
    for _ in range(tc):
        n = int(input().strip())
        hcf = split_number(n, 1)
        print(hcf)


if __name__ == "__main__":
    main()
