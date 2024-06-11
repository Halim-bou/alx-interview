#!/usr/bin/python3
'''
Mock interview preparation "minimum Operations"
'''


def minOperations(n):
    '''
    method to count mininum Operations to make n => 0
    '''
    i = 1
    count = 0
    if n <= 0:
        return 0
    while n > i:
        if i % 2 == 0:
            count += 1
            i = i * 2
        elif i % 2 != 0:
            count += 2
            i = i +  1
    return count + 1
