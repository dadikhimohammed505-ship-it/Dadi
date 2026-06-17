import streamlit as st
import schemdraw
import schemdraw.elements as elm
import pandas as pd

# 1. إعداد واجهة احترافية (CSS متطور)
st.set_page_config(layout="wide", page_title="Circuit Sim Pro")
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: white; }
    div[data-testid="stMetricValue"] { color: #58a6ff; }
    .css-1r6slb0 { background-color: #1a1c22; padding: 20px; border-radius: 15px; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ المحاكي الهندسي الديناميكي")

# 2. إدارة الحالة (الذاكرة)
if 'components' not in st.session_state:
    st.session_state.components = {'V': 20, 'R': 100, 'mode': 'توالي'}

# 3. لوحة التحكم (Sidebar)
with st.sidebar:
    st.header("مدخلات النظام")
    st.session_state.components['mode'] = st.selectbox("Topology", ["توالي", "توازي"])
    st.session_state.components['V'] = st.slider("Voltage (V)", 1, 100, 20)
    st.session_state.components['R'] = st.slider("Resistor (Ω)", 10, 500, 100)

# 4. محرك الحساب والتحليل
v = st.session_state.components['V']
r = st.session_state.components['R']
current = v / r if st.session_state.components['mode'] == 'توالي' else v / (r/2)

# 5. عرض ديناميكي (Columns)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("المخطط الهندسي")
    d = schemdraw.Drawing()
    if st.session_state.components['mode'] == 'توالي':
        d.add(elm.SourceV().label(f"{v}V"))
        d.add(elm.Resistor().label(f"{r}Ω"))
        d.add(elm.Ground())
    else:
        d.add(elm.SourceV().up().label(f"{v}V"))
        d.add(elm.Line().right())
        d.add(elm.Resistor().down().label(f"{r}Ω"))
        d.add(elm.Line().left())
        d.add(elm.Ground())
    st.image(d.get_imagedata('png'), use_container_width=True)

with col2:
    st.subheader("التحليل اللحظي")
    # جدول بيانات احترافي
    df = pd.DataFrame({
        "المعامل": ["الجهد", "المقاومة", "التيار"],
        "القيمة": [f"{v} V", f"{r} Ω", f"{current:.3f} A"]
    })
    st.table(df)
    st.latex(r"I = \frac{V}{R}")
    
