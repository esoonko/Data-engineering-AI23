import os
import requests
import json
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import pendulum
from google.cloud import bigquery

app = FastAPI()
load_dotenv()

#This function fetches the weather data
def fetch_weather_data(api_url, api_key, location, date):
    params = {
        'key': api_key,
        'q': location,
        'date': date
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        print("Fetched data from API")
        return response.json()
    else:
        response.raise_for_status()

def parse_json_response(json_data):
    parsed_json_response = []
    for hour in json_data['hour']:
        ingestion_timestamp = pendulum.now().format('YYYY-MM-DD HH:mm:ss')
        modified_timestamp = pendulum.from_format(json_data['location']['localtime'], 'YYYY-MM-DD HH:mm').format('YYYY-MM-DD HH:mm:ss')
        data = json.dumps(hour, indent=4)
        parsed_json_response.append(
            {
                "ingestion_timestamp":ingestion_timestamp,
                "modified_timestamp":modified_timestamp,
                "data":data
            }
        )
    return parsed_json_response


def json_to_bq(json_data):

    table_id = "de-ai23.de_ai23_project._src_weather_stockholm"
    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of table to append to.
    # table_id = "your-project.your_dataset.your_table"

    rows_to_insert = json_data

    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))


@app.get("/")
def read_root():
    return "Welcome to our ingestion API. To run an ingestion navigate to /ingestion and give parameters for location and date"

@app.get("/ingestion")
def ingestion(location, date):
    API_URL = os.getenv('API_URL')
    API_KEY = os.getenv('API_KEY')


    formatted_data = json
    try:
        weather_data = fetch_weather_data(
            api_url=API_URL,
            api_key=API_KEY,
            location=location,
            date=date
            )
        formatted_data = {
            'location': weather_data['location'],
            'hour': weather_data['forecast']['forecastday'][0]['hour']
        }
        parsed_data = parse_json_response(formatted_data)
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data from API: {e}')

    try:
        json_to_bq(parsed_data)
    except Exception:
        print('Insert to Data Warehouse failed')
