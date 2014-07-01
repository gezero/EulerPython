EulerPython
===========
Here are my Project Euler solutions in Python. The purpouse of the project is to try the Python language... Why is Python so popular? I do not know. But I wanna find out for myself. I decided to take the Project Euler problems and try to learn Python when solving them. Project Euler was hacked recently so they do not allow to check the solutions. After they will fix the site I will fix potential issues in the commited code. I have already solved around 70 of the problems few years back so solving them once more time should be easier. Usually I develop stuff in Java and I also like Ruby language. Im trying this on my notebook, it has W8.1. I am developing in Sublime Text and compiling using Python 3. I did not use Python before this project. I heard about Python before and saw some code.

Diary
=====
Day 1
-----
Ok, I choosed Python 3 as its said on the pages that Python 2 is legacy. It is strange that python executable has diffent mode when you run it without arguments and when you run it to run a program. It took me some time to figure this out. At the end I ended with finally buying a Sublime Text licence so that I can try it out Sublime Text well. I set up the Python3 build system, Python needed to be in path for it to work. Now I press ctrl+b and I see output of the Python program. 

Problem one is easy one. I learned how to create *function*, how to do a simple *for* cycle, *if* statement and *printing*.
Day 2
-----
Problem two is easy as well. Nothing to think about here, simple cycle will do. I learned how to do *while* cycle.
Day 3
-----
Finaly some playing with primes in problem three. As I remember from few years back, there will be a lot of prime problems ahead of me, so I created the Sieve of Eratosthenes function. It probably is somewhere in Python ecosystem already, but I am not that far yet. This is the first time I used *import* to successfully import math module. I learned how to print *last element of array*.
Day 4
-----
Problem four let me play with *converting int to string* as well as *reversing the string*.
Day 5
-----
Ok, so I will need the sieve I created on Day 3 again. Time to create *my own module*. It took me some time to find out how exactly call the methods from my imported module. At the end it is of course trivial - name_of_module.name_of_method. I will leave the old code in problem3.py for historical purposes even though it should be refactored. It is also the first time i am working with *set*. The solution of the fifth problem that I have chosen could be probably improved, but I am not here for the perfection. 
Day 6
-----
Problem six is not interesting at all. Easy solution, nothing to learn here.
Day 7
-----
This problem probably wants us to finally create the sieve. I already have it, so again easy solution not much to learn here. 
Day 8
-----
I decided to version the progress. I created github repository and put the code inside. In problem eight I was practicing how to *work with characters of a string* and convert *string to integer*. To be honest I do not like the global methods - `len`, `str`, `int`. I am used to have this methods on my objects from ruby - size/lenght is attribute of an object why is len a global function?
Day 9
-----
I had a chance to *sort an array* in Python when solving problem nine. I was again surprised that the `sorted` method flies in the air in global namespace. From the [list of build in functions](https://docs.python.org/3/library/functions.html) I also learned that the `range` function that I used in the `for` cycles is also a global function. It is obvious of course.  
Day 10
------
Another easy problem if you already have the sieve.
Day 11
------
I have learned how to *initialize array of arrays*. Also I learned that Python does not like number 04.
Day 12
------
I decided to create the diary because I learned a lot today. The notes from before this one are aproximations of what I remember. 

I found out that just simple counting factors is not enought for problem twelve. So I created another method that is returning *dictionary* structure that contains full factorization of a number. I discovered how to *raise an Error* when debuging the method. I was also playing with the map function but decided to give up for now and return to it later. I refactored the primes library to store the calculated sieve in cache variable. I found out that two leading underscores should make a variable private inside a module. I needed to refactor problem5.py so that it is still runable.
Day 13
------
Problem thirteen is targeting languages where integers can easily overflow. Python is not such a language. I learned that summing an array can be done using the global function `sum`.
Day 14
------
Today I learned how to use the ternary if else operator in Python. Somehow I find it strange that the same operator does not seem to work without the else part. I would enjoy writing `return x if condition` when handling special cases. I also read about how to write the ternary operator in old Python - `(lambda a, lambda b)[a>b]`. Today I also used Python syntax for my benefit for the first time when debuging the solution. Deciding between printing intermediate solutions or printing just a final solution was just moving the printing code with tabs back and forth.  