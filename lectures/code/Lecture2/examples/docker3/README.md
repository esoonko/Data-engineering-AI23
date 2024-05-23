## Running your own Hello world
This is a python script with a dockerfile for building your own docker image.

### Basic
1. with your terminal in the folder docker 3 use the following command to build docker:
```Bash
docker compose up
```

3. Navigate to http://localhost:8000

It should say Users: user1, user2, user3

To see all containers run
```Bash
docker ps -a
```

To stop containers run
```Bash
docker stop CONTAINER_ID
```

To remove containers run
```Bash
docker rm CONTAINER_ID
```

To see all images run
```Bash
docker images
```

To remove images run
```Bash
docker rmi IMAGE_NAME
```

### Intermediate
1. Delete the dockerfile.
2. Delete docker-compose.yml
3. Using your knowledge of dockerfile create a new dockerfile and docker-compose.yml from scratch.
4. Run docker compose up or docker compose up --build