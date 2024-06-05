from airflow.decorators import dag, task
from datetime import datetime, timedelta
from random import randint
import sys

default_args = {
    'owner': 'airflow',
    'retries': 0,
    'retry_delay': timedelta(minutes=0)
}

@dag(
    dag_id='example_task_flow_api',
    default_args=default_args,
    start_date=datetime(2024,5,20),
    schedule_interval='0 2 * * *', #Ändra schedule_interval till Cron expression t ex 0 2 * * *
)
def example_task_flow_api():
    @task()
    def greeting(location, today):
        randomizer = randint(0,1)
        if randomizer == 1:
            print(f'We are at {location} and today is {today}')
        else:
            print(f'We are at {location} and today is {today}')

    @task()
    def location():
        return 'Stockholm'
    
    @task()
    def today():
        return datetime.now().date()
    
    today_task = today()
    location_task = location()
    greeting_task = greeting(location_task, today_task)

example_task_flow_api = example_task_flow_api()
