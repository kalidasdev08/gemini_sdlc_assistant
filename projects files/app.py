import streamlit as st
import google.generativeai as genai

# Load Gemini API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Use the text generation model
model = genai.GenerativeModel("models/text-bison-001")

def call_gemini(prompt):
    try:
        resp = model.generate_text(prompt)
        return resp.text.strip()
    except Exception as e:
        return f"❌ Gemini Error: {e}"

# SDLC functions
def summarize_requirements(text):
    return call_gemini(f"Summarize this software requirement clearly:\n\n{text}")

def generate_python_code(req):
    return call_gemini(f"Generate Python code for this requirement:\n\n{req}")

def review_code(code):
    return call_gemini(f"Review this Python code for bugs or improvements:\n\n{code}")

def generate_test_cases(desc):
    return call_gemini(f"Write detailed test cases for this feature:\n\n{desc}")

# Streamlit UI
st.set_page_config(page_title="Gemini SDLC Assistant", layout="wide")
st.title("🤖 Gemini-Powered SDLC Assistant")

tabs = st.tabs([
    "📄 Requirement Analysis",
    "🛠️ Code Generation",
    "🔍 Code Review",
    "🧪 Test Case Generation"
])

with tabs[0]:
    st.header("📄 Requirement Analysis")
    uf = st.file_uploader("Upload .txt", type="txt")
    text = uf.read().decode("utf-8") if uf else ""
    if st.button("Summarize") and text:
        st.text_area("Summary", summarize_requirements(text), height=200)

with tabs[1]:
    req = st.text_area("Describe requirement")
    if st.button("Generate Code") and req:
        st.code(generate_python_code(req), language="python")

with tabs[2]:
    code = st.text_area("Paste code")
    if st.button("Review Code") and code:
        st.text_area("Review", review_code(code), height=200)

with tabs[3]:
    desc = st.text_area("Describe feature")
    if st.button("Generate Tests") and desc:
        st.text_area("Test Cases", generate_test_cases(desc), height=200)
