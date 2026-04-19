import streamlit as st
import pandas as pd
from database import get_defects, insert_defect, delete_all_defects
from ai_engine import analyze_defect_root_cause
import datetime

# إعدادات الصفحة
st.set_page_config(page_title="Defect Tracker Pro", page_icon="🏭", layout="wide")

# التحميل الأولي للبيانات
if 'data' not in st.session_state:
    st.session_state.data = get_defects()

st.title("🏭 Defect Tracker Pro - Internal System")
st.markdown("---")

# --- لوحة التحكم (Sidebar) ---
st.sidebar.image("https://picsum.photos/seed/factory/200/100", use_container_width=True)
st.sidebar.header("Operations")
if st.sidebar.button("🔄 Refresh Data"):
    st.session_state.data = get_defects()
    st.rerun()

# --- نموذج الإضافة ---
with st.expander("➕ تسجيل بلاغ عطل جديد", expanded=False):
    with st.form("defect_form"):
        c1, c2, c3 = st.columns(3)
        with c1:
            pic = st.text_input("Person In Charge (PIC)")
            date = st.date_input("Incident Date", datetime.date.today())
            model = st.selectbox("Product Model", ["P17", "P7E", "Somalia", "P15A", "O19AE"])
        with c2:
            shift = st.selectbox("Shift", ["Day", "Night"])
            sn = st.text_input("Serial Number (S/N)")
            station = st.text_input("NG Station")
        with c3:
            symptom = st.text_input("Symptom")
            qty = st.number_input("Defect Qty", min_value=1, step=1)
            status = st.selectbox("Status", ["Open", "Pending", "Closed"])

        submitted = st.form_submit_button("إرسال البيانات")
        if submitted:
            new_defect = {
                "pic": pic, "date": str(date), "model": model, "shift": shift,
                "sn": sn, "ng_station": station, "symptom": symptom,
                "defect_qty": qty, "status": status
            }
            insert_defect(new_defect)
            st.success("✅ تم تسجيل العطل بنجاح في قاعدة البيانات!")
            st.session_state.data = get_defects()

# --- قسم التحليل بالذكاء الاصطناعي ---
st.subheader("🤖 AI Technical Analysis")
if not st.session_state.data.empty:
    latest = st.session_state.data.iloc[0]
    if st.button(f"Analyze Latest Incident: {latest['symptom']}"):
        with st.spinner("Gemini is thinking..."):
            analysis = analyze_defect_root_cause(latest.to_dict())
            st.info(analysis)

# --- عرض البيانات ---
st.subheader("📊 Data Explorer")
df = st.session_state.data
if not df.empty:
    st.dataframe(df, use_container_width=True)
    
    # تصدير البيانات
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Report (CSV)", csv, "defect_report.csv", "text/csv")
else:
    st.warning("لا توجد بيانات حالياً.")

st.markdown("---")
st.caption("Developed for Internal Production Environment | Powered by Gemini & PostgreSQL")
