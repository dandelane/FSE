import re
def split_sentences(text):
    sentences = re.split(r'(?<=[.?!])\s+', text)
    cleaned_sentences = [s.strip() for s in sentences if s.strip()]
    return cleaned_sentences
input_text = input("Введите текст: ")
sentences = split_sentences(input_text)
for s in sentences:
    print(s)
print(f"Предложений в тексте: {len(sentences)}")