import google.generativeai as genai
import os

# إعداد Gemini
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

SYSTEM_PROMPT = """
You are a Quality Engineering Expert. Analyze the defect data provided from the factory floor.
Identify potential root causes based on the NG Station and Symptom.
Keep your answer concise and technical.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT
)

def analyze_defect_root_cause(defect_data):
    try:
        if not API_KEY:
            return "Error: Gemini API Key not configured."
            
        prompt = f"Analyze this incident: {defect_data}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI Analysis Error: {str(e)}"
