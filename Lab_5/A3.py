def make_abbreviation(text):
    words = text.split()
    abbreviation = ''.join(word[0].upper() for word in words if len(word) >= 3)
    return abbreviation
input_text = input("Ввод: ")
abbreviation = make_abbreviation(input_text)
print(abbreviation)