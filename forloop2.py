# for loop with dictionaries

d = {"name":"Laxmi","age":22,"income":100}

for key, value in d.items():
    print(key," ", value)
    
for i in range(1,11):
    print(f"2 X {i} = {2*i}")
    
# Nested loop

for i in range(20,30):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")

# Homework
# 1.multiple of3

for i in range(1,31):
    print(f"3 X {i} = {3*i}")
    
# 2. sum of first 10 numbers

total = 0

for i in range(1,11):
    total += i
    print("sum =", total)
    
# 3. print your name letter by letter
name = "Laxmi"
for letters in name :
    print(letters)
    
# 4. Count vowels in a string

text = "Good morining SA"
count = 0

for letter in text.lower():
    if letter in "aeiou":
        count +=1
print("number of vowels :", count)
