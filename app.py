import streamlit as st
import pandas as pd
from supabase import create_client, Client
import datetime
import os

# إعداد الصفحة
st.set_page_config(page_title="Defect Tracker Pro", layout="wide")

# الاتصال بـ Supabase
@st.cache_resource
def init_connection():
    url = st.secrets["https://abjtqvlyelggngxlmaob.supabase.co"] if "SUPABASE_URL" in st.secrets else os.environ.get("SUPABASE_URL")
    key = st.secrets["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFianRxdmx5ZWxnZ25neGxtYW9iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY1NDI0MDksImV4cCI6MjA5MjExODQwOX0.A_3pM9z72zgN0HrSJJalTlPIUI6UbbBJ-CXuj4I5bO4"] if "SUPABASE_KEY" in st.secrets else os.environ.get("SUPABASE_KEY")
    return create_client(url, key)

supabase = init_connection()

# --- Sidebar (فلاتر) ---
st.sidebar.header("Data Slicer")
date_range = st.sidebar.date_input("Date Range", [datetime.date.today(), datetime.date.today()])
selected_model = st.sidebar.selectbox("Select Model", ["All", "P17", "P7E", "Somalia", "P15A"])

# --- جلب البيانات ---
def fetch_data():
    res = supabase.table("defects").select("*").execute()
    return pd.DataFrame(res.data)

df = fetch_data()

# --- Dashboard (الإحصائيات) ---
st.title("🏭 Defect Tracker Dashboard")

col1, col2, col3 = st.columns(3)

if not df.empty:
    with col1:
        st.metric("Total Records", len(df))
    with col2:
        total_defects = df[df['symptom'] != 'TOTAL']['defect_qty'].sum()
        st.metric("Total Defect Qty", total_defects)
    with col3:
        # مثال لحساب النسبة
        st.metric("Avg Defect %", "2.45%")

# --- عرض الجدول الرئيسي ---
st.subheader("Recent Defect Records")
st.dataframe(df.sort_values(by='date', ascending=False), use_container_width=True)

# --- نموذج الإضافة ---
st.divider()
st.subheader("➕ Add New Defect")
with st.form("add_form"):
    c1, c2, c3 = st.columns(3)
    with c1:
        pic = st.text_input("PIC")
        date = st.date_input("Date")
    with c2:
        model = st.selectbox("Model", ["P17", "P7E", "Somalia"])
        symptom = st.text_input("Symptom")
    with c3:
        qty = st.number_input("Qty", min_value=1)
        status = st.selectbox("Status", ["Open", "Pending", "Closed"])
    
    submit = st.form_submit_button("Submit Record")
    if submit:
        data = {
            "pic": pic,
            "date": str(date),
            "model": model,
            "symptom": symptom,
            "defect_qty": qty,
            "status": status
        }
        supabase.table("defects").insert(data).execute()
        st.success("Record saved to Supabase!")
        st.rerun()
