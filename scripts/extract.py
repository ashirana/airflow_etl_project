import requests
import json

def extract():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    response = requests.get(url)
    response.raise_for_status()  # important
    
    data = response.json()

    file_path = "/tmp/data.json"

    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

    return file_path