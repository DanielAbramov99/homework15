fruit_list: list[str] = ["Mango ", "Orange ", "Banana ", "Apple ", "Strawberry", "Pineapple", "Grapes", "Watermelon"]
print(fruit_list)
print("fruits in reverse letters", list(map(lambda fruit: fruit.lower()[::-1], fruit_list)))
print("first letter of all fruits", list(map(lambda fruit: fruit[0], fruit_list)))
print("fruits in capital letters", list(map(lambda fruit: fruit.upper(), fruit_list)))
print("middle letter of all fruits", list(map(lambda fruit: fruit[(len(fruit) // 2) - 1], fruit_list)))
print("fruits that ends with the letter s get !", list(map(lambda fruit:fruit + "!" if fruit.endswith ("s") else fruit, fruit_list)))
