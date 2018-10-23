import random 
play='y'
print("LETS PLAY.....:P")
ucount=0
rcount=0
while play=='y':
	item = ['rock','paper','scissors']
	r=random.choice(item)
	print("select any one:rock,paper,scissors")
	u=input(str)
	#ucount=0
	#rcount=0
	print("computer"+"    "+"player")     
	print(r+"       "+u)
	if r=='rock' and u=='paper':
		rcount+=1
		print(rcount,"         ",ucount)
	elif r=='paper' and u=='rock':
		ucount+=1
		print(rcount,"         ",ucount)
	elif r=='rock'	and u=='scissors':
		rcount+=1
		print(rcount,"         ",ucount)
	elif r=='scissors' and u=='rock':
		ucount+=1
		print(rcount,"         ",ucount)
	elif r=='scissors' and u=='paper':
		rcount+=1
		print(rcount,"         ",ucount)
	elif r=='paper' and u=='scissors':
		ucount+=1
		print(rcount,"         ",ucount)
	elif r=='paper' and u=='paper' or r=='rock' and u=='rock' or r=='scissors' and u=='scissors':
		print(rcount,"         ",ucount)
	print("do you want to continue(y/n)")
	play=input()



	

	
