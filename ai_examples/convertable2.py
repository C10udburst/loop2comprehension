result = []
for i in range(10):
    result.append(i)

result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i)

result = []
for i in range(3):
    for j in range(3):
        result.append((i, j))

result = []
for i in range(5):
    result.append(i * i)

result = []
i = 0
while i < 10:
    result.append(i)
    i += 1

result = []
for i in range(3):
    for j in range(3):
        if (i + j) % 2 == 0:
            result.append((i, j))


def square(x):
    return x * x


result = []
for i in range(5):
    result.append(square(i))


result = []
list_of_lists = [[1, 2], [3, 4], [5, 6]]
for sublist in list_of_lists:
    for item in sublist:
        result.append(item)

result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i * i)

result = []
for i in range(3):
    for j in range(3):
        result.append((i, j * 2))

result = []
i = 0
while i < 10:
    if i % 2 == 0 and (i * i) > 10:
        result.append(i * i)
    i += 1

result = []
list_a = [1, 2, 3]
list_b = ['a', 'b']
for a in list_a:
    for b in list_b:
        result.append((a, b))

result = []
for i in range(5):
    result.append('A' * i)
