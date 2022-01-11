# Closure: クロージャ

# Pythonは全てをオブジェクトとして扱う

# 関数もオブジェクト
def compute_square(num):
    return num * num

func = compute_square
print(type(func))
print(func(10)) # これで関数を呼び出せる

func_list = ["1", 1, True, func]
print(func_list[-1](10)) # オブジェクトなのでリストに格納してこれでも呼び出せる

# 関数を引数にもできる
def execute_func(func, param):
    return func(param)


print(execute_func(func, 10))


# 関数をリターンできる
def return_func():
    def inner_func():
        print("This is an inner function")
    return inner_func  # ()をつけると関数を実行してしまう


f = return_func()
print(f)


# Closure: 状態をキープした関数を作ることができる
# 状態が静的
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power


p4 = power(4)  # exponentが4の状態をキープしている
print(p4(2))


# 状態が動的
def average():
    nums = []

    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average


average_nums = average()
print(average_nums(5))
print(average_nums(15))
