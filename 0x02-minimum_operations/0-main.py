#!/usr/bin/python3
"""
Main file for testing
"""

# Import the function from your 0-minoperations.py file
minOperations = __import__('0-minoperations').minOperations

# Test cases
n = 4
print("Min # of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 9
print("Min # of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 1
print("Min # of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 25
print("Min # of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 100
print("Min # of operations to reach {} characters: {}".format(n, minOperations(n)))
