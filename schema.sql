-- Defect Database Schema for PostgreSQL

CREATE TABLE IF NOT EXISTS defects (
    id SERIAL PRIMARY KEY,
    pic VARCHAR(255),
    date DATE NOT NULL,
    model VARCHAR(100),
    shift VARCHAR(50),
    sn VARCHAR(255),
    ng_station VARCHAR(255),
    symptom TEXT,
    defect_qty INTEGER DEFAULT 1,
    root_cause TEXT,
    related_station TEXT,
    defected_item TEXT,
    defect_pic VARCHAR(100),
    category VARCHAR(100),
    status VARCHAR(50) DEFAULT 'Open',
    actual_out INTEGER DEFAULT 0,
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS root_cause(
    id SERIAL PRIMARY KEY,
    root_cause TEXT,
);

-- Indexing for performance
CREATE INDEX idx_defects_date ON defects(date);
CREATE INDEX idx_defects_model ON defects(model);
