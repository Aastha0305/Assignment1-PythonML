
def getminmax(numbers):
    minvalue=maxvalue=numbers[0]
    for i in numbers:
        minvalue=min(minvalue,i)
        maxvalue=max(maxvalue,i)
    return minvalue,maxvalue

numbers=[int(x) for x in input("Enter space separated numbers for the list").split()]
ans1,ans2=getminmax(numbers)
print("The min no. is {} and the max no. is {}".format(ans1,ans2))