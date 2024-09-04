"""
Examples that should be converted.
"""

# Simple example that should use sum()
def fun1():
    esum = 0
    for i in range(101):
        if i % 2 == 0:
            esum += i
        else:
            esum += 0.21
    print(esum)

# Simple example of common pattern: for [...] .append(), which should be easily converted.
def squares_to_ten():
    squares = []
    for i in range(1, 11):
        squares.append(i ** 2)
    return squares

# Another example of the for [...] .append() pattern
def group_by_three():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    grouped = []
    for i in range(0, len(lst), 3):
        grouped.append(lst[i:i + 3])

# Another example of for [..] append(), but with file
def file_read():
    with open(__file__) as f:
        lines = []
        for line in f.readlines():
            lines.append(line.strip())
        return lines

# Example of two independent loops, the second one should use extend or +=
def test2_loops():
    res = []
    for i in generator_function():
        res.append(i)
    for j in range(20):
        res.append(j)

# Simple while loop example that should convert to specific range()
def while1():
    i = 0
    output = []
    while i < 10:
        i += 1
        output.append(i)
    print(output)

# Simple async example using the same common pattern
async def resolve_entries(client):
    results = []
    for entry in client.entries:
        res = await entry.resolve()
        results.append(res)
    return results

# Async example with sum()
async def balance_sum(client):
    cum_sum = 0
    async for entry in client.entries:
        cum_sum += await entry.balance()
    return cum_sum

# Example of functools.reduce()
def mult1():
    prod = 1
    for i in range(1, 11):
        prod *= i
    return prod

# Example of min() with misleading var name
def reduce2():
    lst = [1, 2, 3, 8, 543, 22, 43, 541, 954, 9]
    even_max = 10e100
    for i in lst:
        if i % 2 == 0 and i < even_max:
            even_max = i
    return even_max


# Example of for ... assert -> assert all(...)
def assert1(client):
    for entry in client.entries:
        assert entry.balance() >= 0