def remove(text):
    result = ''
    skip = 0
    for char in text:
        if char == '(':
            skip += 1
        elif char == ')':
            if skip > 0:
                skip -= 1
        elif skip == 0:
            result += char
    return result
input_text = input("Исходный текст: ")
shortened_text = remove(input_text)
print("Укороченный текст:", shortened_text)