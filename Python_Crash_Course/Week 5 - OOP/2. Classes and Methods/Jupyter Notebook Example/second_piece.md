Once you've made the above methods output 1, 0 and 10, you've successfully coded the Elevator class and its methods. Great work!

For the up and down methods, did you take into account the top and bottom floors? Keep in mind that the elevator shouldn't go above the top floor or below the bottom floor. To check that out, try the code below and verify if it's working as expected. If it's not, then go back and modify the methods so that this code behaves correctly.

```python
# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1
```

Apologies for the oversight. You're right, the `up` and `down` methods should take into account the top and bottom floors. Here's the modified code that ensures the elevator doesn't go above the top floor or below the bottom floor:

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

elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current)  # should be 9

elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current)  # should be 1
```

Now, the `up` method checks if the current floor is less than the top floor before incrementing it. Similarly, the `down` method checks if the current floor is greater than the bottom floor before decrementing it. The `go_to` method ensures that the specified floor is within the valid range before setting the current floor. The additional code you provided now correctly outputs 9 and 1, as expected.