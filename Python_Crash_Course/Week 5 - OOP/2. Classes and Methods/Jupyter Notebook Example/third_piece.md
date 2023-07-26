Now add the str method to your Elevator class definition above so that when printing the elevator using the print( ) method, we get the current floor together with a message. For example, in the 5th floor it should say "Current floor: 5"

```python
elevator.go_to(5)
print(elevator)
```

>Remember, Python uses the default method, that prints the position where the object is stored in the computer’s memory. If your output is something like:

><main.Elevator object at 0x7ff6a9ff3fd0>

>Then you will need to add the special str method, which returns the string that you want to print. Try again until you get the desired output, "Current floor: 5".

To add the `__str__` method to the `Elevator` class, you can modify the class definition as follows:

```python
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current

    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < self.top:
            self.current += 1

    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > self.bottom:
            self.current -= 1

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if self.bottom <= floor <= self.top:
            self.current = floor

    def __str__(self):
        """Returns a string representation of the Elevator."""
        return f"Current floor: {self.current}"

elevator = Elevator(-1, 10, 0)

elevator.go_to(5)
print(elevator)
```
    Current floor: 5

In the updated code, the `__str__` method is added to the `Elevator` class. It returns a string representation of the elevator, which includes the current floor. The `print(elevator)` statement then prints the elevator object, which will display the current floor with the message "Current floor: 5" in this case.