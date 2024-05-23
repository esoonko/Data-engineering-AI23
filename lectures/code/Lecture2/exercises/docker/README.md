## Running your own Hello world
This is an intermediate task where you create a dockerfile for a python file.

1. Using your knowledge of dockerfile create a new dockerfile from scratch.
2. Create an image from your dockerfile.
3. Run a container from you dockerfile.

### Help
Create a file called "dockerfile"

Use the following commands:
FROM
WORKDIR
COPY
RUN
COPY
EXPOSE
CMD


### Solution
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]


Other tasks you can try are following:
## BASICS
1. Pull an image hello-world and run it
2. List through your containers, stop them and remove them
3. List through your images, stop them and remove them


