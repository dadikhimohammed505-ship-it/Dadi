import streamlit as st
import numpy as np
import plotly.graph_objects as go

# إعداد الصفحة لتكون واسعة
st.set_page_config(layout="wide", page_title="المختبر الهندسي المتطور")

# تنسيق CSS مخصص للواجهة الاحترافية (Dark Mode)
st.markdown("""
    <style>
    .main {background-color: #0e1117;}
    .stSlider {padding: 10px;}
    .metric-card {background: #1e1e1e; padding: 20px; border-radius: 10px; border: 1px solid #333;}
    </style>
    """, unsafe_allow_html=True)

# القائمة الجانبية للتحكم
with st.sidebar:
    st.header("إعدادات الدائرة الذكية")
    v1 = st.slider("جهد المصدر الأول (V)", 0.0, 20.0, 10.0)
    v2 = st.slider("جهد المصدر الثاني (V)", 0.0, 20.0, 15.0)
    r1 = st.slider("المقاومة R1 (Ω)", 10.0, 500.0, 250.0)
    r2 = st.slider("المقاومة R2 (Ω)", 10.0, 500.0, 150.0)
    r3 = st.slider("المقاومة R3 (Ω)", 10.0, 500.0, 150.0)

# المحاكاة الرياضية (استخدام المصفوفات)
# هنا تضع معادلات كيرشوف: [R] * [V] = [I]
def calculate_circuit(v1, v2, r1, r2, r3):
    # مثال مبسط لحساب الجهد في العقدة
    # V_node = (v1/r1 + v2/r2) / (1/r1 + 1/r2 + 1/r3)
    node_v = (v1/r1 + v2/r2) / (1/r1 + 1/r2 + 1/r3)
    return node_v

# عرض النتائج في الصفحة الرئيسية
st.title("⚡ المختبر الهندسي المتطور")
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("نتائج التحليل المتكاملة")
    v_a = calculate_circuit(v1, v2, r1, r2, r3)
    st.metric("الجهد عند العقدة A", f"{v_a:.2f} V")
    st.metric("الجهد عند العقدة B", f"{v2:.2f} V")

with col2:
    # استخدام Plotly لرسم الدائرة بشكل احترافي
    fig = go.Figure()
    # هنا تضيف مسارات الدائرة والرموز باستخدام Scatter Plot
    fig.add_trace(go.Scatter(x=[0, 1, 2], y=[0, 1, 0], mode='lines+markers', name='Circuit'))
    fig.update_layout(template="plotly_dark", title="مخطط الدائرة الحي")
    st.plotly_chart(fig)
    
