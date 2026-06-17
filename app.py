import streamlit as st

# إعداد الصفحة لتكون واسعة
st.set_page_config(layout="wide")

st.title("⚡ المختبر الهندسي المتطور")

# تقسيم الصفحة إلى قسمين رئيسيين: الإعدادات (يمين) والرسم البياني/النتائج (يسار)
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("إعدادات الدائرة")
    with st.container(border=True): # حاوية ذات إطار احترافي
        v1 = st.slider("جهد المصدر الأول (V)", -20, 20, 15)
        r1 = st.slider("المقاومة (R1)", 10, 1000, 300)
        
        # أزرار تحكم مجمعة
        c1, c2 = st.columns(2)
        with c1:
            st.button("إضافة مصدر")
        with c2:
            st.button("حذف عنصر")

with col2:
    st.subheader("المحاكاة والتحليل")
    # حاوية للرسم البياني أو التمثيل البصري
    with st.container(border=True):
        st.write("هنا سيظهر الرسم البياني للدائرة")
        # مثال لمساحة رسم بياني فارغة
        st.line_chart([10, 20, 30, 40])
    
    # منطقة عرض المعادلات والنتائج
    st.latex(r'''
        \begin{bmatrix} 
        \frac{1}{R_1} + \frac{1}{R_2} & -\frac{1}{R_2} \\
        -\frac{1}{R_2} & \frac{1}{R_2} + \frac{1}{R_3} 
        \end{bmatrix} 
        \begin{bmatrix} V_A \\ V_B \end{bmatrix} = \begin{bmatrix} I_1 \\ I_2 \end{bmatrix}
    ''')

# تذييل الصفحة أو معلومات إضافية
st.info("💡 نصيحة: يمكنك تغيير القيم من الشريط الجانبي وسيتحدث التحليل الرياضي فوراً.")
