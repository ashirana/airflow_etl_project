import requests
import json
import os

def extract():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()

    os.makedirs("/opt/airflow/tmp", exist_ok=True)

    file_path = "/opt/airflow/tmp/raw_data.json"

    with open(file_path, "w") as f:
        json.dump(data, f)

    return file_path