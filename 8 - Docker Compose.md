![](../img/hkbu.png)

# COM7940 Cloud Computing 

## 2020/21 S2 Lab 8 Docker Compose


| | | |
|--|--|--|
| Instructor | Dr. Kevin Wang  | kevinw@comp.hkbu.edu.hk|
| Teaching Assistant | Mr. Zijian Lei | cszjlei@comp.hkbu.edu.hk |



**Objective:**
---
Throughout this lab you will be able to:

---

* Create a multiple containers service using docker compose.


**Introduction:** 
---
First we are going to use docker-compose to starts your application at local host again. Make sure you are turning off your application on Heroku. In the second part of this lab we will be using our own Redis server instead of the one on Redislab.  

Again, you need to work out the details in some steps.

You are advised to refer to the lecture notes 6 and 7 to get familiar with docker commands. Of course, make sure you got Docker installed properly. Make sure you have also signed up in hub.docker.com. 



---
## Part 1: Your first compose

You are given the following template for your applications. Create the file `part1.yaml` with the following content:

```yaml
version: '3'
services:
  chatbot:
    build: .
```

You should be able to build an image from the `dockerfile` that you have written in Lab 7.

If you think you are ready, you can type the following to run the container:
```
docker-compose -f part1.yaml up
```
It should be equivalent to `docker run --name lab7partB -d 7940image2` that you have typed in lab7.

Please check the command `/add hello` in this step to verify that your redis is working. If it is good, take it down by 
```
docker-compose -f part1.yaml down
```

## Part 2: Something little more

Next, you are going to do the similar things but with the image that you have created in Lab7 part A. The major differences are that the image that you have created in Lab7 part A does not include the environment variables of `HOST`, `PASSWORD`, `REDISPORT`, and `ACCESS_TOKEN` and does not include a correct entrypoint. You will need to spell them out explicitly in the yaml file. Prepare another yaml file `part2.yaml` as follows:

```yaml
version: '3'
services:
  chatbot:
    image: 7940image
    # missing instructions for setting environment variable
    # missing instructions for setting the entrypoint and/or command
```

If you think you are ready, you can type the following to run the container:
```
docker-compose -f part2.yaml up -d
```

You can view the log by `docker-compose logs chatbot`. You can also view the status of your docker by `docker-compose ps`.

Please check the command `/add hello` in this step to verify that your redis is working. If it is good, take it down by 
```
docker-compose -f part2.yaml down
```

---

## Part 3: Adding Redis here

Next we are going to introduce an additional container `redis`. Create a yaml file `part3.yaml` as follows:

```yaml
version: '3'
services:
  chatbot:
    image: 7940image
    # missing instructions for setting environment variable
    # missing instructions for setting the entrypoint and/or command
    depends_on:
      - redis
  redis:
    image: redis
    volumes:
       - ./redis.conf:/usr/local/etc/redis/redis.conf
    command: ["/usr/local/etc/redis/redis.conf"]
```

Add a file `redis.conf` under your directory. This file should contains the following:

```conf
user default on +@all ~*  >comp7940passwordlab8
bind * -::*
protected-mode yes
port 6379
dbfilename dump.rdb
dir ./
```

The file `redis.conf` is a configuration file that tells does some setup in Redis. Now because we are running our own redis server, so you need to change the redis hostname, password, and port to the following:
```conf
HOST=redis
PASSWORD=comp7940passwordlab8
REDISPORT=6379
```
These values should be reflected in `part3.yaml` directly.

You can again start the process by
```
docker-compose -f part3.yaml up
```



Please check the command `/add hello` in this step to verify that your redis is working. If it is good, take it down by 
```
docker-compose -f part3.yaml up
```


---

# Writeup

1. Explain each of the instruction that you have typed in Lab 7 part A by one to two sentences.
2. Paste the dockerfile that you have in Lab 7 part B.
3. Explain the differences between your `part1.yaml` and `part2.yaml` that you have done in Lab 8.
4. What are the differences between the commands `docker ps` and `docker-compose ps`? 
5. (*) When you take down the `redis` service you have created in part 3, say using `docker-compose down`, would that also destroys the data? Why or why not?
