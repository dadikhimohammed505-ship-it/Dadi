import streamlit as st
import numpy as np
import plotly.graph_objects as go

# إعداد الصفحة وتنسيق المظهر المظلم الاحترافي
st.set_page_config(layout="wide", page_title="المختبر الهندسي المتطور")

st.markdown("""
    <style>
    .stApp {background-color: #0e1117; color: white;}
    [data-testid="stSidebar"] {background-color: #1a1a1a; padding: 20px;}
    .metric-card {background: #1e1e1e; padding: 20px; border-radius: 15px; border: 1px solid #333;}
    </style>
""", unsafe_allow_html=True)

# القائمة الجانبية للتحكم
with st.sidebar:
    st.header("إعدادات الدائرة")
    v1 = st.slider("جهد المصدر الأول V1 (V)", 0.0, 20.0, 10.0)
    v2 = st.slider("جهد المصدر الثاني V2 (V)", 0.0, 20.0, 15.0)
    r1 = st.slider("المقاومة R1 (Ω)", 10.0, 500.0, 250.0)
    r2 = st.slider("المقاومة R2 (Ω)", 10.0, 500.0, 150.0)
    r3 = st.slider("المقاومة R3 (Ω)", 10.0, 500.0, 150.0)

# محرك الحل الرياضي (مصفوفات كيرشوف)
G = np.array([[1/r1 + 1/r3, -1/r3],
              [-1/r3, 1/r2 + 1/r3]])
I = np.array([v1/r1, v2/r2])
v_nodes = np.linalg.solve(G, I)

# الواجهة الرئيسية
st.title("⚡ المختبر الهندسي المتطور")

# عرض المعادلات بصيغة LaTeX
st.subheader("النموذج الرياضي (تحليل العقد)")
st.latex(r'''
\begin{bmatrix} \frac{1}{R_1}+\frac{1}{R_3} & -\frac{1}{R_3} \\ -\frac{1}{R_3} & \frac{1}{R_2}+\frac{1}{R_3} \end{bmatrix} 
\begin{bmatrix} V_A \\ V_B \end{bmatrix} = 
\begin{bmatrix} \frac{V_1}{R_1} \\ \frac{V_2}{R_2} \end{bmatrix}
''')

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("الجهد عند العقدة A", f"{v_nodes[0]:.2f} V")
    st.metric("الجهد عند العقدة B", f"{v_nodes[1]:.2f} V")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # رسم الدائرة التفاعلي
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, 1, 2], y=[0, 1, 0], mode='markers+text', 
                             text=["Node V1", "Node A", "Node V2"], 
                             marker=dict(size=30, color=['#FF5733', '#33FF57', '#3357FF'])))
    fig.update_layout(template="plotly_dark", plot_bgcolor="#0e1117", paper_bgcolor="#0e1117",
                      title="تمثيل بصري لمصفوفة الجهد")
    st.plotly_chart(fig, use_container_width=True)

st.success("تم تحديث المحاكاة لحظياً بناءً على مصفوفة كيرشوف.")
