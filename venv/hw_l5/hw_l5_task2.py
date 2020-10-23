"""В данном примере будет взят за основу файл, сгенерированный в предыдущем задании"""

with open("new_text_file.txt", "r") as file:
    content = file.readlines()
    print(f"Количество строк в текстовом файле: {len(content)}")
    words = []
    for line in content:
        words.append(line.split(" ", "\n"))
    print(f"Количество слов в текстовом файле: {len(words)}")
