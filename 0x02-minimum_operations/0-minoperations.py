#!usr/bin/python3
'''
Mock interview preparation "minimum Operations"
'''


def minOperations(n):
    '''
    method to count mininum Operations to make n => 0
    '''
    count = 0
    if n < 0:
        return 0
    while n != 0:
        if n % 2 == 0:
            count += 1
            n = n / 2
        elif n % 2 != 0:
            count += 2
            n -= 1
    return count
