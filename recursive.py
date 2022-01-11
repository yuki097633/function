# 再帰関数 recursive :関数ないで自身の関数をcallする関数

# 階乗　3! = 3 * 2 * 1 = 6
# n! = n * (n-1)!
# (n-1)! = (n-1)! * (n-2)!

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3))


# フィボナッチ数列
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ......

# 再帰バージョン
def fibonacchi_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacchi_recursive(n-1) + fibonacchi_recursive(n-2)

print(fibonacchi_recursive(6))


# 再帰じゃ無いバージョン
def fibonacchi(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result


print(fibonacchi(4))


# 再帰バージョンの方が重い（遅い）
for i in range(50):
    print(i, fibonacchi(i))






