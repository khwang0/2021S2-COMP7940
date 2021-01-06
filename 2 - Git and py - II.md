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



<!--py exercise: function with parameter, return value, array, post/get--->

<!-- git: practice commit in two different machines/with different order, create conflict, resolving using push -f, pull, stash, reset, pull request-->

---

## Write Up

After doing these two labs, please answer the following questions:

1. What is a conflict in Git? What is the cause of such conflict?
2. How can we resolve a conflict?
3. What practices can be do to avoid having a conflict?
4. What is the purpose of `return` in python?
5. Where can we define a function parameter? How can we use it?
6. Write a function that can reverse a string.