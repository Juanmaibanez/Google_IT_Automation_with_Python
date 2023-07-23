# Study Guide: Week 3

## Knowledge

#### Terms

* **variables** - Know how to properly initialize or increment a variable. You will also need to recognize a coding error due to the failure to properly initialize or increment a variable.

* **infinite** loops - Know how to recognize infinite loops and use common solutions to prevent them. For example, check loop conditions, ranges, iterators, control statements, etc. to ensure that at least one of these controls are in place to prevent an infinite loop.

* **iterators** - Know the various options available for iterating a variable (e.g., using assignment operators, using the third range() function parameter). You will also need to analyze where the iteration should occur. A misplaced iterator could produce the wrong output or create an infinite loop.  

* **control statements** - Know how and when to use the **break** and **continue** control statements to prevent infinite loops.  


#### Common Functions

* **range() Function Parameters** - Know the roles of the three possible **range(x, y, z)** function parameters:

    * **x** Start of Range (included)

    * **y** End of Range (excluded index) 

        * To include the end of range index, use the expression **y+1**

        * The end of range must be included in the **range()** parameters.

* **z** Incremental value

* **Example 1:** range(4, 12 **+1**, **2**)

    * This example creates a range that starts at 4 and ends at 12 (without the **+1*+, the range would end at 11). 

    * The third parameter increments the range iteration by 2, as opposed to the default increment of 1. The **range(4, 12+1, 2)** expression would produce the values: 4, 6, 8, 10, 12 

* **Example 2:** range(10, 2 **-1**, **-2**)

    * This example creates a range that starts at 10 and ends at 2 **-1**, with a decremental value of **-2**. When counting down, to include the value of the end of the range index, use -1 (end of range minus 1). This range produces the sequence: 10, 8, 6, 4, 2 


* **print() Function Default Behavior** - Know the default behavior of the **print()** function is to insert a new line character after the print statement runs.

    * To override the insertion of the new line character and replace it with a space, add **end=" "** as the last item in the **print()** parameters. This makes it possible to add the next print output to the same line, separated by a space. You might use this technique when a print() function is part of a **for** or **while loop**. Example syntax:  **print(x+1, end=" ")**

