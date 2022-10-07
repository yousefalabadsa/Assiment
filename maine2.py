
# Assiment 1

from math import *

numbers = [12, 75, 150, 180, 145, 525, 50]

result_number = []
for item in numbers:
    if item > 500:
        break
    if item > 150:
        continue
    if item % 5 == 0:
        result_number.append(item)

print(result_number)

# Assiment 2

from audioop import reverse


for i in range(5):
    print(i)
else:
    print("done!")

number_list = [7, 6, 5, 4, 2]
i = 0
number_list.reverse()

while i < len(number_list):
    print(number_list[i])
    i += 1

keys = ['Ten', 'Twanty', 'Thirty']
values = [10, 20, 30]

output = {}

for i in range(len(keys)):
    output[keys[i]] = values[i]

print(output)

sample_dict ={"name": "Kelly",
            "age": 25,
            "salary": 8000,
            "city": "New york"}

sample_dict.clear()

sample_dict.update({"city": "New york",
                    "age": 25})

print(sample_dict)

# Assiment 3 

sample_set = {"Yellow", "orenge", "Black"}
sample_lest = ["Blue", "Green", "Red"]

print(sample_set.union(sample_lest))


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))

# Assiment 4

tuple1 = (10, 20, 30, 40, 50)
ss = reversed(tuple1)
print(tuple(ss))

tuple2 = ("Orenge", [10, 20, 30], [5, 15, 25])

print(tuple2[1][1])

tuple3 = (10, 20, 30, 40)

print(tuple3[0])
print(tuple3[1])
print(tuple3[2])
print(tuple3[3])