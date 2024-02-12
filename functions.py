# Inbuilt functions
y = max(55, 56, 57, 58, 59, 60, 61)
print(y)

x = min(55, 56, 57, 58, 59, 60, 61)
print(y)

z = pow(2, 3)
print(z)


# User defined functions
def details():
    print('Trevor')


details()  # calling a function


# Parameters and arguments
def students(name, course, age):
    print(name, course, age)


students('Trevor', 'MIT', 19)
students('Goretty', 'Cybersecurity', 18)


# Employees
def employees(fullname, IDnumber, salary, position, age):
    print(fullname, IDnumber, salary, position, age)


employees('Jack Hanma', 67547, 25000, 'secretary', 35)
employees('Johan Liebert', 87547, 30000, 'Treasurer', 32)
employees('Nina Fortuna', 977547, 35000, 'Human resource', 28)
employees('Ezra Scarlet', 61547, 60000, 'Manager', 36)
employees('Griffin Smoke', 46547, 90000, 'Director', 40)

