import pickle 
addressbookfile = 'addressbook.data'
#Считываем словарь из хранилища
f = open(addressbookfile, 'rb')
addresslist = pickle.load(f)
#print(addresslist)
ab = addresslist
#print(ab)

print('greeting')

while True:
	print('(1) >>> (a) add address')
	print('(2) >>> (d) delete address')
	print('(3) >>> (p) print all addresses')
	print('(4) >>> (q) quit')

	varinput=input('>>> ')

	if varinput == 'a':
		name=input('type name : ')
		address=input('type address : ')
		a = addresslist['{0}'.format(name)] = '{0}'.format(address)
		f = open(addressbookfile, 'wb')
		pickle.dump(ab, f)
		f.close

	elif varinput == 'p':
		print(addresslist)

	elif varinput == 'd':
		name=input('type name : ')
		del addresslist['{0}'.format(name)]

	elif varinput == 'q':
		quit()
