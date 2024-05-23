## Running your own Hello world
This is a python script with a dockerfile for building your own docker image.

### Basic
1. with your terminal in the folder docker 1 use the following command to build the docker image:
```Bash
docker build -t my_app_name .
```
2. where my_app_name is the name of your image.
Run the image with 
```Bash
docker run my_app_name
```

It should say hello world.

To see all containers run
```Bash
docker ps -a
```

To see all images run
```Bash
docker images
```

### Intermediate
1. Delete the dockerfile.
2. Using your knowledge of dockerfile create a new dockerfile from scratch.
3. Create an image from your dockerfile.
4. Run a container from you dockerfile.