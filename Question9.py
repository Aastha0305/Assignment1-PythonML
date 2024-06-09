def issubstring(mainstring,substring):
    if substring in mainstring:
        return True
    else:
        return False;
    

str1=input("Enter the main string:")
str2=input("Enter the substring to search for:")
if issubstring(str1,str2):
    print("Yes,{} is a substring of {}".format(str2,str1))
else:
    print("No, {} is not a substring of {}".format(str2,str1))