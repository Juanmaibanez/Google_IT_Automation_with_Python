# Study Guide: Strings

This study guide provides a quick-reference summary of what you learned in this lesson and serves as a guide for the upcoming practice quiz. The string readings in this section are great syntax guides to help you on the Strings Practice Quiz.

In the Strings segment, you learned about the parts of a string, string indexing and slicing, creating new strings, string methods and operations, and formatting strings. 


## Knowledge

#### String Operations and Methods
* **.format()** - String method that can be used to concatenate and format strings. 

    * **{:.2f}** - Within the .format() method, limits a floating point variable to 2 decimal places. The number of decimal places can be customized.

* **len(string)** - String operation that returns the length of the string.

* **string[x]** - String operation that accesses the character at index [x] of the string, where indexing starts at zero.

* **string[x:y]** - String operation that accesses a substring starting at index [x] and ending at index [y-1]. If x is omitted, its value defaults to 0. If y is omitted, the value will default to len(string).

* **string.replace(old, new)** - String method that returns a new string where all occurrences of an old substring have been replaced by a new substring.

* **string.lower()** - String method that returns a copy of the string with all lowercase characters.