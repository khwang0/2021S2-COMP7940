![](../imgs/hkbu.png)

# COM7940 Cloud Computing 

## 2020/21 S2 Lab 6 Git action


| | | |
|--|--|--|
| Instructor | Dr. Kevin Wang  | kevinw@comp.hkbu.edu.hk|
| Teaching Assistant | Mr. Zijian Lei | cszjlei@comp.hkbu.edu.hk |



**Objective:**
---
Throughout this lab you will be able to:

---

* Create a GitHub Action and use it in a workflow

**Introduction:** 
---
GitHub Actions help you automate tasks within your software development life cycle. GitHub Actions are event-driven, meaning that you can run a series of commands after a specified event has occurred. For example, every time someone creates a pull request for a repository, you can automatically run a command that executes a software testing script.

### **The components of GitHub Actions**

---

Below is a list of the multiple GitHub Actions components that work together to run jobs. You can see how these components interact with each other.

![Component and service overview](https://docs.github.com/assets/images/help/images/overview-actions-design.png)

> #### [Workflows](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions#workflows)
>
> The workflow is an automated procedure that you add to your repository. Workflows are made up of one or more jobs and can be scheduled or triggered by an event. The workflow can be used to build, test, package, release, or deploy a project on GitHub.
>
> #### [Events](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions#events)
>
> An event is a specific activity that triggers a workflow. For example, activity can originate from GitHub when someone pushes a commit to a repository or when an issue or pull request is created. You can also use the [repository dispatch webhook](https://docs.github.com/en/rest/reference/repos#create-a-repository-dispatch-event) to trigger a workflow when an external event occurs. For a complete list of events that can be used to trigger workflows, see [Events that trigger workflows](https://docs.github.com/en/actions/reference/events-that-trigger-workflows).
>
> #### [Jobs](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions#jobs)
>
> A job is a set of steps that execute on the same runner. By default, a workflow with multiple jobs will run those jobs in parallel. You can also configure a workflow to run jobs sequentially. 
>
> #### [Steps](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions#steps)
>
> A step is an individual task that can run commands in a job. A step can be either an *action* or a shell command. Each step in a job executes on the same runner, allowing the actions in that job to share data with each other.
>
> #### [Actions](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions#actions)
>
> *Actions* are standalone commands that are combined into *steps* to create a *job*. Actions are the smallest portable building block of a workflow. You can create your own actions, or use actions created by the GitHub community. To use an action in a workflow, you must include it as a step.
>
> #### [Runners](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions#runners)
>
> A runner is a server that has the [GitHub Actions runner application](https://github.com/actions/runner) installed. You can use a runner hosted by GitHub, or you can host your own. A runner listens for available jobs, runs one job at a time, and reports the progress, logs, and results back to GitHub. 





### **Create an example workflow**

---

GitHub Actions uses YAML syntax to define the events, jobs, and steps. These YAML files are stored in your code repository, in a directory called `.github/workflows`.

You can create an example workflow in your repository that automatically triggers a series of commands whenever code is pushed. In this workflow, GitHub Actions checks out the pushed code, installs the software dependencies, and runs `bats -v`.

1. In your repository, create the `.github/workflows/` directory to store your workflow files.

2. In the

    

   ```
   .github/workflows/
   ```

    

   directory, create a new file called

    

   ```
   learn-git-actions.yml
   ```

    

   and add the following code.

   ```yaml
   name: learn-github-actions
   on: [push]
   jobs:
     check-bats-version:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         - uses: actions/setup-node@v1
         - run: npm install -g bats
         - run: bats -v
   ```

3. Commit these changes and push them to your GitHub repository.

Your new GitHub Actions workflow file is now installed in your repository and will run automatically each time someone pushes a change to the repository. 

### **Understanding the workflow file**

---

To help you understand how YAML syntax is used to create a workflow file, this section explains each line of the introduction's example:

| `name: learn-github-actions`        | *Optional* - The name of the workflow as it will appear in the Actions tab of the GitHub repository. |
| ----------------------------------- | ------------------------------------------------------------ |
| `on: [push]`                        | Specify the event that automatically triggers the workflow file. This example uses the `push` event, so that the jobs run every time someone pushes a change to the repository. You can set up the workflow to only run on certain branches, paths, or tags. For syntax examples including or excluding branches, paths, or tags, see ["Workflow syntax for GitHub Actions."](https://docs.github.com/actions/reference/workflow-syntax-for-github-actions#onpushpull_requestpaths) |
| `jobs:`                             | Groups together all the jobs that run in the `learn-github-actions` workflow file. |
| `check-bats-version:`               | Defines the name of the `check-bats-version` job stored within the `jobs` section. |
| `  runs-on: ubuntu-latest`          | Configures the job to run on an Ubuntu Linux runner. This means that the job will execute on a fresh virtual machine hosted by GitHub. For syntax examples using other runners, see ["Workflow syntax for GitHub Actions."](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idruns-on) |
| `  steps:`                          | Groups together all the steps that run in the `check-bats-version` job. Each item nested under this section is a separate action or shell command. |
| `    - uses: actions/checkout@v2`   | The `uses` keyword tells the job to retrieve `v2` of the community action named `actions/checkout@v2`. This is an action that checks out your repository and downloads it to the runner, allowing you to run actions against your code (such as testing tools). You must use the checkout action any time your workflow will run against the repository's code or you are using an action defined in the repository. |
| `    - uses: actions/setup-node@v1` | This action installs the `node` software package on the runner, giving you access to the `npm` command. |
| `    - run: npm install -g bats`    | The `run` keyword tells the job to execute a command on the runner. In this case, you are using `npm` to install the `bats` software testing package. |
| `    - run: bats -v`                | Finally, you'll run the `bats` command with a parameter that outputs the software version. |

#### [Visualizing the workflow file](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions#visualizing-the-workflow-file)

In this diagram, you can see the workflow file you just created and how the GitHub Actions components are organized in a hierarchy. Each step executes a single action or shell command. Steps 1 and 2 use prebuilt community actions. Steps 3 and 4 run shell commands directly on the runner. To find more prebuilt actions for your workflows, see "[Finding and customizing actions](https://docs.github.com/en/actions/learn-github-actions/finding-and-customizing-actions)."

![Workflow overview](https://docs.github.com/assets/images/help/images/overview-actions-event.png)

### [Viewing the job's activity](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions#viewing-the-jobs-activity)

Once your job has started running, you can see a visualization graph of the run's progress and view each step's activity on GitHub.

1. On GitHub, navigate to the main page of the repository.

2. Under your repository name, click **Actions**.

   ![Navigate to repository](https://docs.github.com/assets/images/help/images/learn-github-actions-repository.png)

   

3. In the left sidebar, click the workflow you want to see.

   ![Screenshot of workflow results](https://docs.github.com/assets/images/help/images/learn-github-actions-workflow.png)

   

4. Under "Workflow runs", click the name of the run you want to see.

   ![Screenshot of workflow runs](https://docs.github.com/assets/images/help/images/learn-github-actions-run.png)

   

5. Under **Jobs** or in the visualization graph, click the job you want to see.

   ![Select job](https://docs.github.com/assets/images/help/images/overview-actions-result-navigate.png)

   

6. View the results of each step.

   ![Screenshot of workflow run details](https://docs.github.com/assets/images/help/images/overview-actions-result-updated-2.png)

