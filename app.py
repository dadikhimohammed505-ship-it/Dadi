import streamlit as st
import numpy as np
import plotly.graph_objects as go

# إعداد الصفحة
st.set_page_config(layout="wide", page_title="المحاكي الهندسي")

# CSS المظهر الاحترافي
st.markdown("""
    <style>
    .stApp {background-color: #0e1117;}
    .metric-box {background: #1e1e1e; padding: 15px; border-radius: 10px; border: 1px solid #444;}
    </style>
""", unsafe_allow_html=True)

# القائمة الجانبية للتحكم
with st.sidebar:
    st.header("إعدادات الدائرة")
    v1 = st.slider("V1 (V)", 0.0, 20.0, 10.0)
    v2 = st.slider("V2 (V)", 0.0, 20.0, 15.0)
    r1 = st.slider("R1 (Ω)", 10.0, 500.0, 250.0)
    r2 = st.slider("R2 (Ω)", 10.0, 500.0, 150.0)

# الحساب الرياضي (مصفوفات كيرشوف)
# حل بسيط للدائرة المذكورة في الصور
v_a = (v1/r1 + v2/r2) / (1/r1 + 1/r2)

st.title("⚡ المحاكي الهندسي التفاعلي")

# عرض المعادلات والنتائج
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("التحليل الرياضي")
    st.latex(r"V_A = \frac{\frac{V_1}{R_1} + \frac{V_2}{R_2}}{\frac{1}{R_1} + \frac{1}{R_2}}")
    st.markdown(f'<div class="metric-box">الجهد عند العقدة A: <b>{v_a:.2f} V</b></div>', unsafe_allow_html=True)

with col2:
    # رسم الدائرة التفاعلي
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, 1, 2], y=[0, 0, 0], mode='markers+text', 
                             text=["V1", "Node A", "V2"], marker=dict(size=30, color='gold')))
    fig.update_layout(template="plotly_dark", title="مخطط الدائرة")
    st.plotly_chart(fig, use_container_width=True)
    
