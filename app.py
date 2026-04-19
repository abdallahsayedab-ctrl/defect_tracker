from flask import Flask, render_template, request, redirect, jsonify
from database import get_db_connection, get_root_causes
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
    cur.execute("SELECT * FROM defects ORDER BY date DESC, id DESC")
    defects = cur.fetchall()
    
    # Calculate Dashboard Stats
    total_output = 0
    total_defects = 0
    for d in defects:
        qty = d.get('defect_qty') or 0
        if str(d.get('symptom', '')).upper() == 'TOTAL':
            total_output += qty
        else:
            total_defects += qty
            
    defect_rate = (total_defects / total_output * 100) if total_output > 0 else 0
    ppm = (total_defects / total_output * 1000000) if total_output > 0 else 0
    
    stats = {
        "total_output": total_output,
        "total_defects": total_defects,
        "defect_rate": round(defect_rate, 2),
        "ppm": round(ppm, 0)
    }
    
    cur.close()
    conn.close()
    
    root_causes = get_root_causes()
    return render_template('index.html', defects=defects, stats=stats, root_causes=root_causes)

@app.route('/add', methods=['POST'])
def add_defect():
    data = request.form
    conn = get_db_connection()
    cur = conn.cursor()
    
    query = """
    INSERT INTO defects (
        pic, date, model, shift, sn, symptom, ng_station, 
        defect_qty, root_cause, related_station, defected_item, 
        defect_pic, category, status, actual_out, remarks
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Safely convert to integer
    def to_int(val, default=0):
        try: return int(val) if val else default
        except: return default

    cur.execute(query, (
        data.get('pic'), 
        data.get('date') or datetime.date.today(), 
        data.get('model'), 
        data.get('shift'), 
        data.get('sn'), 
        data.get('symptom'),
        data.get('ng_station'),
        to_int(data.get('defect_qty'), 1),
        data.get('root_cause'),
        data.get('related_station'),
        data.get('defected_item'),
        data.get('defect_pic'),
        data.get('category'),
        data.get('status', 'Open'),
        to_int(data.get('actual_out'), 0),
        data.get('remarks')
    ))
    
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
