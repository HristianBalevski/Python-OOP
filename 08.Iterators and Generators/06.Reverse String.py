def reverse_text(text):
    num = len(text) - 1
    result = ''
    while num >= 0:
        yield text[num]
        result += text[num]
        num -= 1
    return result


for char in reverse_text("step"):
    print(char, end='')