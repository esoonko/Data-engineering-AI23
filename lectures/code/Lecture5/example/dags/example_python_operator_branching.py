from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta

def start():
    print("This is start task")
    
def end():
    print("This is the end of the DAG")

def location_and_date(location, today):
    print(f'We are in {location} and today is {today}')

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024,6,4),
    'retries': 3,
    'retry_delay': timedelta(minutes=3)
}

with DAG(
    'example_python_operator_branching',
    default_args=default_args,
    schedule_interval='@daily'
) as dag:
    start_task = PythonOperator(
        task_id = 'start',
        python_callable=start
    )
    location_and_date = PythonOperator(
        task_id = 'location_and_date',
        python_callable=location_and_date,
        op_kwargs = {'location':'Stockholm', 'today' : datetime.now().date()}
    )
    end_task = PythonOperator(
        task_id = 'end',
        python_callable=end
    )

    start_task >> location_and_date >> end_task