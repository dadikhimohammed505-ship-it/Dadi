import streamlit as st
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title("⚡ المختبر الهندسي الرقمي")

# إعداد البيانات
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🛠️ الإعدادات")
    v = st.slider("الجهد (V)", 0, 20, 10)
    r = st.slider("المقاومة (R)", 10, 1000, 300)

with col2:
    st.subheader("📊 رسم الدارة")
    # رسم توضيحي بسيط واحترافي باستخدام Plotly
    fig = go.Figure()
    # رسم خطوط الدارة
    fig.add_trace(go.Scatter(x=[0, 1, 1, 0], y=[0, 0, 1, 1], mode='lines+text', 
                             text=["", "مصدر", "مقاومة", ""], line=dict(color='cyan', width=4)))
    fig.update_layout(height=300, template="plotly_dark", title=f"تيار الدارة: {v/r:.3f} A")
    st.plotly_chart(fig, use_container_width=True)

# عرض المعادلات
st.latex(r"I = \frac{V}{R} \implies I = \frac{" + str(v) + "}{" + str(r) + "} = " + str(round(v/r, 4)) + " A")
