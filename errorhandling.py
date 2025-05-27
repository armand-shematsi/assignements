# write a program that handles errors, the program should ask for two number using input, and then
# divide them, use an infinite loop to keep asking until a valid input is provide

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero second number.")
        continue
    else:
        print(f"Result: {result}")
        break
