def is_prime(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if value > 1:
            if ((value % i != 0) for i in range(2, int(value ** 0.5) + 1)):
                return "Простое"
            else:
                return "Составное"
    return wrapper

@is_prime
def sum_three(*args):
    res = sum(args)
    print(res)
    return res


result = sum_three(2, 3, 6)
print(result)