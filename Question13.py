from datetime import datetime

def _age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

birth_year = int(input("Enter your birth year: "))
age = _age(birth_year)
print("You are {} years old.".format(age))