def fibosum(n):
    a = 0
    b = 1
    result = a + b
    for i in range(n - 1):
        c = a + b
        a, b = b, c
        result += c
    return result

print("The sum of the 5 first terms in the series is: ", fibosum(5))
print("The sum of the 10 first terms in the series is: ", fibosum(10))
