# 引数と戻り値の型を指定する
# この情報をType annotationという
# 型のヒントであって違う型を設定したとしてもエラーにはならない

def add_nums(num1: int, num2: int) -> int:
    return num1 + num2


print(add_nums(1, 2))


# Pythonは動的型付け言語のため、若干思想がズレる
one = 1
one = "one"

