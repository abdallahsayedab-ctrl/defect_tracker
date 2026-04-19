import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd
import os

# يتم جلب الإعدادات من متغيرات البيئة للأمان
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "defects")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "A.m@2050")
DB_PORT = os.getenv("DB_PORT", "5432")

def get_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Database Connection Error: {e}")
        return None

def get_defects():
    conn = get_connection()
    if not conn: return pd.DataFrame()
    try:
        df = pd.read_sql("SELECT * FROM defects ORDER BY date DESC", conn)
        return df
    finally:
        conn.close()

def insert_defect(d):
    conn = get_connection()
    if not conn: return
    try:
        cur = conn.cursor()
        query = """
        INSERT INTO defects (pic, date, model, shift, sn, ng_station, symptom, defect_qty, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (
            d['pic'], d['date'], d['model'], d['shift'], 
            d['sn'], d['ng_station'], d['symptom'], 
            d['defect_qty'], d['status']
        ))
        conn.commit()
        cur.close()
    finally:
        conn.close()

def delete_all_defects():
    conn = get_connection()
    if not conn: return
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM defects")
        conn.commit()
    finally:
        conn.close()
