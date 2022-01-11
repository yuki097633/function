# *args 不特定多数の引数を受け取ることができる
# *argsにすると不特定多数のtupleで引数を渡すことができる
def get_average(*args):
    # print(args)
    # print(type(args)) # tuple
    num = len(args)
    if num == 0:
        return 0
    total = sum(args)
    return total / num


average = get_average(1, 2, 3, 4, 5)
print(average)


# **kwargsにすると不特定多数のdictionaryで引数を渡すことができる
def kwargs_func(**kwargs):
    # デフォルトの設定をする場合
    param1 = kwargs.get("param1", 1)
    param2 = kwargs.get("param2", 2)

    print(f"param1: {param1}, param2: {param2}")


kwargs_func(param1=10, param2=20, param4=4)



# *と**はアンパッキングオペレーター
numbers = (1, 2, 3)
print(numbers)
print(*numbers) # *をつけるとアンパックされた状態になる

a = {"a": 1, "b": 2}
b = {"c": 1, "d": 2}
c = {**a, **b}
print(c)


