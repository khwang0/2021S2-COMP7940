![](../img/hkbu.png)

# COM7940 Cloud Computing 

## 2020/21 S2 Lab 7 Dockerize


| | | |
|--|--|--|
| Instructor | Dr. Kevin Wang  | kevinw@comp.hkbu.edu.hk|
| Teaching Assistant | Mr. Zijian Lei | cszjlei@comp.hkbu.edu.hk |



**Objective:**
---
Throughout this lab you will be able to:

---

* Create a Docker container for your app.
* Deploy the container to Heroku.

**Introduction:** 
---
Some steps in this lab will not contain detailed instructions. You are supposed to work out those details on your own. Meanwhile, we will show you the steps in details about how it is going to deploy the container to Heroku.

You are advised to refer to the lecture notes 6 and 7 to get familiar with docker commands. Of course, make sure you got Docker installed properly. Make sure you have also signed up in hub.docker.com. 

---
## Part 1: Building a container

### A) Using `docker run`

1. Stop the chatbot service on Heroku through the dashboard. Verify the service is stopped by looking at the log and talking to the chatbot.
2. Run a container from the image `python` in **detached mode**. 
3. Name this container `mycontainer` using `docker rename` if you forget to do it in step 2.
4. Copy your lab6 `chatbot.py`, `requirements.txt` to the container, under the root directory `/`. This can be done via:
   ```sh
   docker cp chatbot.py mycontainer:/
   docker cp requirements.txt mycontainer:/
   ```

5. Execute the following line inside the container
   ```sh
   pip install pip update
   pip install -r requirements.txt
   ```
   You can do it by either launching a new interactive bash shell in the container or execute these command using `docker exec` directly.
6. Commit your image to the name `7940image`.
7. Run the docker container from the image `7940image` by the following command
  
   ```sh
   docker run  --name lab7partA -d --env ACCESS_TOKEN=163... --env HOST="redis-11363.c1..." --env PASSWORD="1nOA..." --env REDISPORT=12345 7990image python chatbot.py
   ```
   Make sure you know how to fill in the values of those `ACCESS_TOKEN`, `HOST`, `PASSWORD` `REDISPORT`. 
8. Check the logs of the container `lab7partA` and test it on telegram again. It should work.
9.  Stop and remove the containers `mycontainer` and `lab7partA`.


### B) Using `Dockerfile`

1. Create a `dockerfile` under the same directory. The `dockerfile` should repeat the steps stated in part A, i.e.
   * Use the image `python`
   * Copy the files `chatbot.py` and `requirements.txt` to the container
   * Install the dependency using the two `pip install` statements.
   * Set the environment variables `ACCESS_TOKEN`, `HOST`, `PASSWORD` `REDISPORT` 
   * Set the ENTRYPOINT and/or CMD correctly so that it will execute `python chatbot.py`
2. Build the image using `docker build -t 7940image2 .`
3. Run the image using `docker run --name lab7partB -d 7940image2`.
4. Check the log of this container and test it with telegram again.

---

## Part 2: Deploy to Heroku as a container

Assume that your container developed in Part 1A is ready, we can push it to heroku via the following commands (replace comp7940chatbot with your heroku app)

```sh
heroku container:push 7940image -a comp7940chatbot  
heroku container:release 7940image -a comp7940chatbot 
```

Make sure you have stopped any running chatbot and have enabled your chatbot.

Notice that the environment variable should have defined in your Heroku app already (see lab5). Therefore, it is not necessary for you to define your environment variable in Dockerfile any more. 

---

# Writeup

Please write down all commands that you have entered for Part 1 and the content of the dockerfile that you have created for Part 1B. You will need to submit those together with the next lab.