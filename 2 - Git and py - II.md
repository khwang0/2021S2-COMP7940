![](../imgs/hkbu.png)

# COM7940 Cloud Computing 

## 2020/21 S2 Lab 2 - More about Python and Git exercise


| | | |
|--|--|--|
| Instructor | Dr. Kevin Wang  | kevinw@comp.hkbu.edu.hk|
| Teaching Assistant | Mr. Zijian Lei | cszjlei@comp.hkbu.edu.hk |


**Objective:**
---
Throughout this lab you will be able to:
1. Practice some more python syntaxes and complete some simple programs;
2. Practice some git operations on conflict resolution and pull request.

---

## Git

In this part we want to create some conflicts on git and try to resolve those conflicts.

You need to prepare two terminals or two different Git UI clients. Let's call them Donald and Joe. Both of them clone from the same remote repo. Make sure you have access to this repo.

## 1. Simple Conflict
Perform the following sequentially. If you forget the commands to perform these steps, please go back to check Lab 1 and lecture 1.

| Donald | | Joe |
|---|---|---|
| create a file A.txt | | |
| stage A.txt & commit | | 
| push to main | |
| | | create a file B.txt |
| | | stage B.txt & commit |
| | | push to main |

This should result in a conflict when you push the code to master from Joe.

Because these two conflicting commit fortunately touch on different files, so it is possible to merge them automatically.

| Donald | | Joe |
|---|---|---|
|  | | Type `git pull origin main` |
|  |  | Type `git log` to check what has happened | 
| Type `git log` and compare it with Joe |  | 
|  |  | push to main |
| pull | | |
| Type `git log` and compare it with Joe again | |

## 2. Manually resolve conflict

Perform the following:
| Donald | | Joe |
|---|---|---|
| Write "Donald" to B.txt | | |
| commit | | 
| push to main | |
| | | Write "Joe" to B.txt |
| | | commit |
| | | push to main |

This should result in a conflict again. 

| Donald | | Joe |
|---|---|---|
|  | | Type `git pull origin main` |
|  |  | Type `git log` to check what has happened | 


This time you will see something like:
```
From https://github.com/khwang0/comp
 * branch            main       -> FETCH_HEAD
   5205117..d411699  main       -> origin/main
Auto-merging B.txt
CONFLICT (content): Merge conflict in B.txt
Automatic merge failed; fix conflicts and then commit the result.
```

In git log you cannot see the merged result. This is because git does not know which version you want to keep. Therefore you need to resolve the conflict on your own.

| Donald | | Joe |
|---|---|---|
|  | | Open B.txt and try to remove the symbols <<< ==== >>> and fix the file |
|  |  | Commit | 
|  |  | push to main again |
| pull | | 
| Type `git log` |  


# 3 Conflict that cannot be resolved manually

Perform the following

| Donald | | Joe |
|---|---|---|
| Add a JPG file a.jpg | | |
| stage a.jpg and commit |
| push |
| | | Add *another* JPG file but still name it a.jpg |
| | | stage a.jpg and commit |
| | | push |
| | | pull and attempt to resolve the conflict |

This will result in a conflict. After `git pull` at Joe, you can confirm that a conflict needs to resolve. But this time the file is a binary file JPG, it cannot be resolved like the TXT file. 

| Donald | | Joe |
|---|---|---|
| | | Type `git reset --hard HEAD~1` | 
| | | pull again to check if it is in Donald version |

This method will give up on the change you have made. The a.jpg you have created will be gone forever. Be careful when you issue this command. This should have resolved the conflict. 

Now try to recreate the conflict and try force push
| Donald | | Joe |
|---|---|---|
| Add a JPG file a.jpg | | |
| stage a.jpg and commit | 
| push |
| | | Add *another* JPG file but still name it a.jpg | 
| | | stage a.jpg and commit | 
| | | Type `git push origin main -f` |
| pull and see what happen | | 


Joe has fixed his problem but leaving Donald in big trouble. That's why force push is strongly discouraged!


<!--py exercise: function with parameter, return value, array, post/get--->

<!-- git: practice commit in two different machines/with different order, create conflict, resolving using push -f, pull, stash, reset, pull request-->

---

## Python

Complete the following code is a bigger program. This program would calls some functions and you need to complete these functions to make it work.

### Ex 
```py
import json
import requests

site="https://api.npoint.io/2b57052af2060e84dc86"

# Your code goes here



# Trying to load JSON into text
r = requests.get(site)
print(r.json())
text = r.json()['users']

# Debug
for i in text:
    print("parse " + str(i))



# call the function convert_number
# convert all elements (except the first one) into number and return it as a list
y = convert_number(text[0]) 

print("y")
print(y)

# call the function replace_number
# replace all number 1 by the number 10 in the function
z = replace_number(number_list = y, being_replace = 1, to_replace = 10)

print("z")
print(z)

sum = 0
for i in z:
    sum = sum + i
    print("sum = " + str(sum) + "; i =" + str(i))
print ("Total = " + str(sum))

```

The expected output is:
```
{'name': 'blogger', 'users': [['admins', '1', '2', '3'], ['editors', '4', '5', '6']]}
parse ['admins', '1', '2', '3']
parse ['editors', '4', '5', '6']
y
[1, 2, 3]
z
[10, 2, 3]
sum = 10; i =10
sum = 12; i =2
sum = 15; i =3
Total = 15
```


---

## Write Up

After doing these two labs, please answer the following questions:

1. What is a conflict in Git? What is the cause of such conflict?
2. How can we resolve a conflict?
3. What practices can be do to avoid having a conflict?
4. What is the purpose of `return` in python?
5. Where can we define a function parameter? How can we use it?
6. Write a function that can reverse a string.