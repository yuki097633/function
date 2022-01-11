# 参照渡し（byref） <-> 値渡し（byvalue）
# Pythonでは全て参照渡しになる 同じメモリ同じオブジェクトを指す
# def add_nums(a, b):
#     print(id(a))
#     print(id(b))
#
#
# one = 1
# two = 2
# add_nums(one, two)
#
# print(id(one))
# print(id(two))


# def add_one(num):
#     print(f"変更前のID: {id(num)}")
#     num += 1
#     print(f"変更後のID: {id(num)}") # mutableなので変わる
#     return num
#
#
# n = 1
# print(id(n))
# print(f"関数呼び出し前のn: {n}")
# add_one(n)
# print(f"関数呼び出し後のn: {n}") # immutableなのでnは変わらないから



def add_fruits(fruits, fruit):
    print(f"変更前のID: {id(fruits)}")
    fruits.append(fruit)
    print(f"変更後のID: {id(fruits)}")
    return fruits


myfruits = ["apple", "banana", "peach"]
myfruit = "lemon"

print(id(myfruits))
print(f"関数呼び出し前のmyfruits: {myfruits}")
add_fruits(myfruits, myfruit)
print(f"関数呼び出し後のmyfruits: {myfruits}")
print(myfruits) # mutableなのでオブジェクト自体を更新ちゃってる

