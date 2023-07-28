## Automation example

So we've talked about the benefits of *automation* and the things we need to be prepared for. Let's now look at an example of something we can automate using Python. 

    Say for example that you wanted to check the health of your computer. This can call for a lot of different checks, verifying that there is enough disk space, that the processor isn't an overloaded, that it has the latest security updates, and that it's running services it's supposed to. To verify all of this, we need to know how to check each of these values. Of course, we'll do it by using some of the handy modules available to us. 
    
    For example, we can use a **shutil** module and a **disk_usage** function to check the current available disk space. Let's try it out in the interpreter. 
    
* We'll start by importing the **shutil** module, then get the disk_usage.

* Let's print the variable and see what's in it. So we get the total number of bytes on disk, the amount that's used and the amount that's free. 

~~~python
>>> import shutil
>>> du = shutil.disk_usage("/")
>>> print(du)
usage(total=494384795648, used=316858990592, free=177525805056)
>>> 
~~~ 

* We can calculate the percentage of free disk space by dividing the number of bytes free by the total and multiplying that by 100.

~~~python
>>> du.free/du.total*100
35.90842732598873
>>> 
~~~

* **What about cpu_usage?** For this, we can use another module called **psutil**. This includes a **cpu_percent** function that returns a number showing how much of the CPU is being used. The amount of CPU used at each instant can change a lot, since processes are starting and finishing all the time. So this function receives an interval of seconds and returns an average percentage of usage in that interval. 

*  We'll start by importing the **psutil** module.

* Then call the **cpu_percent** function with 0.1 seconds.

~~~python
>>> import psutil
>>> psutil.cpu_percent(0.1)
2.9
>>> psutil.cpu_percent(0.1)
3.0
>>> psutil.cpu_percent(0.1)
2.9
>>> psutil.cpu_percent(0.1)
4.7
>>>
~~~

    > When we're using an interactive interpreter, we can use the arrows in our keyboard to get back the lines that we wrote before. So using the up arrow, let's execute the same line a few times.

As you can see, this can vary a lot. Let's try it with 0.5 seconds.

~~~python
>>> psutil.cpu_percent(0.5)
7.2
>>> psutil.cpu_percent(0.5)
1.8
>>> psutil.cpu_percent(0.5)
3.2
>>> psutil.cpu_percent(0.5)
1.8
>>> psutil.cpu_percent(0.5)
1.8
>>> 
~~~

It's taking longer to finish than previous calls but the numbers are more similar to each other? That's because the function needs to wait for the given time to calculate the average. 

So we've done a bunch of research, now we can write our health checking script. Will kick off with a script that'll do two health checks.

* First, we'll set our script to use the Python interpreter with a **shebang**.

~~~python
#!/usr/bin/env python3
~~~

* We know that we'll use **shutil** and **psutil**, so let's import those two modules.

~~~python
#!/usr/bin/env python3
import shutil
import psutil
~~~

* Let's first define a **check_disk_usage** function that will receive a distant check and return true if there's more than 20 percent free or false if it's less.

~~~python
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
~~~

* Now let's write another function called **check_cpu_usage**. In this case, we'll check the usage for a whole second. We'll say the machine is healthy, it a cpu_usage is less than 75 percent.

~~~python
def check_cpu_usage(disk):
    usage = psutil.cpu_percent(1)
    return usage < 75
~~~

Great, we have our two functions. Let's now add the main body of our script where we'll check if either of those two functions returns false.

~~~python
if not checak_disk_usage("/") or not check_cpu_percent():
    print("ERROR!")
else:
    print("Everything is OK!")
~~~

So here, we're just printing a message that the user will see. We'll improve on the script later on once we've learned better ways of notifying our system administrators. Were almost done. Let's save our script, make it executable, and run it.


~~~python
#!/usr/bin/env python 3
import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage(disk):
    usage = psutil.cpu_percent(1)
    return usage < 75

if not checak_disk_usage("/") or not check_cpu_percent():
    print("ERROR!")
else:
    print("Everything is OK!")
~~~

So there you have it, everything is okay, which seems like a great point to wrap up this exercise. All along this course, we'll explore practical automation examples which you'll be able to apply in your job. As we talk about the additional functionality available, we'll be able to extend our automation knowledge some more and more areas.