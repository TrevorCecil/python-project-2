#Exceptions = this is an error

try:
    print(x)
except:
    print('An error occurred')
finally:
    print('success')
num1 = 20
num2 = 0

try:
    print(num1 / num2)

except:
    print ('zero division error')

# User-defined functions
try:
    def multiply(x, y):
        print(x * y)
except:
    print('An error occurred')
finally:
    print('success')
multiply(4,5)