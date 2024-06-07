from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta

def push_function(ti):
    ti.xcom_push(key='python_xcom_test', value="This is the value being pushed")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024,6,4),
    'retries': 3,
    'retry_delay': timedelta(minutes=3)
}

with DAG(
    'example_python_operator_xcom_push',
    default_args=default_args,
    schedule_interval='@daily'
) as dag:
    push_task = PythonOperator(
        task_id = 'push_task',
        python_callable=push_function
    )
    push_task