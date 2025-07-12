#simple calculator using python
import os
os.system('cls' if os.name == 'nt'else 'clear') 
print("\033[4;34m SIMPLE CALCULATOR\033[0m") 
from rich import print
print("[bold red]1 for addition\n2 for substraction\n3 for division\n4 for multiplication\n5 for modulus\n[/bold red]")
a=int(input("\033[1;32menter first number:\033[0m"))
b=int(input("\033[1;32menter second number:\033[0m"))
choice = input("\033[1;34m\nENTER YOUR CHOICE (1-5):\033[0m")
print(f"You selected {choice}")

if choice == '1':
    print(f"{a}+{b} = ", a + b)
elif choice == '2':
    print(f"{a}-{b} =",a - b)
elif choice == '3' and b!=0:
    print(f"{a} / {b} = ",a / b)
elif choice == '3' and b == 0:
    print("Error:division by zero is not possible!")
elif choice == '4':
    print(f"{a}*{b} =",a * b)
elif choice == '5':
    print(f"{a}%{b} =",a % b)
else:
    print("Invalid Choice!!!")