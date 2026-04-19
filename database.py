import psycopg2
from psycopg2.extras import RealDictCursor
import os

def get_db_connection():
    # بيانات الاتصال (تعدل حسب السيرفر الداخلي)
    conn = psycopg2.connect(
        host="localhost",
        database="defects",
        user="postgres",
        password="A.m@2050",
        port="5432",
        cursor_factory=RealDictCursor
    )
    return conn
