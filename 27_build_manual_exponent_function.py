from functools import reduce

'''
manual_exponent(2, 3) #> 8
manual_exponent(10, 2) #> 100
'''

def manual_exponent(base_num, pow_num):
	result = 1
	for index in range(pow_num):
		result =* base_num
	return result

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))