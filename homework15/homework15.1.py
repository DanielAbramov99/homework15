import random
import statistics

random_list: list[int] = [random.randint(1, 100) for _ in range(50)]
print(random_list)
print(statistics.mean(random_list))
print(max(random_list))
print("numbers that bigger than 50",list(filter(lambda num: num > 50, random_list)))
print("numbers that divide by 7",list(filter(lambda num: num % 7 == 0, random_list)))
print("numbers that have 2 digits",list(filter(lambda num: 10 <= num <= 99, random_list)))
print("numbers that have 2 digits and they digits are same",list(filter(lambda num: 10 <= num <= 99 and num % 10 == num // 10, random_list)))
print("numbers that all the digits sums up to 9",list(filter(lambda num: num == 9 or num % 10 + num // 10 == 9, random_list)))
print("numbers that bigger than average",list(filter(lambda num: num > statistics.mean(random_list), random_list)))
print("numbers that bigger than half of the biggest number",list(filter(lambda num: num > max(random_list) // 2, random_list)))
