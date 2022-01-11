# 関数(function)

# Pythonで標準で用意される関数たち
# print()
# len()
# input()


# 華氏(fah)から摂氏(cel)に変換する
# fah = 72
# cel = (fah - 32) * 5/9
# print(cel)


def fah_to_cel(fah):
    cel = (fah - 32) * 5/9
    return cel


fah = 72
cel = fah_to_cel(fah)
print(cel)

