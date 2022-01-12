# 無名関数　関数にするほどでも無いちょっとした関数

def square(x):
    return x * x


print(square(3))


s = lambda x: x * x

print(s(3))


def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power


third_power = power(3)
print(third_power(2))


def power_lambda(exponent):
    return lambda base: base ** exponent


third_power_lambda = power_lambda(3)
print(third_power_lambda(4))


numbers = [6, 3, 5, 8, 10]
# filter(numbers)


# 奇数を判別する
filtered_num = filter(lambda num: num % 2, numbers)
print(list(filtered_num))

# for num in numbers:
#     print(filter_func(num))

