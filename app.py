import streamlit as st
import schemdraw
import schemdraw.elements as elm
from io import BytesIO

# 1. إعداد واجهة احترافية
st.set_page_config(page_title="Circuit Sim Pro", layout="wide")

# إزالة الهوامش الزائدة وتنسيق الخلفية
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    div[data-testid="stMetricValue"] { font-size: 25px; color: #58a6ff; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ المحاكي الهندسي الاحترافي")

# 2. لوحة التحكم
with st.sidebar:
    st.header("إعدادات الدائرة")
    v1 = st.slider("Voltage V1 (V)", 0, 50, 15)
    r1 = st.slider("Resistor R1 (Ω)", 10, 500, 150)
    
# 3. محرك الرسم التوليدي (Schemdraw)
def draw_circuit(v, r):
    d = schemdraw.Drawing()
    d.add(elm.SourceV().label(f"{v}V"))
    d.add(elm.Resistor().label(f"{r}Ω"))
    d.add(elm.Line())
    d.add(elm.Ground())
    return d

# 4. التنفيذ والعرض
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("مخطط الدائرة")
    fig = draw_circuit(v1, r1)
    st.image(fig.get_imagedata('png'))

with col2:
    st.subheader("تحليل النتائج")
    current = v1 / r1
    st.metric("التيار المار (I)", f"{current:.3f} A")
    st.info("تم التحليل باستخدام قوانين أوم كيرشوف.")
    
