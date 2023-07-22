# Coding skills

## Skill Group 1

* Use the assignment operator =  to assign values to variables

* Use basic arithmetic operators with variables to create expressions

* Use explicit conversion to change a data type from float to string

```python
# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests 
 
# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) # change a data type
```

    Each person needs to pay: 27.0

## Skill Group 2

* Output multiple string variables on a single line to form a sentence

* Use the plus (+) connector or a comma to connect strings in a print() function

* Create spaces between variables in  a print() function

```python
# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
 
print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.
 
# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string.
```

    Dr. Prisha Jai Agarwal, Ph.D.
    Dr. Prisha Jai Agarwal , Ph.D.

## Skill Group 3

* Resolve TypeError caused by a data type mismatch issue

* Use an explicit conversion function

```python
print("5 * 3 = " + str(5*3)) 
 
# Resolution: 
# print("5 * 3 = " + str(5*3))
#
# To avoid a type error between the string and the integer within the
# print() function, you can make an explicit data type conversion by
# using the str() function to convert the integer to a string.  
```

    5 * 3 = 15

## Skill Group 4

* Resolve a ZeroDivisionError caused by an attempt to divide by 0

```python
numerator = 7
denominator = 0   # Possible resolution: Change the denominator value 
result = numerator / denominator
print(result)
 
# One possible assumption for a number divided by zero error might
# include the issue of a null value as a denominator (could happen when
# using a loop to iterate over values in a database). In such cases, the
# desired outcome may be to leave the numerator value intact. The
# numerator value can be preserved by reassigning the denominator with 
# the integer value of 1. The result would then equal the numerator.
```

    Error on line 3:
    result = numerator / denominator
    ZeroDivisionError: division by zero

```python
numerator = 7
denominator = 1 
result = numerator / denominator
print(result)
```

    7.0
