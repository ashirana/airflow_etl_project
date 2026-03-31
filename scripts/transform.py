import json

def transform(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    transformed = []

    for record in data:
        transformed.append({
            "id": record["id"],
            "user_id": record["userId"],   
            "title": record["title"],
            "body": record["body"][:100]   
        })

    output_path = "/opt/airflow/tmp/transformed_data.json"

    with open(output_path, "w") as f:
        json.dump(transformed, f)

    return output_path