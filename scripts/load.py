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
            title TEXT
        );
    """)

with open(file_path, 'r') as f:
    data = json.load(f)
for post in data:
    cur.execute("""
            INSERT INTO posts (id, title) VALUES (%s, %s)
            ON CONFLICT (id) DO NOTHING;
        """, (post['id'], post['title']))
conn.commit()
cur.close() 
conn.close()
