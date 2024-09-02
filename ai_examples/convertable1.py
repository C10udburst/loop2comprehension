# 1. Simple for loop
def test1():
    result1 = []
    for i in range(10):
        result1.append(i)
    return result1


# 2. For loop with condition
def test2():
    result2 = []
    for i in range(10):
        if i % 2 == 0:
            result2.append(i)
    return result2


# 3. Nested for loops
def test3():
    result3 = []
    for i in range(3):
        for j in range(3):
            result3.append((i, j))
    return result3


# 4. Nested for loops with condition
def test4():
    result4 = []
    for i in range(3):
        for j in range(3):
            if i != j:
                result4.append((i, j))
    return result4


# 5. While loop
def test5():
    result5 = []
    i = 0
    while i < 10:
        result5.append(i)
        i += 1
    return result5


# 6. While loop with condition
def test6():
    result6 = []
    i = 0
    while i < 10:
        if i % 2 == 0:
            result6.append(i)
        i += 1
    return result6


# 7. Nested while loops
def test7():
    result7 = []
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            result7.append((i, j))
            j += 1
        i += 1
    return result7


# 8. For loop with function call
def test8():
    def square(x):
        return x * x

    result8 = []
    for i in range(10):
        result8.append(square(i))
    return result8


# 9. For loop with multiple conditions
def test9():
    result9 = []
    for i in range(10):
        if i % 2 == 0 and i % 3 == 0:
            result9.append(i)
    return result9


# 10. For loop iterating over a list
def test10():
    numbers = [1, 2, 3, 4, 5]
    result10 = []
    for num in numbers:
        result10.append(num * 2)
    return result10


# 11. Nested for loops with list
def test11():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result11 = []
    for row in matrix:
        for num in row:
            result11.append(num)
    return result11


# 12. For loop with dictionary
def test12():
    data = {'a': 1, 'b': 2, 'c': 3}
    result12 = []
    for key in data:
        result12.append((key, data[key]))
    return result12


# 13. For loop with string
def test13():
    text = "hello"
    result13 = []
    for char in text:
        result13.append(char.upper())
    return result13


# 14. For loop with enumerate
def test14():
    numbers = [10, 20, 30, 40]
    result14 = []
    for index, value in enumerate(numbers):
        result14.append((index, value))
    return result14


# 15. For loop with zip
def test15():
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    result15 = []
    for a, b in zip(list1, list2):
        result15.append((a, b))
    return result15


# 16. For loop with list of tuples
def test16():
    pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
    result16 = []
    for num, char in pairs:
        result16.append(f"{num}-{char}")
    return result16


# 17. Nested for loops with string
def test17():
    words = ["hello", "world"]
    result17 = []
    for word in words:
        for char in word:
            result17.append(char)
    return result17


# 18. For loop with set
def test18():
    unique_numbers = {1, 2, 3, 4, 5}
    result18 = []
    for num in unique_numbers:
        result18.append(num * 3)
    return result18


# 19. For loop with range and step
def test19():
    result19 = []
    for i in range(0, 10, 2):
        result19.append(i)
    return result19


# 20. For loop with reversed range
def test20():
    result20 = []
    for i in range(10, 0, -1):
        result20.append(i)
    return result20


# 21. Three-level nested loops (for in for in for)
def test21():
    result21 = []
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result21.append((i, j, k))
    return result21


# 22. Three-level nested loops (for in while in for)
def test22():
    result22 = []
    for i in range(2):
        j = 0
        while j < 2:
            for k in range(2):
                result22.append((i, j, k))
            j += 1
    return result22


# 23. Three-level nested loops (while in for in while)
def test23():
    result23 = []
    i = 0
    while i < 2:
        for j in range(2):
            k = 0
            while k < 2:
                result23.append((i, j, k))
                k += 1
        i += 1
    return result23


# 24. Three-level nested loops (while in while in for)
def test24():
    result24 = []
    for i in range(2):
        j = 0
        while j < 2:
            k = 0
            while k < 2:
                result24.append((i, j, k))
                k += 1
            j += 1
    return result24


# 25. Three-level nested loops (for in for in while)
def test25():
    result25 = []
    for i in range(2):
        for j in range(2):
            k = 0
            while k < 2:
                result25.append((i, j, k))
                k += 1
    return result25
