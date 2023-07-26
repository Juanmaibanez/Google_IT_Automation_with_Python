The code below defines an Elevator class. The elevator has a current floor, it also has a top and a bottom floor that are the minimum and maximum floors it can go to. Fill in the blanks to make the elevator go through the floors requested.

```python
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        pass
    def up(self):
        """Makes the elevator go up one floor."""
        pass
    def down(self):
        """Makes the elevator go down one floor."""
        pass
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        pass

elevator = Elevator(-1, 10, 0)
```

To make the elevator go through the floors requested, you need to fill in the blanks in the code. Here's the updated code:

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

elevator = Elevator(-1, 10, 0)

elevator.up()
print(elevator.current)  # should output 1
```

In the updated code, the `__init__` method initializes the elevator instance with the `bottom`, `top`, and `current` floors. The `up` method increments the `current` floor by 1 if it's below the `top` floor. The `down` method decrements the `current` floor by 1 if it's above the `bottom` floor. The `go_to` method sets the `current` floor to the specified `floor` if it's within the valid range. Finally, the `elevator.up()` call and `print(elevator.current)` statement demonstrate the elevator going up one floor and outputting the current floor, which should be 1.

So now:

