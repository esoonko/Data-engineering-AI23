## Docker Compose Task
For this task you will use docker compose.
The python file downloads a csv and populates the target which is a postgres db
Use the database credentials "postgresql://user:password@db:5432/mydatabase"
Also, in your dockerfile use the following command as the code uses uvicorn
```BASH
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### For this task create the following services:
    - A dockerfile for python that creates an image that exposes the service on port 8000
    - A postgres server on postgres:alpine










### Solution:
#### dockerfile
```BASH
# api/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

```

#### docker-compose.yml
```yml
version: '3.8'

services:
  db:
    image: postgres:alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydatabase
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  api:
    build: ./api
    command: uvicorn main:app --host 0.0.0.0 --port 8000
    volumes:
      - ./api:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/mydatabase

volumes:
  postgres_data:
   
```