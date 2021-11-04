'''
Author : Nadim Mansuri.
Date : 02/11/2021.
Purpose : Purpose of this function , Print Pattern:
					     *
					    **
					   ***
					  ****
					 *****    
'''
def Pattern():
	for i in range(1,6):
		print(" "*(6-i) + "*"*i)
Pattern()		