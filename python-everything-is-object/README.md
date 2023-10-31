0. What function would you use to print the type of an object?
a = 50
print(type(a))

1. How do you get the variable identifier (which is the memory address in the CPython implementation)?
a = 50
print(id(a))

2. In the following code, do a and b point to the same object?
a = 89
b = 100
No. Values assigned to variables point to new objects and integers are immutable.

3. In the following code, do a and b point to the same object?
a = 89
b = 89
Yes, a and b point to the same object.

4. In the following code, do a and b point to the same object?
a = 89
b = a
a and b point to the same object

5. In the following code, do a and b point to the same object?
>>> a = 89
>>> b = a + 1
a and b are 2 different objects

6. What does this print?
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
True

7. What does this print?
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
True


8. What does this print?
s1 = "Best School"
s2 = "Best School"
print(s1 == s2)
True

9. What does this print?
s1 = "Best School"
s2 = "Best School"
print(s1 is s2)
True


10. What does this print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
True


11. What does this print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
False

12. What does this print?
l1 = [1, 2, 3]
l2 = l1
print(l1 == l2)


13. What does this print?
l1 = [1, 2, 3]
l2 = l1
print(l1 is l2)
True


14. What does this print?
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
[1, 2, 3, 4]


15. What does this print?
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
[1, 2, 3]


16. What does this print?
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
It prints 1 

17. What does this print?
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
It prints [1, 2, 3, 4] the updated list

18. What does this print?
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
It prints the original value of l1

19. What would these lines print?
dict_ = {"WebDriver": "Camp"}
dict_copy = dict_
print(dict_ == dict_copy)
print(dict_ is dict_copy)

dict_copy = dict_.copy()
print(dict_ == dict_copy)
print(dict_ is dict_copy)
 
True - both dictionaries are equal
True - both point same object
True - variables are equal
False- dict_copy is a different object


19. What would these lines print?
list_ = [1, 2, 3, 4, 5]
list_copy = list_
print(list_ == list_copy)
print(list_ is list_copy)

list_copy = list_.copy()
print(list_ == list_copy)
print(list_ is list_copy)  

True - both are equal
True - both point to same object
True - variables are equal
False- object are not same after being copied

20. Tuple or not?
a = () - it is a tuple


21. Tuple or not?
a = (1, 2) - it is a tuple


22. Tuple or not?
a = (1) - it is not a tuple because of missing ,


23. Tuple or not
a = (1, )
b = 1,
Both are tuple as only , defines the tuple not paranthesis

24. What does this script print?
a = (1)
b = (1)
a is b

It checks whether they point the same object. As integers they are same



25. What does this script print?
a = (1, 2)
b = (1, 2)
a is b
As tuple they are same and points the same object.


26. What does this print?
a = ()
b = ()
a is b
Both empty tuple variable points the same object


27. What does this print?
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)

Prints a new set of code with id(a) as the list a is updated


28. What does this print?
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)

Prints the same code on id(a) as no new object created

