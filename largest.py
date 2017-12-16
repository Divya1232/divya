a=34
b=44
c=87
if(a>=b)and(a>=c):
	largest=a
if(b>=a)and(b>=c):
	largest=b
else:
	largest=c
print("The largest number between",a,",",b,"and",c,"is",largest)