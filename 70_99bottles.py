def bottleForm(n):
	if n == 0:
		return 'no more bottles'
	elif n == 1:
		return str(n) + ' bottle'
	else:
		return str(n) + ' bottles'


def printLyrics(n=99):
	if(n==0):
		return bottleForm(n) + 'beer on the wall, ' + bottleForm(n) + ' of beer\nGo to the store and buy some more, ' + bottleForm(99) + ' of beer on the wall'
	else:
		return (bottleForm(n) + 'beer on the wall, ' + bottleForm(n) + ' of beer\nTake one down past it around, ' + printLyrics(n-1))

print(printLyrics(99))
