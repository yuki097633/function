
# 関数の中で関数を定義
msg = "I'm global"


def outer():
    outer_param = "outer arg"
    msg = "I'm outer"
    def inner():
        nonlocal msg # outterの変数を使用できるようになる
        innner_param = "inner arg"
        msg = "I'm inner"
        print("This is inner function")
        print(outer_param)
        print(msg)
    # print(innner_param) これは呼び出せない
    inner()
    print(msg)


outer()
print(msg)