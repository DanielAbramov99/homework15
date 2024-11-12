import random

random_list: list[int] = [random.randint(-50, 50) for _ in range(20)]
print(random_list)
print("numbers in power of 3", list(map(lambda num: num ** 3, random_list)))
print("only ahadot", list(map(lambda num: abs(num) % 10, random_list)))
print("numbers converted to Fahrenheit", list(map(lambda num: (num * (9 / 5)) + 32, random_list)))
print("negative or positive", list(map(lambda num: "negative" if num < 0 else "positive", random_list)))
