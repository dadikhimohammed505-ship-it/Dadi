import streamlit as st

st.set_page_config(layout="wide")
st.title("⚡ المختبر الهندسي (وضع الرسم التوضيحي)")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🛠️ الإعدادات")
    v = st.slider("الجهد (V)", 0, 50, 10)
    r = st.slider("المقاومة (R)", 10, 1000, 200)

with col2:
    st.subheader("📍 رسم الدارة التفاعلي")
    # نستخدم كود SVG مباشر - لا يحتاج أي مكتبة، وهو "لغة الويب" للرسوم
    st.markdown(f"""
    <svg width="400" height="150" viewBox="0 0 400 150">
      <line x1="50" y1="75" x2="150" y2="75" stroke="white" stroke-width="3" />
      <rect x="150" y="60" width="100" height="30" fill="none" stroke="cyan" stroke-width="3" />
      <line x1="250" y1="75" x2="350" y2="75" stroke="white" stroke-width="3" />
      <text x="170" y="45" fill="white" font-size="16">المقاومة {r}Ω</text>
      <text x="150" y="130" fill="yellow" font-size="20" font-weight="bold">التيار المحسوب: {v/r:.3f} A</text>
    </svg>
    """, unsafe_allow_html=True)

st.latex(rf"I = \frac{{{v}}}{{{r}}} = {v/r:.4f} A")
