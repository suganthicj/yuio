x11,y11=map(int,input().split())
for p in range(0,1000):
	if y11**p==x11:
		flag=0
		break
	else:
		flag=1
if flag==0:
	print("yes")
else:
	print("no")
