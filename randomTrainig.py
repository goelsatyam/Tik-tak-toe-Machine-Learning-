import random
import sqlite3 as sqlite
from number import twos,threes,ones

db=sqlite.connect('vales.db')
try:
	db.execute('''create table  counts (o1,o2,t1,t2,th1,th2)''')
	db.execute('''insert into counts values (1.0,1.0,1.0,1.0,1.0,1.0)''')	
	db.commit()
except:
	pass			


v=db.execute('''select * from counts ''').fetchone()
my_value=[v[0],v[1],v[2],v[3],v[4],v[5]]
alpha=0.001

def isOver(a):
	'''To check if anyone wins '''
	for i in range(3):
		if a[i][0]!=0 and a[i][0]==a[i][1] and a[i][1]==a[i][2]:
			return 1
		if a[0][i]!=0 and a[0][i]==a[1][i] and a[1][i]==a[2][i]:
			return 1	
	
	if a[0][0]!=0 and a[0][0]==a[1][1] and a[1][1]==a[2][2]:
		return 1
	if a[1][1]!=0 and a[0][2]==a[1][1] and a[1][1]==a[2][0]:
		return 1

	return 0


def calV(a):
	ans=1.0
	for i in range(6):
		ans+=a[i]*my_value[i]
	return ans

def ML(a,v_val,v_train):
	for i in range(6):
		my_value[i]+=alpha*(v_train-v_val)*a[i]
		
def randomMoves(a,b,c):
	''' create random moves'''

	#if matrix is full then return
	if(len(a)==0):
		return 0
		

	#Creating random move
	x=random.randint(0,len(a)-1)
	z=x	
	x=a[x]
	del a[z]
	
	y=int(x/3)	
	b[y][x-y*3]=c
	
	#check does anyone wins
	if isOver(b):
		if c==1:
			return 1
		else:
			return -1
	#Next player moves
	vals=[ones(b,1),ones(b,-1),twos(b,1),twos(b,-1),threes(b,1),threes(b,-1)]
	v_val=calV(vals)

	v_train=randomMoves(a,b,c*-1)

	ML(vals,v_val,v_train)
	return v_val

	
def updateTable():
	db.execute('update counts set o1=%f,o2=%f,t1=%f,t2=%f,th1=%f,th2=%f'%(float(my_value[0]),my_value[1],float(my_value[2]),my_value[3],my_value[4],my_value[5]))
	db.commit()

if __name__=='__main__':
	n=raw_input()
	n=int(n)
	print my_value
	for i in range(n):
		randomMoves([i for i in range(9)],[[0,0,0],[0,0,0],[0,0,0]],1)	
	print my_value

	updateTable()
