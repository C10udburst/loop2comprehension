"""
Examples which AI should refuse to convert to list comprehension.
There should be no changes in code after running the intention and an error hint should show up with an explanation.
"""

# Collatz conjecture - iterator can't be cleanly converted to comprehension
def fun1(n: int):
    arr = []
    while n > 1:
        arr.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return arr

# Print statements shouldn't be converted
def fun2():
    for i in range(5):
        print(f"Simple for loop: {i}")