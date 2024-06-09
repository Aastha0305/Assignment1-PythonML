def sum_digits(n):
    ans=0
    while(n!= 0):
        ans+=(n%10)
        n=n//10
    return ans
num=int(input("Enter a number whose sum of digits you want to calculate"))
print(sum_digits(num))