'''
Author : Nadim Mansuri.
Date : 02/11/2021.
Purpose : How to print :
			*****
			*	*
			*	*
			*	*
			***** 
'''
def pattern():
	for i in range(6):
		for j in range(6):
			if i==0 or j==0 or j==5 or i==5 :
				print("*" ,end = "")
			else:
				print(end = " ")	  
		print()	
pattern()			