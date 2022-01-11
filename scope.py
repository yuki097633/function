# グローバル変数（モジュール変数）
age = 30


def print_age():
    global age # ローカル変数ではなくグローバル変数のageを操作できるようになる
    age = 20
    print(f"I'm {age} years old")


print_age()
print(age)

