from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
from extract import extract 
from transform import transform
from load import load

def extract_task(**context):
    path = extract()
    context['ti'].xcom_push(key='file_path', value=path)

def transform_task(**context):
    file_path = context['ti'].xcom_pull(key='file_path', task_ids='extract_task')
    transformed_path = transform(file_path)
    context['ti'].xcom_push(key='transformed_file_path', value=transformed_path)

def load_task(**context):
    transformed_file_path = context['ti'].xcom_pull(key='transformed_file_path', task_ids='transform_task')
    load(transformed_file_path)

with DAG(
    dag_id = 'elt_pipeline_project',
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:
    extract_task = PythonOperator(
        task_id='extract_task',
        python_callable=extract_task,
        provide_context=True
    )

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_task,
        provide_context=True
    )

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=load_task,
        provide_context=True
    )

    extract_task >> transform_task >> load_task