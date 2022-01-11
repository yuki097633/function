# カプセル化　外からアクセスできないようにする

def casino_entrance(age, min_age=21):
    if age < min_age:
        print(f"{min_age}未満お断り")
        return

    def inner_casino_entrance():
        print("ようこそカジノへ")

    return inner_casino_entrance()


casino_entrance(30)
# innner_casino_entrance() は呼べない
# →外からメインの処理にはアクセスできず、必ずcasino_entranceを通さないといけない




