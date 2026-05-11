import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="defects",
        user="postgres",
        password="A.m@2050",
        port="5432",
        cursor_factory=RealDictCursor
    )
    return conn

# ─── Models ──────────────────────────────────────────────────────

def get_models():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM models ORDER BY name")
    results = cur.fetchall()
    cur.close(); conn.close()
    return results

def add_model(name):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO models (name) VALUES (%s)", (name,))
        conn.commit()
        return True
    except Exception:
        conn.rollback()
        return False
    finally:
        cur.close(); conn.close()

def delete_model(model_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM models WHERE id = %s", (model_id,))
    conn.commit()
    cur.close(); conn.close()

# ─── Dropdowns ───────────────────────────────────────────────────

def get_root_causes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT root_cause FROM root_cause ORDER BY root_cause")
    results = cur.fetchall()
    cur.close(); conn.close()
    return [r['root_cause'] for r in results]

def get_pics():
    return [
        'Nourhan Abo El Ela', 'Sherif Fathy', 'Asmaa Abdelrahman', 'Youssef Ashraf',
        'Ahmed Fekri', 'Mohamed Bahaa', 'Abdullah Sayed', 'Abdulrahim'
    ]

def get_symptoms():
    return [
        'TOTAL', 'UUT', 'ADB LENSOR', 'ACC Calibration', 'ATA Start', 'ATA Switch',
        'Abnormal Display', 'Accelerometer Sensor Fail', 'Aging Fail', 'Aging Mode',
        'Audio Jack', 'Auto Restart', 'BACK Light', 'Battery Fail Aging',
        'Black Point OLEDM', 'Blocked Screw Hole', 'Bluetooth Fail', 'Broken Antenna',
        'Broken Bracket', 'CCD Machine Issue', 'Calibration', 'Calibration Value',
        'Camera Dent', "Camera Doesn't Work", 'Camera Far / Near Sensor RMT',
        'Camera Not Working', 'Cat Front', 'Cat Rear Blemish', 'Cat Rear Main',
        'Cat Rear Ultra', 'Cat Rear Wide', 'Change Color Battery Cover',
        'Change Color Middle frame', 'Charger Fail RMT', 'Charging Current',
        'Check Camera Fuse ID', 'Check Chip', 'Check Volume Up',
        'Corrosion in Battery Cover', 'Crack Battery Cover', 'Cut FPC', 'Cut Main Camera',
        'DDR Fail Aging', 'DENT OLEDM', 'Damage BTB', 'Damage Battery',
        'Damage Battery Cover', 'Damage Bracket', 'Damage Camera', 'Damage Cam Ultra',
        'Damage Coaxial Black RF Main PCBA', 'Damage Coaxial RF',
        'Damage Coaxial RF Sub PCBA', 'Damage Coaxial White RF Main PCBA',
        'Damage Component', 'Damage FPC', 'Damage Flash', 'Damage Lens',
        'Damage Main Camera', 'Damage Middle Frame', 'Damage OLEDM', 'Damage PCBA Main',
        'Damage PCBA Sub', 'Damage screw', 'Damage speaker Rubber', 'Damaged Flash',
        'Dark Spot OLEDM', 'Deformation BTB', 'Deformation Battery Cover',
        'Deformation Flash', 'Deformation Middle frame', 'Deformation OLED',
        'Deformation lens', 'Dent Battery Cover', 'Dent DECO', 'Dent Deco Plate',
        'Dent Lens', 'Dent Middle Frame ( USB )', 'Dot on Battery Cover', 'Dot on DECO',
        'Dot on Display', 'Dot on lens', 'Double Face missing', 'Dust Back Camera',
        'Dust Front camera', 'Dust Wide Camera', 'Dust flash', 'Fail Back Camera FMT',
        'Fail RMT LED', 'Fast boot', 'FMT Fail', 'Finger Chart', 'Finger Print Fail',
        'Fingerprint under lens', 'Flash Fail', 'Flicker in Screen Display', 'Freeze',
        'Front Camera Fail', 'Front Camera Rubber', 'GPS', 'GSM', 'Gap Battery Cover',
        'Gap Middle Frame', 'Gap OLEDM', 'Get At Port', 'Google Key', 'Gyroscope',
        'Hair under Lens', 'Hall Gyro Cal', 'IDLE FAIL', 'IR Sensor', 'Keyparts 7',
        'LTE', 'Light Sensor', 'Locked Device', 'Loop Back', 'MAIN Blemish',
        'Magnetic Sensor', 'Magnetic Sensor Fail', 'Main Mic', 'Mic Tightness',
        'Missing Camera', 'Missing Flash', 'Missing Flash Board', 'Missing Flash Lens',
        'Missing Flash Sticker', 'Missing Process', 'Missing QR Code', 'Missing SIM Rubber',
        'Missing Scan', 'Missing Side key Button', 'Missing Sticker in speaker',
        'Missing Sticker under Lens', 'Mix Colors', 'Mix DECO Color', 'Mix Lens',
        'NFC Fail', 'NR 5G Fail', 'No Display', 'No Power', 'No charge', 'OIS Fail',
        'OTG Fail', 'Out of Workorder', 'Over Glue Battery Cover', 'Over Glue OLEDM',
        'Phantom Check Error', 'Power Off', 'Power on', 'Print Camera', 'Proximity Sensor',
        'QVGA Fail', 'RF Check', 'RF Damage', 'RF Fail Aging', 'Rear Main Blemish',
        'Rear Wide Blemish', 'Receiver', 'Red Line on Display', 'SAR Sensor Fail',
        'SIM Card fail', 'Scratch Battery Cover', 'Scratch DECO Bracket',
        'Scratch DECO Composite', 'Scratch Deco Plate', 'Scratch Deco Ring',
        'Scratch Middle frame', 'Scratch OLED', 'Scratch lens', 'Search V-Comport',
        'Set Pre Loader', 'Shift Camera', 'Shifted Battery', 'Shifted Front camera Bracket',
        'Shifted Motor', 'Side Keys Not Working', 'Sleep Current', 'Software', 'Speaker',
        'Sticker under Front Camera', 'TP Vendor', 'Top Speaker', 'Touch not Working',
        'Type C', 'UP Battery cover', 'USB not Working', 'Up DECO', 'Up RF Cable',
        'Up Screw', 'Upload camera', 'Vibration Fail', 'WCDMA', 'WCDMA Band 5', 'WIFI',
        'White Point Battery Cover', 'Wide Screw Hole', 'Wrong Direction Deco Plate',
        'chart UP', 'top mic', 'sticker under fingerprint', 'white point OLEDM',
        'Deformation Deco Plate', 'Read Lux',
    ]

def get_ng_stations():
    return [
        'FAI','IDLE','KEYPARTS7','YH1','KEYPARTS1','BTB1','BTB2','KEYPARTS2','ALEAK',
        'KEYPARTS3','YH2','COSMETIC1','ANT','Aging','RAUD','FCT','LST','CAM1','RMT',
        'COSMETIC2','RFQC','COSMETIC3','COSMETIC4','COSMETIC5','RPCT','USFT','CAMCV',
        'FAMMI','CAM2'
    ]

def get_related_stations():
    return [
        'LCM Function Test Jig 1','LCM Function Test Jig 2','LCM appearance inspection',
        'Receiver + moto + press together',
        'Mainboard appearance inspection/tearing off the MIC hole',
        'Install the photosensitive rubber sleeve','Glue machine','magnetic copper foil',
        'Install the Main PCBA','Small board appearance inspection','Install the small board',
        'Apply motor conductive cloth','Assemble the main FPC',
        'Buckle Screen BTB / Main FPC / Fingerprint Base','assemble fingerprint/buckle BTB',
        'Assemble the front camera/fasten the BTB',
        'Copper foil wrapping for the main rear camera',
        'Assemble the main camera / Attach the Ultra camera',
        'Visual Ant board and Snap on the coaxial line',
        'Assemble the ANT board to the BOX / BOX end coaxial cable','Keyparts1',
        'Install the Speaker and snap on the coaxial cable on the motherboard side',
        'Manage White Coaxial cable/FPC BTB*1','Install black coaxial cable',
        'Manage black Coaxial cable / (BTB1 pressing)',
        'Device inspection / Attaching the front ground copper foil',
        '( IDLE + KEYPARTS7 ) Current Test + Camera Binding',
        'Assembling batteries / tearing off battery release paper / rolling batteries',
        'Snap battery BTB / Remove Front camera conductive Sticker / BTB2',
        'Device inspection / Install the mainboard bracket','Tear-off paper/install flash board',
        'install the steel sheet/binding (Speaker, Battery, Bracket )',
        'Pre-locking screws*1 ( Steel Sheet Screw )','put into screw machine 1',
        'Automatic Screw Machine 2','FMT + Visual Screws + Hand screw',
        'Visual Battery Cover','ALEAK','Plasma cleaning',
        'Device Visual + Bind Battery Cover ( Keyparts 3 )',
        'Tear off the camera protective cover*2//remove the release paper from the battery cover/clean and inspect',
        'CCD assembly battery cover','Battery cover curved surface pressing',
        'Device Inspection','Installation of protective cover/Scan Pass QR Code/vibration test',
        'ANT test','Aging','USFT','FCT','LST','RAUD','CAM1','CAM2','CAMCV','RPCT','FAMMI',
        'SD card test & SIM card test & card tray insertion test','Vibration',
        'LED light/touch screen test','Screen test*26',
        'Handset / Upper Speaker / Lower Speaker / WLAN AP Scan Test / Bluetooth Device Scan',
        'Headphone/main microphone','secondary microphone test',
        'Gyroscope test / Accelerometer sensor test / Geomagnetic sensor test',
        'Distance Sensor/Light Sensor/OTG Test','Charger test','Fingerprint entry',
        'Rear main camera/rear secondary camera/rear large wide-angle camera/front camera test',
        'SAR sensor calibration/SAR sensor testing',
        'Sim Tray Insertion / removal of protective cover + Scan RMT','Visual Device 2',
        'Cosmetics 2 Scan','Pending','BTB SUB PCBA','Supplier',
        'Bad handling from PD operators on the Assy line',
        'Bad handling from PD operators on the subline',
        'Bad handling from PD operators on the Testing line',
        'Bad handling from PD operators on the Packing line','Analysis in Progress',
        'Zone leader (Keyparts3)','Zone leader (Test)','Zone leader (Subline)',
        'Zone leader (Packing Input)','Zone leader (Packing Output)'
    ]

def get_defected_items():
    return [
        'PCBA','SUB PCBA','Black RF Cable','White RF Cable','Speaker','Receiver',
        'Battery','OLED','Antenna Bracket','Light Sensor Rubber','Front Camera',
        'OIS Camera','Ultra Camera','Battery Cover','Link FPC','Fingerprint','Motor',
        'Motor Conductive','Front camera Conductive','Flash PCBA','No Defect Item',
        'N/A','OLED Main Mic Rubber','OLED Top Mic Rubber','ANT PCBA','Steel Sheet'
    ]

def get_categories():
    return ['Manpower','Machine','Material','No Defect Item','Pending']

def get_statuses():
    return ['Damage','Material','Pending','No Defect Item']

# ─── Defect Queries ──────────────────────────────────────────────

def get_filtered_defects(model=None, date_str=None, date_from=None, date_to=None,
                         symptom_filter=None, item_filter=None, station_filter=None,
                         unified_search=False):
    conn = get_db_connection()
    cur  = conn.cursor()
    query  = "SELECT * FROM defects WHERE 1=1"
    params = []
    if model:
        query += " AND model ILIKE %s"; params.append(model)
    if date_str:
        query += " AND date = %s"; params.append(date_str)
    if date_from:
        query += " AND date >= %s"; params.append(date_from)
    if date_to:
        query += " AND date <= %s"; params.append(date_to)
    if unified_search and symptom_filter:
        # OR search across symptom, defected_item, ng_station
        q = f'%{symptom_filter}%'
        query += " AND (symptom ILIKE %s OR defected_item ILIKE %s OR ng_station ILIKE %s)"
        params.extend([q, q, q])
    else:
        if symptom_filter:
            query += " AND symptom ILIKE %s"; params.append(f'%{symptom_filter}%')
        if item_filter:
            query += " AND defected_item ILIKE %s"; params.append(f'%{item_filter}%')
        if station_filter:
            query += " AND ng_station ILIKE %s"; params.append(f'%{station_filter}%')
    query += " ORDER BY date DESC, id DESC"
    cur.execute(query, params)
    defects = cur.fetchall()
    cur.close(); conn.close()
    return defects

def get_daily_defects_summary(model=None, date_from=None, date_to=None):
    conn = get_db_connection()
    cur  = conn.cursor()
    query = """
        SELECT date,
            SUM(CASE WHEN UPPER(symptom)='TOTAL' THEN COALESCE(actual_out,0) ELSE 0 END) as total_output,
            SUM(CASE WHEN UPPER(symptom)!='TOTAL' THEN COALESCE(defect_qty,0) ELSE 0 END) as total_defects
        FROM defects WHERE 1=1
    """
    params = []
    if model:
        query += " AND model ILIKE %s"; params.append(model)
    if date_from:
        query += " AND date >= %s"; params.append(date_from)
    if date_to:
        query += " AND date <= %s"; params.append(date_to)
    query += " GROUP BY date ORDER BY date DESC"
    cur.execute(query, params)
    results = cur.fetchall()
    cur.close(); conn.close()
    return results

def get_defect_by_id(defect_id):
    conn = get_db_connection()
    cur  = conn.cursor()
    cur.execute("SELECT * FROM defects WHERE id = %s", (defect_id,))
    defect = cur.fetchone()
    cur.close(); conn.close()
    return defect

def update_defect(defect_id, data):
    conn = get_db_connection()
    cur  = conn.cursor()
    cur.execute("""
        UPDATE defects SET pic=%s,date=%s,model=%s,shift=%s,sn=%s,symptom=%s,
            ng_station=%s,defect_qty=%s,root_cause=%s,related_station=%s,
            defected_item=%s,defected_item_sn=%s,defected_item_qty=%s,
            defect_pic=%s,category=%s,status=%s,target_in=%s,target_out=%s,
            actual_in=%s,actual_out=%s,defect_percent=%s,ppm=%s,remarks=%s
        WHERE id=%s
    """, (
        data.get('pic'), data.get('date'), data.get('model'), data.get('shift'),
        data.get('sn'), data.get('symptom'), data.get('ng_station'),
        int(data.get('defect_qty', 1) or 1), data.get('root_cause'),
        data.get('related_station'), data.get('defected_item'),
        data.get('defected_item_sn'), int(data.get('defected_item_qty', 1) or 1),
        data.get('defect_pic'), data.get('category'), data.get('status', 'Pending'),
        int(data.get('target_in', 0) or 0), int(data.get('target_out', 0) or 0),
        int(data.get('actual_in', 0) or 0), int(data.get('actual_out', 0) or 0),
        float(data.get('defect_percent', 0) or 0), int(data.get('ppm', 0) or 0),
        data.get('remarks', ''), defect_id
    ))
    conn.commit()
    cur.close(); conn.close()

def get_top_defects_chart_data(model=None, date_from=None, date_to=None, limit=3):
    conn = get_db_connection()
    cur  = conn.cursor()
    query  = "SELECT symptom, SUM(defect_qty) as total_qty FROM defects WHERE UPPER(symptom)!='TOTAL' AND symptom IS NOT NULL AND symptom!=''"
    params = []
    if model:
        query += " AND model ILIKE %s"; params.append(model)
    if date_from:
        query += " AND date >= %s"; params.append(date_from)
    if date_to:
        query += " AND date <= %s"; params.append(date_to)
    query += " GROUP BY symptom ORDER BY total_qty DESC LIMIT %s"
    params.append(limit)
    cur.execute(query, params)
    tops = cur.fetchall()
    cur.close(); conn.close()
    return tops

def get_top_items_chart_data(model=None, date_from=None, date_to=None, limit=3):
    conn = get_db_connection()
    cur  = conn.cursor()
    query = (
        "SELECT defected_item, SUM(defect_qty) as total_qty FROM defects "
        "WHERE defected_item IS NOT NULL AND defected_item != '' "
        "AND LOWER(defected_item) NOT IN ('n/a','pending','no defect item') "
        "AND LOWER(COALESCE(category,'')) != 'pending' "
        "AND LOWER(COALESCE(status,'')) != 'pending' "
    )
    params = []
    if model:
        query += " AND model ILIKE %s"; params.append(model)
    if date_from:
        query += " AND date >= %s"; params.append(date_from)
    if date_to:
        query += " AND date <= %s"; params.append(date_to)
    query += " GROUP BY defected_item ORDER BY total_qty DESC LIMIT %s"
    params.append(limit)
    cur.execute(query, params)
    tops = cur.fetchall()
    cur.close(); conn.close()
    return tops

def get_top_symptoms(model=None, date_str=None, limit=3):
    conn = get_db_connection()
    cur  = conn.cursor()
    query  = "SELECT symptom, SUM(defect_qty) as total_qty FROM defects WHERE UPPER(symptom)!='TOTAL' AND symptom IS NOT NULL"
    params = []
    if model:
        query += " AND model ILIKE %s"; params.append(model)
    if date_str:
        query += " AND date = %s"; params.append(date_str)
    query += " GROUP BY symptom ORDER BY total_qty DESC LIMIT %s"; params.append(limit)
    cur.execute(query, params)
    tops = cur.fetchall()
    cur.close(); conn.close()
    return tops

def get_top_items(model=None, date_str=None, limit=3):
    conn = get_db_connection()
    cur  = conn.cursor()
    query  = "SELECT defected_item, SUM(defect_qty) as total_qty FROM defects WHERE defected_item IS NOT NULL AND defected_item!=''"
    params = []
    if model:
        query += " AND model ILIKE %s"; params.append(model)
    if date_str:
        query += " AND date = %s"; params.append(date_str)
    query += " GROUP BY defected_item ORDER BY total_qty DESC LIMIT %s"; params.append(limit)
    cur.execute(query, params)
    tops = cur.fetchall()
    cur.close(); conn.close()
    return tops

# ─── User Management ─────────────────────────────────────────────

def get_user_by_username(username):
    conn = get_db_connection()
    cur  = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close(); conn.close()
    return user

def get_all_users():
    conn = get_db_connection()
    cur  = conn.cursor()
    cur.execute("SELECT id, username, role, status, created_at FROM users WHERE status='approved' ORDER BY id")
    users = cur.fetchall()
    cur.close(); conn.close()
    return users

def get_pending_users():
    conn = get_db_connection()
    cur  = conn.cursor()
    cur.execute("SELECT id, username, role, created_at FROM users WHERE status='pending' ORDER BY created_at DESC")
    users = cur.fetchall()
    cur.close(); conn.close()
    return users

def get_pending_users_count():
    conn = get_db_connection()
    cur  = conn.cursor()
    cur.execute("SELECT COUNT(*) as cnt FROM users WHERE status='pending'")
    row = cur.fetchone()
    cur.close(); conn.close()
    return int(row['cnt']) if row else 0

def create_user_pending(username, password_hash, role='user'):
    conn = get_db_connection()
    cur  = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (username, password_hash, role, status) VALUES (%s,%s,%s,'pending')",
            (username, password_hash, role)
        )
        conn.commit()
        return True
    except Exception:
        conn.rollback()
        return False
    finally:
        cur.close(); conn.close()

