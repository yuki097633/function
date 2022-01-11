# デフォルトで設定する引数は後ろに書く
def func(first, second, third="3"):
    print(first, second, third)


# デフォルトで設定しているので"3"が出力される
func("1", "2")

func("1st", third="3rd", second="2nd")

