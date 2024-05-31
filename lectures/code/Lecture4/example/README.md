## Data Pipeline and Data Transformation
Here are the codes for our data pipeline, data storage and data transformation we did.
- Data pipeline is in the ingestion folder
- Data Storage is the database folder. Use raw__weatherapp.sql to instantialize the raw layer.
- Data transformation is in the database folder in clean__weatherapp.sql.

## How to run
### Database
1. First create an .env file and copy everything from .env.example into .env
2. Navigate to database and start the service through
```docker compose up --build -d```
3. Connect to http://localhost:8080 to login to adminer with credentials from .env. Remember to set database to Postgres and server to db
4. Copy the SQL code from raw__weatherapp.sql in "Run SQL" to instantiate raw layer.

### CREATE DOCKER NETWORK (Only for this example)
1. Create a docker network through ```docker network create ai23network```

### Data ingestion pipeline
1. First create an .env file and copy everything from .env.example into .env
2. Navigate to ingestion and build the docker image through
```docker build -t ingestion ./src```
3. Start the service through
```docker run --network=ai23network -p 8000:8000 ingestion```
4. Run api requests through address http://localhost:8000/ingestion?ocation=LOCATION&date=DATE where LOCATION can be the location you want (STOCKHOLM) and Date should be in the format 2024-05-30

### Data transformation layer
1. Copy the SQL code from clean__weatherapp.sql and run it in adminer(http://localhost:8080)