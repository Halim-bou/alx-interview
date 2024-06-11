#!/usr/bin/python3
'''
Mock interview preparation "minimum Operations"
'''


def minOperations(n):
    '''
    method to count mininum Operations to make n => 0
    '''
    if n <=1:
        return 0
    count = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            count += factor
            n //= factor
        factor += 1
    return count
