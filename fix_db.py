import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="defects",
    user="postgres",
    password="A.m@2050",
    port="5432"
)
cur = conn.cursor()

cur.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS status VARCHAR(20) NOT NULL DEFAULT 'approved'")
cur.execute("UPDATE users SET status = 'approved'")

conn.commit()
cur.close()
conn.close()
print("Done! status column added and all users set to approved.")