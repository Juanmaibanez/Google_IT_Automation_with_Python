# Study Guide: while Loops 

In the **while** Loops segment, you learned about the logical structure and syntax of **while** loops. You also learned about the importance of initializing variables and how to resolve infinite **while** loops with the **break** keyword.  


## While Loopsç

A **while** loop executes the body of the loop while a specified condition remains True. They are commonly used when there’s an unknown number of operations to be performed, and a condition needs to be checked at each iteration.

Syntax:

```python
while specified condition is True:
    body of loop
```

Example while loop:

```python
multiplier = 1
result = multiplier*5
while result <= 50:
  print(result)
  multiplier += 1
  result = multiplier*5
print("Done")

# This while loop prints the multiples of 5 between 1 and 50. The
# "multiplier" variable is initialized with the starting value of 1. 
# The "result" variable is initialized with the value of the 
# "multiplier" variable times 5. 
 
# The while loop specifies that the loop must iterate while it is True 
# that the "result" is less than or equal to 50. Within the while loop, 
# the code tells the Python interpreter to print the value of the 
# "result" variable. Then, the "multiplier" is incremented by 1 and the
# "result" is assigned the new value of the "multiplier" times 5. 
 
# The end of the while loop is indicated by the indentation of the next 
# line of code moving one tab to the left. At this point, the Python
# interpreter automatically loops back to the beginning of the while
# loop to check the condition again with the new value of the "result"
# variable. When the while loop condition becomes False (meaning
# "result" is no longer less than or equal to 50), the interpreter exits
# the loop and reads the next line of code outside of the loop. In this 
# case, that next line tells the interpreter to print the string "Done". 
 
# Click the "Run" button to check the result of this while loop.  
```

    5
    10
    15
    20
    25
    30
    35
    40
    45
    50
    Done


**Common Errors in while Loops**

If you get an error message on a loop or it appears to hang, your debugging checklist should include the following checks:

* **Failure to initialize variables**. Make sure all the variables used in the loop’s condition are initialized before the loop.

* **Unintended infinite loops**. Make sure that the body of the loop modifies the variables used in the condition, so that the loop will eventually end for all possible values of the variables. You can often prevent an infinite loop by using the **break** keyword or by adding end criteria to the condition part of the **while** loop.

 

**while Loop Terms**

* **while loop** - Tells the computer to execute a set of instructions while a specified condition is True. In other words, **while** loops keep executing the same group of instructions until the condition becomes False.

* **infinite loop** - Missing a method for exiting the loop, causing the loop to run forever.

* **break** - A keyword that can be used to end a loop at a specific point. 

 

## Math Concepts on the Practice Quiz

The coding problems on the upcoming practice quiz will involve a few math concepts. Don’t worry if you are rusty on math. You will have plenty of support with these concepts on the quiz. The following is a quick overview of the math terms you will encounter on the quiz:  

* **prime numbers** - Integers that have only two factors, which are the number itself multiplied by 1. The lowest prime number is 2.

* **prime factors** - Prime numbers that are factors of an integer. For example, the prime numbers 2 and 5 are the prime factors of the number 10 (2x5=10). The prime factors of an integer will not produce a remainder when used to divide that integer. 

* **divisor** - A number (denominator) that is used to divide another number (numerator). For example, if the number 10 is divided by 5, the number 5 is the divisor.

* **sum of all divisors of a number** - The result of adding all of the divisors of a number together.  

* **multiplication table** - An integer multiplied by a series of numbers and their results formatted as a table or a list. For example:

                 
        4x1=4
        4x2=8
        4x3=12
        4x4=16
        4x5=20


