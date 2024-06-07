from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta
from hooks.ingestion_api_hook import IngestionApiHook


def call_api(ds, location):
    hook = IngestionApiHook(http_conn_id='ingestion_api', method='GET')
    response = hook.run(endpoint=f'/ingestion?location={location}&date={ds}')
    print(response)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024,6,1),
    'retries': 3,
    'retry_delay': timedelta(minutes=3)
}

with DAG(
    'example_python_operator_hook',
    default_args=default_args,
    schedule_interval='@daily'
) as dag:
    
    api_call_task = PythonOperator(
        task_id = 'call_api_task',
        python_callable=call_api,
        op_kwargs={'location':'Stockholm'}
    )

    api_call_task