cortege = []
products = []
all_products = {"name" : x, "price" : x, "quantity" : x, "unit" : x}
num = 1
n = int(input("Enter the number of products to add to the list: "))
print("Get ready, we'll write each item of products!")
while num <= n:
    products = dict({"name" : input("Write name: "), "price" : input("Write price: "),
                     "quantity" : input("Write quantity: "), "unit" : input("Write unit: ")})
    cortege.append((num, products))
    num += 1
print(f"This is cortege: {cortege}")
