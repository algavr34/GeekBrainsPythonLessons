def int_func(some_word):
    return some_word.title()

word = input("Write one word: ")
print(int_func(word))
words = input("Write some words separated by space: ").split(" ")
new_words = list(map(int_func, words))
print(new_words)