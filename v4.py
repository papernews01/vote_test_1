def count_words(text):
    words = text.lower().split()
    total_words = len(words)
    unique_words = len(set(words))
    return total_words, unique_words

text = input("Введите текст: ")
total, unique = count_words(text)
print(f"Всего слов: {total}")
print(f"Уникальных слов: {unique}")