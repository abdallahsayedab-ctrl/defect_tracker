from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from supabase import create_client, Client
import os
from typing import List, Optional

app = FastAPI(title="AIzaSyAPmu6OpBpbxdhT4nOgNrt3YBq6VX4TlIg")

# إعداد Supabase
# يجب تعيين هذه القيم في متغيرات البيئة (Environment Variables)
SUPABASE_URL = os.environ.get("https://abjtqvlyelggngxlmaob.supabase.co")
SUPABASE_KEY = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFianRxdmx5ZWxnZ25neGxtYW9iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY1NDI0MDksImV4cCI6MjA5MjExODQwOX0.A_3pM9z72zgN0HrSJJalTlPIUI6UbbBJ-CXuj4I5bO4")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# موديل البيانات (Defect Schema)
class DefectSchema(BaseModel):
    pic: str
    date: str
    model: str
    shift: str
    sn: Optional[str] = None
    symptom: str
    ng_station: Optional[str] = None
    defect_qty: int = 1
    root_cause: Optional[str] = None
    status: str = "Open"

@app.get("/defects")
async def get_defects(date_start: str = None, date_end: str = None):
    query = supabase.table("defects").select("*")
    if date_start:
        query = query.gte("date", date_start)
    if date_end:
        query = query.lte("date", date_end)
    
    response = query.execute()
    return response.data

@app.post("/defects")
async def add_defect(defect: DefectSchema):
    response = supabase.table("defects").insert(defect.dict()).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Failed to add defect")
    return {"status": "success", "data": response.data}

@app.put("/defects/{defect_id}")
async def update_defect(defect_id: str, updates: dict):
    response = supabase.table("defects").update(updates).eq("id", defect_id).execute()
    return response.data

@app.delete("/defects/{defect_id}")
async def delete_defect(defect_id: str):
    response = supabase.table("defects").delete().eq("id", defect_id).execute()
    return {"status": "deleted"}
