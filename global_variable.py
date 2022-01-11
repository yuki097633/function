call_count = 0


def print_count1():
    global call_count
    call_count += 1
    print(f"関数1：{call_count}回目")


def print_count2():
    global call_count
    call_count += 1
    print(f"関数2：{call_count}回目")


print_count1()
print_count2()

# 基本的にはグローバル変数は使わない
# 慣習的に定数は大文字にするといい