def create_user(username, password_hash, role='user'):
    conn = get_db_connection()
    cur  = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (username, password_hash, role, status) VALUES (%s,%s,%s,'approved')",
            (username, password_hash, role)
        )
        conn.commit()
        return True
    except Exception:
        conn.rollback()
        return False
    finally:
        cur.close(); conn.close()

def approve_user(user_id, role='user'):
    conn = get_db_connection()
    cur  = conn.cursor()
    cur.execute("UPDATE users SET status='approved', role=%s WHERE id=%s", (role, user_id))
    conn.commit()
    cur.close(); conn.close()

def reject_user(user_id):
    conn = get_db_connection()
    cur  = conn.cursor()
    cur.execute("UPDATE users SET status='rejected' WHERE id=%s", (user_id,))
    conn.commit()
    cur.close(); conn.close()

def update_user_role(user_id, role):
    conn = get_db_connection()
    cur  = conn.cursor()
    cur.execute("UPDATE users SET role=%s WHERE id=%s", (role, user_id))
    conn.commit()
    cur.close(); conn.close()

def delete_user(user_id):
    conn = get_db_connection()
    cur  = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    cur.close(); conn.close()

def update_user_password(user_id, password_hash):
    conn = get_db_connection()
    cur  = conn.cursor()
    cur.execute("UPDATE users SET password_hash=%s WHERE id=%s", (password_hash, user_id))
    conn.commit()
    cur.close(); conn.close()

