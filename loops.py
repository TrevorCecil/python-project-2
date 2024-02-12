# While loop
# Incrementing a value
numbers = 5  # initializing
while numbers <= 10:  # loop
    print(numbers)
    numbers += 1

# Decrementing values

num = 105
while num >= 100:
    print(num)
    num -= 1

# Break statement

x = 1
while x <= 5:
    print(x)
    if x == 3:
        break
    x += 1

# continue - to skip an element

count = 19
while count < 25:
    count += 1
    if count == 23:
        continue
    print(count)

#for loop
languages = ['Python', 'Java', 'C++', 'Kotlin']
for language in languages:
    print(language)

#range
for i in range(1,11):
    print(i)

print()

for j in range(20,31):
    print(j)

print()

for k in range(30,41,2):
    print(k)

print()

h= 'innovation'
for g in h:
    print(g)

