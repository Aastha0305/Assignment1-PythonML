def fib(n):
    fib_seq=[]
    a,b=0,1
    for i in range(n):
        fib_seq.append(a)
        a,b=b,a+b
    return fib_seq

num=int(input("Enter a number"))

print(fib(num))