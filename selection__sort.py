a=[9,3,8,2,4]
n=len(a)
m=a[0]
pos=0
temp=0

for i in range(0,n-1):
	min=a[i]
	pos=i
	print(i)
	for j in range(i+1,n):
		print(j)
		if a[j]<min:
			min=a[j]
			pos=j

	temp=a[i]
	a[i]=a[pos]
	a[pos]=temp

print(a)
