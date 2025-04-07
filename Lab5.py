# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n < 1:
        return ""
    square = ""
    i = 0
    while i < n:
        if i == 0 or i == n - 1:
            square += "*" * n + "\n"
        else:
            square += "*" + " " * (n - 2) + "*" + "\n"
        i += 1
    return square.rstrip()
    


# 1
# 12
# 123
# 1234
def number_pattern(n):
    if n < 1:
        return ""
    pattern = ""
    for i in range(1, n + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        pattern += line + "\n"
    return pattern.rstrip()


# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    counter = 1
    total = 0
    while counter <= n:
        total = total + counter
        counter = counter + 1
    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    if n < 1:
        return ""
    pyramid = ""
    for i in range(1, n + 1):
        stars = "*" * (2 * i -1)
        spaces = " " * (n - i)
        pyramid += spaces + stars + "\n"
    return pyramid.rstrip()