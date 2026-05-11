import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="defects",
    user="postgres",
    password="A.m@2050",
    port="5432"
)
cur = conn.cursor()

# Run full schema
with open('schema.sql', 'r') as f:
    cur.execute(f.read())

conn.commit()
cur.close()
conn.close()
print("✅ Schema updated – all columns added!")
