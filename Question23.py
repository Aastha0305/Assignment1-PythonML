def celsius_to_fahrenheit(cel):
    return (cel * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

choice = input("Enter 'C' to convert Celsius to Fahrenheit, or 'F' to convert Fahrenheit to Celsius: ").upper()

if choice == 'C':
    cel = float(input("Enter temperature in Celsius: "))
    f = celsius_to_fahrenheit(cel)
    print("Temperature in Fahrenheit:", f)
elif choice == 'F':
    f = float(input("Enter temperature in Fahrenheit: "))
    cel = fahrenheit_to_celsius(f)
    print("Temperature in Celsius:", cel)
else:
    print("Invalid choice. Please enter 'C' or 'F'.")
