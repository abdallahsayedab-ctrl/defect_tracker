from flask import Flask, render_template, request, redirect, jsonify
from database import get_db_connection
import datetime

app = Flask(__name__)

# محرك تحليل محلي (قاعدة بيانات خبرة مصغرة)
KNOWLEDGE_BASE = {
    "No Power": "Check battery BTB connection and mainboard voltage points.",
    "Touch not Working": "Check LCM FPC alignment and static electricity on line.",
    "TOTAL": "Daily output record. No defect analysis needed."
}

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM defects ORDER BY date DESC")
    defects = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', defects=defects)

@app.route('/add', methods=['POST'])
def add_defect():
    data = request.form
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO defects (pic, date, model, shift, sn, symptom, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (data['pic'], data['date'], data['model'], data['shift'], data['sn'], data['symptom'], data['status'])
    )
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

@app.route('/analyze/<symptom>')
def analyze(symptom):
    suggestion = "No local match found. Consult tech manual."
    for key in KNOWLEDGE_BASE:
        if key.lower() in symptom.lower():
            suggestion = KNOWLEDGE_BASE[key]
    return jsonify({"suggestion": suggestion})

if __name__ == '__main__':
    # تشغيل السيرفر على الشبكة الداخلية
    app.run(host='0.0.0.0', port=5000, debug=False)
