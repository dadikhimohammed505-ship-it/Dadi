import streamlit as st

# تنظيم الصفحة
st.title("⚡ المختبر الهندسي المتطور")

# إنشاء حاوية للنتائج بشكل أفقي (احترافي)
col1, col2 = st.columns(2)

with col1:
    st.info("### الجهد عند العقدة A")
    st.metric(label="النتيجة", value=f"{v_a:.2f} V")

with col2:
    st.info("### الجهد عند العقدة B")
    st.metric(label="النتيجة", value=f"{v_b:.2f} V")

# إضافة خط فاصل جمالي
st.divider()

# إضافة نص توضيحي للنتائج
st.success("هذا المحول يحسب النتائج بدقة هندسية باستخدام المصفوفات.")
