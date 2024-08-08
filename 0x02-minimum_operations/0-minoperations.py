#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n: int) -> int:
    """
    Minimum Operations needed to get n H characters
    """
    next_char = 'H'
    body = 'H'
    op = 0

    while (len(body) < n):
        if n % len(body) == 0:
            op += 2
            next_char = body
            body += body
        else:
            op += 1
            body += next_char
    if len(body) != n:
        return 0
    return op
