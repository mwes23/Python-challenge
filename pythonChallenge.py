def qn1():
	numlist = []
	for number in range(2000,3201):
		if number%7 == 0 and number%5 == 0:
			numlist.append(number)
	print(numlist)

def qn2():
	string = input()
	print(string.upper())



def qn3():
	binlist = []
	newlist = input().split(',')
	print(newlist)
	for binarynum in newlist:
		print(binarynum)
		number = int(binarynum,2)
		if number % 5 == 0:
			binlist.append(number)
	print(binlist)



def question0():
	studentMarks = [23,4,5,6,64,90,67,98,45,23,67,78,89]
	list1 = []
	list2 = []

	def grade(studentMark):
		if studentMark >= 90:
			return (studentMark , "Excellent")
		elif 89 >= studentMark >= 70:
			return (studentMark ,'Very Good')
		elif 69 >= studentMark >= 60:
			return (studentMark ,'Good')
		elif 59 >= studentMark >= 40:
			return (studentMark ,'poor')
		elif 39 >= studentMark >= 20:
			return (studentMark ,'Very Poor')
		else:
			return (studentMark ,'repeat')


	for studentMark in studentMarks:
		if studentMark >=50:
			list1.append(grade(studentMark))
		else:
			list2.append(grade(studentMark))




	print(list1)
	print(list2)


def question4():
	transaction = int(input("Enter the number transactions: "))
	balance = 0
	for x in range(transaction):
		x = input("Enter transaction: ").split()
		if x[0] == 'D':
			balance += int(x[1]) 
		else:
			balance -= int(x[1])
	return balance

def qn5():
	squarelist = []
	for numbers in range(1,21):
		squarelist.append(numbers**2)
	print(squarelist[0:5])


		
if __name__ == '__main__':
	qn5()
	question4()
	qn3()
	qn2()
	qn1()
	question0()