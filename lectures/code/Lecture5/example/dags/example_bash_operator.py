from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024,6,4),
    'retries': 3,
    'retry_delay': timedelta(minutes=3)
}

with DAG(
    'example_bash_operator',
    default_args=default_args,
    schedule_interval='@daily'
) as dag:
    start = BashOperator(
        task_id = 'start',
        bash_command = 'echo This is the start task'   
    )
    bash_task_1 = BashOperator(
        task_id = 'bash_task_1',
        bash_command = 'echo hello world'   
    )
    end = BashOperator(
        task_id = 'end',
        bash_command = 'echo This is the end of the DAG'
    )

    bash_task_1.set_upstream(start)
    end.set_upstream(bash_task_1)

    start.set_downstream(bash_task_1)
    bash_task_1.set_downstream(end)