## Running your own Hello world
This is a python script with a dockerfile for building your own docker image.

### Basic
1. with your terminal in the folder docker 2 use the following command to build the docker image:
```Bash
docker build -t my_app_name .
```
2. where my_app_name is the name of your image.
Run the image with 
```Bash
docker run -p 8000:8000 my_app_name
```
We set a port with 8000 by adding "-p 8000:8000"

3. Navigate to http://localhost:8000

It should say hello world.

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
2. Using your knowledge of dockerfile create a new dockerfile from scratch.
3. Create an image from your dockerfile.
4. Run a container from you dockerfile.