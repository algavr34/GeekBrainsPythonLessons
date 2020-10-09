list = input("Enter some words separated by a space and then press Enter: ").split(" ")
for i in range(len(list)):
    print(f"{i+1}. {list[i][:10]}", sep='\n')