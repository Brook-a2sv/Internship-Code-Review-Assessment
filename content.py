
count = 0

# incremets the value of the global variable count


def increment_count():
    global count
    count += 1

# multiplies two numbers


def product(x, y):
    return x * y


def calculateArea(radius):
    return 3.14 * radius ** 2


def divide_numbers(a, b):
    return a / b


increment_count()
print(count)
