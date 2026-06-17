import streamlit as st

# إعداد الصفحة لتكون واسعة وتملأ الشاشة
st.set_page_config(layout="wide", page_title="المختبر الهندسي")

# تنسيق CSS مخصص للوصول لمظهر "اللوحة التقنية"
st.markdown("""
    <style>
    .main { background-color: #121212; }
    .stApp { color: #ffffff; }
    .css-1r6slb0 { background-color: #1e1e1e; border: 1px solid #333; }
    /* تنسيق العناوين */
    h1 { color: #00d4ff; text-align: center; }
    h3 { color: #ff9f43; font-size: 1.2rem; }
    /* تنسيق البطاقات (الحاويات) */
    div[data-testid="stVerticalBlock"] > div:nth-of-type(1) {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #444;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ المختبر الهندسي المتطور")

# تقسيم الصفحة إلى قسمين رئيسيين (تحكم في اليسار، وعرض في اليمين)
col_controls, col_display = st.columns([1, 2])

with col_controls:
    st.subheader("🛠️ أدوات التحكم")
    
    # اختيار الطوبولوجيا (القائمة المنسدلة)
    topology = st.selectbox("شكل الدارة (Topology)", ["توالي", "توازي", "فرع"])
    
    # إعدادات المصدر والمقاومات
    st.slider("مصدر الجهد (V)", -20, 20, 15)
    st.slider("المقاومة (R)", 10, 1000, 300)
    
    # أزرار تحكم مجمعة
    c1, c2 = st.columns(2)
    with c1:
        st.button("إضافة مصدر", use_container_width=True)
    with c2:
        st.button("حذف عنصر", use_container_width=True)

with col_display:
    st.subheader("📊 المحاكاة والحل الرياضي")
    
    # منطقة عرض الرسم البياني أو الدائرة
    st.container(border=True)
    st.write("هنا يتم عرض الدائرة أو الرسم البياني التفاعلي")
    
    # منطقة الحل الرياضي (معادلات كيرشوف)
    st.markdown("### 📝 النتائج")
    st.latex(r'''
        \begin{bmatrix} 
        \frac{1}{R_1} + \frac{1}{R_2} & -\frac{1}{R_2} \\
        -\frac{1}{R_2} & \frac{1}{R_2} + \frac{1}{R_3} 
        \end{bmatrix} 
        \begin{bmatrix} V_A \\ V_B \end{bmatrix} = \begin{bmatrix} I_1 \\ I_2 \end{bmatrix}
    ''')

# تذييل بسيط
st.divider()
st.caption("نظام المحاكاة التفاعلية - الإصدار الاحترافي")
