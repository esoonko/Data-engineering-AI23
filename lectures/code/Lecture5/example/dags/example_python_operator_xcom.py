from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta

def start():
    return 'Stockholm'

def location_and_date(ti):
    location = ti.xcom_pull(task_ids='start')
    print(f'We are in {location} and today is {datetime.now().date()}')

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024,6,4),
    'retries': 3,
    'retry_delay': timedelta(minutes=3)
}

with DAG(
    'example_python_operator_xcom',
    default_args=default_args,
    schedule_interval='@daily'
) as dag:
    start_task = PythonOperator(
        task_id = 'start',
        python_callable=start
    )
    location_and_date = PythonOperator(
        task_id = 'location_and_date',
        python_callable=location_and_date
    )
    start_task >> location_and_date