![](../imgs/hkbu.png)

# COM7940 Cloud Computing 

## 2020/21 S2 Lab 1 - Python and Git exercise


| | | |
|--|--|--|
| Instructor | Dr. Kevin Wang  | kevinw@comp.hkbu.edu.hk|
| Teaching Assistant | Mr. Zijian Lei | cszjlei@comp.hkbu.edu.hk |



**Objective:**
---
Throughout this lab you will be able to:
1. Practice some basic python syntax and complete some simple programs;
2. Practice some basic git functions/commands like `clone`, `pull`, `commit`, `push`.



---
## Git
## 1. Installation

Install the following software into your machine:
* latest version of [python3](https://www.python.org/downloads/) (e.g. Version 3.9)
* [git](https://git-scm.com/downloads)
* Optionally if you prefer a GUI version: [Git Desktop](https://docs.github.com/en/free-pro-team@latest/desktop/installing-and-configuring-github-desktop) (But we would not teach it)

## 2. Register an account on GitHub

GitHub is (still) considered the largest public repository in the world. It nurtures a large number of software dev communities. You will need to create an account on GitHub. If you have created an account on GitHub before, you should use your old account. A GitHub account can be considered as a CV of a developer. Having multiple accounts does not bring any benefit to you.

After you have applied the account, make sure you also apply for [GitHub Student Developer Pack](https://education.github.com/pack). This will be useful.

## 3. Create a repo and clone it.

In this lab we want you to create a blank the repo named `comp7940-lab1`. 

Then you should `clone` the repo into your local machine. To clone an image, you simply type the following in your terminal (mac) /command prompt (Windows).

```
git clone <your_git_repo> 
```

Your git repo URL may looks like https://www.github.com/peter/comp7940-lab1.git where `peter` is your GitHub account name, `comp7940-lab1` is your repo's name.

To verify you have done it correctly, you should be able to find a new folder called `comp7940-lab1` under your directory. Switch to this directory from your terminal/command prompt by typing:

```
cd comp7940-lab1
```
Then, type 
```
git status
```

You might probably see
```sh
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

## 4. Add and edit a file

Try to add a python file `main.py` under the directory `comp7940-lab1`. Enter the following:

```
def main():
    print("Hello World")

if __name__ == '__main__':
    main()
```

Remember python is very sensitive to indentation. You should use either `tab` or `space` for the indentation **but not mixing both of them at the same time**.

Try to run the file in the terminal by
```
py -m main
```
You should see `Hello World` printed.

Next we are going to add the file into your Git, type:

```
git add main.py
```

Check it by typing `git status`
```
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   main.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        __pycache__/
```

## 5. First Commit

You want to take a "snapshot" of your file system. Do it by 
```
git commit -am "First commit"
```
You will probably see this
```
[main 6d57875] First commit
 1 file changed, 6 insertions(+)
 create mode 100644 a.py
```

Git status again you will see this:
```
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        __pycache__/

nothing added to commit but untracked files present (use "git add" to track)
```

### 6. Push to Github

Type the following to push the content to github

```
git push origin main
```

> Note: we used to name the default branch as `master`. In the chaotic 2020, Github decided to further complicate the world by initiating a renaming process, to rename `master` to `main` as the default branch.

You will probably see this as the output
```
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 342 bytes | 342.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/peter/comp7940-lab1.git
   f510f42..6d57875  main -> main
```

> Double check your result from Github webpage! 

To get familiar with these commands, try to repeat the above steps (Step 4 to 6) several times while you are writing your python code.

---

## Python Exercise

Try to finish the following tasks by adding one or two lines in the program.

### Ex 1
```py
# Find the all factors of x using a loop and the operator % 
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
x = 52633
for i in range(x+1):
  # your code here
```

### Ex 2
```py
# Write a function that prints all factors of the given parameter x
def print_factor(x):
  # your code here
```

### Ex 3
```py
# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]

# your code here
```


---

# No submission for this lab.


