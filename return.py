# returnしない関数も多くある　print()とか
# 正確にはNoneを返す

def print_dict(input_dict):
    for k, v in input_dict.items():
        print(f"key：{k} value:{v}")


a = {"one": 1, "two": 2}
return_value = print_dict(a)
print(return_value)


def get_first_last_word(text):
    text = text.replace(",", "") # 第一を第二にリプレイスする
    words = text.split()
    return words[0], words[-1] # 複数にするとtupleで返す


text = "Hello, My name in Mike"
first, last = get_first_last_word(text) # 複数でtupleなのでアンパックで
print(f"first word is {first}, last word is {last}")



