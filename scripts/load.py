import psycopg2
import json

def load(file_path):

    conn = psycopg2.connect(
        host="postgres",
        database="airflow",
        user="airflow",
        password="airflow"
    )

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INT PRIMARY KEY,
            user_id INT,
            title TEXT,
            body TEXT
        );
    """)

    with open(file_path, "r") as f:
        data = json.load(f)

    for record in data:
        cur.execute("""
            INSERT INTO posts (id, user_id, title, body)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
        """, (
            record["id"],
            record["user_id"],   
            record["title"],
            record["body"]
        ))

    conn.commit()
    cur.close()
    conn.close()