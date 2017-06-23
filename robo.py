import random
import randomTrainig 
import sqlite3
from number import ones,twos,threes

db=sqlite3.connect('vales.db')
v=db.execute('''select * from counts ''').fetchone()
my_value=[v[0],v[1],v[2],v[3],v[4],v[5]]

def printMatrix(a):
	'''Print the matrix after each player turn '''
	for i in range(0,3):
		print a[i][0],
		for j in range(1,3):
			print ' | ',
			print " %c "%a[i][j],
		print "\n"	

def convert(a):
	'''convet matrix(x,_,o) to matrix(1,0,-1) '''
	ans=[[0,0,0],[0,0,0],[0,0,0]]
	for i in range(3):
		for j in range(3):
			if a[i][j]=='x':
				ans[i][j]=1
			elif a[i][j]=='o':
				ans[i][j]=-1
	return ans


def nextMove(b):
	''' calculate value for each next move player can take '''	
	o1=ones(b,1)
	o2=ones(b,-1)
	t1=twos(b,1)
	t2=twos(b,-1)
	th1=threes(b,1)
	th2=threes(b,-1)

	ans=9.0+my_value[0]*o1+my_value[1]*o2+my_value[2]*t1+my_value[3]*t2
	return ans

if __name__=='__main__':
	while True:
		a=raw_input('want to start Game (enter "y")')
		if a=='y' or a=='Y':
			pass
		else:
			break
		
		matrix=[['_','_','_'],['_','_','_'],['_','_','_']]
		
		move=1
		count=-1
		while True:
			printMatrix(matrix)
			print "\n\n"
			if randomTrainig.isOver(convert(matrix)):
				if move==-1:
					print "Machine learning wins"
				else:
					print "Player wins"
				break
			count+=1

			if count==9:
				print 'Match is Drawn'
				break

			if move==-1:
				while True:
					a=raw_input('enter valid block')
					a=int(a)
					x=int(a/3)	
					if matrix[x][a-3*x]=='_':
						matrix[x][a-3*x]='o'
						break		
			else:
				flag=0
				x=None
				y=None
				ans1=-99999999999999.0
				for i in range(3):
					for j in range(3):
						
						if matrix[i][j]=='_':
							matrix[i][j]='x'
							if threes(convert(matrix),1)>0:
								x,y=i,j
								flag=1
								break
							val=nextMove(convert(matrix))
							matrix[i][j]='_'	
							if val>ans1:
								ans1=val
								x,y=i,j
					if flag==1:
						break
				#print ans1
				matrix[x][y]='x'
			move*=-1	
