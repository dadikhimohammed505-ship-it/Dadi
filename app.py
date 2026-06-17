import streamlit as st

# 1. إعداد الصفحة (كامل العرض)
st.set_page_config(page_title="مختبر الكهرباء", layout="wide")

# 2. القائمة الجانبية للتحكم (احترافية ومنظمة)
with st.sidebar:
    st.header("⚙️ أدوات التحكم")
    st.write("اضبط قيم الدائرة من هنا")
    v = st.slider("مصدر الجهد (V)", -20.0, 20.0, 15.0)
    r = st.slider("المقاومة (R) [أوم]", 0.1, 1000.0, 300.0)
    st.markdown("---")
    st.write("النمط: وضع المختبر")

# 3. العنوان الرئيسي
st.title("⚡ مختبر الدوائر الكهربائية التفاعلي")

# 4. تقسيم الصفحة الرئيسية
col1, col2 = st.columns([2, 3])

with col1:
    st.subheader("نتائج الحساب")
    # عرض النتائج في مربعات احترافية
    current = v / r
    st.metric(label="الجهد", value=f"{v} V")
    st.metric(label="المقاومة", value=f"{r} Ω")
    st.metric(label="التيار الكهربائي", value=f"{current:.3f} A", delta=f"{current*1000:.0f} mA")

with col2:
    st.subheader("رسم توضيحي")
    # حاوية الرسم
    with st.container(border=True):
        st.write("مخطط الدائرة الكهربائية:")
        # Placeholder للرسم
        st.info("هنا يمكنك وضع صورة دائرتك (st.image) بعد رفعها للمستودع.")
        # مثال: st.image("circuit.jpg")

# 5. القوانين في الأسفل
st.markdown("---")
st.subheader("القوانين المستخدمة")
tab1, tab2 = st.tabs(["قانون أوم", "قانون كيرشوف"])
with tab1:
    st.latex(r'''I = \frac{V}{R}''')
with tab2:
    st.write("قوانين كيرشوف للتيار والجهد تعتمد على حفظ الشحنة والطاقة.")
    
