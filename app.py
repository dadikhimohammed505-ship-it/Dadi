
import streamlit as st

st.title("لوحة تحكم دارتي الكهربائية ⚡")
st.write("أهلاً بك في أول تطبيق تفاعلي لمقرري!")

# إضافة منزلق للتحكم في الجهد
voltage = st.slider("اختر الجهد (فولت)", 0, 50, 12)
st.write(f"الجهد المختار حالياً هو: {voltage} فولت")

# إضافة زر بسيط
if st.button("احسب"):
    st.success(f"تم الحساب بنجاح لجهد {voltage} فولت!")
  
