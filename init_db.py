import psycopg2
from werkzeug.security import generate_password_hash

def init_db():
    conn = psycopg2.connect(
        host="localhost", database="defects", user="postgres", password="A.m@2050", port="5432"
    )
    cur = conn.cursor()

    # Users table with status column
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            role VARCHAR(20) NOT NULL DEFAULT 'user',
            status VARCHAR(20) NOT NULL DEFAULT 'approved',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Add status column if missing (migration)
    try:
        cur.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS status VARCHAR(20) NOT NULL DEFAULT 'approved'")
    except Exception:
        conn.rollback()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS root_cause (
            id SERIAL PRIMARY KEY,
            root_cause VARCHAR(255) UNIQUE NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS models (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS defects (
            id SERIAL PRIMARY KEY,
            pic VARCHAR(100),
            date DATE,
            model VARCHAR(50),
            shift VARCHAR(20),
            sn VARCHAR(100),
            symptom VARCHAR(200),
            ng_station VARCHAR(100),
            defect_qty INT DEFAULT 1,
            root_cause VARCHAR(255),
            related_station TEXT,
            defected_item VARCHAR(100),
            defected_item_sn VARCHAR(100),
            defected_item_qty INT DEFAULT 1,
            defect_pic VARCHAR(100),
            category VARCHAR(50),
            status VARCHAR(50) DEFAULT 'Pending',
            target_in INT DEFAULT 0,
            target_out INT DEFAULT 0,
            actual_in INT DEFAULT 0,
            actual_out INT DEFAULT 0,
            defect_percent NUMERIC(10,4) DEFAULT 0.00,
            ppm NUMERIC(12,2) DEFAULT 0,
            remarks TEXT
        );
    """)

    # Migrations
    for alter in [
        "ALTER TABLE defects ALTER COLUMN related_station TYPE TEXT",
        "ALTER TABLE defects ALTER COLUMN symptom TYPE VARCHAR(200)",
        "ALTER TABLE defects ALTER COLUMN ppm TYPE NUMERIC(12,2)",
        "ALTER TABLE defects ALTER COLUMN defect_percent TYPE NUMERIC(10,4)",
    ]:
        try:
            cur.execute(alter)
        except Exception:
            conn.rollback()

    # Seed models
    for m in ['Somalia', 'P17', 'P7E', 'O19AE', 'P15A', 'P15AP']:
        try:
            cur.execute("INSERT INTO models (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (m,))
        except Exception:
            conn.rollback()

    # Default super_admin
    cur.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cur.fetchone():
        cur.execute(
            "INSERT INTO users (username, password_hash, role, status) VALUES (%s,%s,%s,'approved')",
            ('admin', generate_password_hash('admin123'), 'super_admin')
        )

    conn.commit()
    cur.close(); conn.close()
    print("[OK] Database initialized. Default login: admin / admin123")

if __name__ == '__main__':
    init_db()
