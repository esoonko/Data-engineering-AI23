from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta

def pull_function(ti):
    value = ti.xcom_pull(key='python_xcom_test', dag_id='example_python_operator_xcom_push', task_ids='push_task')
    print(f'The pulled value is {value}')

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024,6,4),
    'retries': 3,
    'retry_delay': timedelta(minutes=3)
}

with DAG(
    'example_python_operator_xcom_pull',
    default_args=default_args,
    schedule_interval='@daily'
) as dag:
    pull_task = PythonOperator(
        task_id = 'pull_task',
        python_callable=pull_function
    )
    pull_task