def get_category_chart_data(model=None, date_from=None, date_to=None):
    conn = get_db_connection()
    cur  = conn.cursor()
    query  = "SELECT category, SUM(defect_qty) as total_qty FROM defects WHERE category IS NOT NULL AND category != ''"
    params = []
    if model:
        query += " AND model ILIKE %s"; params.append(model)
    if date_from:
        query += " AND date >= %s"; params.append(date_from)
    if date_to:
        query += " AND date <= %s"; params.append(date_to)
    query += " GROUP BY category ORDER BY total_qty DESC"
    cur.execute(query, params)
    results = cur.fetchall()
    cur.close(); conn.close()
    return results

def get_station_chart_data(model=None, date_from=None, date_to=None, limit=6):
    conn = get_db_connection()
    cur  = conn.cursor()
    query  = "SELECT ng_station, SUM(defect_qty) as total_qty FROM defects WHERE ng_station IS NOT NULL AND ng_station != '' AND UPPER(symptom) != 'TOTAL'"
    params = []
    if model:
        query += " AND model ILIKE %s"; params.append(model)
    if date_from:
        query += " AND date >= %s"; params.append(date_from)
    if date_to:
        query += " AND date <= %s"; params.append(date_to)
    query += " GROUP BY ng_station ORDER BY total_qty DESC LIMIT %s"
    params.append(limit)
    cur.execute(query, params)
    results = cur.fetchall()
    cur.close(); conn.close()
    return results
