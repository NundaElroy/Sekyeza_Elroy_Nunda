from multipledispatch import dispatch

#Example 1
class AreaCalculator:
    
    @dispatch(float)  # Circle: radius only
    def area(self, radius):
        print("Circle area:", 3.14 * radius * radius)

    @dispatch(float, float)  # Rectangle: length and breadth
    def area(self, length, breadth):
        print("Rectangle area:", length * breadth)

# Using the class
calc = AreaCalculator()
calc.area(5.0)           # Circle
calc.area(4.0, 6.0)      # Rectangle

#Example 2 
class DiscountCalculator:
    def calculate(self, price, quantity=1):
        if quantity == 1:
            print("Flat 5% discount:", price * 0.05)
        else:
            print("Bulk 10% discount:", price * quantity * 0.10)

# Using the class
disc = DiscountCalculator()
disc.calculate(100)        # Single item
disc.calculate(100, 5)     # Bulk

