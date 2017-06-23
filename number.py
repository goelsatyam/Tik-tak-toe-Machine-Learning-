def ones(b,c):
	ans=0
	for i in range(3):
		x=0
		y=0
		x1=0
		y1=0
		for j in range(3):
			if b[i][j]==c:
				x+=1
			if b[j][i]==c:
				y+=1	

			if b[i][j]==0:
				x1+=1
			if b[j][i]==0:
				y1+=1
		
		if x1==2 and x==1:
			ans+=1
		if y1==2 and y==1:
			ans+=1
	x=0
	y=0
	x1=0
	y1=0
	
	for i in range(3):
		if b[2-i][2-i]==c:
			x+=1
		if b[2-i][2-i]==0:
			x1+=1
		if b[i][2-i]==c:
			y+=1
		if b[i][2-i]==0:
   			y1+=1

		
	if x1==2 and x==1:
		ans+=1
	if y1==2 and y==1:
		ans+=1
	return ans		
	

def threes(b,c):
	ans=0
	for i in range(3):
		x=0
		y=0
		for j in range(3):
			if b[i][j]==c:
				x+=1
			if b[j][i]==c:
				y+=1	
		
		if x==3:
			ans+=1
		if y==3:
			ans+=1
	x=0
	y=0
	
	for i in range(3):
		if b[2-i][2-i]==c:
			x+=1
		if b[i][2-i]==c:
			y+=1

		
	if x==3:
		ans+=1
	if y==3:
		ans+=1
	return ans


def twos(b,c):
	ans=0
	for i in range(3):
		x=0
		y=0
		x1=0
		y1=0
		for j in range(3):
			if b[i][j]==c:
				x+=1
			if b[j][i]==c:
				y+=1	

			if b[i][j]==0:
				x1+=1
			if b[j][i]==0:
				y1+=1
		
		if x1==1 and x==2:
			ans+=1
		if y1==1 and y==2:
			ans+=1
	x=0
	y=0
	x1=0
	y1=0
	
	for i in range(3):
		if b[2-i][2-i]==c:
			x+=1
		if b[2-i][2-i]==0:
			x1+=1
		if b[i][2-i]==c:
			y+=1
		if b[i][2-i]==0:
   			y1+=1

		
	if x1==1 and x==2:
		ans+=1
	if y1==1 and y==2:
		ans+=1
	return ans
