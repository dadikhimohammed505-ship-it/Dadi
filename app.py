import streamlit as st

# ضبط إعدادات الصفحة لتكون احترافية
st.set_page_config(page_title="مختبر الدوائر", layout="wide")

st.title("⚡ مختبر الدوائر الكهربائية التفاعلي")
st.write("مرحباً بك في لوحة التحكم الخاصة بك!")

# إضافة قانون أوم
st.subheader("حاسبة قانون أوم")
col1, col2 = st.columns(2)
with col1:
    v = st.number_input("الجهد (فولت)", value=12.0)
with col2:
    r = st.number_input("المقاومة (أوم)", value=10.0)

if r > 0:
    st.success(f"التيار = {v/r:.2f} أمبير")
else:
    st.error("المقاومة يجب أن تكون أكبر من صفر")
    
