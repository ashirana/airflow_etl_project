from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load


def run_extract():
    return extract()


def run_transform(ti):
    file_path = ti.xcom_pull(task_ids="extract_task")
    return transform(file_path)


def run_load(ti):
    file_path = ti.xcom_pull(task_ids="transform_task")
    load(file_path)


default_args = {
    "start_date": datetime(2023, 1, 1)
}

with DAG(
    dag_id="etl_pipeline_project",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=run_extract
    )

    transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=run_transform
    )

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=run_load
    )

    extract_task >> transform_task >> load_task