string="hello"
def foo(string,n):
	print string*n
def my_fun(string,foo,n):
	foo(string,n)
my_fun(string,foo,5)