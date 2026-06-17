import streamlit as st

st.title("مختبر الدوائر الكهربائية التفاعلي ⚡")

tab1, tab2, tab3 = st.tabs(["قانون أوم", "التوصيل على التسلسل", "التوصيل على التوازي"])

with tab1:
    st.header("حاسبة قانون أوم")
    v = st.number_input("الجهد (فولت)", value=12.0)
    r = st.number_input("المقاومة (أوم)", value=10.0)
    if r > 0:
        st.success(f"التيار = {v/r:.2f} أمبير")

with tab2:
    st.header("التسلسل (Series)")
    r1 = st.number_input("المقاومة 1 (أوم)", value=5.0)
    r2 = st.number_input("المقاومة 2 (أوم)", value=5.0)
    st.write(f"المقاومة الكلية = {r1 + r2} أوم")

with tab3:
    st.header("التوازي (Parallel)")
    p1 = st.number_input("المقاومة 1 (أوم) ", value=10.0)
    p2 = st.number_input("المقاومة 2 (أوم) ", value=10.0)
    if p1 > 0 and p2 > 0:
        req = (p1 * p2) / (p1 + p2)
        st.write(f"المقاومة الكلية = {req:.2f} أوم")
        
