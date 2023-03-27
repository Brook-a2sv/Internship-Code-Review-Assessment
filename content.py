count = 0


def increment_count():
    # incremets the value of the global variable count
    global count
    count += 1


def product(x, y):
    # multiplies two numbers
    return x * y


def divide_numbers(a, b):
    # divides two numbers
    return a / b


def calculateArea(radius):
    # calculates the area of a circle with a given radius
    return 3.14 * radius ** 2


increment_count()
print(count)
