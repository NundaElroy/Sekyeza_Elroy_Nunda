# Assignment Two: Division with error handling

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
        break
        
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error! Cannot divide by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")