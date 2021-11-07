'''
Author : Nadim Mansuri.
Date : 02/11/2021.
Purpose : How to print :
			 *   * 
			*  *  *
			*	  *
			 *   *
			   *
'''
def pattern():
	for i in range(6):
		for j in range(7):
			if i==0 and j==1  or i==0 and j==5 or i==1 and j==0 or i==1 and j==3 or i==1 and j==6 or i==2 and j==0 or i==2 and j==6 or i==3 and j==1 or i==3 and j==5 or i==4 and j==2 or i==4 and j==4 or i==5 and j==3:
				print("*" ,end = "")
			else:
				print(end = " ")	  
		print()	
pattern()			