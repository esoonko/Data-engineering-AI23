from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta

def python_function_1():
    print('Hello world')

def start():
    print("This is start task")

def end():
    print("This is the end of the DAG")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024,6,4),
    'retries': 3,
    'retry_delay': timedelta(minutes=3)
}

with DAG(
    'example_python_operator',
    default_args=default_args,
    schedule_interval='@daily'
) as dag:
    start_task = PythonOperator(
        task_id = 'start',
        python_callable=start
    )
    python_task_1 = PythonOperator(
        task_id = 'python_task_1',
        python_callable=python_function_1
    )
    end_task = PythonOperator(
        task_id = 'end',
        python_callable=end
    )

    start_task >> python_task_1 >> end_task