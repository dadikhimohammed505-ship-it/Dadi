import streamlit as st
import numpy as np

def solve_circuit(v1, v2, r1, r2, r3):
    # محاكاة لدائرة بسيطة (أوم ومقسم جهد)
    # هنا نقوم ببناء مصفوفة الدائرة وحلها
    # A * x = B
    A = np.array([[1/r1 + 1/r2, -1/r2], [-1/r2, 1/r2 + 1/r3]])
    B = np.array([v1/r1, v2/r3])
    
    try:
        voltages = np.linalg.solve(A, B)
        return voltages
    except:
        return [0, 0]

st.title("⚡ المختبر الهندسي المتطور")

with st.sidebar:
    st.header("إعدادات الدائرة")
    v1 = st.slider("جهد المصدر الأول (V)", 0.0, 20.0, 10.0)
    v2 = st.slider("جهد المصدر الثاني (V)", 0.0, 20.0, 5.0)
    r1 = st.slider("المقاومة R1", 1.0, 100.0, 10.0)
    r2 = st.slider("المقاومة R2", 1.0, 100.0, 10.0)
    r3 = st.slider("المقاومة R3", 1.0, 100.0, 10.0)

# الحل
results = solve_circuit(v1, v2, r1, r2, r3)

st.subheader("نتائج المحاكاة الرياضية")
col1, col2 = st.columns(2)
col1.metric("الجهد عند العقدة A", f"{results[0]:.2f} V")
col2.metric("الجهد عند العقدة B", f"{results[1]:.2f} V")

st.info("هذا هو 'المحرك' الذي يحسب النتائج بدقة هندسية باستخدام المصفوفات.")
