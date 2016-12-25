def call_numbers():

	for number in range(0,10):

		print(number)

def call_numbers_with_limit(limit):

	list = range(0,10)

	for number in range(limit):

		print(number)

def calculator(x=4,y=-1):

	return x-y


call_numbers()

call_numbers_with_limit(4)

result = calculator(2,5)
print(result)

result = calculator(y=2,x=5)
print(result)

result = calculator()
print(result)
