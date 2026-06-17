import streamlit as st
import schemdraw
import schemdraw.elements as elm
import pandas as pd

# 1. إعداد الواجهة الاحترافية (Custom Theme)
st.set_page_config(layout="wide", page_title="Professional Circuit Sim")
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #e6edf3; }
    .css-1r6slb0 { background-color: #161b22; border: 1px solid #30363d; border-radius: 10px; padding: 20px; }
    h1 { color: #58a6ff !important; }
    </style>
""", unsafe_allow_html=True)

# 2. إدارة حالة الدائرة (حتى لا تضيع القيم عند التفاعل)
if 'circuit_state' not in st.session_state:
    st.session_state.circuit_state = {'V1': 20.0, 'R1': 100.0, 'mode': 'توالي'}

# 3. الشريط الجانبي (أدوات تحكم احترافية)
with st.sidebar:
    st.header("⚙️ أدوات التحكم")
    st.session_state.circuit_state['mode'] = st.selectbox("طوبولوجيا الدائرة", ["توالي", "توازي"])
    st.session_state.circuit_state['V1'] = st.slider("الجهد V1 (V)", 5.0, 50.0, 20.0)
    st.session_state.circuit_state['R1'] = st.slider("المقاومة R1 (Ω)", 10.0, 500.0, 100.0)
    
    if st.button("إعادة ضبط المحاكاة"):
        st.session_state.circuit_state = {'V1': 20.0, 'R1': 100.0, 'mode': 'توالي'}
        st.rerun()

# 4. المحرك الرياضي والرسم التوليدي
def generate_circuit():
    v = st.session_state.circuit_state['V1']
    r = st.session_state.circuit_state['R1']
    
    d = schemdraw.Drawing()
    if st.session_state.circuit_state['mode'] == 'توالي':
        d.add(elm.SourceV().label(f"{v}V"))
        d.add(elm.Resistor().label(f"{r}Ω"))
        d.add(elm.Ground())
        I = v / r
    else:
        d.add(elm.SourceV().up().label(f"{v}V"))
        d.add(elm.Line().right())
        d.add(elm.Resistor().down().label(f"{r}Ω"))
        d.add(elm.Line().left())
        d.add(elm.Ground())
        I = v / (r/2) # مثال تبسيطي
    return d, I

# 5. الواجهة الرئيسية (التوزيع الاحترافي)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 المخطط الهندسي التفاعلي")
    drawing, current = generate_circuit()
    st.image(drawing.get_imagedata('png'), use_container_width=True)

with col2:
    st.subheader("📈 التحليل الرقمي")
    st.metric("التيار المار (I)", f"{current:.3f} A")
    
    st.subheader("المنطق الرياضي")
    st.latex(r"I = \frac{V}{R_{total}}")
    
    # جدول بيانات احترافي
    df = pd.DataFrame({
        "العنصر": ["V1", "R1", "I"],
        "القيمة": [f"{st.session_state.circuit_state['V1']} V", 
                  f"{st.session_state.circuit_state['R1']} Ω", 
                  f"{current:.3f} A"]
    })
    st.table(df)
    
