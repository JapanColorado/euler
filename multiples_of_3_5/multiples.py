#!/usr/bin/env python

def multiples_3_5(end: int) -> int:
    '''Finds the sum of all the multiples of 3 and 5 up to the end number.'''
    return sum(i for i in range(end) if i % 3 == 0 or i % 5 == 0)

if __name__ == "__main__":
    print(multiples_3_5(1000))