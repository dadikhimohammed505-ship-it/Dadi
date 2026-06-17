import streamlit as st
import schemdraw
import schemdraw.elements as elm

st.set_page_config(layout="wide")

st.title("⚡ المختبر الهندسي المتطور")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("أدوات التحكم")
    v_val = st.slider("جهد المصدر (V)", 0, 20, 10)
    r_val = st.slider("المقاومة (R) [أوم]", 10, 1000, 300)

with col2:
    st.subheader("رسم الدارة")
    
    # محرك الرسم (schemdraw)
    d = schemdraw.Drawing()
    d.add(elm.SourceV().label(f"{v_val}V"))
    d.add(elm.Resistor().right().label(f"{r_val}Ω"))
    d.add(elm.Line().down())
    d.add(elm.Ground())
    
    # عرض الدارة في واجهة Streamlit
    st.pyplot(d.draw())
    
    st.write("---")
    st.latex(r"I = \frac{V}{R} = \frac{" + str(v_val) + "}{" + str(r_val) + "} = " + str(round(v_val/r_val, 3)) + " A")
    
