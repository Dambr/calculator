from math import *
def main():
	while(True):
		try:
			exit = input('Input:  ')
			if exit == 'exit':
				return
			else:
				print('Output:', eval(exit))
		except:
			print('Error of input')
main()